# About Rekcurd projects
<img src="./docs/img/logo.png" width="100">

Rekcurd is a software package of managing machine learning (ML) modules. Rekcurd makes it "easy to serve ML module", "easy to manage and deploy ML models" and "easy to integrate into the existing service". Rekcurd can be run on Kubernetes.


## Features
- Kubernetes
- Istio
- Developer-Friendly web interface ([Rekcurd-dashboard](https://github.com/rekcurd/dashboard))
  - Deploying ML service
  - Controlling traffic (AB testing)
  - Upload and versioning ML model
  - Switch ML model of ML service
  - Upload and versioning quality assurance data (TBD)
  - Visualizing evaluation result of ML model using QA data (TBD)
- Django-like gRPC micro-framework ([Rekcurd](https://github.com/rekcurd/rekcurd-python))
- SDK ([Rekcurd-client](https://github.com/rekcurd/python-client))


## Components
- [Rekcurd](https://github.com/rekcurd/rekcurd-python): Project for serving ML module. This is a gRPC micro-framework and it can be used like [Django](https://docs.djangoproject.com/) and [Flask](http://flask.pocoo.org/).
- [Rekcurd-dashboard](https://github.com/rekcurd/dashboard): Project for managing ML model and deploying ML module. Any Rekcurd service is manageable. It can deploy the Rekcurd service to Kubernetes cluster and can control traffic weights which Istio manages.
- [Rekcurd-client](https://github.com/rekcurd/python-client): Project for integrating ML module. Any Rekcurd service is connectable. It can connect the Rekcurd service on Kubernetes.

### Sub components
- [dockerfiles](https://github.com/rekcurd/dockerfiles): Rekcurd's container image. Since it works with [Docker Hub](https://hub.docker.com/r/rekcurd/rekcurd), you can pull image via `docker pull`.
- [grpc-proto](https://github.com/rekcurd/grpc-proto): Rekcurd's gRPC spec.
- [Airflow-plugin](https://github.com/rekcurd/airflow-plugin): Airflow Plugins for Rekcurd Dashboard
- [rekcurd-example](https://github.com/rekcurd/rekcurd-example): Example project of rekcurd.
- [rekcurd-client-example](https://github.com/rekcurd/rekcurd-client-example): Example project of rekcurd-client.


## Architecture
<img src="./docs/img/architecture.png" width="480">

### Recommended requirement
- Python 3.6
- Kubernetes 1.11~
- MySQL 5.7
- Online storage (Ceph, AWS S3)
- (If necessary) Private Docker registry
- (If necessary) Private git repository (e.g. GitHub Enterprise, GitLab, ...)


## Getting Started
See [docs](./docs/).


## Support
Give us **Star**, **Issues** and **Pull requests**!

- [Twitter](https://twitter.com/rekcurd)
- [Facebook](https://www.facebook.com/rekcurd/)
- [Slack](https://join.slack.com/t/rekcurd/shared_invite/enQtNTA4NDU3ODAzMzgwLTVhNWYyMTUwOTQ2NGZjMzAzNzYzNTZlZDYzY2ViMjVlOWExY2EwYmRlMDhhMDE3ZmNlNGE2Nzk4NTYzZjAwOTM)
- [Google group](https://groups.google.com/forum/?hl=ja#!forum/rekcurd-dev)


## Contributors
- [keigohtr](https://github.com/keigohtr): Lead committer
- [Kenji Yamauchi](https://github.com/yustoris): Frontend
- [Wen Chun Kao](https://github.com/jkw552403): Unit test
- [yoquankara](https://github.com/yoquankara): Code review
- [Shimpei Yotsukura](https://github.com/shimpei-yotsukura): DAO
- [sugyan](https://github.com/sugyan): Authentication
- [yuki-mt](https://github.com/yuki-mt): Committer
