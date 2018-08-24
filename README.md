# Drucker-Parent
<img src="./docs/img/logo.png" width="100">

Drucker is a microservice framework for serving a machine learning module. Drucker makes it easy to serve, manage and integrate your ML models into your existing services. Moreover, Drucker can be used on Kubernetes. We strongly recommend to use Kubernetes for a production service.

## Components
- [Drucker](https://github.com/drucker/drucker): Serving framework for a machine learning module.
- [Drucker-dashboard](https://github.com/drucker/drucker-dashboard): Management web service for the machine learning models to the drucker service.
- [Drucker-client](https://github.com/drucker/drucker-client): SDK for accessing a drucker service.
- [Drucker-example](https://github.com/drucker/drucker-example): Example of how to use drucker.

## Requirements
- Drucker v0.3.0
- Python 3.6
- Kubernetes 1.9
- MySQL 5.7
- Online storage (e.g. AWS EBS, GCS, WebDAV, ...)
- Online Docker registry
- Online git repository

## Features
- High Availability
- Management
  - Upload the latest model
  - Switch a model without stopping services
  - Versioning models
- Monitor
  - Load balancing
  - Auto healing
  - Auto scaling
  - (WIP) Performance/Results check
- Others
  - Managing the service level (e.g. development/beta/staging/sandbox/production)
  - [WebUI](https://github.com/drucker/drucker-dashboard)
  - [SDK](https://github.com/drucker/drucker-client)
  - AB testing
  - Managing all ML services
  - Log forwarding

## Installation
See [here](./docs).

## Unit test

### Requirements
- minikube v0.25.2 (later version upto v0.28.2 doesn't work well on macOS)

### Execute test case all

```
$ sh tests/drucker_dashboard/startup.sh
$ python -m unittest discover
$ sh tests/drucker_dashboard/cleanup.sh
```

### Execute test cases one by one

```
$ sh drucker-grpc-proto/run_codegen.sh
$ sh drucker_client/drucker-grpc-proto/run_codegen.sh
$ python -m unittest tests/drucker/test_worker_servicer.py
$ python -m unittest tests/drucker_client/test_worker_client.py
$ sh tests/drucker_dashboard/startup.sh
$ python -m unittest tests/drucker_dashboard/test_application.py
$ python -m unittest tests/drucker_dashboard/test_kubernetes.py
$ python -m unittest tests/drucker_dashboard/test_model.py
$ python -m unittest tests/drucker_dashboard/test_service.py
$ sh tests/drucker_dashboard/cleanup.sh
```

## Support
Give us `Issues` and `Pull requests`.

## Contributors
- [keigohtr](https://github.com/keigohtr)
- [Kenji Yamauchi](https://github.com/yustoris)
- [Wen Chun Kao](https://github.com/jkw552403)
- [yoquankara](https://github.com/yoquankara)
- [Shimpei Yotsukura](https://github.com/shimpei-yotsukura)
- [sugyan](https://github.com/sugyan)
