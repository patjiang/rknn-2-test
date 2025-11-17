FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR ~/rknn_test

COPY rknn_toolkit_lite2-2.3.2-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl .
RUN pip install --no-cache-dir rknn_toolkit_lite2-2.3.2-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl \
    numpy \
    opencv-python-headless

COPY test.py .
COPY resnet18_for_rk3566_rk3568.rknn .
COPY space_shuttle_224.jpg .

CMD ["python3", "test.py"]
