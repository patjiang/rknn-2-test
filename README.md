## build:
```
docker build -t rknn_test .
```

## Run:
```
docker run -it --rm \
  --privileged \
  -v /dev/dri:/dev/dri \
  -v /proc/device-tree/compatible:/proc/device-tree/compatible:ro \
  rknn_test
```

ghtp:
```
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
```

```
echo "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" | docker login ghcr.io -u patjiang --password-stdin
```
