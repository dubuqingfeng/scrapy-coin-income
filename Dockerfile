FROM alpine:3.9

ENV RUNTIME_PACKAGES python3  libxslt libxml2 git curl
ENV BUILD_PACKAGES build-base libxslt-dev libxml2-dev libffi-dev python3-dev openssl-dev

RUN apk add --no-cache ${RUNTIME_PACKAGES} ${BUILD_PACKAGES} && \
  pip3 install scrapy && \
  apk del ${BUILD_PACKAGES} && \
  rm -rf /root/.cache

#ADD ./scrapyd.conf /etc/scrapyd/
#VOLUME /var/lib/scrapyd/

COPY . /work/app
RUN pip3 install -r /work/app/requirements.txt
RUN /usr/bin/crontab /work/app/install/crontab.txt
CMD ["/usr/sbin/crond", "-f", "-l", "8"]