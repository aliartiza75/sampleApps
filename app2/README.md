# App 2

#

##

1. To build image

```bash
sudo docker build -t app2:0.0.1 -f package/Dockerfile .
```

2. To run docker image
```bash
udo docker run -p 5001:5001  -e FLASK_HOST_IP=0.0.0.0 -e FLASK_HOST_PORT=5001 -it docker.io/library/app2:0.0.1
```

1. 