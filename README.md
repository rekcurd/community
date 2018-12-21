# Rekcurd-Parent
<img src="./docs/img/logo.png" width="100">

Rekcurd is a software package of managing machine learning (ML) modules. Rekcurd makes it "easy to serve ML module", "easy to manage ML model and deploy ML module" and "easy to integrate into the existing service". Rekcurd can be run on Kubernetes.


## Features
- High Availability
- Free from managing
  - Upload the latest ML model
  - Versioning ML models
  - Evaluate the accuracy of ML model and visualize it (TBD)
  - Switching ML model to the ML module
  - Non stop deployment (a.k.a Rolling update)*
- Free from monitoring
  - Health check and auto healing*
  - Load balancing and auto scaling*
- Others
  - WebUI available
  - Service level (development/staging/production) management*
  - AB testing and canary release (TBD)
  - Log forwarding*
  - Easy to integrate into the existing service

*Kubernetes features


## Components
- [Rekcurd](https://github.com/rekcurd/drucker): Project for serving ML module. This is a gRPC micro-framework and it can be used like [Flask](http://flask.pocoo.org/).
- [Rekcurd-dashboard](https://github.com/rekcurd/drucker-dashboard): Project for managing ML model and deploying ML module. Any Rekcurd service is manageable. It can deploy the Rekcurd service to Kubernetes cluster.
- [Rekcurd-client](https://github.com/rekcurd/drucker-client): Project for integrating ML module. Any Rekcurd service is connectable. It can connect the Rekcurd service on Kubernetes.

### Sub components
- [dockerfiles](https://github.com/rekcurd/dockerfiles): Project for Rekcurd's container image. Since it works with [Docker Hub](https://hub.docker.com/r/rekcurd/rekcurd), you can pull image via `docker pull`.
- [drucker-grpc-proto](https://github.com/rekcurd/drucker-grpc-proto): Project for Rekcurd's gRPC spec.
- [Drucker-example](https://github.com/rekcurd/drucker-example): Example project. This sample turns a scikit-learn Linear SVC algorithm into a Rekcurd service.


## Environment
<img src="./docs/img/architecture.png" width="480">

### Minimum environment
- Python 3.6

### Recommended environment for production
- Python 3.6
- Kubernetes 1.9~
- MySQL 5.7
- Online storage (e.g. AWS S3, GCS, WebDAV, ...)
- DNS
- (If necessary) Private Docker registry
- (If necessary) Private git repository (e.g. GitHub Enterprise, GitLab, ...)


## Installation
See [docs](./docs/).


## Roadmap
### ~v0.2
Initial release. This version is a Minimal Viable Software.

### v0.4
- Pipnize

### v1.0
- Access control
- User authentication
- ML model evaluation and visualization
- Rancher/GCP/AWS installation support
- Unittest and Travis support

### v2.0
- C++/Java support
- Istio support
- Traffic tracing
- AB test/Canary release
- Access control (Access token)
- ML evaluation model management and versioning
- GPU support
- Kubeflow support
- Airflow support
- GitOps support

### v3.0
- Security

### vX.Y
- Open platform (e.g. marketplace)


## Support
Give us **Star**, **Issues** and **Pull requests**!

- [Twitter](https://twitter.com/rekcurd)
- [Facebook](https://www.facebook.com/rekcurd/)
- [Slack](https://rekcurd.slack.com/)
  - Join [rekcurd.slack.com](https://join.slack.com/t/rekcurd/shared_invite/enQtNTA4NDU3ODAzMzgwLTVhNWYyMTUwOTQ2NGZjMzAzNzYzNTZlZDYzY2ViMjVlOWExY2EwYmRlMDhhMDE3ZmNlNGE2Nzk4NTYzZjAwOTM)
- [Google group](https://groups.google.com/forum/?hl=ja#!forum/rekcurd-dev)

## Contributors
- [keigohtr](https://github.com/keigohtr)
- [Kenji Yamauchi](https://github.com/yustoris)
- [Wen Chun Kao](https://github.com/jkw552403)
- [yoquankara](https://github.com/yoquankara)
- [Shimpei Yotsukura](https://github.com/shimpei-yotsukura)
- [sugyan](https://github.com/sugyan)
- [yuki-mt](https://github.com/yuki-mt)
