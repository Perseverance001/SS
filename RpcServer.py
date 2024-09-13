# 服务端 RpcServer.py
# -*- coding: utf-8 -*-
import json
import subprocess
import os
import socket
from PIL import Image
import os

funs = {}


def register_function(func):
    """Server端方法注册，Client端只可调用被注册的方法"""
    name = func.__name__
    funs[name] = func


class TCPServer(object):

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket = None

    def bind_listen(self, port):
        self.sock.bind(('0.0.0.0', port))
        self.sock.listen(5)

    def accept_receive_close(self):
        """获取Client端信息"""
        if self.client_socket is None:
            (self.client_socket, address) = self.sock.accept()
        if self.client_socket:
            msg = self.client_socket.recv(36864)
            data = self.on_msg(msg)
            self.client_socket.send(data)  # 回传


class RPCStub(object):

    def __init__(self):
        self.data = None

    def call_method(self, data):
        """解析数据，调用对应的方法变将该方法执行结果返回"""
        if len(data) == 0:
            return json.dumps("something wrong").encode('utf-8')
        self.data = json.loads(data.decode('utf-8'))
        method_name = self.data['method_name']
        method_args = self.data['method_args']
        method_kwargs = self.data['method_kwargs']
        res = funs[method_name](*method_args, **method_kwargs)
        data = res
        return json.dumps(data).encode('utf-8')


class RPCServer(TCPServer, RPCStub):
    def __init__(self):
        TCPServer.__init__(self)
        RPCStub.__init__(self)

    def loop(self, port):
        # 循环监听 5003 端口
        self.bind_listen(port)
        print('Server listen 5003 ...')
        while True:
            try:
                self.accept_receive_close()
            except Exception:
                self.client_socket.close()
                self.client_socket = None
                continue

    def on_msg(self, data):
        return self.call_method(data)


@register_function
def add(a, b, c):
    print("已连接1")

    def run_calculate_sum(a, b, c):
        command = f"python calculate_sum.py {a} {b} {c}"
        output = os.popen(command).read()
        return output.strip()

    result = run_calculate_sum(a, b, c)
    print("计算结果:", result)
    return result


@register_function
def sub():
    print("已连接2")

    def run_image():
        command = ["python",  "D:\yolov5-5.0\detect.py"]

        # 执行命令
        subprocess.run(command)
        print("已完成")

    run_image()



@register_function
# 文件读取
def file_wr():
    print("连接成功3")

    def run_process_file(file_path):
        command = f"python process_file.py {file_path}"
        output = os.popen(command).read()
        return output.strip()

    file_path = "C:/Users/27815/Desktop/rpc_c_s/file_w.txt"
    result = run_process_file(file_path)
    print("处理结果:", result)
    return result


@register_function
# 文件读取
def file_wr1(data1):
    print("连接成功5")
    with open('uploaded_file.txt', 'w') as file:
        file.write(data1)

    def run_process_file(file_path):
        command = f"python process_file.py {file_path}"
        output = os.popen(command).read()
        return output.strip()

    # file_name = 'uploaded_file.txt'
    # file_path = os.path.abspath(file_name)
    file_path = "C:/Users/27815/Desktop/rpc_c_s/uploaded_file.txt"
    result = run_process_file(file_path)
    print("处理结果:", result)
    return result


@register_function
# 图片传输测试
def img(image_path):
    print("连接成功4")

    def run_image():
        command = f"D:\yolov5-5.0\detect.py"
        output = os.popen(command).read()
        return output.strip()

    def save_image(image_path, save_directory):
        # 打开图片
        image = Image.open(image_path)

        # 确保保存目录存在
        os.makedirs(save_directory, exist_ok=True)

        # 获取图片文件名
        image_name = os.path.basename(image_path)

        # 拼接保存路径
        save_path = os.path.join(save_directory, image_name)

        # 保存图片
        image.save(save_path)

        print(f"图片已保存至：{save_path}")

    save_directory = "D:\yolov5-5.0\data\images"
    save_image(image_path, save_directory)
    path1 = "D:\yolov5-5.0\runs\detect\exp13\test.jpg"
    result = run_image()
    print("处理结果:", result)
    return result
    # 接收图片数据


@register_function
# 图片传输测试
def img1(image_data):
    print("连接成功6")

    # 保存图片数据到文件
    with open("D:/develop/rpc_c_s/image000.jpg", "wb") as f:
        f.write(image_data)

    def run_image(image_path):
        command = f"python image.py {image_path}"
        output = os.popen(command).read()
        return output.strip()

    image_path = "D:/develop/rpc_c_s/image000.jpg"
    result = run_image(image_path)
    print("处理结果:", result)
    return result
    # 接收图片数据


s = RPCServer()
s.loop(5003)  # 传入要监听的端口
