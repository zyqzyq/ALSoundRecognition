README for ALSoundRecognition SDK
-----------------------
## 模块介绍
    ALSoundRecognition 是适用于NAO机器人的语音识别模块。
    该模块通过调用科大讯飞平台api实现语音识别以及语义理解功能。
    相对于系统自带的模块有对中文识别准确率更高，识别反应速度更快的优势。
    目前处于试验阶段，每日交互体验次数有500次的限制。
    欢迎大家测试使用，如果有什么建议可以发邮件到497533265@qq.com.
    
## 快速上手
    1.使用winscp将asr文件夹复制到机器人/home/nao/目录下并全部给可执行权限。
    2.使用asr文件夹中的autoload.ini替换系统naoqi/preferences/autoload.ini文件。
    3.重启naoqi，运行demo/demo.py
    
    在线文档：[https://zyqzyq.github.io/ALSoundRecognition](https://zyqzyq.github.io/ALSoundRecognition)
    
    
## 文件目录
    asr:
        lib
        autoload.ini (NAO 开机自启动文件)
        loadasr.sh (加载模块的文件)
        soundrecognition (模块的可执行文件)
    demo:
        demo.py(python sample)
    docs:
        index.html (ALSoundRecognition API文档)

