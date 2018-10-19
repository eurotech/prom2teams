# Build container

FROM alpine:3.8 as build

RUN apk add build-base curl git make python3 python3-dev

RUN ln -s /usr/bin/python3 /usr/local/bin/python3

COPY . /opt/prom2teams

WORKDIR /opt/prom2teams

RUN make package

# Distribution container

FROM alpine:3.8

COPY --from=build /opt/prom2teams/dist/prom2teams-*.tar.gz /tmp/prom2teams.tar.gz
COPY ./etc /etc/prom2teams

RUN apk add --no-cache curl python3 && \
    curl https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py && \
    python3 /tmp/get-pip.py && \
    pip install /tmp/prom2teams.tar.gz && \
    rm -f /tmp/get-pip.py /tmp/prom2teams.tar.gz

EXPOSE 8699

CMD [ "/usr/bin/prom2teams"]