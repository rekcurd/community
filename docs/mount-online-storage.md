# Mount online storage
Use your favorite (e.g. bare metal, AWS S3, GCS, WebDAV). This storage is used for storing the ML models. In our usage, we mount it on `/mnt/drucker-model` to every Kubernetes cluster nodes. Rekcurd pod will mount it to pod's `/mnt/drucker-model`.

**If you set up k8s with Amazon EKS, CloudFormation will create a S3 bucket, so you can skip this step.**

## How to mount AWS S3 volume
### Put your credentials
Put your AWS credentials on `/root/.aws/credentials` to every Kubernetes cluster nodes..

```text
[default]
aws_access_key_id={{ aws_access_key_id }}
aws_secret_access_key={{ aws_secret_access_key }}
```

### Install golang
```bash
$ yum install -y golang
```

### Install fuse
```bash
$ yum install -y fuse
```

### Install goofys
```bash
$ go get github.com/kahing/goofys
$ go install github.com/kahing/goofys
```

### (Optional) Set fstab
Add this line on `/etc/fstab`.
```text
/home/{{ sudoer_user }}/go/bin/goofys#{{ s3_backet }} {{ s3_mount_dir }} fuse _netdev,allow_other,--file-mode=0666,--endpoint={{ s3_endpoint }} 0 0
```

#### Create shell script on `/home/{{ sudoer_user }}/s3_mount.sh`
Make sure you have a `{{ s3_mount_dir }}/healthy.txt` file since we use it as a health checker.
```text
#!/usr/bin/env bash
if [ ! -e {{ s3_mount_dir }}/healthy.txt ]; then
  sudo /bin/umount {{ s3_mount_dir }}
  sudo /bin/mount -a
  echo 'remount s3'
fi
```

#### Create service file on `/etc/systemd/system/s3_mount.service`
```text
[Unit]
Description=S3 mount for rekcurd
RefuseManualStart=no
RefuseManualStop=yes

[Service]
Type=oneshot
ExecStart=/home/{{ sudoer_user }}/s3_mount.sh
RemainAfterExit=yes
```

#### Create timer file on `/etc/systemd/system/s3_mount.timer`
```text
[Unit]
Description=S3 mount for rekcurd

[Timer]
OnBootSec=1min
OnUnitActiveSec=5min
Unit=s3_mount.service
Persistent=true

[Install]
WantedBy=timers.target
```
