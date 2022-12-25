# 人机交互期末项目

## 介绍
本项目基于MediaPipe框架实现手势识别的功能，用python3.8完成开发，依赖于python版本的numpy，joblib，pandas，sklearn等库和jupyter Notebook工具完成人工智能部分的模型训练，开发和使用，以及用opencv和pyqt完成客户端的简单开发和对视频流的操作。

本项目在原项目的基础上中学习和重写，修改了一些无效的操作，对图像数据训练并转存为csv文件的代码进行了修改，新增了交互界面封装了原手势识别文件，并在原项目代码上添加了注释。本项目非本人原创，
地址：[https://github.com/arpita739/Real-time-Vernacular-Sign-Language-Recognition-using-MediaPipe-and-Machine-Learning](https://github.com/arpita739/Real-time-Vernacular-Sign-Language-Recognition-using-MediaPipe-and-Machine-Learning)

## 软件结构
项目的文件结构图如下： (不包括数据集文件夹)

```
files_tree
│
│  EXTRACT_DATA.py
│  files_arrange.py
│  hand_detection_webcam.py
│  main.py
│  TrainImgCapture.py
│  ui.py
│  UI.ui
│  
├─dataSet
│      final_datasetBSL.csv
│      
├─Detection
│      Numbers_Detection.ipynb
│      
└─model
        model.pkl
        
```
项目数据集的创建规则为 RESIZED_DATASET > 以标签名区分的文件夹 > 图像文件.png，文件夹也可根据自己需要改名，但需要同步更新EXTRACT_DATA.py代码。

- EXTRACT_DATA.py： 将创建的数据集（图片）在MediaPipe的帮助下转换为MediaPipe规则的63个数据点，并存入到csv文件中保存，即将图像转换为数据。
- files_arrange.py： 文件整理程序，负责将数据集图片按规律命名。
- hand_detection_webcam.py： 原项目文件，已通过自己的理解加上注释。
- TrainImgCapture.py： 通过opencv快速截取数据集图片，保存路径得自己修改。程序按下键盘's'截取一张图片（可反复点击），按下'q'退出程序。
- ui.py： 依靠pyqt的pyuic工具将Designer.exe生成的ui文件转换的py文件。
- UI.ui： 依靠pyqt的图形化设计程序Designer.exe构建的交互界面文件。
- main.py: 主程序入口，运行即可使用。
- dataSet文件夹：存放的是图像集转换成的数据集
- Detection文件夹： 存放的是训练模型的算法
- model文件夹： 存放的是生成的模型

## 运行界面
![输入图片说明](%E7%B4%A0%E6%9D%90%E5%9B%BE%E7%89%87/1.png)
![输入图片说明](%E7%B4%A0%E6%9D%90%E5%9B%BE%E7%89%87/2.png)
![输入图片说明](%E7%B4%A0%E6%9D%90%E5%9B%BE%E7%89%87/3.png)

## 使用说明

若要运行该程序，请确保本机python环境有MediaPipe框架，sklearn，opencv，pyqt，pyqt-tool，numpy，ipython，jupyter notebook等（缺什么下什么就ok）

- 若要自建数据，请按上面描述的去建文件夹；
- 先拍照，用TrainImgCapture.py；
- 拍完整理文件名，用files_arrange.py；
- 然后将图像转为csv文件数据，用EXTRACT_DATA.py；
- 训练数据，用Detection文件夹里的ipython_notebook文件训练；
- 完成上述步骤后，要使用自建数据的手势识别，用main.py即可。

### 小小建议

喜欢的话可以点个小星星

若项目出现问题，请联系我
