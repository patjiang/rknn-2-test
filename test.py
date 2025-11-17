import cv2
import numpy as np
import platform
from rknnlite.api import RKNNLite

DEVICE_COMPATIBLE_NODE = '/proc/device-tree/compatible'

def get_host():
    system = platform.system()
    machine = platform.machine()
    os_machine = system + '-' + machine
    if os_machine == 'Linux-aarch64':
        try:
            with open(DEVICE_COMPATIBLE_NODE) as f:
                device_compatible_str = f.read()
                if 'rk3562' in device_compatible_str:
                    host = 'RK3562'
        except IOError:
            print('Read device node {} failed.'.format(DEVICE_COMPATIBLE_NODE))
            exit(-1)
    else:
        host = os_machine
    return host

INPUT_SIZE = 224
RK3562_RKNN_MODEL = 'resnet18_for_rk3562.rknn'


def show_top5(result):
    output = result[0].reshape(-1)
    output = np.exp(output) / np.sum(np.exp(output))
    output_sorted_indices = np.argsort(output)[::-1][:5]
    top5_str = 'resnet18\n-----TOP 5-----\n'
    for i, index in enumerate(output_sorted_indices):
        value = output[index]
        if value > 0:
            topi = '[{:>3d}] score:{:.6f}\n'.format(index, value)
        else:
            topi = '-1: 0.0\n'
        top5_str += topi
    print(top5_str)


if __name__ == '__main__':
    host_name = get_host()
    if host_name == 'RK3562':
        rknn_model = RK3562_RKNN_MODEL
    else:
        print("This demo cannot run on the current platform: {}".format(host_name))
        exit(-1)

    rknn_lite = RKNNLite()
    print('--> Load RKNN model')
    ret = rknn_lite.load_rknn(rknn_model)
    if ret != 0:
        print('Load RKNN model failed')
        exit(ret)
    print('done')

    ori_img = cv2.imread('./space_shuttle_224.jpg')
    img = cv2.cvtColor(ori_img, cv2.COLOR_BGR2RGB)
    img = np.expand_dims(img, 0)
    print('--> Init runtime environment')
    ret = rknn_lite.init_runtime()
    if ret != 0:
        print('Init runtime environment failed')
        exit(ret)
    print('done')
    print('--> Running model')
    outputs = rknn_lite.inference(inputs=[img])
    show_top5(outputs)
    print('done')

    rknn_lite.release()
