import page_dh
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
import cv2
import FaceLogin
import sys


class mainWindow(QDialog, page_dh.Ui_Form_main):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.OpenLoginClass)
        # self.pushButton2.clicked.connect(self.play)

    def OpenLoginClass(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

    def PirCheck(self):
        pirPin = 7
        GPIO.setup(pirPin, GPIO.IN, GPIO.PUD_UP)
        counter = 0
        while True:
            if GPIO.input(pirPin) == GPIO.LOW:
                #다음 창 열고, 현재 창 없애는 작업, 초 설정작업 필요
                self.OpenLoginClass()
            else:
                counter += 1


        ###로그인 페이지
class Login(QDialog, page_dh.Ui_Form_next):
    def __init__(self):
        faceid=FaceLogin.DetectFace()
        super(Login, self).__init__()
        self.setupUi(self, faceid)
        self.pushButton.clicked.connect(self.back)

    ### 페이스 로그인
    def face_login(self):
        pass

    def OpenMedicineClass(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

    ###임시 뒤로가기 버튼
    def back(self):
        widget.setCurrentIndex(widget.currentIndex()-1)



class Medicine(QDialog):
    def __init__(self) :
        super().__init__()


class Emotion(QDialog):
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
    #FaceLogin.TakeImages()
    #FaceLogin.TrainImages()
    app = QtWidgets.QApplication(sys.argv)

    ###스택용 위젯
    widget=QtWidgets.QStackedWidget()

    ### 다이얼로그 위젯 생성
    main_window = mainWindow()
    Login = Login()


    widget.addWidget(main_window)
    widget.addWidget(Login)

    widget.showFullScreen()

    sys.exit(app.exec_())
