# Overview

This project is an experimental test on the scaling characteristics of
docker services. The setup includes a client, a proxy server and a
HTTP service connected to a redis DB where the proxy server, the HTTP
service and the database are run as  docker containers.

![Design Overview](./load_balancer.png)

The proxy server is configured to listen for traffic on port 80 and in
this case the only resource available through the proxy is an api that
calculates the factorial of a number -which is a cpu bound operation
and generates significant processing workload for a large number. 


```
server{
	listen 80;
        location / {
	proxy_pass http://frontend:5000/factorial;
        }
}
```

The HTTP server is a simple server that takes takes a value from the
database (a key-value storage) and computes the factorial of that
number.

To run a single instance of the service:
`sudo docker-compose up`

To scale the service the `yml` file in stage2 folder is run using a
scaling option and the proxy server's load balancing feature will
allocate resources in the default round-robin fashion.
`sudo docker-compose up --scale frontend=3`