FROM alpine:3.20.3

RUN apk update
RUN apk add --no-cache python3 pipx

RUN pipx install --global 'poetry==1.8.3'

# COPY ./it_ticket /var/it_ticket
COPY ./tools /var/tools

RUN chmod +x /var/tools/entry.sh

STOPSIGNAL SIGINT

ENTRYPOINT ["/var/tools/entry.sh"]
