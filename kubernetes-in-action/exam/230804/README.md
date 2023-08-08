```shell
# Exam1 - check
# Get the list of nodes in JSON format and store it in a file at {your-folder}/json-{your-name}.json
kubectl get nodes -o json > /Users/younghyo/Projects/k8s-guide/kubernetes-in-action/exam/230804/json-dante.json

# Exam2
# Create Namespace exam-{your-name}
kubectl create namespace exam-dante

# Exam 3
# Create a new deployment {your-name}-deployment --image={your-image} --replicas=2 of namespaces exam-{your-name}
kubectl create deployment dante-deployment --image=busybox --replicas=2 -n exam-dante

kubectl apply -f ./exam3.yaml -n exam-dante
kubectl get deploy -n exam-dante
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
dante-deployment   2/2     2            2           36s

# Exam 4 - check
# Print the names of all deployments in the exam-{your_name} namespace in the following format:
# DEPLOYMENT CONTAINER_IMAGE READY_REPLICAS NAMESPACE
kubectl get deploy -n exam-dante

kubectl get deploy -n exam-dante -o custom-columns=DEPLOYMENT:.metadata.name,CONTAINER_IMAGE:.spec.template.spec.containers.image,READY_REPLICAS:.spec.replicas,NAMESPACE:.metadata.namespace
DEPLOYMENT         CONTAINER_IMAGE   READY_REPLICAS   NAMESPACE
dante-deployment   <none>            2                exam-dante

# Exam 5
# Create a new deployment called nginx-deploy, with image nginx:1.16 and 1 replica. Record the version. 
# Next upgrade the deployment to version 1.17 using rolling update. 
# Make sure there version update is recorded int the resource annotation.
kubectl create deploy nginx-deploy -n exam-dante --image=nginx:1.16 --replicas=1
kubectl set image deployment/nginx-deploy nginx=nginx:1.17 -n exam-dante

kubectl apply -f ./exam5_nginx1_16.yaml -n exam-dante
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
nginx-deploy       1/1     1            1           15s

kubectl set image deploy/nginx-deploy -n exam-dante nginx=nginx:1.17

kubectl rollout history deploy/nginx-deploy -n exam-dante
deployment.apps/nginx-deploy
REVISION  CHANGE-CAUSE
1         <none>
2         <none>

# Exam 6
# Create a new service "web-application" :
# Name: web-application; Type: NodePort; port: 8080; nodePort: 30083; selector: simple-webapp; targetPort: 8080;
kubectl apply -f ./exam6.yaml -n exam-dante

kubectl get services -n exam-dante
NAME              TYPE       CLUSTER-IP    EXTERNAL-IP   PORT(S)          AGE
web-application   NodePort   10.3.247.69   <none>        8081:30083/TCP   9s


# Exam 7
# Create a service {your-name}-service to expose the messaging application within the cluster on port 9090
kubectl apply -f ./exam7.yaml -n exam-dante
service/dante-service created

kubectl get svc -n exam-dante
NAME              TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
dante-service     ClusterIP   10.3.242.157   <none>        9090/TCP         5s
web-application   NodePort    10.3.247.69    <none>        8081:30083/TCP   12h


# Exam 8
# Create a deployment named {your-name}-deployment using a pod {your-name}-pod of the image {your-image} with 2 replicas with yaml.
kubectl apply -f ./exam8_deploy.yaml -n exam-dante

# Change Replica count from 2 to 1 at yaml file and update your original deployment.
kubectl apply -f ./exam8_deploy_replicas_1.yaml -n exam-dante

# Setting config-map as a volume of pod config-map key=value
# hello=world drink=good happy=work
kubectl apply -f ./exam8_configmaps.yaml -n exam-dante
kubectl apply -f ./exam8_deploy_configmaps_volume.yaml -n exam-dante


# Exam 9
# Access your pod and make a file and print "Hello World! to "hello.txt" files.
kubectl get pods -n exam-dante
NAME                                READY   STATUS    RESTARTS   AGE
dante-deploy-5dd4d4d6c9-vxn84       1/1     Running   0          13m
dante-deployment-57d4cf5785-c5k5k   1/1     Running   0          3d19h
dante-deployment-57d4cf5785-vtxqg   1/1     Running   0          3d19h
nginx-deploy-7df54cf9fd-9fdjq       1/1     Running   0          22h

kubectl exec dante-deploy-5dd4d4d6c9-vxn84 -n exam-dante -i -t /bin/bash
touch hello.txt
echo "Hello World!" > hello.txt
cat hello.txt
exit


# Exam 10
# Create a pod myapp-pod and the use an initContainer that uses the busybox image and sleeps for 20 seconds

```
