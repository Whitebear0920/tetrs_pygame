from setting import *
from sys import exit

class Main:
    def __init__(self):
        
        #general 
        pygame.init() #初始化
        self.Dispay_Surface = pygame.display.set_mode((Window_Width, Window_Height)) #執行遊戲外框
        self.clock = pygame.time.Clock() #遊戲時刻
        pygame.display.set_caption("Tetris") #設定視窗標題名稱

    def run(self):
        while(True):
            for event in pygame.event.get(): #pygame.event.get() 取得當前發生的事件
                if event.type == pygame.QUIT: #當遊戲狀態為停止時 離開遊戲
                    pygame.quit() #exit everything 
                    exit()
            #display
            self.Dispay_Surface.fill(Gray) #設定背景顏色
            
            #updatating the game
            pygame.display.update()
            self.clock.tick() #控制遊戲幀數

if __name__ == "__main__":
    main = Main()
    main.run()