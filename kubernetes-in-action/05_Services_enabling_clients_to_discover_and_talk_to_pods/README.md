# Index
* [5.서비스: 클라이언트가 파드를 검색하고 통신을 가능하게 함](#5서비스--클라이언트가-파드를-검색하고-통신을-가능하게-함)
* [5.1 서비스 소개](#51-서비스-소개)
  * [5.1.1 서비스 생성](#511-서비스-생성)
  * [5.1.2 서비스 검색](#512-서비스-검색)
* [5.2 클러스터 외부에 있는 서비스 연결](#52-클러스터-외부에-있는-서비스-연결)
  * [5.2.1 서비스 엔드포인트 소개](#521-서비스-엔드포인트-소개)
  * [5.2.2 서비스 엔드포인트 수동 구성](#522-서비스-엔드포인트-수동-구성)
  * [5.2.3 외부 서비스를 위한 별칭 생성](#523-외부-서비스를-위한-별칭-생성)
* [5.3 외부 클라이언트에 서비스 노출](#53-외부-클라이언트에-서비스-노출)
  * [5.3.1 노드포트 서비스 사용](#531-노드포트-서비스-사용)
  * [5.3.2 외부 로드밸런서로 서비스 노출](#532-외부-로드밸런서로-서비스-노출)
  * [5.3.3 외부 연결의 특성 이해](#533-외부-연결의-특성-이해)
* [5.4 인그레스 리소스로 서비스 외부 노출](#54-인그레스-리소스로-서비스-외부-노출)
  * [5.4.1 인그레스 리소스 생성](#541-인그레스-리소스-생성)
  * [5.4.2 인그레스로 서비스 액세스](#542-인그레스로-서비스-액세스)
  * [5.4.3 하나의 인그레스로 여러 서비스 노출](#543-하나의-인그레스로-여러-서비스-노출)
  * [5.4.4 TLS 트래픽을 처리하도록 인그레스 구성](#544-tls-트래픽을-처리하도록-인그레스-구성)
* [5.5 파드가 연결을 수락 할 준비가 됐을 떄 신호 보내기](#55-파드가-연결을-수락-할-준비가-됐을-떄-신호-보내기)
  * [5.5.1 레디니스 프로브 소개](#551-레디니스-프로브-소개)
  * [5.5.2 파드에 레디니스 프로브 추가](#552-파드에-레디니스-프로브-추가)
  * [5.5.3 실제 환경에서 레디니스 프로브가 수행해야 하는 기능](#553-실제-환경에서-레디니스-프로브가-수행해야-하는-기능)


---


# [5.서비스: 클라이언트가 파드를 검색하고 통신을 가능하게 함](#Index)
* 파드가 다른 파드에게 제공하는 서비스를 사용하려면 다른 파드를 찾는 방법이 필요
* 쿠버네티스가 제공하는 서버의 정확한 IP 주소나 호스트 이름을 지정하면 문제가 생길 수 있다.
  * 파드는 일시적
  * 클라이언트는 서버인 파드의 IP 주소를 미리 알 수 없다.
  * 스케일링이 자유롭기 때문에 여러 파드가 동일한 서비스를 제공할 수 있다. 하지만 각 파드는 고유한 IP 주소가 있다.


# [5.1 서비스 소개](#Index)
> 쿠버네티스의 서비스는 동일한 서비스를 제공하는 파드 그룹에 지속적인 단일 접점을 만들기 위해 생성하는 리소스  
> 서비스는 서비스가 존재하는 동안 절대 바뀌지 않는 IP 주소와 포트가 존재  
> 클라이언트는 해당 IP 와 포트로 접속한 뒤, 해당 서비스를 지원하는 파드 중 하나로 연결됨

### 예제를 통한 서비스 설명
![figure 5.1.png](figures/figure%205.1.png)


## [5.1.1 서비스 생성](#Index)
* 서비스 연결은 서비스 뒷단의 모든 파드로 로드밸런싱
* 서비스에 따른 파드 구분은 *레이블 셀렉터*를 사용한다.

![figure 5.2.png](figures/figure%205.2.png)

### `kubectl expose` 로 서비스 생성
* `expose` 커맨드는 레플리케이션컨트롤러에서 사용된 것과 동일한 파드 셀렉터를 사용해 서비스 리소스를 생성하고 모든 파드를 단일 IP 주소와 포트로 노출한다.

### YAML 디스크립터를 통한 서비스 생성
```shell
❯ kubecolor get svc
NAME         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1        <none>        443/TCP   12d
kubia        ClusterIP   10.106.177.211   <none>        80/TCP    6s   # 생성된 서비스
```
* 클러스터 IP 므로 클러스터 내부에서만 액세스할 수 있다.
* 서비스의 기본 목적은 파드 그룹을 클러스터의 다른 파드에 노출시키는 것
* 서비스를 외부로 노출시키는 것은..?

### 클러스터 내에서 서비스로 요청을 보내기
* 서비스의 클러스터 IP 로 요청을 보내고 응답을 로그로 남기는 파드 생성
* 쿠버네티스 노드로 ssh 접속 -> curl 커맨드 사용
* `kubectl exec` 커맨드로 기존 파드에서 curl 실행 가능

### 실행 중인 컨테이너에 원격으로 명령어 실행
* `kubectl exec` 커맨드를 사용해서 기존 파드의 컨테이너 내에서 원격으로 임의의 명령어 실행 가능
  * 컨테이너 내용, 상태, 환경을 검사할 때 유용
  * 파드명과 서비스 클러스터 IP 를 알아야 한다.

```shell
❯ kubectl exec kubia-44cff -- curl -s http://10.106.177.211
You've hit kubia-44cff

❯ kubectl exec kubia-44cff -- curl -s http://10.106.177.211
You've hit kubia-c9ww4

❯ kubectl exec kubia-44cff -- curl -s http://10.106.177.211
You've hit kubia-cpqtj
```

* `kubectl exec kubia-44cff -- curl -s http://10.106.177.211` 실행 후 발생하는 이벤트
  1. 파드의 컨테이너 내에서 curl 명령을 실행하도록 쿠버네티스에 지시
  2. curl 은 HTTP 요청을 서비스 IP 로 전송 (해당 IP 에는 파드가 연결됨)
  3. 쿠버네티스 서비스 프록시가 연결을 가로채 세 개의 파드 중 임의의 파드로 요청을 전달
  4. 해당 파드 내에서 실행 중인 서버가 요청을 처리하고 해당 파드의 이름을 포함하는 HTTP 응답 반환
  5. curl 은 표준 출력으로 응답. kubectl 이 있는 로컬 시스템의 표준 출력에 다시 표시

![figure 5.3.png](figures/figure%205.3.png)

### 서비스의 세션 어피니티 (sessionAffinity) 구성
* 동일한 명령을 몇 번 더 실행하면 동일한 클라이언트에서 요청하더라도 서비스 프록시가 각 연결을 임의의 파드를 선택해 연결을 다시 전달 (forward) 하기 때문에 요청할 떄마다 다른 파드가 선택됨
* 특정 클라이언트의 모든 요청을 매번 같은 파드로 리디렉션하려면 서비스의 세션 어피니티 (sessionAffinity) 속성을 기본값 None 대신 ClientIP 로 설정

```yaml
apiVersion: v1
kind: Service
spec:
  sessionAffinity: ClientIP
```
```shell
❯ kubecolor describe svc kubia
Name:              kubia
Namespace:         default
Labels:            <none>
Annotations:       <none>
Selector:          app=kubia
Type:              ClusterIP
IP Family Policy:  SingleStack
IP Families:       IPv4
IP:                10.100.198.80
IPs:               10.100.198.80
Port:              <unset>  80/TCP
TargetPort:        8080/TCP
Endpoints:         10.244.0.198:8080,10.244.0.199:8080,10.244.0.200:8080
Session Affinity:  ClientIP
Events:            <none>
```

### 동일한 서비스에서 여러 개의 포트 노출
* 서비스는 단일 포트만 노출하지만 여러 포트를 지원할 수도 있다.
* 하나의 서비스를 사용해 멀티 포트 서비스를 사용하면 단일 클러스터 IP 로 모든 서비스 포트가 노출된다.

### 이름이 지정된 포트 사용
* 각 파드의 포트에 이름을 지정하고 서비스 스펙에서 이름으로 참조 가능
* 후에 서비스 스펙을 변경하지 않고도 포트 번호를 변경할 수 있다.
  * 파드 스펙에서 포트 번호를 변경하면 된다.


## [5.1.2 서비스 검색](#Index)
> 서비스에서 생성한 파드로 접속 할 수 있는 안정적인 IP 와 포트를 클라이언트 파드에서 어떻게 알 수 있는가?

### 환경변수를 통한 서비스 검색
* 파드가 시작되면 쿠버네티스는 해당 시점에 존재하는 각 서비스를 가리키는 환경변수 셋을 초기화
```shell
# 컨테이너 내의 서비스와 연관된 환경 변수
❯ kubectl exec kubia-8jfd8 -- env
HOME=/root
YARN_VERSION=0.24.4
NODE_VERSION=7.10.1
NPM_CONFIG_LOGLEVEL=info
KUBERNETES_SERVICE_PORT=443 # 서비스가 제공되는 포트
KUBERNETES_SERVICE_HOST=10.96.0.1 # 서비스 클러스터 IP
KUBERNETES_PORT_443_TCP_ADDR=10.96.0.1
KUBERNETES_PORT_443_TCP_PORT=443
KUBERNETES_PORT_443_TCP_PROTO=tcp
KUBERNETES_PORT_443_TCP=tcp://10.96.0.1:443
KUBERNETES_PORT=tcp://10.96.0.1:443
KUBERNETES_SERVICE_PORT_HTTPS=443
HOSTNAME=kubia-8jfd8
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```

### DNS를 통한 서비스 검색
* `kube-system` 네임스페이스에 있는 서비스 중 `kube-dns` 라는 서비스가 존재
* DNS 서버를 실행하며 클러스터에서 실행 중인 다른 모든 파드는 자동으로 이를 사용하도록 구성
  * (*/etc/resolv.conf* 파일을 통해 수정 가능)
* 파드에서 실행 중인 프로세스에서 수행된 모든 DNS 쿼리는 시스템에서 실행 중인 모든 서비스를 알고 있는 쿠버네티스의 자체 DNS 서버로 처리된다.
 
```shell
❯ kubecolor get svc --namespace=kube-system
NAME       TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)                  AGE
kube-dns   ClusterIP   10.96.0.10   <none>        53/UDP,53/TCP,9153/TCP   86d
```

### FQDN 을 통한 서비스 연결
> backend-database.default.svc.cluster.local
* `backend-database` : 서비스 명
* `default` : 서비스가 정의된 네임프세이트
* `svc.cluster.local` : 모든 클러스터의 로컬 서비스 이름에 사용되는 클러스터 도메인 접미사

### 파드의 컨테이너 내에서 셸 실행
* 서비스에 액세스 할 수 없는 경우


---

# [5.2 클러스터 외부에 있는 서비스 연결](#Index)
> 쿠버네티스 서비스 기능으로 외부 서비스를 노출하려는 경우  
> 서비스 로드밸런싱과 서비스 검색 모두 활용 가능


## [5.2.1 서비스 엔드포인트 소개](#Index)
* 엔드포인트 리소스는 서비스로 노출되는 파드의 IP 주소와 포트 목록
* 파드 셀렉터는 서비스 스펙에 정의되지만, 들어오는 연결을 전달할 때 직접 사용하지는 않는다.
* 셀렉터는 IP 와 포트 목록을 작성하는 데 사용되며, 엔드포인트 리소스에 저장된다.


## [5.2.2 서비스 엔드포인트 수동 구성](#Index)
* 서비스의 엔드포인트를 서비스와 분리하면 엔드포인트를 수동으로 구성하고 업데이트할 수 있다.

### 셀렉터 없이 서비스 생성
* `external-service.yaml`

### 셀렉터가 없는 서비스에 관한 엔드포인트 리소스 생성
* 엔드포인트는 별도의 리소스이며, 서비스 속성은 아니다.
* `external-service-endpoints.yaml`
* 엔드포인트 오브젝트는 서비스와 이름이 같아야 한다.
* 엔드포인트 오브젝트는 서비스를 제공하는 대상 IP 주소와 포트 목록을 가져야 한다.

![figure 5.4.png](figures/figure%205.4.png)


## [5.2.3 외부 서비스를 위한 별칭 생성](#Index)

### ExternalName 서비스 생성
* `external-service-externalname.yaml`

---

# [5.3 외부 클라이언트에 서비스 노출](#Index)
> * 외부 클라이언트에서 서비스를 액세스할 수 있는 방법
>   1. 노트 포트로 서비스 유형 설정
>   2. 서비스 유형을 로드밸런서로 설정
>   3. 인그레스 리소스 만들기


## [5.3.1 노드포트 서비스 사용](#Index)
* 서비스 생성시 유형을 노드포트로 설정
* 노드포트 서비스 생성시 쿠버네티스는 모든 노드에 특정 포트를 할당 (모든 노드에서 동일 포트 번호 사용)
* 서비스를 구성하는 파드로 들어오는 연결을 전달

### 노드포트 서비스 생성
* `kubia-svc-nodeport.yaml`

### 노드포트 서비스 확인
```shell
❯ kubecolor get svc kubia-nodeport
NAME             TYPE       CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
kubia-nodeport   NodePort   10.103.204.165   <none>        80:30123/TCP   37s
```
* 서비스가 액세스 할 수 있는 주소
  * 10.103.204.165:80
  * <노드 IP>:30123

![figure 5.6.png](figures/figure%205.6.png)

### 외부 클라이언트가 노드포트 서비스에 액세스할 수 있도록 방화벽 규칙 변경
* 노드포트로 서비스에 액세스하려면 해당 노드포트에 대한 외부 연결을 허용하도록 GCP 방화벽을 구성해야 한다.
* 클라이언트가 특정 노드에만 요청하는 경우, 해당 노드에 장애가 발생하면 서비스에 액세스 할 수 없다.
* 그렇게 때문에 모든 노드에 요청을 분산시키고 오프라인 상태인 노드로 요청을 보내지 않도록 노드 앞에 로드밸런서를 배치하는 것이 좋다.


## [5.3.2 외부 로드밸런서로 서비스 노출](#Index)
* 노드포트 대신 서비스 유형을 로드밸런서로 설정
* 로드밸런서는 공개적으로 액세스 가능한 고유 IP 주소를 가지며 모든 연결을 서비스로 전달
* 로드밸런서 서비스는 노드포트 서비스의 확장으로 노드포트 서비스처럼 작동한다.

### 로드밸런서 서비스 생성
* `kubia-svc-loadbalancer.yaml`
* 특정 노드포트를 지정할 수 있지만 지정하지 않고 쿠버네티스가 포트를 선택하도록 한다.

```shell
❯ kubecolor get svc kubia-loadbalancer
NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
kubia-loadbalancer   LoadBalancer   10.97.224.198   <pending>     80:32280/TCP   23s
```

![figure 5.7.png](figures/figure%205.7.png)
* 로드밸런서 유형 서비스는 추가 인프라 제공 로드밸런서가 있는 노드포트 서비스


## [5.3.3 외부 연결의 특성 이해](#Index)

### 불필요한 네트워크 홉의 이해와 예방
> *network hop* : 컴퓨터 네트워크에서 출발지와 목적지 사이에 위치한 경로의 한 부분

* 외부의 연결을 수신한 노드에서 실행 중인 파드로만 외부 트래픽을 전달하도록 서비스를 구성해 추가 홉을 방지할 수 있다.
  * 서비스 스펙의 *externalTrafficPolicy* 필드 설정
  * 서비스 정의에 해당 설정이 포함돼 있고 서비스의 노드포트로 외부 연결이 열린 경우 서비스 프록시는 로컬에 실행 중인 파드를 선택
  * 로컬 파드가 존재하지 않으면 연결이 중단되기 때문에 로드밸런서는 로컬 파드가 하나 이상 있는 노드에만 연결을 전달하도록 해야 한다.

### 클라이언트 IP 가 보존되지 않음 인식
* 노드포트로 연결을 수신하면 패킷에서 소스 네트워크 주소 변환 (SNAT)이 수행되므로 패킷의 소스 IP 가 변경된다.
* 파드는 실제 클라이언트 IP 를 볼 수 없는데, 이 정보를 알아야하는 애플리케이션에서 문제가 될 수 있다.
* *Local External Traffic Policy* 는 연결을 수신하는 노드와 대상 파드를 호스팅하는 노드 사이에 추가 홉이 없기 떄문에 클라이언트 IP 보존이 가능하다.


--- 

# [5.4 인그레스 리소스로 서비스 외부 노출](#Index)

### 인그레스가 필요한 이유
* 로드밸런서 서비스는 자신의 공용 IP 주소를 가진 로드밸런서가 필요
* 인그레스는 한 IP 주소로 수십 개의 서비스에 접근이 가능하도록 지원한다.
* 인그레스는 네트워크 스택의 애플리케이션 계층(HTTP)에서 작동하며, 서비스가 할 수 없는 쿠키 기반 세션 어피니티 등과 같은 기능을 제공할 수 있다.

![figure 5.9.png](figures/figure%205.9.png)

### 인그레스 컨트롤러가 필요한 경우
* 인그레스 리소스를 작동시키려면 클러스터에 인그레스 컨트롤러를 실행해야 한다.
```shell
❯ kubecolor get pods --all-namespaces
NAMESPACE              NAME                                        READY   STATUS      RESTARTS        AGE
ingress-nginx          ingress-nginx-admission-create-gr9vx        0/1     Completed   0               42s
ingress-nginx          ingress-nginx-admission-patch-wrh4w         0/1     Completed   0               42s
ingress-nginx          ingress-nginx-controller-6cc5ccb977-stkd5   0/1     Running     0               42s
```


## [5.4.1 인그레스 리소스 생성](#Index)
* `kubia-ingress.yaml`


## [5.4.2 인그레스로 서비스 액세스](#Index)

### 인그레스의 IP 주소 얻기
```shell
❯ kubecolor get ingresses
NAME    CLASS   HOSTS               ADDRESS        PORTS     AGE
kubia   nginx   kubia.example.com   192.168.49.2   80, 443   16m
```

### 인그레스 컨트롤러가 구성된 호스트의 IP 를 인그레스 엔드포인트로 지정

### 인그레스로 파드 액세스

### 인그레스 동작 방식
1. 클라이언트에서 _kubia.example.com_ DNS 조회 후 DNS 서버가 인그레스 컨트롤러 IP 반환
2. 클라이언트는 HTTP 요청을 인그레스 컨트롤러로 전송. host 헤더에 _kubia.example.com_ 지정
3. 인그레스 컨트롤러는 헤더에서 클라이언트가 액세스하려는 서비스를 결정
   1. 서비스와 관련된 엔드포인트 오브젝트로 파드 IP 조회
   2. 클라이언트 요청을 파드에 전달

![figure 5.10.png](figures/figure%205.10.png)


## [5.4.3 하나의 인그레스로 여러 서비스 노출](#Index)

### 동일한 호스트의 다른 경로로 여러 서비스 매핑
```yaml
- host: kubia.example.com
  http:
    paths:
    - path: /kubia
      backend:
        serviceName: kubia
        servicePort: 80
    - path: /bar
      backend:
        serviceName: kubia
        servicePort: 80
```

### 서로 다른 호스트로 서로 다른 서비스 매핑
```yaml
spec:
  rules:
  - host: foo.example.com
    http:
      paths:
      - path: /
        backend:
          serviceName: foo
          servicePort: 80
  - host: bar.example.com
    http:
      paths:
      - path: /
        backend:
          serviceName: bar
          servicePort: 80
```


## [5.4.4 TLS 트래픽을 처리하도록 인그레스 구성](#Index)

### 인그레스를 위한 TLS 인증서 생성
* 클라이언트와 컨트롤러 간의 통신은 암호화되지만 컨트롤러와 백엔드 파드 간의 통신은 암호화되지 않는다.
* 파드는 HTTP 트래픽만 허용하고, 인그레스에서 TLS 와 관련된 모든 것을 처리하도록 한다.
  * 이 경우 인증서와 개인 키를 인그레스에 첨부해야 한다.
  * _secret_ 에 저장하며 인그레스 매니페스트에서 참조한다.

```shell
# 개인키
❯ openssl genrsa -out tls.key 2048

# 인증서
❯ openssl req -new -x509 -key tls.key -out tls.cert -days 360 -subj /CN=kubia.example.com

# 두 파일로 시크릿 생성
❯ kubectl create secret tls tls-secret --cert=tls.cert --key=tls.key
secret/tls-secret created

❯ kubectl get secret
NAME         TYPE                DATA   AGE
tls-secret   kubernetes.io/tls   2      93s
```

* `kubia-ingress-tls.yaml`

```shell
❯ kubecolor get ingress kubia -o yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"networking.k8s.io/v1","kind":"Ingress","metadata":{"annotations":{},"name":"kubia","namespace":"default"},"spec":{"rules":[{"host":"kubia.example.com","http":{"paths":[{"backend":{"service":{"name":"kubia-nodeport","port":{"number":80}}},"path":"/","pathType":"Prefix"}]}}],"tls":[{"hosts":["kubia.example.com"],"secretName":"tls-secret"}]}}
  creationTimestamp: "2023-07-19T12:48:00Z"
  generation: 2
  name: kubia
  namespace: default
  resourceVersion: "214333"
  uid: 5f42edec-09a5-4944-bcd8-00c6c85bbf36
spec:
  ingressClassName: nginx
  rules:
  - host: kubia.example.com
    http:
      paths:
      - backend:
          service:
            name: kubia-nodeport
            port:
              number: 80
        path: /
        pathType: Prefix
  tls:
  - hosts:
    - kubia.example.com
    secretName: tls-secret
status:
  loadBalancer:
    ingress:
    - ip: 192.168.49.2
```


---

# [5.5 파드가 연결을 수락 할 준비가 됐을 떄 신호 보내기](#Index)
* 파드가 요청을 처리할 준비가 되기 전까지는 요청을 보내지 않는 것이 좋다.

## [5.5.1 레디니스 프로브 (Readiness probe) 소개](#Index)
* 레디니스 프로브는 주기적으로 호출되며 특정 파드가 클라이언트 요청을 수신할 수 있는지를 결정
* 애플리케이션 특성에 따라 상세한 레디니스 프로브를 작성하는 것은 애플리케이션 개발자의 몫

### 레디니스 프로브 유형
1. **Exec 프로브** : 프로세스를 실행
2. **HTTP GET 프로브** : HTTP GET 요청을 컨테이너로 보낸 뒤 응답 상태 코드로 컨테이너 준비 여부 판단
3. **TCP 소켓 프로브** : 컨테이너의 지정된 포트로 TCP 연결을 연다.

### 레디니스 프로브의 동작
* 파드가 준비되지 않았다고 하면 서비스에서 제거된다.
* 파드가 준비되면 서비스에 다시 추가
* 라이브니스 프로브와 달리 컨테이너가 준비 상태 점검에 실패하더라도 컨테이너가 종료되거나 다시 시작되지 않는다.
* 레디니스 프로브는 요청을 처리할 준비가 된 파드의 컨테이너만 요청을 수신하도록 한다.

![figure 5.11.png](figures/figure%205.11.png)


## [5.5.2 파드에 레디니스 프로브 추가](#Index)

### 파드 템플릿에 레디니스 프로브 추가

### 파드의 레디니스 상태 확인과 수정

### 하나의 READY 파드로 서비스를 호출


## [5.5.3 실제 환경에서 레디니스 프로브가 수행해야 하는 기능](#Index)

### 레디니스 프로브를 항상 정의하라
* 파드에 레디니스 프로브를 추가하지 않으면 파드가 시작하는 즉시 서비스 엔드포인트가 된다.

### 레디니스 프로브에 파드의 종료 코드를 포함하지 마라


---