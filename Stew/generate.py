# -*- coding: utf-8 -*-
#@Pjname ;QRcoderecognition
#@Time   :2019/12/11/19:14
#@Author :GhostGuanyin
#@File   :generate.py

import qrcode
import os
import sys
import time


Base_content ="https://www.baidu.com/"
QRImagePath = os.getcwd() + '/qrcode.png'  # 临时存储位置
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)  # 设置图片格式

data = Base_content # 运行时输入数据
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image()
img.save('qrcode.png')  # 生成图片

if sys.platform.find('darwin') >= 0:
    os.system('open %s' % QRImagePath)

elif sys.platform.find('linux') >= 0:
    os.system('xdg-open %s' % QRImagePath)
else:
    os.system('call %s' % QRImagePath)

time.sleep(60)  # 间隔60个单位
os.remove(QRImagePath)  # 删除图