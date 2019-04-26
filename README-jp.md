# About Rekcurd projects
<img src="./docs/img/logo.png" width="100">

Rekcurdは機械学習モジュールの運用のためのソフトウェア群です。「機械学習モジュールの配信を簡単に」「機械学習モデルの管理と機械学習モジュールのデプロイを簡単に」「機械学習モジュールの組み込みを簡単に」というコンセプトで設計しています。RekcurdはKubernetesをサポートしています。


## Features
- Kubernetes
- Istio
- Developer-Friendly web interface ([Rekcurd-dashboard](https://github.com/rekcurd/dashboard))
  - 機械学習サービスのデプロイ
  - トラフィックコントロール (AB testing)
  - 機械学習モデルのアップロード、バージョニング
  - 機械学習モデルの切り替え
  - 性能評価データのアップロード、バージョニング (TBD)
  - 性能評価結果の可視化 (TBD)
- Django-like gRPC micro-framework ([Rekcurd](https://github.com/rekcurd/rekcurd-python))
- SDK ([Rekcurd-client](https://github.com/rekcurd/python-client))


## Components
- [Rekcurd](https://github.com/rekcurd/rekcurd-python): 機械学習モジュールのウェブサービス化のためのプロジェクト。gRPCのマイクロフレームワークで、[Django](https://docs.djangoproject.com/) や [Flask](http://flask.pocoo.org/) のように使えます。
- [Rekcurd-dashboard](https://github.com/rekcurd/dashboard): 機械学習モジュールのデプロイと機械学習モデルの管理のためのプロジェクトです。あらゆるRekcurdサービスをWebUIで扱うことができます。また、KubernetesやIstioの操作もできます。
- [Rekcurd-client](https://github.com/rekcurd/python-client): 機械学習モジュールの組み込みのためのプロジェクトです。あらゆるRekcurdサービスに接続できます。

### Sub components
- [dockerfiles](https://github.com/rekcurd/dockerfiles): Rekcurd exampleのためのコンテナイメージです。[Docker Hub](https://hub.docker.com/r/rekcurd/rekcurd)と連携していますので、`docker pull`で利用することもできます。
- [grpc-proto](https://github.com/rekcurd/grpc-proto): RekcurdのためのgRPC specです。
- [Airflow-plugin](https://github.com/rekcurd/airflow-plugin): Airflowプラグインです。Rekcurd DashboardのAPIに接続します。
- [rekcurd-example](https://github.com/rekcurd/rekcurd-example): Rekcurdのサンプルです。
- [rekcurd-client-example](https://github.com/rekcurd/rekcurd-client-example): Rekcurd clientのサンプルです。


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
- [Slack](https://rekcurd.slack.com/)
- [Google group](https://groups.google.com/forum/?hl=ja#!forum/rekcurd-dev)


## Contributors
- [keigohtr](https://github.com/keigohtr): Lead committer
- [Kenji Yamauchi](https://github.com/yustoris): Frontend
- [Wen Chun Kao](https://github.com/jkw552403): Unit test
- [yoquankara](https://github.com/yoquankara): Code review
- [Shimpei Yotsukura](https://github.com/shimpei-yotsukura): DAO
- [sugyan](https://github.com/sugyan): Authentication
- [yuki-mt](https://github.com/yuki-mt): Committer
