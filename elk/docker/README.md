# [Install Elasticsearch with Docker](https://www.elastic.co/guide/en/elasticsearch/reference/8.12/docker.html#docker)

## Start a single-node cluster

1. 사전 준비
    * docker 설치
    * docker desktop 메모리는 최소 4GB

```shell
# 2. Create new docker network
docker network create elastic

# 3. Pull Elasticsearch docker iamge
docker pull docker.elastic.co/elasticsearch/elasticsearch:8.12.2

# 4. Optional: install cosign for verifying container images
# 운영 환경에서는 보안적인 측면으로 체크하는게 좋아보인다.
wget https://artifacts.elastic.co/cosign.pub
cosign verify --key cosign.pub docker.elastic.co/elasticsearch/elasticsearch:8.12.2

# 5. Start an Elasticsearch container
docker run --name es01 --net elastic -p 9200:9200 -it -m 1GB docker.elastic.co/elasticsearch/elasticsearch:8.12.2

# 6. Copy the generated elastic password
docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic
docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana

# 7. Copy the http_ca.crt SSL certificate from the container to local machine
docker cp es01:/usr/share/elasticsearch/config/certs/http_ca.crt .

# 8. es container 에 인증서로 호출
# TODO: --insecure 옵션을 줬는데 실제로는 인증서 등록이 필요해보임
curl --cacert http_ca.crt --insecure -u elastic:$ELASTIC_PASSWORD https://localhost:9200
{
  "name" : "90cd0f63b8d4",
  "cluster_name" : "docker-cluster",
  "cluster_uuid" : "gXcpiUUIS4iME1lwFeUBzQ",
  "version" : {
    "number" : "8.12.2",
    "build_flavor" : "default",
    "build_type" : "docker",
    "build_hash" : "48a287ab9497e852de30327444b0809e55d46466",
    "build_date" : "2024-02-19T10:04:32.774273190Z",
    "build_snapshot" : false,
    "lucene_version" : "9.9.2",
    "minimum_wire_compatibility_version" : "7.17.0",
    "minimum_index_compatibility_version" : "7.0.0"
  },
  "tagline" : "You Know, for Search"
}
```

## Add more nodes

```shell
# 1. 기존 노드를 사용해 새 노드에 대한 enrollment token 생성 (token 은 30분간 유효)
docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s node

# 2. enrollment token 사용하여 노드 추가 (token 은 환경 변수 옵션으로 전달)
docker run -e ENROLLMENT_TOKEN="<token>" --name es02 --net elastic -it -m 1GB docker.elastic.co/elasticsearch/elasticsearch:8.12.2

# 3. cat node API 로 노드 확인
curl --cacert http_ca.crt --insecure -u elastic:$ELASTIC_PASSWORD https://localhost:9200/_cat/nodes
172.18.0.2 31 92 7 1.25 1.21 1.06 cdfhilmrstw * 90cd0f63b8d4
172.18.0.3 19 92 5 1.25 1.21 1.06 cdfhilmrstw - 34eab49349bc
```

## Run Kibana

```shell
# 1. Pull the Kibana Docker image.
docker pull docker.elastic.co/kibana/kibana:8.12.2

# 2. Optional: Verify the Kibana image's signature.
wget https://artifacts.elastic.co/cosign.pub
cosign verify --key cosign.pub docker.elastic.co/kibana/kibana:8.12.2

# 3. Start a Kibana container
docker run --name kib01 --net elastic -d -p 5601:5601 docker.elastic.co/kibana/kibana:8.12.2

# 4. 최초 시작시 kibana docker log 에 unique 한 링크가 생성됨. 엘라스틱서치 실행시 발급받은 토큰을 넣어라
# 5. kibana token 재발급
docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana

# 6. 해당 링크에 계정, 패스워드 입력 후 접속!
```

## Remove containers

```shell
# Remove the Elastic network
docker network rm elastic

# Remove Elasticsearch containers
docker rm es01
docker rm es02

# Remove the Kibana container
docker rm kib01
```

---

```shell
docker compose up -d
docker-compose down
```