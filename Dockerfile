FROM alpine:3.20

RUN apk add --no-cache ca-certificates

COPY --from=ghcr.io/zeroclaw-labs/zeroclaw:latest /usr/local/bin/zeroclaw /usr/local/bin/zeroclaw

COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

WORKDIR /zeroclaw-data

EXPOSE 42617

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["zeroclaw", "daemon"]
