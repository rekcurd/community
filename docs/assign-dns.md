# Assign DNS
Keep a wildcard DNS (e.g. `*.example.com`) to the Kubernetes cluster nodes.

We uses Kubernetes's hostname routing via ingress to access the services which run on Kubernetes. Subdomain name is assigned as the application access point. For example, `application_name=sample` and `service_level=development` will be accessible on `sample-development.example.com`.
