# 人机交互期末项目

#### 介绍
本项目基于MediaPipe框架实现手势识别的功能，用python3.8完成开发，依赖于python版本的numpy，joblib，pandas，sklearn等库和tensorflow2.8框架，jupyter Notebook工具完成人工智能部分的模型训练和开发，以及用opencv和pyqt完成客户端的简单开发和对视频流的操作。

本项目在原项目的基础上中学习和重写，修改了一些无效的操作，对图像数据训练并转存为csv文件的代码进行了修改，新增了交互界面封装了原手势识别文件，并在原项目代码上添加了注释。本项目非本人原创，
地址：[https://github.com/arpita739/Real-time-Vernacular-Sign-Language-Recognition-using-MediaPipe-and-Machine-Learning](http://https://github.com/arpita739/Real-time-Vernacular-Sign-Language-Recognition-using-MediaPipe-and-Machine-Learning)

#### 软件结构
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


#### 安装教程

1.  xxxx
2.  xxxx
3.  xxxx

#### 使用说明

1.  xxxx
2.  xxxx
3.  xxxx

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
