---
layout: post
title: A development v2 Docker Registry on Docker for Mac
published: true
date: 2016-04-25T16:02:55.665831
categories: [docker, programming]
---

Update (2016-04-25): I use a `json` command below that you can install via
`npm install -g json`. See <http://trentm.com/json/>.

---

I got a key to the beta Docker for Mac recently and I'm working at updating
Joyent's [node.js Docker Registry client](https://github.com/joyent/node-docker-registry-client)
for some recent [Docker Distribution](https://github.com/docker/distribution)
changes. I wanted to play around with a local registry running in my Docker
for Mac. This post shows how.

With Docker on Linux a local dev registry container would be on *locahost*.
The Docker Engine special cases registries on "localhost", treating them
as "insecure", meaning it uses http for access and avoiding the need for you
to setup a TLS proxy and certs. The way to do that for a registry not on
localhost is to use [`docker daemon
--insecure-registry=...`](https://docs.docker.com/engine/reference/commandline/daemon/#insecure-registries).
But how to set that on Docker for Mac? That was the only (small) hurdle.


Start a v2 registry:

    docker pull registry:2
    docker run --name reg2 -d --restart=always -p 5000:5000 registry:2

Get the registry container's host and port:

    $ docker port reg2
    5000/tcp -> 192.168.64.2:5000

Use the [Docker-for-Mac config tool
"pinata"](https://beta.docker.com/docs/mac/experiment/) to set
insecure-registries:

    cd /Applications/Docker.app/Contents/Resources/bin
    ./pinata.bin get daemon \
        | json -e 'this["insecure-registries"] = ["192.168.64.2:5000"]' -0 \
        | ./pinata.bin set daemon -

Now you should be able to push an image to it:

    docker pull alpine:latest
    docker tag alpine:latest 192.168.64.2:5000/alpine:latest
    docker push 192.168.64.2:5000/alpine:latest