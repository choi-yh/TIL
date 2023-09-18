# Index
* [3.8 파드 중지와 제거](#38-파드-중지와-제거)
  * [3.8.1 이름으로 파드 삭제](#381-이름으로-파드-삭제)
  * [3.8.2 레이블 셀렉터를 이용한 파드 삭제](#382-레이블-셀렉터를-이용한-파드-삭제)
  * [3.8.3 네임스페이스를 삭제한 파드 제거](#383-네임스페이스를-삭제한-파드-제거)
  * [3.8.4 네임스페이스를 유지하면서 네임스페이스 안에 있는 모든 파드 삭제](#384-네임스페이스를-유지하면서-네임스페이스-안에-있는-모든-파드-삭제)
  * [3.8.5 네임스페이스에서 (거의) 모든 리소스 삭제](#385-네임스페이스에서--거의--모든-리소스-삭제)

---

# [3.8 파드 중지와 제거](#Index)


## [3.8.1 이름으로 파드 삭제](#Index)
```shell
kubectl delete pod <pod-name> # 이름으로 파드 삭제
```

* 파드 삭제시 쿠버네티스는 파드 안에 있는 모든 컨테이너를 종료하도록 지시
* 쿠버네티스는 `SIGTERM` 신호를 프로세스에 보내고, 지정된 시간 (기본값 30초) 동안 대기
* 시간 내에 종료되지 않으면 `SIGKILL` 신호를 통해 종료

---

## [3.8.2 레이블 셀렉터를 이용한 파드 삭제](#Index)
```shell
kubectl delete pod -l creation_method=manual
#pod "kubia-manual" deleted
#pod "kubia-manual-v2" deleted
```

## [3.8.3 네임스페이스를 삭제한 파드 제거](#Index)
```shell
kubectl delete ns <namespace>
```

## [3.8.4 네임스페이스를 유지하면서 네임스페이스 안에 있는 모든 파드 삭제](#Index)
```shell
kubectl delete pod --all
#pod "kubia-64c9d4f775-ndbwr" deleted
#pod "nginx-787969776-2z9hw" deleted
#pod "nginx-787969776-h9c78" deleted
#pod "nginx-787969776-llpzz" deleted
#pod "nginx-787969776-nsttw" deleted
#pod "nginx-787969776-qvrnq" deleted
```

* 파드는 종료됐지만 새로운 파드 생성된다. (파드 생성시 deployment 를 이용해서 만들었기 떄문)

## [3.8.5 네임스페이스에서 (거의) 모든 리소스 삭제](#Index)
```shell
kubectl delete all --all
#pod "kubia-64c9d4f775-vp5s6" deleted
#pod "nginx-787969776-75sfc" deleted
#pod "nginx-787969776-97bnx" deleted
#pod "nginx-787969776-9zq2l" deleted
#pod "nginx-787969776-bsfbb" deleted
#pod "nginx-787969776-x26m6" deleted
#service "kubernetes" deleted
#service "kubia-http" deleted
#deployment.apps "kubia" deleted
#deployment.apps "nginx" deleted
```
* 네임스페이스 내의 모든 리소스 (deployment, pod, services) 삭제 가능