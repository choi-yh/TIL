# Index
* [3.2 YAML 또는 JSON 디스크립터로 파드 생성](#32-yaml-또는-json-디스크립터로-파드-생성)
  * [3.2.1 기존 파드의 YAML 디스크립터 살펴보기](#321-기존-파드의-yaml-디스크립터-살펴보기)
  * [3.2.2 파드를 정의하는 간단한 YAML 정의 작성](#322-파드를-정의하는-간단한-yaml-정의-작성)
  * [3.2.3 kubectl create 명령으로 파드 만들기](#323-kubectl-create-명령으로-파드-만들기)
  * [3.2.4 애플리케이션 로그 보기](#324-애플리케이션-로그-보기)
  * [3.2.5 파드에 요청 보내기](#325-파드에-요청-보내기)

# 3.2 YAML 또는 JSON 디스크립터로 파드 생성
* https://kubernetes.io/docs/reference
* YAML 파일을 사용해 쿠버네티스 오브젝트 정의

---

## 3.2.1 기존 파드의 YAML 디스크립터 살펴보기
* 2장에서 생성한 파드

```shell
kubecolor get pod kubia-64c9d4f775-ndbwr -o yaml
```

```yaml
apiVersion: v1 # 이 YAML 디스크립터에서 사용한 쿠버네티스 API 버전
kind: Pod # 쿠버네티스 오브젝트 / 리소스 유형
metadata: # 파드 메타데이터 (이름, 레이블, 어노테이션 등)
  creationTimestamp: "2023-06-27T11:46:26Z"
  generateName: kubia-64c9d4f775-
  labels:
    app: kubia
    pod-template-hash: 64c9d4f775
  name: kubia-64c9d4f775-ndbwr
  namespace: default
  ownerReferences:
  - apiVersion: apps/v1
    blockOwnerDeletion: true
    controller: true
    kind: ReplicaSet
    name: kubia-64c9d4f775
    uid: e2676cd6-d811-4f51-8ab8-f2e64a356f47
  resourceVersion: "93078"
  uid: 1b5e8b13-d307-428b-b928-5718fdd30053
spec: # 파드 정의 / 내용 (파드 컨테이너 목록, 볼륨 등)
  containers:
  - image: hyooo/kubia
    imagePullPolicy: Always
    name: kubia
    ports:
    - containerPort: 8080
      protocol: TCP
    resources: {}
    terminationMessagePath: /dev/termination-log
    terminationMessagePolicy: File
    volumeMounts:
    - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
      name: kube-api-access-v4wv4
      readOnly: true
  dnsPolicy: ClusterFirst
  enableServiceLinks: true
  nodeName: minikube
  preemptionPolicy: PreemptLowerPriority
  priority: 0
  restartPolicy: Always
  schedulerName: default-scheduler
  securityContext: {}
  serviceAccount: default
  serviceAccountName: default
  terminationGracePeriodSeconds: 30
  tolerations:
  - effect: NoExecute
    key: node.kubernetes.io/not-ready
    operator: Exists
    tolerationSeconds: 300
  - effect: NoExecute
    key: node.kubernetes.io/unreachable
    operator: Exists
    tolerationSeconds: 300
  volumes:
  - name: kube-api-access-v4wv4
    projected:
      defaultMode: 420
      sources:
      - serviceAccountToken:
          expirationSeconds: 3607
          path: token
      - configMap:
          items:
          - key: ca.crt
            path: ca.crt
          name: kube-root-ca.crt
      - downwardAPI:
          items:
          - fieldRef:
              apiVersion: v1
              fieldPath: metadata.namespace
            path: namespace
status: # 파드와 그 안의 여러 컨테이너의 상세한 상태
  conditions:
  - lastProbeTime: null
    lastTransitionTime: "2023-06-27T11:46:26Z"
    status: "True"
    type: Initialized
  - lastProbeTime: null
    lastTransitionTime: "2023-07-04T11:39:09Z"
    status: "True"
    type: Ready
  - lastProbeTime: null
    lastTransitionTime: "2023-07-04T11:39:09Z"
    status: "True"
    type: ContainersReady
  - lastProbeTime: null
    lastTransitionTime: "2023-06-27T11:46:26Z"
    status: "True"
    type: PodScheduled
  containerStatuses:
  - containerID: docker://771505c998129e36919146a29575b3613c9ca5e76bc842f75b70c1c79aa57949
    image: hyooo/kubia:latest
    imageID: docker-pullable://hyooo/kubia@sha256:68b91da1103f0946d44d4cb37cdb205f7a83aa28cd940377672df7dc5c9e24ac
    lastState:
      terminated:
        containerID: docker://00d4a889a1b6c6090aa21adadaa047828f1e349960958e416702c173fe986e89
        exitCode: 143
        finishedAt: "2023-06-29T12:10:39Z"
        reason: Error
        startedAt: "2023-06-27T11:46:29Z"
    name: kubia
    ready: true
    restartCount: 1
    started: true
    state:
      running:
        startedAt: "2023-07-04T11:39:08Z"
  hostIP: 192.168.49.2
  phase: Running
  podIP: 10.244.0.127
  podIPs:
  - ip: 10.244.0.127
  qosClass: BestEffort
  startTime: "2023-06-27T11:46:26Z"
```

### 파드를 정의하는 주요 부분 소개

* Metadata
  * 이름, 네임스페이스, 레이블 및 파드에 관한 기타 정보를 포함
* Spec
  * 파드 컨테이너, 볼륨, 기타 데이터 등 파드 자체에 관한 실제 명세
* Status
  * 파드 상태, 각 컨테이너 설명과 상태, 파드 내부 IP, 기타 기본 정보 등 현재 실행 중인 파드에 관한 현재 정보를 포함
  * 특정 시간의 리소스 상태를 보여주는 읽기 전용 런타임 데이터 포함
  * 새 파드 생성시 작성할 필요 X

---

## 3.2.2 파드를 정의하는 간단한 YAML 정의 작성

### 컨테이너 포트 지정
* 포트를 명시적으로 정의한다면, 클러스터를 사용하는 모든 사람이 파드에서 노출한 포트를 빠르게 볼 수 있다.
* 생략해도 포트를 통해 파드에 연결 가능 여부에는 지장이 없다.

### kubectl explain 을 이용해 사용 가능한 API 오브젝트 필드 찾기
* https://kubernetes.io/ko/docs/concepts/overview/kubernetes-api/ 에서 레퍼런스 참조 혹은 `kubectl explain` 명령을 통해 개별 API 오브젝트에서 지원되는 속성 확인 가능

```shell
kubectl explain pod

KIND:       Pod
VERSION:    v1

DESCRIPTION:
FIELDS:
     apiVersion	<string>
     APIVersion defines the versioned schema of this representation of an object.
     Servers should convert recognized schemas to the latest internal value, and
     may reject unrecognized values. More info:
     https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources

     kind	<string>
     Kind is a string value representing the REST resource this object
     represents. Servers may infer this from the endpoint the client submits
     requests to. Cannot be updated. In CamelCase. More info:
     https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds

     metadata	<ObjectMeta>
     Standard object's metadata. More info:
     https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata

     spec	<PodSpec>
     Specification of the desired behavior of the pod. More info:
     https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status

     status	<PodStatus>
     Most recently observed status of the pod. This data may not be up to date.
     Populated by the system. Read-only. More info:
     https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status
```

---

## 3.2.3 kubectl create 명령으로 파드 만들기

```shell
kubectl create -f kubia-manual.yaml
```

* `kubectl create -f` : YAML 혹은 JSON 파일로 리소스를 생성한다.
```shell
kubectl create --help

-f, --filename=[]:
	Filename, directory, or URL to files to use to create the resource
```

### 실행 중인 파드의 전체 정의 가져오기
```shell
kubecolor get pod kubia-manual -o yaml # 파드 생성후 yaml 형식으로 파드를 본다
kubecolor get pod kubia-manual -o json # json 도 가능
```

### 파드 목록에서 새로 생성된 파드 보기
```shell
❯ kubecolor get pods

NAME                     READY   STATUS    RESTARTS        AGE
kubia-64c9d4f775-ndbwr   1/1     Running   1 (4d23h ago)   7d
kubia-manual             1/1     Running   0               3m14s
nginx-787969776-2z9hw    1/1     Running   2 (4d23h ago)   72d
nginx-787969776-h9c78    1/1     Running   2 (4d23h ago)   72d
nginx-787969776-llpzz    1/1     Running   2 (4d23h ago)   72d
nginx-787969776-nsttw    1/1     Running   2 (4d23h ago)   72d
nginx-787969776-qvrnq    1/1     Running   2 (4d23h ago)   72d
```

---

## 3.2.4 애플리케이션 로그 보기
* 컨테이너화된 애플리케이션은 로그를 파일에 쓰기보다는 표준 출력과 표준 에러에 로그를 남기는 게 일반적

```shell
docker logs <container id> # ssh 로 파드가 실행 중인 노드에 접속해서 확인하는 방법

# kubectl logs 를 이용해 파드 로그 가져오기
kubectl logs kubia-manual
#Kubia server starting...
```

---

## 3.2.5 파드에 요청 보내기
* 파드에 테스트와 디버깅 목적으로 연결 할 수 있는 방법

### 로컬 네트워크 포트를 파드의 포트로 포워딩

```shell
kubectl port-forward kubia-manual 8888:8080
#Forwarding from 127.0.0.1:8888 -> 8080
#Forwarding from [::1]:8888 -> 8080

curl localhost:8888
#You've hit kubia-manual
```

![figure 3.5.png](figures/figure%203.5.png)
* 요청을 보낼 떄 발생하는 상황