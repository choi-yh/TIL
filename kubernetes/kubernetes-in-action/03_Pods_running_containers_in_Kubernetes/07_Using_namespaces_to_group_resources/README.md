# Index
* [3.7 네임스페이스를 사용한 리소스 그룹화](#37-네임스페이스를-사용한-리소스-그룹화)
  * [3.7.1 네임스페이스의 필요성](#371-네임스페이스의-필요성)
  * [3.7.3 네임스페이스 생성](#373-네임스페이스-생성)
  * [3.7.4 다른 네임스페이스의 오브젝트 관리](#374-다른-네임스페이스의-오브젝트-관리)
  * [3.7.5 네임스페이스가 제공하는 격리 이해](#375-네임스페이스가-제공하는-격리-이해)

---

# [3.7 네임스페이스를 사용한 리소스 그룹화](#Index)
* 오브젝트들은 여러 레이블을 가질 수 있기 때문에 오브젝트 그룹은 겹칠 수 있다.
* 클러스터에서 작업을 수행할 때, 레이블 셀렉터를 지정하지 않는다면 모든 오브젝트를 보게 된다.
* 오브젝트를 그룹별로 구분하기 위해 **쿠버네티스는 오브젝트를 네임스페이스로 그룹화**한다.
  * 여기서 네임스페이스는 프로세스 격리를 위한 리눅스 네임스페이스는 아니다.


## [3.7.1 네임스페이스의 필요성](#Index)
* 리소스 이름은 네임스페이스 안에서만 고유하면 된다.

---

## [3.7.2 다른 네임스페이스와 파드 살펴보기](#Index)

```shell
kubecolor get namespace
#NAME                   STATUS   AGE
#default                Active   74d
#kube-node-lease        Active   74d
#kube-public            Active   74d
#kube-system            Active   74d
#kubernetes-dashboard   Active   8d

kubectl get pod --namespace kube-system # kube-system namespace 에 있는 파드 확인
#NAME                               READY   STATUS    RESTARTS      AGE
#coredns-787d4945fb-9d5m4           1/1     Running   3 (6d ago)    74d
#etcd-minikube                      1/1     Running   3 (6d ago)    74d
#kube-apiserver-minikube            1/1     Running   3 (6d ago)    74d
#kube-controller-manager-minikube   1/1     Running   3 (6d ago)    74d
#kube-proxy-7gk4p                   1/1     Running   3 (6d ago)    74d
#kube-scheduler-minikube            1/1     Running   3 (6d ago)    74d
#storage-provisioner                1/1     Running   7 (25h ago)   74d
```

* 여러 사용자 또는 그룹이 동일한 쿠버네티스 클러스터를 사용하고 있고, 각자 자신들의 리소스를 관리한다면 각각 고유한 네임스페이스를 사용해야 한다.

---

## [3.7.3 네임스페이스 생성](#Index)

### YAML 파일에서 네임스페이스 생성

```shell
kubectl create -f custom-namespace.yaml
#namespace/custom-namespace created

# namespace 삭제
kubectl delete namespace custom-namespace
#namespace "custom-namespace" deletedmespace
```

### kubectl create namespace 명령으로 네임스페이스 생성
```shell
kubectl create namespace custom-namespace
#namespace/custom-namespace created
```

> 대부분의 오브젝트 명은 RFC 1035 (도메인 이름)에 지정된 규칙을 따라야 한다.  
> 글자, 숫자, 대시, 점 포함 가능  
> 네임스페이스를 포함한 몇몇 리소스는 점을 포함 할 수 없다.

---

## [3.7.4 다른 네임스페이스의 오브젝트 관리](#Index)

* 생성한 네임스페이스 안에 리소스를 만들기 위해서는
  * metadata  섹션에 `namespace: custom-namespace` 항목을 넣거나 `kubectl create` 사용시 네임스페이스를 지정한다.

```shell
kubectl create -f kubia-manual.yaml -n custom-namespace
#pod/kubia-manual created

kubectl get pods --namespace=custom-namespace
#NAME           READY   STATUS    RESTARTS   AGE
#kubia-manual   1/1     Running   0          36s
```
* kubectl 명령 사용시 네임스페이스를 지정하지 않으면 kubectl 은 kubectl context 에 구성된 기본 네임스페이스에서 작업을 수행한다.
* 현재 컨텍스트의 네임스페이스와 현재 컨텍스트 자체는 kubectl config 를 사용해 변경 가능

```shell
kubectl config get-contexts
#CURRENT   NAME                                       CLUSTER                                    AUTHINFO                                   NAMESPACE
#*         minikube                                   minikube                                   minikube                                   default
```

* [kubectx](https://github.com/ahmetb/kubectx) 사용 중

---

## [3.7.5 네임스페이스가 제공하는 격리 이해](#Index)
* 네임스페이스에서 제공하지 않는 것
  * 네임스페이스 사용시, 오브젝트를 별도 그룹으로 분리해 특정한 네임스페이스 안에 속한 리소스를 대상으로 작업 할 수 있게 해주지만,
  * **실행 중인 오브젝트에 대한 격리는 제공하지 않는다.**
* 네임스페이스에서 네트워크 격리를 제공하는지는 쿠버네티스와 함께 배포하는 네트워킹 솔루션에 따라 다르다.
