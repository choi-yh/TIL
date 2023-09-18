# Index
* [3.3 레이블을 이용한 파드 구성](#33-레이블을-이용한-파드-구성)
  * [3.3.1 레이블 소개](#331-레이블-소개)
  * [3.3.2 파드를 생성할 때 레이블 지정](#332-파드를-생성할-때-레이블-지정)
  * [3.3.3 기존 파드 레이블 수정](#333-기존-파드-레이블-수정)


# 3.3 레이블을 이용한 파드 구성
* 파드 수가 증가함에 따라 파드를 부분 집합으로 분류 할 필요가 있다.


## 3.3.1 레이블 소개
> 레이블은 파드와 모든 다른 쿠버네티스 리소스를 조직화 할 수 있는 단순하면서 강력한 쿠버네티스 기능  

* 리소스에 첨부하는 key-value 쌍으로, 레이블 셀렉터를 사용해 리소스를 선택할 때 활용된다.
* 레이블 키가 해당 리소스 내에서 고유하다면, 하나 이상 원하는 만큼 레이블을 가질 수 있다.

* 2개의 레이블을 붙인 마이크로 서비스 예시 (figure 3.7)
  * `app`: 파드가 속한 애플리케이션, 구성 요소 혹은 마이크로서비스를 지정
  * `rel`: 파드에서 실행 중인 애플리케이션이 stable, beta, canary release 인지 보여준다.

![figure 3.7](figures/figure%203.7.png)

---

## 3.3.2 파드를 생성할 때 레이블 지정

```shell
kubectl create -f kubia-manual-with-labels.yaml
# pod/kubia-manual-v2 created

kubecolor get pods --show-labels # label 표시 옵션
#NAME                     READY   STATUS    RESTARTS       AGE    LABELS
#kubia-64c9d4f775-ndbwr   1/1     Running   1 (5d1h ago)   7d2h   app=kubia,pod-template-hash=64c9d4f775
#kubia-manual             1/1     Running   0              107m   <none>
#kubia-manual-v2          1/1     Running   0              42s    creation_method=manual,env=prod

kubectl get pods -L creation_method,env # -L 옵션을 통해 특정 레이블만 확인이 가능
#NAME                     READY   STATUS    RESTARTS       AGE    CREATION_METHOD   ENV
#kubia-64c9d4f775-ndbwr   1/1     Running   1 (5d1h ago)   7d2h
#kubia-manual             1/1     Running   0              108m
#kubia-manual-v2          1/1     Running   0              115s   manual            prod
```

```shell
-L, --label-columns=[]:
	Accepts a comma separated list of labels that are going to be presented as columns. Names are case-sensitive. You can also use multiple flag options like -L label1 -L label2...
```

---

### 3.3.3 기존 파드 레이블 수정

```shell
kubectl label pod kubia-manual creation_method=manual # 기존 파드에 레이블 추가
#pod/kubia-manual labeled

kubectl label pod kubia-manual-v2 env=debug --overwrite # 기존에 가지고 있던 레이블 변경 (--overwrite 옵션이 필요하다.)
#pod/kubia-manual-v2 labeled

kubectl label pod kubia-manual createion_method- # 잘못 생성한 레이블 제거
#pod/kubia-manual unlabeled
```