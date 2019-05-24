# Setup Kubernetes with Amazon EKS
## Environments
* EKS version: eks.3
* Kubernetes version: 1.10
* Rekcurd version: 1.0.0
* Rekcurd dashboard version: 1.0.0

## Steps

Basically, you just need to follow [the official document](https://docs.aws.amazon.com/eks/latest/userguide/getting-started-console.html).  
The diffrences are:

- You need to use [our YAML file](https://github.com/rekcurd/community/blob/master/aws/config) for CloudFormation to launch your worker nodes in `Step 3: Launch and Configure Amazon EKS Worker Nodes`.  
  The details are in the section below.

### Edit and Upload YAML file to launch your worker nodes.
1. Edit [env-list.txt](https://github.com/rekcurd/community/blob/master/aws/config/env-list.txt).
    - If you want only development, staging and production environments for Rekcurd, delete beta and sandbox from the file (or comment out with `#`)
2. Run [build_eks_nodegroup.py](https://github.com/rekcurd/community/blob/master/aws/scripts/build_eks_nodegroup.py)
3. Follow the instructions instead of the official documemnt Step 3-5 and 3-6.
    1. For **Choose a template**, select **Upload a template to Amazon S3.**
    2. Select amazon-eks-nodegroup.yaml generated in [config directory](https://github.com/rekcurd/community/blob/master/aws/config) and choose **Next.**

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
