from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_MainWindow
import sys
import cv2
import mediapipe as mp
import joblib
import numpy as np

class Ui_main(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)  # 父类的构造函数
        self.widget = QtWidgets.QMainWindow()
        self.timer_camera = QtCore.QTimer()  # 定义定时器，用于控制显示视频的帧率
        self.cap = cv2.VideoCapture()  # 视频流
        self.CAM_NUM = 0  # 为0时表示视频流来自笔记本内置摄像头
        self.setupUi(self.widget)
        self.slot_init()  # 初始化槽函数
        self.widget.show()

        # 初始化mediaPipe框架
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)

    # 调用所有函数
    def slot_init(self):
        self.button_open_camera.clicked.connect(self.button_open_camera_clicked)  # 若该按键被点击，启动定时器开始循环检测
        self.timer_camera.timeout.connect(self.show_camera)
        self.button_close.clicked.connect(self.widget.close)

    def button_open_camera_clicked(self):
        if self.timer_camera.isActive() == False:
            flag = self.cap.open(self.CAM_NUM)
            if flag == False:
                QtWidgets.QMessageBox.warning(self, 'warning', "请检查相机于电脑是否连接正确", buttons=QtWidgets.QMessageBox.Ok)
            else:
                self.timer_camera.start(15)  # 每过15ms从摄像头中取一帧显示
                self.button_open_camera.setText('关闭摄像头')
        else:
            self.timer_camera.stop()  # 关闭定时器
            self.cap.release()  # 释放视频流
            self.label_show_camera.clear()  # 清空视频显示区域
            self.button_open_camera.setText('打开摄像头')
            self.hands.close()
            cv2.destroyAllWindows()

    # 处理mediaPipe返回的数据
    def data_clean(self, landmark):
        data = landmark[0]
        # 手部有21个坐标点，每个坐标点用三个轴代表，共有63个元素
        try:
            data = str(data)
            data = data.strip().split('\n')
            garbage = ['landmark {', '  visibility: 0.0', '  presence: 0.0', '}']
            without_garbage = []
            clean = []
            for i in data:
                if i not in garbage:
                    without_garbage.append(i)

            for i in without_garbage:
                i = i.strip()
                clean.append(i[2:])

            for i in range(0, len(clean)):
                clean[i] = float(clean[i])
            return ([clean])

        except:
            return (np.zeros([1, 63], dtype=int)[0])

    def show_camera(self):
        success, self.image = self.cap.read()  # 从视频流中读取
        show = cv2.flip(self.image, 1)
        show = cv2.resize(show, (640, 480))  # 把读到的帧的大小重新设置为 640x480
        if not success:
            self.timer_camera.stop()
            QtWidgets.QMessageBox.warning(self, 'warning', "打开失败！", buttons=QtWidgets.QMessageBox.Ok)

        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        show.flags.writeable = False  # 为了提高性能，可以选择将图像标记为不可写
        results = self.hands.process(show)  # 将图像输入mediaPipe模型，返回结果

        show.flags.writeable = True  # 恢复图像可写
        show = cv2.cvtColor(show, cv2.COLOR_RGB2BGR)  # 将图像颜色恢复

        # 摄像头打开时，当模型检测到手掌，multi_hand_landmarks值为True
        if results.multi_hand_landmarks:
            # 可能有多个手掌，此处是遍历每个手掌
            for hand_landmarks in results.multi_hand_landmarks:
                # 在图像上绘制手部关节节点
                self.mp_drawing.draw_landmarks(show, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

            # 调用数据处理函数
            cleaned_landmark = self.data_clean(results.multi_hand_landmarks)
            # 如果检测到手掌，并且数据有效，则加载预训练模型
            if cleaned_landmark:
                clf = joblib.load('model/model.pkl')
                y_pred = clf.predict(cleaned_landmark)  # 模型预测
            self.answer.setText(str(int(y_pred)))
            self.answer.setStyleSheet(
                "font-family: Microsoft YaHei; \n"
                "font-size: 100px; \n"
                "font-weight: 1800; \n"
                "padding-left: 80px; \n"
                "background: white; \n"
                "border-style:solid;\n"
                "border-color: black;\n"
            )
        else:
            self.answer.setText(" ")    # 未检测到手掌则清空label栏中内容

        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0],
                                 QtGui.QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
        self.label_show_camera.setPixmap(QtGui.QPixmap.fromImage(showImage))  # 往显示视频的Label里 显示QImage


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_main()
    sys.exit(app.exec_())