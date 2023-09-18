```shell
# 2.1.4 컨테이너 이미지 생성
docker build -t kubia .

# 2.1.5 컨테이너 이미지 실행 및 조회
docker run --name kubia-container -p 8080:8080 -d kubia
docker ps
docker inspect kubia-container

# 2.1.6 실행 중인 컨테이너 내부 탐색
docker exec -it kubia-container bash

# 2.1.7 컨테이너 중지 및 삭제
docker stop kubia-container
docker rm kubia-container

# 2.1.8 이미지 레지스트리에 이미지 푸시
docker tag kubia hyooo/kubia
docker push hyooo/kubia
docker run -p 8080:8080 -d hyooo/kubia # 다른 머신에서 이미지 실행하기
```