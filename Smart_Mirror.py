# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets #pip install pyqt5(pip install python3-pyqt5)
import forecastio #pip install python-forecastio  [Weather api] [https://github.com/ZeevG/python-forecast.io]
import yapi #pip install yapi [https://github.com/ahmetkotan/yapi]
import feedparser #pip install feedparser [News api] [http://w3devlabs.net/wp/?p=16964]
import datetime
from time import sleep
import threading
import tkinter as tk #this can't pip install
import requests
import json
import cv2
from PyQt5.QtGui import QPixmap, QImage
import pafy #pip install pafy , pip install youtube_dl

#==================================================================================================
#==============UI_MAIN==============================================================================
#==================================================================================================

class Ui_MainWindow(object):
    hello_world = 0
    root = tk.Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    News_url = "http://fs.jtbc.joins.com//RSS/newsflash.xml"
    start_or_stop=False
    start=True

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        palette = QtGui.QPalette()

        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)

        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)

        MainWindow.setPalette(palette)
        #MainWindow.resize(800, 600)
        MainWindow.showFullScreen()

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #날씨 이모티콘 ====================================================================
        self.weather = QtWidgets.QLabel(self.centralwidget)
        self.weather.setGeometry(QtCore.QRect(20, 15, 150,130))
        self.weather.setObjectName("weather")

        #온도 label [온도 출력]
        self.temperature = QtWidgets.QLabel(self.centralwidget)
        self.temperature.setGeometry(QtCore.QRect(25, 120, 150,130))
        self.temperature.setObjectName("temperature")
        self.temperature.setFont(QtGui.QFont("맑은 고딕",20))

        #================================================================================
        #clock 이라는 이름으로 label 생성 [hello world]===================================
        self.clock = QtWidgets.QLabel(self.centralwidget)
        self.clock.setGeometry(QtCore.QRect(200,300,100,50))
        self.clock.setObjectName("clock")

        #time 이라는 이름으로 label 생성 [(오전/오후)시/분]
        self.time = QtWidgets.QLabel(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(170,80,800,60))
        self.time.setObjectName("time")
        #setFont(QtGui.QFont("Font_name",Font_size))
        self.time.setFont(QtGui.QFont("맑은 고딕",50))

        #date 이라는 이름으로 label 생성 [년/월/일]
        self.date = QtWidgets.QLabel(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(180, 15, 300, 50))
        self.date.setObjectName("date")
        self.date.setFont(QtGui.QFont("맑은 고딕",20))
        #===============================================================================
        #clock_button 이라는 이름으로 버튼을 생성 [쓰레드가 잘 작동하는지 확인]
        # self.clock_button = QtWidgets.QPushButton(self.centralwidget)
        # self.clock_button.setGeometry(QtCore.QRect(200, 280, 75, 23))
        # self.clock_button.setObjectName("clock_button")

        # self.youtube_button = QtWidgets.QPushButton(self.centralwidget)
        # self.youtube_button.setGeometry(QtCore.QRect(1500, 450, 75, 23))
        # self.youtube_button.setObjectName("youtube_button")
        #===================================================================
        #new 라벨 생성========================================================
        self.news1 = QtWidgets.QLabel(self.centralwidget)
        self.news1.setGeometry(QtCore.QRect(self.width-470,self.height-350,470,50))
        self.news1.setObjectName("news1")
        self.news1.setFont(QtGui.QFont("맑은 고딕",11))

        self.news2 = QtWidgets.QLabel(self.centralwidget)
        self.news2.setGeometry(QtCore.QRect(self.width-470,self.height-320,470,50))
        self.news2.setObjectName("news2")
        self.news2.setFont(QtGui.QFont("맑은 고딕",11))

        self.news3 = QtWidgets.QLabel(self.centralwidget)
        self.news3.setGeometry(QtCore.QRect(self.width-470,self.height-290,470,50))
        self.news3.setObjectName("news3")
        self.news3.setFont(QtGui.QFont("맑은 고딕",11))

        self.news4 = QtWidgets.QLabel(self.centralwidget)
        self.news4.setGeometry(QtCore.QRect(self.width-470,self.height-260,470,50))
        self.news4.setObjectName("news4")
        self.news4.setFont(QtGui.QFont("맑은 고딕",11))

        self.news5 = QtWidgets.QLabel(self.centralwidget)
        self.news5.setGeometry(QtCore.QRect(self.width-470,self.height-230,470,50))
        self.news5.setObjectName("news5")
        self.news5.setFont(QtGui.QFont("맑은 고딕",11))

        self.news6 = QtWidgets.QLabel(self.centralwidget)
        self.news6.setGeometry(QtCore.QRect(self.width-470,self.height-200,470,50))
        self.news6.setObjectName("news6")
        self.news6.setFont(QtGui.QFont("맑은 고딕",11))

        self.news7 = QtWidgets.QLabel(self.centralwidget)
        self.news7.setGeometry(QtCore.QRect(self.width-470,self.height-170,470,50))
        self.news7.setObjectName("news7")
        self.news7.setFont(QtGui.QFont("맑은 고딕",11))

        self.news8 = QtWidgets.QLabel(self.centralwidget)
        self.news8.setGeometry(QtCore.QRect(self.width-470,self.height-140,470,50))
        self.news8.setObjectName("news8")
        self.news8.setFont(QtGui.QFont("맑은 고딕",11))

        self.news9 = QtWidgets.QLabel(self.centralwidget)
        self.news9.setGeometry(QtCore.QRect(self.width-470,self.height-110,470,50))
        self.news9.setObjectName("news9")
        self.news9.setFont(QtGui.QFont("맑은 고딕",11))

        self.news10 = QtWidgets.QLabel(self.centralwidget)
        self.news10.setGeometry(QtCore.QRect(self.width-470,self.height-80,470,50))
        self.news10.setObjectName("news10")
        self.news10.setFont(QtGui.QFont("맑은 고딕",11))

        #====================================================================
        #meal_label 생성 =====================================================
        self.b_label = QtWidgets.QLabel(self.centralwidget)
        self.b_label.setGeometry(QtCore.QRect(50,self.height-500,470,200))
        self.b_label.setObjectName("b_label")
        self.b_label.setText("아침")
        self.b_label.setFont(QtGui.QFont("맑은 고딕",11))
        self.breakfast_label = QtWidgets.QLabel(self.centralwidget)
        self.breakfast_label.setGeometry(QtCore.QRect(125,self.height-500,470,200))
        self.breakfast_label.setObjectName("breakfast_label")
        self.breakfast_label.setFont(QtGui.QFont("맑은 고딕",11))

        self.l_label = QtWidgets.QLabel(self.centralwidget)
        self.l_label.setGeometry(QtCore.QRect(50,self.height-350,470,200))
        self.l_label.setObjectName("l_label")
        self.l_label.setText("점심")
        self.l_label.setFont(QtGui.QFont("맑은 고딕",11))
        self.lunch_label = QtWidgets.QLabel(self.centralwidget)
        self.lunch_label.setGeometry(QtCore.QRect(125,self.height-350,470,200))
        self.lunch_label.setObjectName("lunch_label")
        self.lunch_label.setFont(QtGui.QFont("맑은 고딕",11))

        self.d_label = QtWidgets.QLabel(self.centralwidget)
        self.d_label.setGeometry(QtCore.QRect(50,self.height-200,470,200))
        self.d_label.setObjectName("d_label")
        self.d_label.setText("저녁")
        self.d_label.setFont(QtGui.QFont("맑은 고딕",11))
        self.dinner_label = QtWidgets.QLabel(self.centralwidget)
        self.dinner_label.setGeometry(QtCore.QRect(125,self.height-200,470,200))
        self.dinner_label.setObjectName("dinner_label")
        self.dinner_label.setFont(QtGui.QFont("맑은 고딕",11))

        #====================================================================
        #video_viewer_label 생성 =====================================================
        self.video_viewer_label = QtWidgets.QLabel(self.centralwidget)
        self.video_viewer_label.setGeometry(QtCore.QRect(self.width-400,0,400,225))
        self.video_viewer_label.setObjectName("video_viewer_label")

        self.video_name_label = QtWidgets.QLabel(self.centralwidget)
        self.video_name_label.setGeometry(QtCore.QRect(self.width-400,250,400,20))
        self.video_name_label.setObjectName("video_name_label")
        self.video_name_label.setFont(QtGui.QFont("맑은 고딕",11))
        #===================================================================
        #===================================================================

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SmartMirror"))
        # self.clock_button.setText(_translate("MainWindow", "PushButton"))
        # self.youtube_button.setText(_translate("MainWindow", "Youtube"))

    #-----------------------------------------------------------------------------------------
    # 이벤트
    # EVENT
    #-----------------------------------------------------------------------------------------

    #버튼을 누를시
    # def button(self,MainWindow):
    #     self.clock_button.clicked.connect(self.hello) #누를시 hello 함수랑 연결
    #     self.youtube_button.clicked.connect(self.Stop_video)

    #프린트 hello world 함수
    def hello(self,MainWindow):
        self.hello_world = self.hello_world + 1
        self.clock.setText("%d %s" %(self.hello_world, "hello world"))

    #시간을 알려주는 함수 메인 화면에 생성
    # now.(year,month,day,hour,minute,second)
    def set_time(self,MainWindow):
        EvenOrAfter = "오전"
        while True:
            now=datetime.datetime.now() #현재 시각을 시스템에서 가져옴
            hour=now.hour

            if(now.hour>=12):
                EvenOrAfter="오후"
                hour=now.hour%12

                if(now.hour==12):
                    hour=12

            else:
                EvenOrAfter="오전"

            self.date.setText("%s년 %s월 %s일"%(now.year,now.month,now.day))
            self.time.setText(EvenOrAfter+" %s시 %s분" %(hour,now.minute))
            sleep(1)

    #weather (아이콘 설정 및 기온 출력)
    def weather_icon(self,MainWindow):
        while True:
            api_key = "darksky_api_key"

            #대구소프트웨어고등학교 위치
            lat = 35.663106
            lng = 128.413759

            #서버 접속후 데이터를 받아옴
            forecast = forecastio.load_forecast(api_key, lat, lng)
            weather=forecast.currently()


            weather_cashe=weather.icon

            self.temperature.setText("[ %.1f ℃ ]" %(weather.temperature))

            if "day" in weather_cashe:
                if "partly-cloudy" in weather_cashe:
                    self.weather.setPixmap(QtGui.QPixmap("weather_icon\cloudy_day.png"))
                elif "cloudy" in weather_cashe:
                    self.weather.setPixmap(QtGui.QPixmap("weather_icon\clouds.png"))
                elif "clear" in weather_cashe:
                    self.weather.setPixmap(QtGui.QPixmap("weather_icon\sun.png"))

            elif "night" in weather_cashe:
                if "partly-cloudy" in weather_cashe:
                    self.weather.setPixmap(QtGui.QPixmap("weather_icon\cloudy_night.png"))
                elif "cloudy" in weather_cashe:
                    self.weather.setPixmap(QtGui.QPixmap("weather_icon\clouds.png"))
                elif "clear" in weather_cashe:
                    self.weather.setPixmap(QtGui.QPixmap("weather_icon\moon.png"))

            elif "cloudy" in weather_cashe:
                self.weather.setPixmap(QtGui.QPixmap("weather_icon\clouds.png"))

            elif "rain" in weather_cashe:
                self.weather.setPixmap(QtGui.QPixmap("weather_icon\drop.png"))

            elif "snow" in weather_cashe:
                self.weather.setPixmap(QtGui.QPixmap("weather_icon\snowflake.png"))

            sleep(300)

    #News (타이틀&기사 출력)
    def News(self,MainWindow) :
        d = feedparser.parse(self.News_url)
        while True :
            num = 1
            for e in d.entries :
                if num%10==1:
                    self.news1.setText("[%d] %s"%(num,e.title))
                elif num%10==2:
                    self.news2.setText("[%d] %s"%(num,e.title))
                elif num%10==3:
                    self.news3.setText("[%d] %s"%(num,e.title))
                elif num%10==4:
                    self.news4.setText("[%d] %s"%(num,e.title))
                elif num%10==5:
                    self.news5.setText("[%d] %s"%(num,e.title))
                elif num%10==6:
                    self.news6.setText("[%d] %s"%(num,e.title))
                elif num%10==7:
                    self.news7.setText("[%d] %s"%(num,e.title))
                elif num%10==8:
                    self.news8.setText("[%d] %s"%(num,e.title))
                elif num%10==9:
                    self.news9.setText("[%d] %s"%(num,e.title))
                elif num%10==0:
                    self.news10.setText("[%d] %s"%(num,e.title))
                num=num+1
                sleep(1)

    #급식 출력
    def School_meal(self,MainWindow):
        while True:
            now=datetime.datetime.now()

            response = requests.get('https://schoolmenukr.ml/api/high/D100000282?year='+str(now.year)+'&month='+str(now.month)+'&date='+str(now.day)+'&hideAllergy=true')
            meal_menu = json.loads(response.text)

            str_menu=str(meal_menu)

            breakfast=""
            lunch=""
            dinner=""

            br=0
            lu=0
            di=0

            i=0

            while True:
                try :
                    if "'" in str_menu[br]:
                        if "[" in str_menu[br-1] :
                            if " " in  str_menu[br-2] :
                                if ":" in str_menu[br-3] :
                                    if "'" in str_menu[br-4] :
                                        if "t" in str_menu[br-5] :
                                            br=br+1
                                            break
                    br=br+1
                except IndexError as e :
                    pass
            breakfast=breakfast+" "
            while True:
                try :
                    if "]" in str_menu[br] :
                        break
                    elif "'" in str_menu[br] :
                        pass
                    elif "," in str_menu[br] :
                        breakfast=breakfast+"\n"
                    else :
                        breakfast=breakfast+str_menu[br]

                    br=br+1
                except IndexError as e :
                    pass
            self.breakfast_label.setText(breakfast)

            while True:
                try :
                    if "'" in str_menu[lu]:
                        if "[" in str_menu[lu-1] :
                            if " " in  str_menu[lu-2] :
                                if ":" in str_menu[lu-3] :
                                    if "'" in str_menu[lu-4] :
                                        if "h" in str_menu[lu-5] :
                                            lu=lu+1
                                            break
                    lu=lu+1;
                except IndexError as e:
                    pass
            lunch=lunch+" "
            while True:
                try :
                    if "]" in str_menu[lu] :
                        break
                    elif "'" in str_menu[lu] :
                        pass
                    elif "," in str_menu[lu] :
                        lunch=lunch+"\n"
                    else :
                        lunch=lunch+str_menu[lu]

                    lu=lu+1
                except IndexError as e:
                    pass
            self.lunch_label.setText(lunch)

            while True:
                try :
                    if "'" in str_menu[di]:
                        if "[" in str_menu[di-1] :
                            if " " in  str_menu[di-2] :
                                if ":" in str_menu[di-3] :
                                    if "'" in str_menu[di-4] :
                                        if "r" in str_menu[di-5] :
                                            di=di+1
                                            break
                    di=di+1;
                except IndexError as e :
                    pass
            dinner=dinner+" "
            while True:
                try :
                    if "]" in str_menu[di] :
                        break
                    elif "'" in str_menu[di] :
                        pass
                    elif "," in str_menu[di] :
                        dinner=dinner+"\n"
                    else :
                        dinner=dinner+str_menu[di]

                    di=di+1
                except IndexError as e:
                    pass
            self.dinner_label.setText(dinner)

    def Video_to_frame(self, MainWindow):
        while True:
            url = "https://youtu.be/"

            api = yapi.YoutubeAPI('youtube_data_api_ver3_key')
            video_name="자막뉴스 "
            results = api.general_search(video_name, max_results=2)

            str_results=str(results)

            i=0
            TrueOrFalse=False
            video_id=""

            #print(str_results)

            while True:
                try :

                    if "'" in str_results[i]:
                        if "=" in str_results[i-1]:
                            if "d" in str_results[i-2]:
                                if "I" in str_results[i-3]:
                                    if "o" in str_results[i-4]:
                                        i=i+1
                                        TrueOrFalse=True
                                        break
                    i=i+1

                except IndexError as e:
                    print("error")
                    break

            while TrueOrFalse:
                if "'" in str_results[i]:
                    break
                else :
                    video_id=video_id+str_results[i]

                i=i+1

            url = url+video_id

            try :
                vPafy = pafy.new(url)
                self.video_name_label.setText(vPafy.title)
                video_length=vPafy.length/60

            except Exception as e :
                self.video_viewer_label.setText("Error")
                self.start=False
            print(video_length/60)

            play = vPafy.getbest(preftype="mp4")

            cap = cv2.VideoCapture(play.url)

            while self.start:
                self.ret, self.frame = cap.read()
                if self.ret:
                    self.rgbImage = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                    self.convertToQtFormat = QImage(self.rgbImage.data, self.rgbImage.shape[1], self.rgbImage.shape[0], QImage.Format_RGB888)

                    self.pixmap = QPixmap(self.convertToQtFormat)
                    self.p = self.pixmap.scaled(400, 225, QtCore.Qt.IgnoreAspectRatio)

                    self.video_viewer_label.setPixmap(self.p)
                    self.video_viewer_label.update()

                    sleep(0.02) #Youtube 영상 1프레임당 0.02초

                else :
                    break

                if self.start_or_stop:
                    break

            cap.release()
            cv2.destroyAllWindows()

    # def Stop_video(self,MainWindow) :
    #     if self.start_or_stop :
    #         self.start_or_stop=False
    #     else :
    #         self.start_or_stop=True

    #----------------------------------------------------------------------------------------------------
    #------------------------ 쓰레드 ---------------------------------------------------------------------
    #----------------------------------------------------------------------------------------------------

    #Set_time을 쓰레드로 사용
    def time_start(self,MainWindow):
        thread=threading.Thread(target=self.set_time,args=(self,))
        thread.daemon=True #프로그램 종료시 프로세스도 함께 종료 (백그라운드 재생 X)
        thread.start()

    #weather_icon을 쓰레드로 사용
    def weather_start(self,MainWindow):
        thread=threading.Thread(target=self.weather_icon,args=(self,))
        thread.daemon=True #프로그램 종료시 프로세스도 함께 종료 (백그라운드 재생 X)
        thread.start()

    #News를 쓰레드로 사용
    def News_start(self,MainWindow):
        thread=threading.Thread(target=self.News,args=(self,))
        thread.daemon=True #프로그램 종료시 프로세스도 함께 종료 (백그라운드 재생 X)
        thread.start()

    #school_meal을 쓰레드로 사용
    def meal_start(self,MainWindow):
        thread=threading.Thread(target=self.School_meal,args=(self,))
        thread.daemon=True #프로그램 종료시 프로세스도 함께 종료 (백그라운드 재생 X)
        thread.start()

    #video_to_frame을 쓰레드로 사용
    def video_thread(self,MainWindow):
        thread=threading.Thread(target=self.Video_to_frame,args=(self,))
        thread.daemon=True #프로그램 종료시 프로세스도 함께 종료 (백그라운드 재생 X)
        thread.start()

#-------------메인---------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)
    # ui.button(MainWindow)

    ui.time_start(MainWindow) #time thread
    ui.weather_start(MainWindow) #weather thread
    ui.News_start(MainWindow) #news thread
    ui.meal_start(MainWindow) #meal thread
    ui.video_thread(MainWindow) #video thread

    MainWindow.show()

    sys.exit(app.exec_())
