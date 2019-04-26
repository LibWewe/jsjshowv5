#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@file: icoToPy.py
@version: v1.0 
@author: WeWe 
@time: 2018/07/13 9:22
@lib v: Python 3.6.4 /2.7.14
@description:This file is fro ...  
"""
import base64


def picToPy(fileNames):
    for file in fileNames:
        with open(file, "rb") as pic:
            b64Str = base64.b64encode(pic.read())
        picDataStr = "%s = '%s'" % (file.replace(".", "_"), b64Str.decode()) + "\n"
        with open("icon.py", "a+") as fpy:
            fpy.write(picDataStr)


def main():
    files = ["Back.ico", "Close.ico", "endPage1.ico", "Eye.ico", "firstPage1.ico",
             "lastPage2.ico", "prevPage2.ico", "Printer.ico", "refresh1.ico",
             "table.png","table2.png","logo.png","logo2.png"]
    picToPy(files)


if __name__ == "__main__":
    main()
    pass


"""
table2 表头部分代码
pointArray = [QPoint(15, 22), QPoint(25, 46), QPoint(25, 70), QPoint(25, 94), QPoint(25, 119),
                      QPoint(25, 143),QPoint(25, 167), QPoint(25, 192), QPoint(25, 217), QPoint(25, 242),
                      QPoint(25, 265),QPoint(25, 291), QPoint(25, 315), QPoint(25, 340), QPoint(25, 364)]
        font.setPixelSize(14)
        painter.setFont(font)
        painter.drawText(pointArray[0], "织轴卡信息")
        font.setPixelSize(12)
        painter.setFont(font)
        painter.drawText(pointArray[1], "设备名称")
        painter.drawText(pointArray[2], "机台号")
        painter.drawText(pointArray[3], "所属厂区")
        painter.drawText(pointArray[4], "设备型号")
        painter.drawText(pointArray[5], "纱支")
        painter.drawText(pointArray[6], "轴号")
        painter.drawText(pointArray[7], "班次")
        painter.drawText(pointArray[8], "挡车工姓名")
        painter.drawText(pointArray[9], "班长姓名")
        painter.drawText(pointArray[10], "匹数")
        painter.drawText(pointArray[11], "纱长")
        painter.drawText(pointArray[12], "纱长详情")
        painter.drawText(pointArray[13], "品种")
        painter.drawText(pointArray[14], "落轴时间")
"""