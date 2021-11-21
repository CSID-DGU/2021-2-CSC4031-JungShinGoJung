from pymysql import NULL
import page_dh
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
import cv2
import FaceLogin
import sys
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
import playsound
import os
import pyaudio
import speech_recognition as sr
import time
import simpleaudio
import pygame
from konlpy.tag import Komoran, Kkma, Mecab


class mainWindow(QDialog, page_dh.Ui_Form_main):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        
       
        # self.playsignal.sig.connect(self.playSoundEmitted)
       
        # self.Pir_run()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_A:
            self.OpenLoginClass()
    def mousButtonKind(self, buttons):
        if buttons & Qt.LeftButton:
            self.OpenLoginClass()

    def mousePressEvent(self, e):
        self.mousButtonKind(e.buttons())



        


    def OpenLoginClass(self):
        faceid = FaceLogin.DetectFace()
        login_window = login(faceid)
        widget.addWidget(login_window) #####
        widget.setCurrentIndex(widget.currentIndex()+1) ######

    
    # @pyqtSlot()
    # def playSoundEmitted(self):
    #     playsound.playsound('medi.mp3')
    #     os.remove('medi.mp3')
    #     print("소리재생")



class PlaySignal(QObject):
    sig = pyqtSignal()
    def run(self):
        self.sig.emit()


        



    # def PirCheck(self):
    #     pirPin = 7
    #     GPIO.setup(pirPin, GPIO.IN, GPIO.PUD_UP)
    #     counter = 0
    #     while True:
    #         if GPIO.input(pirPin) == GPIO.LOW:
    #             #다음 창 열고, 현재 창 없애는 작업, 초 설정작업 필요
    #             self.OpenLoginClass()
    #         else:
    #             counter += 1

    def Pir_run(self):
        t1 = pir_thread(self)
        t1.start()

        ###로그인 페이지

class pir_thread( QThread, page_dh.Ui_Form_main):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
    def run(self):
        while True:
            pirPin = 7
            GPIO.setup(pirPin, GPIO.IN, GPIO.PUD_UP)
            counter = 0
            while True:
                if GPIO.input(pirPin) == GPIO.LOW:
                    #다음 창 열고, 현재 창 없애는 작업, 초 설정작업 필요
                    self.OpenLoginClass()
                else:
                    counter += 1


class login(QDialog, page_dh.Ui_Form_next):
    def __init__(self, faceid):
        super(login, self).__init__()
        self.faceid = faceid
        #여기에 위치해 주세요 png
        # self.playsignal = PlaySignal()
        self.setupUi(self, self.faceid)

        # self.playsignal.sig.connect(self.playSoundEmitted)

    def mousButtonKind(self, buttons):
        if buttons & Qt.LeftButton:
            self.OpenEmotionClass()
        if buttons & Qt.RightButton:
            self.playSound()

    def mousePressEvent(self, e):
        self.mousButtonKind(e.buttons())

        
    # def keyPressEvent(self, event):
    #     if event.key() == Qt.Key_N:
    #         self.OpenEmotionClass()
    #     elif event.key() == Qt.Key_P:
    #         self.playSound()


    # @pyqtSlot()
    # def playSoundEmitted(self):
    #     pygame.mixer.init()
    #     pygame.mixer.music.load("medi.mp3")
    #     pygame.mixer.music.play()
    #     # os.remove('medi.mp3')
    #     print("소리재생")

    def playSound(self):
        pygame.mixer.init()
        pygame.mixer.music.load("medi.mp3")
        pygame.mixer.music.play()
        
    

    def OpenEmotionClass(self):
        emotionClass = emotion(self.faceid)
        widget.addWidget(emotionClass)
        widget.setCurrentIndex(widget.currentIndex()+1)
        

    ###임시 뒤로가기 버튼
    def back(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
    

class emotion(QDialog, page_dh.Ui_Form_emotion):
    def __init__(self, faceid):
        super(emotion, self).__init__()
        self.faceid = faceid
        #여기에 위치해 주세요 png
        self.setupUi(self, self.faceid)

    
    def mousButtonKind(self, buttons):
        if buttons & Qt.LeftButton:
            self.record()
        
        if buttons & Qt.RightButton:
            self.playSound()
    
    def mousePressEvent(self, e):
        self.mousButtonKind(e.buttons())




    def playSound(self):
        pygame.mixer.init()
        pygame.mixer.music.load("mood.mp3")
        pygame.mixer.music.play()

    def record(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
        
        stt = r.recognize_google(audio, language='ko')    
        try: print("Google Speech Recognition thinks you said : " + stt)
        except sr.UnknownValueError: print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e: print("Could not request results from Google Speech Recognition service; {0}".format(e))
        
        #텍스트 비식별화
        komoran = Komoran()
        sen = komoran.pos(stt)
        for nlpy in sen:
            if nlpy[1] == 'NNP':
                mk=''
                for a in nlpy[0]:
                    mk = mk + '*'
                print(nlpy[0])
                stt = stt.replace(nlpy[0], mk)
        
        idDate = str(self.faceid) +"_"+time.strftime('%Y_%m_%d', time.localtime(time.time()))
        content = '\n'+idDate +': '+ stt
        file = open('record.txt', 'a') 
        file.write(content)     
        file.close()
        self.capture()
        pygame.mixer.init()
        pygame.mixer.music.load("stretching.mp3")
        pygame.mixer.music.play()
        self.playVideo(self.faceid)
        self.init()
 

    def capture(self):
        filename = str(self.faceid) +"_"+time.strftime('%Y_%m_%d', time.localtime(time.time()))+".jpg"
        cap = cv2.VideoCapture(0)
        if cap.isOpened(): 
            while True:
                ret, fram = cap.read()
                if ret:
                    cv2.imshow("camera",fram) #프레임 이미지 표시
                    cv2.imwrite("Facial_recognition/caputre/"+filename,fram)
                    break
                else:
                    print("no fram")
                    break
        else: print("can't open camera")
        cap.release()
        cv2.destroyAllWindows()


    def init(self):
        widget.setCurrentIndex(widget.currentIndex()-2)
        
    
    def back(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
       
            






class Medicine(QDialog):
    def __init__(self) :
        super().__init__()


class Exercise(QDialog):
    def __init__(self) :
        super().__init__()

    def play(self):
        video = '1234.mp4'
        capture = cv2.VideoCapture(video)
        while(capture.isOpened()):
            ret, img = capture.read()
            if ret:
                cv2.imshow(video, img)
                if cv2.waitKey(25) & 0xFF == ord('q'): break
            else:print("재생불가")
        capture.release()
        cv2.destroyAllWindows()






if __name__ == "__main__":
    ###페이스 로그인 아이디 생성
    # FaceLogin.TakeImages()
    # FaceLogin.TrainImages()
    app = QtWidgets.QApplication(sys.argv)
    print("시작")

    ###스택용 위젯
    widget=QtWidgets.QStackedWidget()
    print("시작2")
    ### 다이얼로그 위젯 생성
    main_window = mainWindow()
    widget.addWidget(main_window)

    widget.showFullScreen()
    print("시작3")




    sys.exit(app.exec_())
