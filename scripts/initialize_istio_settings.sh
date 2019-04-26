#!/usr/bin/env bash

echo "Start initialize_istio_settings.sh"

cat <<EOF | kubectl apply -f -
apiVersion: networking.istio.io/v1alpha3
kind: ServiceEntry
metadata:
name: rekcurd-egress-service-entry
spec:
hosts:
- "*.local"
- "*.com"
- "*.jp"
- "*.org"
- "*.net"
- "*.io"
- "*.edu"
- "*.me"
ports:
- number: 80
  name: http
  protocol: HTTP
- number: 443
  name: https
  protocol: HTTPS
- number: 20306
  name: tcp
  protocol: TCP
resolution: NONE
location: MESH_EXTERNAL
---
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
name: rekcurd-egress-virtual-service
spec:
hosts:
- "*.local"
- "*.com"
- "*.jp"
- "*.org"
- "*.net"
- "*.io"
- "*.edu"
- "*.me"
tls:
- match:
  - port: 443
    sni_hosts:
    - "*.local"
  route:
  - destination:
      host: "*.local"
      port:
        number: 443
    weight: 100
- match:
  - port: 443
    sni_hosts:
    - "*.com"
  route:
  - destination:
      host: "*.com"
      port:
        number: 443
    weight: 100
- match:
  - port: 443
    sni_hosts:
    - "*.jp"
  route:
  - destination:
      host: "*.jp"
      port:
        number: 443
    weight: 100
- match:
  - port: 443
    sni_hosts:
    - "*.org"
  route:
  - destination:
      host: "*.org"
      port:
        number: 443
    weight: 100
- match:
  - port: 443
    sni_hosts:
    - "*.net"
  route:
  - destination:
      host: "*.net"
      port:
        number: 443
    weight: 100
- match:
  - port: 443
    sni_hosts:
    - "*.io"
  route:
  - destination:
      host: "*.io"
      port:
        number: 443
    weight: 100
- match:
  - port: 443
    sni_hosts:
    - "*.edu"
  route:
  - destination:
      host: "*.edu"
      port:
        number: 443
    weight: 100
- match:
  - port: 443
    sni_hosts:
    - "*.me"
  route:
  - destination:
      host: "*.me"
      port:
        number: 443
    weight: 100
---
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
name: rekcurd-ingress-gateway
namespace: development
spec:
selector:
  istio: ingressgateway
servers:
- port:
    number: 80
    name: http
    protocol: HTTP
  hosts:
  - "*"
---
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
name: rekcurd-ingress-gateway
namespace: staging
spec:
selector:
  istio: ingressgateway
servers:
- port:
    number: 80
    name: http
    protocol: HTTP
  hosts:
  - "*"
---
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
name: rekcurd-ingress-gateway
namespace: production
spec:
selector:
  istio: ingressgateway
servers:
- port:
    number: 80
    name: http
    protocol: HTTP
  hosts:
  - "*"
---
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
name: rekcurd-ingress-gateway
namespace: sandbox
spec:
selector:
  istio: ingressgateway
servers:
- port:
    number: 80
    name: http
    protocol: HTTP
  hosts:
  - "*"
---
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
name: rekcurd-ingress-gateway
namespace: beta
spec:
selector:
  istio: ingressgateway
servers:
- port:
    number: 80
    name: http
    protocol: HTTP
  hosts:
  - "*"
EOF

echo "...End"
