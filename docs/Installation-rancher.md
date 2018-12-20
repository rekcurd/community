# Setup Kubernetes with Rancher
Table of Contents.

1. [Rancher installation](#rancher-installation)
1. [Docker image creation](#docker-image-creation)
1. [gRPC Load Balancing](#grpc-load-balancing)
1. [fluentd installation](#fluentd-installation)

---

## Rancher installation
This section is the setup manual for [Rancher](https://rancher.com/) version 1.6. You can follow the official guide [here](https://rancher.com/docs/rancher/v1.6/en/installing-rancher/installing-server/). If you want to install Rancher version 2.x, you can follow the guide [here](https://rancher.com/docs/rancher/v2.x/en/installation/). We recommend to use Rancher 2.x.

### Environments
- CentOS 7.4
- Rancher 1.6.16
- Docker 17.03
- MySQL 5.7

### HA configurations
#### Rancher server specs
- HA nodes (a minimum of 3 nodes is required):
  - CentOS 7
  - 8GB RAM instance
- MySQL 5.7
- DNS

#### MySQL
```mysql
CREATE DATABASE /*!32312 IF NOT EXISTS*/ `cattle` /*!40100 DEFAULT CHARACTER SET utf8 */;
```

You must have a DDL privilege for the node servers.

#### Rancher server settings
Set <mysql-host>, <port>, <user>, <password> and <IP_of_the_Node>. <IP_of_the_Node> is the self IP address which runs on.

```bash
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo yum -y makecache fast
sudo yum -y install yum-versionlock
echo 'docker-ce-17.03.2.ce-1.el7.centos.x86_64' | sudo tee -a /etc/yum/pluginconf.d/versionlock.list
sudo yum -y install docker-ce-17.03.2.ce-1.el7.centos.x86_64
sudo systemctl start docker
sudo systemctl enable docker
sudo docker run -d --restart=unless-stopped -p 8080:8080 -p 9345:9345 rancher/server:v1.6.16 --db-host <mysql-host> --db-port <port> --db-user <user> --db-pass <password> --db-name cattle --advertise-address <IP_of_the_Node>
```

After 60 seconds, Rancher dashboard is available on `http://localhost:8080/`

### Setup Rancher
#### DNS
Create a VIP or load balancer for node servers and assign DNS to it. Then go to "Admin" -> "Settings" on Rancher dashboard and set DNS to "Host Registration URL".

#### Activate Kubernetes
Go to "Add from Catalog" and activate Kubernetes with a configuration of "Enable Rancher Ingress Controller = False".

#### Wrap up
Go to "Admin" -> "High Availability" and confirm the status of HA clusters.


### Setup Kubernetes cluster node
- Cluster nodes
  - CentOS 7
  - 8GB RAM instance

#### Cluster node settings
```
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo yum -y makecache fast
sudo yum -y install yum-versionlock
echo 'docker-ce-17.03.2.ce-1.el7.centos.x86_64' | sudo tee -a /etc/yum/pluginconf.d/versionlock.list
sudo yum -y install docker-ce-17.03.2.ce-1.el7.centos.x86_64
sudo systemctl start docker
sudo systemctl enable docker
```

#### Join node to Kubernetes cluster
1. Go to "Infrastracture" -> "Host" -> "Add Host" -> "Custom" on Rancher dashboard.
1. Click "Add Label" and set to "key=host" and "value=development". If you want to add a node for "staging", set "value" to "staging".
1. Copy the script on the above page and run it on client nodes.

#### Assign DNS
We uses Kubernetes's hostname routing via ingress to access the services which run on Kubernetes. Keep DNS and assigned it to the Kubernetes cluster nodes. Or create a l4/l7 load balancer and assign DNS to them.

#### Mount online storage
We uses an online storage (e.g. AWS S3, GCS, WebDAV) as the storage of ML models. In our usage, we mounts it on `/mnt/drucker-model` on every cluster nodes. Rekcurd pod will mount the node's that volume to pod's `/mnt/drucker-model`.

#### Add git ssh
If you use a private git repository like GitHub enterprise, you need to add your credentials to `/root/.ssh/` on every cluster nodes. Rekcurd pod will mount the node's that volume to pod's `/root/.ssh`.

---

## Docker image creation
Kubernetes uses a container image. The simplest docker image is available on [Docker Hub](https://hub.docker.com/r/rekcurd/rekcurd) (`rekcurd/rekcurd:v0.2.1`).

If you want to use your own docker image, please import our [Dockerfile](https://github.com/rekcurd/dockerfiles).

---

## Namespace creation
We uses these namespace for Rekcurd. These values are also used as Kubernetes cluster node label.

- development
- staging
- production
- beta
- sandbox

### Install namespaces
Apply the code below or upload them via "Kubernetes Dashboard".

```bash
$ cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Namespace
metadata:
  name: development
---
apiVersion: v1
kind: Namespace
metadata:
  name: beta
---
apiVersion: v1
kind: Namespace
metadata:
  name: staging
---
apiVersion: v1
kind: Namespace
metadata:
  name: sandbox
---
apiVersion: v1
kind: Namespace
metadata:
  name: production
EOF
```

---

## gRPC Load Balancing
Rancher's load balancer does not support gRPC protocol. We use [nghttpx Ingress Controller](https://github.com/zlabjp/nghttpx-ingress-lb) as gRPC load balancer. 

### Disable Rancher Ingress Controller
On Rancher dashboard

1. Select "Manage Environments"
1. Select "Kubernetes → Edit"
1. Select "Edit Config"
1. Set "Enable Rancher Ingress Controller" to "False"

### Install nghttpx Ingress Controller
Apply the files below or upload the files via "Kubernetes Dashboard".

```bash
$ kubectl apply -f https://raw.githubusercontent.com/zlabjp/nghttpx-ingress-lb/master/examples/default-backend.yaml
$ kubectl apply -f https://raw.githubusercontent.com/zlabjp/nghttpx-ingress-lb/master/examples/default-backend-svc.yaml
$ kubectl apply -f https://raw.githubusercontent.com/zlabjp/nghttpx-ingress-lb/master/examples/default/service-account.yaml
$ kubectl apply -f https://raw.githubusercontent.com/zlabjp/nghttpx-ingress-lb/master/examples/daemonset/as-daemonset.yaml
```

---

## fluentd installation
We uses [fluentd](https://github.com/fluent/fluentd-kubernetes-daemonset) to aggregate the logs. After installing "fluentd daemonset" on Kubernetes, you can forward the logs to the server you specify by printing to stdout/stderr.
