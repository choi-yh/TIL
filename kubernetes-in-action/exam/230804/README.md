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

# Exam 6
# Create a new service "web-application" :
# Name: web-application; Type: NodePort; port: 8080; nodePort: 30083; selector: simple-webapp; targetPort: 8080;
kubectl apply -f ./exam6.yaml -n exam-dante

# Exam 7
# Create a service {your-name}-service to expose the messaging application within the cluster on port 9090


# Exam 8
# Create a deployment named {your-name}-deployment using a pod {your-name}-pod of the image {your-image} with 2 replicas with yaml.
# Change Replica count from 2 to 1 at yaml file and update your original deployment.
# Setting config-map as a volume of pod config-map key=value
# hello=world drink=good happy=work


# Exam 9
# Access your pod and make a file and print "Hello World! to "hello.txt" files.


# Exam 10
# Create a pod myapp-pod and the use an initContainer that uses the busybox image and sleeps for 20 seconds

```
