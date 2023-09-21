```shell

# exam5
kubectl get pods -A > ./pods-list.yaml

# exam6
kubectl get pods --sort-by="metadata.name" -A
```