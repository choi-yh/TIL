FROM ubuntu:latest
RUN apt-get update; apt-get -y install fortune
ADD fortuneloop.sh /bin/fortuneloo.sh
ENTRYPOINT ["/bin/fortuneloop.sh"]
CMD ["10"]