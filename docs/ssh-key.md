# SSH Key
Put your SSH key to `/root/.ssh/` on every Kubernetes cluster nodes.

In some use cases, you need to use your private git repository (e.g. GitHub Enterprise, GitLab). In those cases, you need to use your own SSH key to access them. Please put your SSH key to `/root/.ssh/` on every Kubernetes cluster nodes, then Rekcurd pod will mount it to pod's `/root/.ssh`.

## For EKS Users
If you set up k8s with Amazon EKS, you set your SSH key in ["Edit and Upload YAML file to launch your worker nodes" section](./Installation-eks.md#edit-and-upload-yaml-file-to-launch-your-worker-nodes).
