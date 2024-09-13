# 客户端 RpcClient.py
# -*- coding: utf-8 -*-
import json
import socket
import os

class TCPClient(object):
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host, port):
        """链接Server端"""
        self.sock.connect((host, port))

    def send(self, data):
        """将数据发送到Server端"""
        self.sock.send(data)

    def recv(self, length):
        """接受Server端回传的数据"""
        return self.sock.recv(length)


class RPCStub(object):

    def __getattr__(self, function):
        def _func(*args, **kwargs):
            d = {'method_name': function, 'method_args': args, 'method_kwargs': kwargs}
            self.send(json.dumps(d).encode('utf-8'))  # 发送数据
            data = self.recv(36864)  # 接收方法执行后返回的结果
            return data.decode('utf-8')

        setattr(self, function, _func)
        return _func


class RPCClient(TCPClient, RPCStub):
    pass


c = RPCClient()
c.connect('127.0.0.1', 5003)
while True:
    data = input('请输入一个字符来进行模型选择（1整数传递加法；2整数传递减法；5写入文件；6图片测试；）：')   #接收用户输入

    if data == '1':
        data1 = input('请输入属性1的值：')
        data2 = input('请输入属性2的值：')
        data3 = input('请输入属性3的值：')
        print(c.add(data1, data2, data3))
    if data == '2':

      c.sub()
    if data == '3':

        # 获取用户输入的数值
        values = input("请输入数值，多个数值之间用空格分隔：")
        # 将输入的数值拆分成列表
        numbers = values.split()
        # 打开文件并写入数值
        with open("file_w.txt", "w") as file:
            # 遍历数值列表
            for number in numbers:
                # 写入数值到文件，并加上回车符
                file.write(number + "\n")
        # 关闭文件
        file.close()
        print(c.file_wr())

    if data == '4':
        # 获取用户输入的图片路径
        image_path = input("请输入图片路径：")
        #D:\develop\rpc_c_s\0001-01.jpg
        # 读取图片内容
        print(c.img(image_path))

    if data == '5':
        # 获取用户输入的数值
        values = input("请输入数值，多个数值之间用空格分隔：")
        # 将输入的数值拆分成列表
        numbers = values.split()
        # 打开文件并写入数值
        with open("file_to_send.txt", "w") as file:
            # 遍历数值列表
            for number in numbers:
                # 写入数值到文件，并加上回车符
                file.write(number + "\n")
        # 关闭文件
        file.close()

        with open('file_to_send.txt', 'r') as file:
            data1 = file.read()
        #print(data1)
        #data1=9
        print(c.file_wr1(data1))
    if data == '6':
        # 获取用户输入的图片路径
        image_path = input("请输入图片路径：")
        #D:\yolov5-5.0\rpc_c_s\0001-01.jpg
        # 读取图片数据
        with open(image_path, "r") as f:
            image_data = f.read()
        # 读取图片内容
        print(c.img1(image_data))
    if not data:  #如果用户输入为空，直接回车就会发送""，""就是代表false
        break