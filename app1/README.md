# App 1

#

##

1. To build image

```bash
sudo docker build -t app1:0.0.1 -f package/Dockerfile .
```

2. To run docker image
```bash
sudo docker run -p 5000:5000  -e FLASK_HOST_IP=0.0.0.0 -e FLASK_HOST_PORT=5000 -it docker.io/library/app1:0.0.1
```

1. 