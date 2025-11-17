## build/pull image:
```
balena login ghcr.io
balena pull ghcr.io/patjiang/rknn-test:latest
```

## Run:
```
balena run -it --rm \
  --privileged \
  -v /dev/dri:/dev/dri \
  -v /proc/device-tree/compatible:/proc/device-tree/compatible:ro \
  ghcr.io/patjiang/rknn-test:latest
```

ghtp:
```
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
```

```
echo "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" | docker login ghcr.io -u patjiang --password-stdin
```
