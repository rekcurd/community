# Drucker-Parent
<img src="./docs/img/logo.png" width="100">

Drucker is a microservice framework for serving a machine learning module. Drucker makes it easy to serve, manage and integrate your ML models into your existing services. Moreover, Drucker can be used on Kubernetes. We strongly recommend to use Kubernetes for a production service.

## Components
- [Drucker](https://github.com/drucker/drucker): Serving framework for a machine learning module.
- [Drucker-dashboard](https://github.com/drucker/drucker-dashboard): Management web service for the machine learning models to the drucker service.
- [Drucker-client](https://github.com/drucker/drucker-client): SDK for accessing a drucker service.
- [Drucker-example](https://github.com/drucker/drucker-example): Example of how to use drucker.

## Requirements
- Drucker v0.2.0
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
  - Managing the service level (e.g. development/staging/production)
  - [WebUI](https://github.com/drucker/drucker-dashboard)
  - [SDK](https://github.com/drucker/drucker-client)
  - AB testing
  - Managing all ML services
  - Log forwarding

## Installation
See [here](./docs).

## Unit test
Discover test cases automatically.

```
python -m unittest discover -v
```

Execute test cases one by one

```
python -m unittest tests/worker/test_peter_servicer.py
python -m unittest tests/example/test_peter_client.py
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