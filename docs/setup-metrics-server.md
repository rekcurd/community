# Install Metrics Server
You need to install metrics server for autoscaler to work.
Please run the following commands to set up metrics server.

```bash
$ git clone https://github.com/kubernetes-incubator/metrics-server.git
$ cd metrics-server
$ git checkout refs/tags/v0.3.1
$ kubectl create -f deploy/1.8+/
```
