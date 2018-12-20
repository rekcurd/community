# Setup MySQL
Use your favorite (e.g. bare metal, GCP, AWS). DB scheme is automatically set by `Rekcurd` and `Rekcurd-dashboard`. DDL privilege is required to the nodes of all `Rekcurd` and `Rekcurd-dashboard` services.

In some cases, when you access your MySQL DB, you need to assign all IP addresses which are joined in Kubernetes cluster a DDL privilege. This operation is really troublesome, so we recommend to use [ProxySQL](https://proxysql.com/). The flow is like this; `Rekcurd` or `Rekcurd-dashboard` <-> ProxySQL <-> MySQL. In this architecture, you just assign ProxySQL server a DDL privilege.
