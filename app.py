import sys
import subprocess
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QLabel
from PyQt6.QtGui import QIcon, QPixmap, QPalette, QBrush
from PyQt6.QtCore import QTimer, QSize, Qt

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 設定視窗的標題
        self.setWindowTitle(' ' * 20 + '圖片按鈕範例')  # 添加空格以模擬標題居中
        self.setGeometry(100, 100, 400, 300)

        # 設置背景圖片
        self.set_background_image('background.png')

        # 初始化按鈕點擊次數和計時器
        self.button1_click_count = 0
        self.button2_click_count = 0
        self.button3_click_count = 0
        self.double_click_interval = 1000  # 1 秒
        self.timer1 = QTimer()
        self.timer2 = QTimer()
        self.timer3 = QTimer()

        self.timer1.setInterval(self.double_click_interval)
        self.timer1.timeout.connect(self.reset_button1_clicks)

        self.timer2.setInterval(self.double_click_interval)
        self.timer2.timeout.connect(self.reset_button2_clicks)

        self.timer3.setInterval(self.double_click_interval)
        self.timer3.timeout.connect(self.reset_button1_clicks)

        # 創建按鈕並設置不同的圖片和大小
        self.button1 = QPushButton("實時辨識")
        self.button1.setIcon(QIcon('button1_image.png'))  # 設置按鈕1的圖示
        self.button1.setIconSize(QSize(80, 80))  # 設置按鈕1圖示的大小
        self.button1.setFixedSize(100, 100)  # 設置按鈕1的固定大小

        self.button2 = QPushButton("圖片辨識")
        self.button2.setIcon(QIcon('button2_image.png'))  # 設置按鈕2的圖示
        self.button2.setIconSize(QSize(80, 80))  # 設置按鈕2圖示的大小
        self.button2.setFixedSize(100, 100)  # 設置按鈕2的固定大小

        self.button3 = QPushButton("拍照")
        self.button3.setIcon(QIcon('button2_image.png'))  # 設置按鈕2的圖示
        self.button3.setIconSize(QSize(80, 80))  # 設置按鈕2圖示的大小
        self.button3.setFixedSize(100, 100)  # 設置按鈕2的固定大小

        # 連接按鈕點擊信號到槽函數
        self.button1.clicked.connect(self.on_button1_click)
        self.button2.clicked.connect(self.on_button2_click)
        self.button3.clicked.connect(self.on_button3_click)

        # 創建水平佈局來對齊按鈕
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.button1, alignment=Qt.AlignmentFlag.AlignVCenter)
        h_layout.addWidget(self.button2, alignment=Qt.AlignmentFlag.AlignVCenter)
        h_layout.addWidget(self.button3, alignment=Qt.AlignmentFlag.AlignVCenter)

        # 創建一個垂直佈局，將標題標籤和按鈕佈局添加進去
        v_layout = QVBoxLayout()
        
        
        # 創建標題標籤並居中顯示
        title_label = QLabel('圖片按鈕範例', self)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        v_layout.addWidget(title_label)

        # 添加按鈕佈局到垂直佈局中
        v_layout.addLayout(h_layout)

        # 將垂直佈局設置為主容器的佈局
        container = QWidget()
        container.setLayout(v_layout)
        self.setCentralWidget(container)

    def set_background_image(self, image_path):
        # 設置視窗背景圖片
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(QPixmap(image_path).scaled(self.size())))
        self.setPalette(palette)

    def reset_button1_clicks(self):
        self.button1_click_count = 0
        self.timer1.stop()

    def reset_button2_clicks(self):
        self.button2_click_count = 0
        self.timer2.stop()

    def reset_button3_clicks(self):
        self.button3_click_count = 0
        self.timer3.stop()

    def on_button1_click(self):
        self.button1_click_count += 1

        if self.button1_click_count == 1:
            self.timer1.start()
        elif self.button1_click_count == 2:
            self.timer1.stop()
            self.button1_click_count = 0
            self.run_script1()

    def on_button2_click(self):
        self.button2_click_count += 1

        if self.button2_click_count == 1:
            self.timer2.start()
        elif self.button2_click_count == 2:
            self.timer2.stop()
            self.button2_click_count = 0
            self.run_script2()

    def on_button3_click(self):
        self.button3_click_count += 1

        if self.button3_click_count == 1:
            self.timer3.start()
        elif self.button3_click_count == 2:
            self.timer3.stop()
            self.button3_click_count = 0
            self.run_script3()

    def run_script1(self):
        print("按鈕1雙擊偵測到，使用 cmd 開啟 Real-timeIdentification.py...")
        subprocess.Popen(['python', 'Real-timeIdentification.py'], shell=True)  # 替換 'script1.py' 為你的第一個腳本名稱
        # self.close()  # 關閉視窗

    def run_script2(self):
        print("按鈕2雙擊偵測到，使用 cmd 開啟 ImageRecognition.py...")
        subprocess.Popen(['python', 'ImageRecognition.py'], shell=True)  # 替換 'script2.py' 為你的第二個腳本名稱
        # self.close()  # 關閉視窗

    def run_script3(self):
        print("按鈕3雙擊偵測到，使用 cmd 開啟 Photograph.py...")
        subprocess.Popen(['python', 'Photograph.py'], shell=True)  # 替換 'script2.py' 為你的第二個腳本名稱
        # self.close()  # 關閉視窗

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
