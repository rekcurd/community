# Setup Drucker Environment with Amazon EKS
## Setup Kubernetes with Amazon EKS
### Environments
* EKS version: eks.3

### Steps

Basically, you just need to follow [the official document](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html).  
The diffrences are:

- You do not need `Step 4: Launch a Guest Book Application`.
- You need to use [our YAML file](https://github.com/drucker/drucker-parent/blob/master/config/amazon-eks-nodegroup.yaml) for CloudFormation to launch your worker nodes in `Step 3: Launch and Configure Amazon EKS Worker Nodes`.  
  The details are in the section below.

#### Edit and Upload YAML file to launch your worker nodes.
1. If you run `git clone` with SSH when you use drucker, replace `REPLACE_YOUR_OWN_SSH_KEY` with your own SSH private key in [autoscaling-group.yaml](https://github.com/drucker/drucker-parent/blob/master/config/autoscaling-group.yaml).
   You can skip this step if you use public repository and run `git clone` with HTTPS
2. Edit [env-list.txt](https://github.com/drucker/drucker-parent/blob/master/config/env-list.txt).
    - If you want only development, staging and production environments for Drucker, delete beta and sandbox from the file (or comment out with `#`)
3. Run [build_eks_nodegroup.py](https://github.com/drucker/drucker-parent/blob/master/config/build_eks_nodegroup.py)
4. Follow the instructions instead of the official documemnt Step 3-5 and 3-6.
    1. For **Choose a template**, select **Upload a template to Amazon S3.**
    2. Select amazon-eks-nodegroup.yaml generated in [config directory](https://github.com/drucker/drucker-parent/blob/master/config) and choose **Next.**

**Be careful that AutoScalingGroup will be created for each env,  
so if your env-list.txt has all 5 environments, `5 * NodeAutoScalingGroupDesiredCapacity` nodes will be created.**


## Install Metrics Server
You need to install metrics server for autoscaler to work.  
Please run the following commands to set up metrics server.

```bash
$ git clone https://github.com/kubernetes-incubator/metrics-server.git
$ cd metrics-server
$ git checkout refs/tags/v0.3.1
$ kubectl create -f deploy/1.8+/
```

## Install Ingress controller
### Prerequisites
- Domain owned by you (set to load balancer)

### Steps
For now, you can only access drucker services nghttpx Ingress.  
Please follow instructions below to set up nghttpx Ingress Controller.

1. Run the commands

```bash
$ git clone https://github.com/zlabjp/nghttpx-ingress-lb.git
$ cd nghttpx-ingress-lb
# ELB will be created in the same region as your EKS cluster
$ kubectl apply -f examples/proxyproto/
```

2. Register your domain in Route 53
- Set up hosted zone in [Route 53 Hosted Zone](https://console.aws.amazon.com/route53/home) and register your domain
- Create record set
  - Name: `*.<your-domain>`
  - Alias: `Yes`
  - Alias Target: `domain name of ELB created by running the commands above`

Then, http requests to `*.<your-domain>` will reach to your EKS cluster.

## Drucker
Please follow the Drucker part on this [page](https://github.com/drucker/drucker-parent/blob/master/docs/Installation.md) to install drucker and deploy your services.  

When you add Kubernetes Host in drucker-dashboard, please refer the information.

- DNS Name: domain name you set to LoadBalancer in [Install Ingress controller](https://github.com/rekcurd/drucker-parent/blob/master/docs/Installation-eks.md#install-ingress-controller)
- Host Config File: the file you obtain by running `aws eks update-kubeconfig --name cluster_name` in [EKS official document](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html)
