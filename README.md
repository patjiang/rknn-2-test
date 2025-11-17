## build:
```
docker build -t rknn_test .
```

## Run:
```
docker run -it --rm \
  --privileged \
  -v /dev:/dev \
  -v /proc/device-tree/compatible:/proc/device-tree/compatible:ro \
  rknn_test
```
