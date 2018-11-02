# Setup Kubernetes with kubeadm
## Prerequisites
1. This guide is tested on CentOS 7.4. Please check the [official guide](https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/) if you're using other OS like Ubuntu.
2. Ensure the account has sudo privileges to run commands below.
3. Only non-HA cluster(singler master cluster) is set up in this guide. Please refer to [this page](https://kubernetes.io/docs/setup/independent/high-availability/) if you need a HA cluster.
4. Calico is run as the pod network add-on. Please follow the [official guide](https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/) if you prefer another network add-on.

## Environments
* Docker: 18.06.1.ce
* kubeadm, kubectl, kubelet: 1.12.2

## Steps
Steps here are copied from Docker and Kubernetes offical sites. The details could be found in the following sites:
* [Install Docker](https://docs.docker.com/install/linux/docker-ce/centos/)
* [Install kubeadm](https://kubernetes.io/docs/setup/independent/install-kubeadm/)
* [Create a single master cluster with kubeadm](https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/)

**Install and run Docker**


```bash
$ sudo yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2
$ sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
$ sudo yum install -y docker-ce
$ sudo systemctl enable docker && sudo systemctl start docker
```

**Install and run kubeadm**


Read the `Before you begin` section on this [page](https://kubernetes.io/docs/setup/independent/install-kubeadm/) to check your environment and run:

```bash
$ sudo echo "
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
exclude=kube*" | sudo tee /etc/yum.repos.d/kubernetes.repo > /dev/null
$ sudo yum install -y kubelet kubeadm kubectl --disableexcludes=kubernetes
$ sudo systemctl enable kubelet && sudo systemctl start kubelet
```

**Master initialization**


Please run the following commands on the master node and keep the join command logged in `kubeadm init` command.
```bash
# Run command below and save the join command in the logs
# The join command looks like kubeadm join {ip} --token ... --discovery-token-ca-cert-hash ...
$ sudo kubeadm init --pod-network-cidr=192.168.0.0/16
# Set up kubectl
$ mkdir -p $HOME/.kube
$ sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
$ sudo chown $(id -u):$(id -g) $HOME/.kube/config
# Set up Calico
$ kubectl apply -f https://docs.projectcalico.org/v3.1/getting-started/kubernetes/installation/hosted/rbac-kdd.yaml
$ kubectl apply -f https://docs.projectcalico.org/v3.1/getting-started/kubernetes/installation/hosted/kubernetes-datastore/calico-networking/1.7/calico.yaml
```

**Joining your nodes**


On each your node(non-master), run
```bash
# Use the command saved in the last step
$ sudo kubeadm join --token <token> <master-ip>:<master-port> --discovery-token-ca-cert-hash sha256:<hash>
```

The `<master-ip>` could be replaced with the host name of the master node.


If you lost the join command, use `kubeadm token create --print-join-command` on the master to get the join command but you might need to regenerate the token because the token only has 24-hour TTL. Please check the `kubeadm token` command [here](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-token/) for details.

# Install Ingress controller
For now, you can only access drucker services nghttpx Ingress. Please follow instructions below to set up nghttpx Ingress Controller.

```bash
$ kubectl apply -f https://raw.githubusercontent.com/zlabjp/nghttpx-ingress-lb/master/examples/default-backend.yaml
$ kubectl apply -f https://raw.githubusercontent.com/zlabjp/nghttpx-ingress-lb/master/examples/default-backend-svc.yaml
$ kubectl apply -f https://raw.githubusercontent.com/zlabjp/nghttpx-ingress-lb/master/examples/default/service-account.yaml
$ kubectl apply -f https://raw.githubusercontent.com/zlabjp/nghttpx-ingress-lb/master/examples/daemonset/as-daemonset.yaml
```

Also, apply the following ClusterRole and ClusterRoleBinding to make ingress controller work.
```
apiVersion: rbac.authorization.k8s.io/v1beta1
kind: ClusterRole
metadata:
  name: system:ingress
rules:
- apiGroups:
  - ""
  resources: ["configmaps","secrets","endpoints","events","services"]
  verbs: ["list","watch","create","update","delete","get"]
- apiGroups:
  - ""
  - "extensions"
  resources: ["services","nodes","ingresses","pods","ingresses/status"]
  verbs: ["list","watch","create","update","delete","get"]
---
apiVersion: rbac.authorization.k8s.io/v1beta1
kind: ClusterRoleBinding
metadata:
  name: ingress
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: system:ingress
subjects:
  - kind: ServiceAccount
    name: ingress
    namespace: kube-system
```

# Drucker
Please follow the Drucker part on this [page](https://github.com/drucker/drucker-parent/blob/master/docs/Installation.md) to install drucker and deploy your services.