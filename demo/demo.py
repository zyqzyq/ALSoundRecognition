#coding:utf-8
from naoqi import ALProxy
import chardet
import json
'''/*
 * isr_status参数说明
 * 0:未开始语音识别
 * 1:初始化成功
 * 2:正在识别中
 * 3:识别中止
 * 4:识别失败，请对照错误进行处理
 * 5:识别成功
*/'''
def main():
    asr = ALProxy("ALSoundRecognition", "192.168.3.13", 9559)
    tts = ALProxy("ALTextToSpeech", "192.168.3.13", 9559)
    rec = asr.getStatus()
    print rec
    if rec == 0:
        print u"未初始化成功"
    elif rec == 4:
        asr.restart()
    while 1:
        print "start recognition"
        asr.startSession()
        while 1:
            rec = asr.getStatus()
            if rec == 2:
                continue
            else:
                break
        if rec == 5:
            result = asr.getResult()
            print "result:"
            if result!='':
                result_json = json.loads(result)
                print result_json
                if result_json["rc"]==0:
                    tts.say(result_json["answer"]["text"].encode("utf-8"))
                else:
                    #print result_json["text"],type(result_json["text"])
                    tts.say(result_json["text"].encode("utf-8"))
        elif rec == 4:
            errorCode = asr.getResult()
            print u"error:",errorCode
            asr.stopSession()
        elif rec == 3:
            print "识别中止"
 
if __name__ == "__main__":
    main()
