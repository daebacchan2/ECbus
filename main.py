# import xmltodict
# import json
# import tkinter
# import time
# import threading
#
# from tkinter import *
# window=tkinter.Tk()
# window.title("YUN DAE HEE")
# window.geometry("640x400")
# window.resizable(False, False)
#
# canvas=tkinter.Canvas(window,relief="solid", bd='1')
# line=canvas.create_line(0,330,640,330,width="10")
# line1=canvas.create_line(0,230,640,230,width="10")
# line3=canvas.create_line(50,280,100,280,width="10")
# line4=canvas.create_line(150,280,200,280,width="10")
# line5=canvas.create_line(250,280,300,280,width="10")
# line6=canvas.create_line(350,280,400,280,width="10")
# line7=canvas.create_line(450,280,500,280,width="10")
# line8=canvas.create_line(550,280,600,280,width="10")
# sq=canvas.create_rectangle(0,330,640,400,fill="#a0e060")
# oval=canvas.create_oval(100,155,150,105,fill="#98F306",width=3)
# line9=canvas.create_line(125,155,125,230,width=5)
# oval1=canvas.create_oval(300,155,350,105,fill="#98F306",width=3)
# line10=canvas.create_line(325,155,325,230,width=5)
# oval2=canvas.create_oval(500,155,550,105,fill="#98F306",width=3)
# line11=canvas.create_line(525,155,525,230,width=5)
#
# canvas.pack(expand=True, fill="both")
# img = PhotoImage(file='eunchan.png')
# smallPng=img.subsample(5,3)
# x=0
# bus=canvas.create_image(0,280,image=smallPng)
# def myway():
#     global x,bus
#     canvas.delete(bus)
#     for i in range(1000):
#         bus = canvas.create_image(x, 280, image=smallPng)
#         x += 1
#         print(x)
#         time.sleep(0.1)
#         canvas.delete(bus)
# thread1=threading.Thread(target=myway)
# thread1.start()
# window.mainloop()
#
# canvas=tkinter.Canvas(window, relief="solid", bd=2)
#
#
# polygon=canvas.create_polygon(50, 50, 170, 170, 100, 170, outline="yellow")
# oval=canvas.create_oval(100, 200, 150, 250, fill="blue", width=3)
# arc=canvas.create_arc(100, 100, 300, 300, start=0, extent=150, fill='red')
#
# canvas.pack()
# Python3 샘플 코드 #
import pandas as pd
import numpy as np
# Python3 샘플 코드 #

# Python3 샘플 코드 #
#
#
# import requests
#
# url = 'http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRouteAll'
# params ={'serviceKey' : 'De9xX5IQfcrOPRXQnr4v7a/NyzYfniSnX/x5RIh4q6vgLKS2JbZXxPl0Vb1ax4fsc3CFkyKjffKfZ0Iu5fi2aA==', 'busRouteId' : '100100118' }
#
# response = requests.get(url, params=params)
# print(response.content)

# import requests
#
# url = 'http://ws.bus.go.kr/api/rest/arrive/getLowArrInfoByStId'
# params ={'serviceKey' : 'De9xX5IQfcrOPRXQnr4v7a/NyzYfniSnX/x5RIh4q6vgLKS2JbZXxPl0Vb1ax4fsc3CFkyKjffKfZ0Iu5fi2aA==', 'stId' : '112000001' }
#
# response = requests.get(url, params=params)
# print(response.content)
# print()
import requests

class Station():
    def __init__(self):
        self.stationListIDList =[]
    def push(self,stationId):
        self.stationListIDList.append(stationId)
class Arrmsg1():
    def __init__(self):
        self.Arrmsg1List = []
    def push(self, arrmsg1):
        self.Arrmsg1List.append(arrmsg1)
class Arrmsg2():
    def __init__(self):
        self.Arrmsg2List = []
    def push(self, arrmsg2):
        self.Arrmsg2List.append(arrmsg2)
class BusRouteAbrv():
    def __init__(self):
        self.busRouteAbrvList = []
    def push(self, busRouteAbrv):
        self.busRouteAbrvList.append(busRouteAbrv)
class BusRouteId():
    def __init__(self):
        self.busRouteIdList = []
    def push(self, busRouteId):
        self.busRouteIdList.append(busRouteId)


station= Station()
arrmsg1=Arrmsg1()
arrmsg2=Arrmsg2()
busRouteAbrv=BusRouteAbrv()
busRouteId=BusRouteId()

def getLowStationByNameFunction():
    global station
    url = 'http://ws.bus.go.kr/api/rest/stationinfo/getLowStationByName'
    params ={'serviceKey' : 'De9xX5IQfcrOPRXQnr4v7a/NyzYfniSnX/x5RIh4q6vgLKS2JbZXxPl0Vb1ax4fsc3CFkyKjffKfZ0Iu5fi2aA==', 'stSrch' : '시립은평병원','resultType' : 'json' }
    response = requests.get(url, params=params)
    json_type = response.json()

    for i in json_type['msgBody']['itemList']:
        station.push(i['stId'])
def getArrmsg1():
    global arrmsg1
    url = 'http://ws.bus.go.kr/api/rest/arrive/getLowArrInfoByStId'
    params = {'serviceKey': 'De9xX5IQfcrOPRXQnr4v7a/NyzYfniSnX/x5RIh4q6vgLKS2JbZXxPl0Vb1ax4fsc3CFkyKjffKfZ0Iu5fi2aA==','stId':'111000173','resultType' : 'json'}
    response = requests.get(url, params=params)
    json_type = response.json()
    for i in json_type['msgBody']['itemList']:
        arrmsg1.push(i['arrmsg1'])
        arrmsg2.push(i['arrmsg2'])
        busRouteAbrv.push(i['busRouteAbrv'])
        busRouteId.push(i['busRouteId'])




# getLowStationByNameFunction()
getArrmsg1()

print()
for i in range(len(station.stationListIDList)):
    print(station.stationListIDList[i])
print()
for i in range(len(arrmsg1.Arrmsg1List)):
    print(arrmsg1.Arrmsg1List[i])
print()
for i in range(len(arrmsg2.Arrmsg2List)):
    print(arrmsg2.Arrmsg2List[i])
print()
for i in range(len(busRouteAbrv.busRouteAbrvList)):
    print(busRouteAbrv.busRouteAbrvList[i])
print()
for i in range(len(busRouteId.busRouteIdList)):
    print(busRouteId.busRouteIdList[i])


# import requests
#
# url = 'http://ws.bus.go.kr/api/rest/stationinfo/getLowStationByName'
# params ={'serviceKey' : 'De9xX5IQfcrOPRXQnr4v7a/NyzYfniSnX/x5RIh4q6vgLKS2JbZXxPl0Vb1ax4fsc3CFkyKjffKfZ0Iu5fi2aA==', 'stSrch' : '은평시립병원' , 'resultType' : 'json'}
# response = requests.get(url, params=params)
#
# # data라는 dict형에 retData를 복사해줌
# json_type = response.json()
# print(json_type)
# for i in json_type['msgBody']['itemList']:
#     print(i)
#     break

# import requests, xmltodict, json
# import pandas as pd
#
# key = "De9xX5IQfcrOPRXQnr4v7a%2FNyzYfniSnX%2Fx5RIh4q6vgLKS2JbZXxPl0Vb1ax4fsc3CFkyKjffKfZ0Iu5fi2aA%3D%3D" # 일반 인증키 라는 부분을 지우고 대입하시면 됩니다. ex) key = "2@dfg3#dafgrt$"
# url = "http://ws.bus.go.kr/api/rest/busRouteInfo/getStaionByRoute?ServiceKey={}&busRouteId=100100112".format(key)
#
# content = requests.get(url).content # GET요청
# dict=xmltodict.parse(content) # XML을 dictionary로 파싱
# #파싱은 어떤 페이지(문서, html 등)에서 내가 원하는 데이터를 특정 패턴이나 순서로 추출해 가공하는 것
#
# jsonString = json.dumps(dict['ServiceResult']['msgBody']['itemList'], ensure_ascii=False) # dict을 json으로 변환
# jsonObj = json.loads(jsonString) # json을 dict으로 변환
#
# for i in range(len(jsonObj)):
#     print(jsonObj[i]['stationNm']) # stationNm : 정류소명