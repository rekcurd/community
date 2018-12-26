# Setup Namespace
We uses these namespaces for Rekcurd. 
- development
- staging
- production
- beta
- sandbox

## Apply namespaces
Apply the code below or upload them via "Kubernetes Dashboard".

```bash
$ cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Namespace
metadata:
  name: development
---
apiVersion: v1
kind: Namespace
metadata:
  name: beta
---
apiVersion: v1
kind: Namespace
metadata:
  name: staging
---
apiVersion: v1
kind: Namespace
metadata:
  name: sandbox
---
apiVersion: v1
kind: Namespace
metadata:
  name: production
EOF
```
