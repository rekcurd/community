# Assign DNS
Keep a wildcard DNS (e.g. `*.example.com`) to the Kubernetes cluster nodes.

We uses Kubernetes's hostname routing via ingress to access the services which run on Kubernetes. Subdomain name is assigned as the application access point. For example, `application_name=sample` and `service_level=development` will be accessible on `sample-development.example.com`.

## For EKS Users
If you set up k8s with Amazon EKS, ELB is created in [this section](./Installation-eks.md#install-ingress-controller).  
Then, set up hosted zone in [Route 53 Hosted Zone](https://console.aws.amazon.com/route53/home) and register your wildcard domain as an Alias record of the ELB.
