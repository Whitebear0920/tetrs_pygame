import threading 
import json 
import socket
import os
import time
from game import Game
"""
data = {
            "player" : ,
            "type" : ,
            "value" :
        }

"""

class date_process():

    def __init__(self):
        
        self.Max_Bytes = 65535
        self.server_addr = ("127.0.0.1",57414)
        #取得自己的ip位置
        self.name = socket.gethostname()    #取代nickname


        self.ip_address = socket.gethostbyname(self.name)

        #自己的位置資料 預設port為57414
        self.my_address = (self.ip_address, 57414)

        #對方的位置資料
        self.his_address = ("127.0.0.1", 57414)

        #socket 初始化
        
        
    def connect(self):
        self.msgdict = {
            "type": "connecting"
        }
        self.data = json.dumps(self.msgdict).encode('utf-8')
        # 將Enter Request送到Server
        self.sock.sendto(self.data, self.Server_addr)

        # 等待並接收Server傳回來的訊息，若為Enter Response則繼續下一步，否則繼續等待
        self.is_entered = False
        while not self.is_entered:
            try:
                self.data, address = self.sock.recvfrom(self.Max_Bytes)
                msgdict = json.loads(data.decode('utf-8'))
                if msgdict['type'] == 2:
                    is_entered = True
                    print('成功進入伺服器!!!')
            except:
                print("伺服器連線失敗,5秒後重試")
                for i in range(5):
                    time.sleep(1)
                    print(".", end="",flush = True)
                print()
                data = json.dumps(msgdict).encode("utf-8")
                self.sock.sendto(data, self.server_addr)

    def connect(self):
        return self.is_entered

    def send_message(self):
        print("開始執行send message")
        while(True):
            # 取得使用者輸入的聊天訊息
            self.msgtext = input('請輸入聊天訊息：')
            if self.msgtext[:2] == "%%" and self.msgtext[-2:] == "%%":
                if self.msgtext[2:7] == "Leave":
                    msgdict = {
                        "type" : 6,
                        "nickname" : self.name
                    }
            else:    
                # 建立Message Request訊息的dict物件
                msgdict = {
                    "type": 3,
                    "nickname": self.name,
                    "message": self.msgtext
                }
    # 轉成JSON字串，再轉成bytes
            msgdata = json.dumps(msgdict).encode('utf-8')
            print(msgdata)
            # 將Enter Request送到Server
            self.sock.sendto(msgdata, self.server_addr)
            if (msgdict["type"] == 6):
                print("leave")
                os._exit(0)

    def recv_message(self):
        print("開始執行recv_message")
        while(True):
            # 接收來自Server傳來的訊息
            self.Recdata, self.address = self.sock.recvfrom(self.Max_Bytes)
            self.Recdata = json.loads(self.Recdata.decode('utf-8'))
            if self.Recdata["type"] == "GameOver":
                if self.Recdata["value"] == True:
                    self.game.gameover = True
                    print("win")
            elif self.Recdata["type"] == "Attack":
                print("got attack!")

            
            




        


