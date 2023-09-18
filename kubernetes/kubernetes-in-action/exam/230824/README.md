1. Create an nginx pod and set an env value as 'var1=val1'. Check the env value existence within the pod.
```shell
kubectl apply -f ./exam1.yaml -n exam-dante
```

2. Create an nginx pod and exec into containers and verify that main.txt exist.
```shell
kubectl exec -i -t pod/nginx-dante -n exam-dante -- /bin/bash

```

3. Create a Pod with main container busybox and which executes this "while true; do echo `Hi I am from Main container' >> /var/log/index.html; sleep 5; done" and with sidecar container with nginx image which exposes on port 80. Use emptyDir Volume and mount this volume on path /var/log for busybox and on path /usr/share/nginx/html for nginx container. Verify both containers are running.
```shell
kubectl apply -f ./exam3.yaml -n exam-dante

kubectl get pods -n exam-dante

NAME                                READY   STATUS             RESTARTS           AGE
busybox-dante                       0/1     Init:0/1           0                  12s
nginx-dante                         1/1     Running            0                  14m
```

4. Create a Pod with three busy box containers with commands "ls; sleep 3600;", "echo Hello World; sleep 3600;" and "echo this is the third container; sleep 3600" respectively and check the status
```shell
kubectl apply -f ./exam4.yaml -n exam-dante
```

5. Check logs of each container that "busyboxpod-{1,2,3}"
```shell
kubectl logs pod/busybox-dante-exam4 -n exam-dante
```

6. Create a redis pod, and have it use a non-persistent storage Note: In exam, you will have access to kubernetes.io site, Refer : https://kubernetes.io/docs/tasks/configure-pod-container/configurevolume-storage/
```shell
kubectl apply -f ./exam6.yaml
```

7. Change the Image version back to 1.17.1 for the pod you just updated and observe the changes
```shell
kubectl apply -f ./exam7.yaml
pod/redis-dante-exam6 configured
```

8. Change the Image version to 1.15-alpine for the pod you just created and verify the image version is updated.

9. Create the nginx pod with version 1.17.4 and expose it on port 80
```shell
kubectl apply -f ./exam9.yaml
```

10. Create a redis pod and expose it on port 6379
```shell
kubectl apply -f ./exam10.yaml
```

11. Delete the pod without any delay (force delete)
```shell

```

12. List "nginx-dev" and "nginx-prod" pod and delete those pods
```shell
kubectl get pods -n nginx-dev,nginx-prod
No resources found in nginx-dev,nginx-prod namespace.

kubectl delete pods -n nginx-dev,nginx-prod
error: resource(s) were provided, but no name was specified
```

13. List all the pods showing name and namespace with a json path expression
```shell

```

14. List all the pods sorted by created timestamp
```shell
kubectl get pods --sort-by="metadata.creationTimestamp" -n exam-dante
NAME                                READY   STATUS             RESTARTS           AGE
dante-deployment-85ccd66555-kdtg5   0/1     CrashLoopBackOff   5857 (75s ago)     21d
dante-deployment-85ccd66555-nmcj7   0/1     CrashLoopBackOff   5874 (5m14s ago)   21d
nginx-deploy-c848b6868-8vjw6        1/1     Running            0                  21d
nginx-dante                         1/1     Running            0                  51m
busybox-dante                       0/1     Init:0/1           0                  36m
busybox-dante-exam4                 0/1     CrashLoopBackOff   11 (2m11s ago)     33m
redis-dante-exam6                   0/1     Pending            0                  19m
nginx-dante-exam9                   1/1     Running            0                  11m
redis-dante-exam10                  1/1     Running            0                  11m
```

15. List all the pods sorted by name
```shell
kubectl get pods --sort-by="metadata.name" -n exam-dante
NAME                                READY   STATUS             RESTARTS           AGE
busybox-dante                       0/1     Init:0/1           0                  37m
busybox-dante-exam4                 0/1     CrashLoopBackOff   11 (3m22s ago)     34m
dante-deployment-85ccd66555-kdtg5   0/1     CrashLoopBackOff   5857 (2m26s ago)   21d
dante-deployment-85ccd66555-nmcj7   0/1     CrashLoopBackOff   5875 (70s ago)     21d
nginx-dante                         1/1     Running            0                  52m
nginx-dante-exam9                   1/1     Running            0                  13m
nginx-deploy-c848b6868-8vjw6        1/1     Running            0                  21d
redis-dante-exam6                   0/1     Pending            0                  20m
redis-dante-exam10                  1/1     Running            0                  12m
```