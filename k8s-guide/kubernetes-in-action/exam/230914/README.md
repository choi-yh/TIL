```shell

# exam4
kubectl apply -f ./exam4.yaml -n exam-dante
kubectl scale deployment/nginx-deployment -n exam-dante --replicas=6
kubectl describe deploy -n exam-dante

Events:
  Type    Reason             Age    From                   Message
  ----    ------             ----   ----                   -------
  Normal  ScalingReplicaSet  2m26s  deployment-controller  Scaled up replica set nginx-deployment-7fb96c846b to 3
  Normal  ScalingReplicaSet  51s    deployment-controller  Scaled up replica set nginx-deployment-7fb96c846b to 6 from 3
```