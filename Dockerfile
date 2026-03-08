FROM alpine:3.20

RUN apk add --no-cache ca-certificates

ADD https://github.com/zeroclaw-labs/zeroclaw/releases/download/v0.1.7/zeroclaw-x86_64-unknown-linux-gnu.tar.gz /tmp/zeroclaw.tar.gz

RUN tar xzf /tmp/zeroclaw.tar.gz -C /usr/local/bin zeroclaw && \
    rm /tmp/zeroclaw.tar.gz && \
    chmod +x /usr/local/bin/zeroclaw

COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

WORKDIR /zeroclaw-data

EXPOSE 42617

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["zeroclaw", "daemon"]
