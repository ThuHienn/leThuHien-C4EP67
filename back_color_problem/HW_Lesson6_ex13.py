# #13 run méo lên :<<
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont, QBrush
from PyQt5.QtCore import Qt, QRectF, QTimer
from PyQt5.QtMultimedia import  QSound
from random import choice

import back_color

class GameWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.shapes = back_color.get_shapes()
        self.generate_quiz()
        self.initUI()
        self.initTimer()
        # self.initSound()


    # def initSound(self):
    #     self.correctSound = QSound('sound/correct.wav')
    #     self.incorrectSound = QSound('sound/incorrect.wav')


    def initTimer(self):
        self.timer = QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.timerTick)


    def timerTick(self):
        self.timer.stop()
        self.generate_quiz()
        self.repaint()


    def initUI(self):
        self.text = "Back color"
        self.setGeometry(0, 0, 260, 340)
        self.setFixedSize(260, 340)
        self.show()


    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.fillRect(event.rect(), QBrush(QColor("#FFFFFF")))

        for shape in self.shapes:
            brush = QBrush(QColor(shape['color']))
            rect = shape['rect']
            qp.fillRect(rect[0], rect[1], rect[2], rect[3], brush)
        qp.setPen(QColor(self.quiz_color))
        qp.setFont(QFont('Times New Roman', 20, QFont.Bold))
        if self.quiz_type:
            textRect = QRectF(0, 0, 260, 60)
        else:
            textRect = QRectF(0, 280, 260, 60)
        qp.drawText(textRect, Qt.AlignCenter, self.quiz_text)
        qp.end()


    def generate_quiz(self):
        [self.quiz_text, self.quiz_color, self.quiz_type] = back_color.generate_quiz()


    # def mouseReleaseEvent(self, mouseEvent):
    #     x = mouseEvent.x()
    #     y = mouseEvent.y()
    #     if back_color.mouse_press(x, y, self.quiz_text, self.quiz_color, self.quiz_type):
    #         self.quiz_text = 'Correct'
    #         self.correctSound.play()
    #     else:
    #         self.quiz_text = 'Incorrect'
    #         self.incorrectSound.play()
    #     self.timer.start()
    #     self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = GameWindow()
    sys.exit(app.exec_())


from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]
def generate_quiz():
    import random
    text = random.choice(['blue','red','yellow','green'])
    color = random.choice(['#3F51B5','#C62828','#FFD600','#4CAF50'])
    quiz_type = random.choice([0,1])
    return [text,color,quiz_type]

quiz = generate_quiz()

def mouse_press():
    import win32gui
    (x,y) = win32gui.GetCursorPos()
    if quiz[2] == 0:
        for item in shapes:
            if item('text') == quiz[0]:
                i = shapes.index(item)
                x_range = shapes[i]['rect'][0] + 100
                y_range = shapes[i]['rect'][1] + 100 
                if x in range(shapes[i]['rect'][0], x_range + 1):
                    if y in range(shapes[i]['rect'][1], y_range + 1):
                        return True
                    else:
                        return False
                else:
                    return False
            
    elif quiz[2] == 1:
        for item in shapes:
            if item('color') == quiz[1]:
                i = shapes.index(item)
                x_range = shapes[i]['rect'][0] + 100
                y_range = shapes[i]['rect'][1] + 100 
                if x in range(shapes[i]['rect'][0], x_range + 1):
                    if y in range(shapes[i]['rect'][1], y_range + 1):
                        return True
                    else:
                        return False
                else:
                    return False

result = mouse_press()
print(result)
        
   
 