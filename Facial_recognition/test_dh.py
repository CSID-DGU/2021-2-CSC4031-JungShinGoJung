import page 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
import cv2
import FaceLogin



class mainWindow(QDialog, page.Ui_Form_main):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.nextpage)
        self.pushButton2.clicked.connect(self.play)
    
    def nextpage(self):
      widget.setCurrentIndex(widget.currentIndex()+1)

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


class nextPage(QDialog, page.Ui_Form_next):
    def __init__(self):
        faceid=FaceLogin.DetectFace()
        super(nextPage, self).__init__()
        self.setupUi(self, faceid)
        self.pushButton.clicked.connect(self.back)

    def back(self):
        widget.setCurrentIndex(widget.currentIndex()-1)


       
 


if __name__ == "__main__":
    import sys
    #FaceLogin.TakeImages()
    #FaceLogin.TrainImages()
    
    app = QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QStackedWidget()
    main_window = mainWindow()
    next_page = nextPage()
    widget.addWidget(main_window)
    widget.addWidget(next_page)
    widget.showFullScreen()
    widget.show()
    sys.exit(app.exec_())

