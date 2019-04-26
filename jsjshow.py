#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@file: jsjshow.py
@version: v1.0 
@author: WeWe 
@time: 2018/06/21 9:36
@lib v: Python 3.6.4 /2.7.14
@description:This file is fro ...  
"""

import urllib.request
import urllib.parse
import json
import http.cookiejar
import time

headerstr = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8'
}


def func():
    pass


class jsj():
    """
    通过url访问浆纱机云平台，实现对其的登陆、获取设备列表、织轴卡列表、织轴卡详细情况
    """

    def __init__(self):
        """
        cookies_filename:将获取的cookie存入到本地文件
        """
        self.cookies_filename = "cookies.py"
        self.url = 'http://47.94.84.139:82'
        self.cookies = http.cookiejar.MozillaCookieJar(self.cookies_filename)
        self.handler = urllib.request.HTTPCookieProcessor(self.cookies)
        self.opener = urllib.request.build_opener(self.handler)
        self.message = ""
        self.machineData = {}
        self.wearListData = {}
        self.wearCardData = {}

    def login(self, account=None, password=None):
        """
        登陆浆纱机云平台
        :param account: 用户名
        :param password: 密码
        :return:0 登陆成功；-1账号或密码错误；-2网络访问异常
        """
        loginInfo = {"account": account, "password": password}
        loginInfoJson_str = json.dumps(loginInfo).encode("utf-8")
        loginUrl = self.url + '/login'
        req = urllib.request.Request(url=loginUrl, data=loginInfoJson_str, headers=headerstr)
        try:
            res = self.opener.open(req)
            jsoncode = json.load(res)
            self.cookies.save(ignore_discard=True, ignore_expires=True)
            for item in self.cookies:
                print('Name = ' + item.name)
                print('Value = ' + item.value)
        except Exception as e:
            print("================login err=====================")
            print(e)
            print("==============================================")
            return -2
        if jsoncode["code"] != 0:
            self.message = jsoncode["message"]
            return jsoncode["code"]
        return 0

    def machineList(self, pageNo=1, pageSize=10):
        """

        :param pageNo:
        :return:
        """
        machineCountUrl = self.url + "/machine/listByStatus"
        listPar = {"pageNo": pageNo, "pageSize": pageSize}
        listParStr = json.dumps(listPar).encode("utf-8")
        req = urllib.request.Request(url=machineCountUrl, data=listParStr, headers=headerstr)
        try:
            res = self.opener.open(req)
            jsoncode = json.load(res)
            # print(jsoncode)
            # print("设备编号 设备名称 厂区 在线状态")
            # for machine in jsoncode["data"]["rows"]:
            #     # print(machine['machineNo'], machine['machineName'], machine['plantName'], machine['status'])
            #     print(machine)
        except Exception as e:
            print("================machine list err=====================")
            print(e)
            print("=====================================================")
            return -2
        if jsoncode["code"] != 0:
            self.message = jsoncode["message"]
            return jsoncode["code"]
        self.machineData = jsoncode
        return 0

    def weaverCardList(self, machineId=0, pageNo=1, pageSize=10):
        """

        :param machineId:
        :param pageNo:
        :param pageSize:
        :return:
        """
        weaverCardUrl = self.url + "/weaverCard/list"
        weaverCardInfo = {"pageNo": pageNo, "pageSize": pageSize, "machineId": machineId}
        weaverCardInfostr = json.dumps(weaverCardInfo).encode("utf-8")
        req = urllib.request.Request(url=weaverCardUrl, data=weaverCardInfostr, headers=headerstr)
        try:
            res = self.opener.open(req)
            jsoncode = json.load(res)
            # print(jsoncode)
            # for item in jsoncode["data"]["rows"]:
            #     print(item)
        except Exception as e:
            print("================weaver Card List err=====================")
            print(e)
            print("=========================================================")
            return -2
        if jsoncode["code"] != 0:
            self.message = jsoncode["message"]
            return jsoncode["code"]
        self.wearListData = jsoncode
        return 0

    def weaverCard(self, cardId=0):
        """

        :param cardId:
        :return:
        """
        weaverCardUrl = self.url + "/weaverCard/detail"
        weaverCardInfo = {"id": cardId}
        weaverCardInfostr = json.dumps(weaverCardInfo).encode("utf-8")
        req = urllib.request.Request(url=weaverCardUrl, data=weaverCardInfostr, headers=headerstr)
        try:
            res = self.opener.open(req)
            jsoncode = json.load(res)
            # print(jsoncode["data"]["gmtDoff"])
            # timesttam = int(jsoncode["data"]["gmtDoff"])
            # time_array = time.localtime(timesttam / 1000)
            # datestr = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
            # print(datestr)
        except Exception as e:
            print("================weaver Card err=====================")
            print(e)
            print("=========================================================")
            return -2
        if jsoncode["code"] != 0:
            self.message = jsoncode["message"]
            return jsoncode["code"]
        self.wearCardData = jsoncode
        return 0


def main():
    """

    :return:
    """
    lfjsj = jsj()
    lfjsj.login("jslfscz", "123456")
    # lfjsj.machineList(pageNo=1,pageSize=15)
    lfjsj.weaverCardList(pageNo=1, pageSize=3, machineId=29)
    # lfjsj.weaverCard(cardId=159002)


if __name__ == "__main__":
    main()
    pass
