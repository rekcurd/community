#!/usr/bin/env bash
# Delete clusters
minikube delete -p drucker-test1
minikube delete -p drucker-test2

rm -f ${KUBE_CONFIG_PATH1:-/tmp/kube-config-path1}
rm -f ${KUBE_CONFIG_PATH1:-/tmp/kube-config-path2}
