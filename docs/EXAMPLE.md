# Example Deploy

Launch this command from your local machine:

```
$ vagrant ssh vm0
```

Then launch a demo service:

```
[vagrant@vm0 ~]$ docker service create --replicas 1 --name helloworld alpine ping docker.com
mpn6ptk6d3gscb8vs37oiwpyd
overall progress: 1 out of 1 tasks
1/1: running   [==================================================>]
verify: Service converged
```

Log onto a worker:

```
$ vagrant ssh vm1
```

Verify the service that is running:

```
[vagrant@vm1 ~]$ docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
844f4e8b3a01        alpine:latest       "ping docker.com"   28 seconds ago      Up 23 seconds                           helloworld.1.j2hihpx9d9as10zxq6xk1nq2p
```
