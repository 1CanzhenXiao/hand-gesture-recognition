import cv2
import mediapipe as mp
import joblib
import numpy as np

# mediaPipe python解决方案的API在solutions中
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# 初始化,第一个参数为检测置信度，第二个为追踪置信度（值越高调用越多，关节模型越稳定，但越卡）
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)
cap = cv2.VideoCapture(0)   # 打开电脑摄像头，参数也可为路径

# 处理mediaPipe返回的数据，因为程序不是面向对象建模，因此函数得先写前面
def data_clean(landmark):
    data = landmark[0]
    # 手部有21个坐标点，每个坐标点用三个轴代表，共有63个元素
    try:
        data = str(data)
        data = data.strip().split('\n')
        garbage = ['landmark {', '  visibility: 0.0', '  presence: 0.0', '}']
        without_garbage = []
        for i in data:
            if i not in garbage:
                without_garbage.append(i)

        clean = []
        for i in without_garbage:
            i = i.strip()
            clean.append(i[2:])
        for i in range(0, len(clean)):
            clean[i] = float(clean[i])
        return ([clean])

    except:
        return (np.zeros([1, 63], dtype=int)[0])


while cap.isOpened():
    success, image = cap.read()
    image = cv2.flip(image, 1)   # 图像水平翻转，提升用户观感
    if not success:
        break

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)   # 转换图像色值，否则图像显示时颜色失真
    image.flags.writeable = False   # 为了提高性能，可以选择将图像标记为不可写
    results = hands.process(image)  # 将图像输入mediaPipe模型，返回结果

    image.flags.writeable = True    # 恢复图像可写
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)     # 将图像颜色恢复

    # 摄像头打开时，当模型检测到手掌，multi_hand_landmarks值为True
    if results.multi_hand_landmarks:
        # 可能有多个手掌，此处是遍历每个手掌
        for hand_landmarks in results.multi_hand_landmarks:
            # 在图像上绘制手部关节节点
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # 调用数据处理函数
        cleaned_landmark = data_clean(results.multi_hand_landmarks)
        # 如果检测到手掌，并且数据有效，则加载预训练模型
        if cleaned_landmark:
            clf = joblib.load('model/model.pkl')
            y_pred = clf.predict(cleaned_landmark)  # 模型预测
            image = cv2.putText(image, str(y_pred[0]), (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 2,
                                cv2.LINE_AA)

    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
        break

hands.close()
cap.release()
cv2.destroyAllWindows()
