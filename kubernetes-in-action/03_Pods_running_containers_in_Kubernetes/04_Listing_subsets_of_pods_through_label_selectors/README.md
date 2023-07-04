# Index
* [3.4 레이블 셀렉터를 이용한 파드 부분 집합 나열](#34-레이블-셀렉터를-이용한-파드-부분-집합-나열)
  * [3.4.1 레이블 셀렉터를 사용해 파드 나열](#341-레이블-셀렉터를-사용해-파드-나열)
  * [3.4.2 레이블 셀렉터에서 여러 조건 사용](#342-레이블-셀렉터에서-여러-조건-사용)

# [3.4 레이블 셀렉터를 이용한 파드 부분 집합 나열](#Index)
* 레이블 셀렉터는 특정 레이블로 태그된 파드의 부분 집합을 선택해 원하는 작업을 수행
* 레이블 셀렉터는 특정 값과 레이블을 갖는지 여부에 따라 리소스를 필터링하는 기준이 된다.
* 레이블 셀렉터가 리소스 중에서 리소스를 선택하는 기준
  * 특정한 키를 포함하거나 포함하지 않는 레이블
  * 특정한 키와 값을 가진 레이블
  * 특정한 키를 갖고 있지만, 다른 값을 가진 레이블]

## [3.4.1 레이블 셀렉터를 사용해 파드 나열](#Index)

```shell
kubecolor get pods -l creation_method=manual # -l option 을 사용한다.
#NAME              READY   STATUS    RESTARTS   AGE
#kubia-manual      1/1     Running   0          141m
#kubia-manual-v2   1/1     Running   0          35m

kubecolor get pod -l '!env' # env label 을 가지지 않은 파드들
#NAME                     READY   STATUS    RESTARTS       AGE
#kubia-64c9d4f775-ndbwr   1/1     Running   1 (5d2h ago)   7d2h
#kubia-manual             1/1     Running   0              143m
```

---

## [3.4.2 레이블 셀렉터에서 여러 조건 사용](#Index)