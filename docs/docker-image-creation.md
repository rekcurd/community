# Docker image
Our Dockerfile is available [here](https://github.com/rekcurd/dockerfiles). 

You can also use our simplest docker image on [Docker Hub](https://hub.docker.com/r/rekcurd/rekcurd)
```bash
$ docker pull rekcurd/rekcurd:v0.2.1
```

Since Kubernetes uses a container image, if you want to use your own docker image, please extend our [Dockerfile](https://github.com/rekcurd/dockerfiles). 

In some use cases, you cannot open your docker image. If you want to use your own private docker registry, please follow the official document [here](https://docs.docker.com/registry/deploying/)
