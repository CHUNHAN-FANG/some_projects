import numpy as np
import cv2
import dlib
from PIL import Image, ImageDraw, ImageFont

# 使用dlib自带的frontal_face_detector作为人脸提取器
detector = dlib.get_frontal_face_detector()

# 使用官方模型构建特征提取器
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


def cv2ImgAddText(img,text,left, top, textColor=(0, 255, 0), textSize=20):
    if (isinstance(img, np.ndarray)):  #判断是否OpenCV图片类型
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img)
    fontText = ImageFont.truetype("font/simsun.ttc", textSize, encoding="utf-8")
    draw.text((left, top), text, textColor, font=fontText)
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)


if __name__ == '__main__':

    #框住人脸的矩形边框颜色
    #color = (0, 255, 0)

    #捕获指定摄像头的实时视频流
    cap = cv2.VideoCapture(0)

    #循环检测识别人脸
    while True:
        _, frame = cap.read()   #读取一帧视频

        # 图像灰化，降低计算复杂度
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 使用detector进行人脸检测 rects为返回的结果
        rects = detector(frame_gray, 1)

        if len(rects) > 0:            
            for i in range(len(rects)):
                landmarks = np.matrix([[p.x, p.y] for p in predictor(frame,rects[i]).parts()])
                for idx, point in enumerate(rects):
                    shape = predictor(frame, point)
                #左眼
                pot_0 = "攒竹穴"
                pos_0 = (landmarks[21,0],int(landmarks[21,1]*1.05))#0
                pot_1 = "鱼腰穴"
                pos_1 = (int((landmarks[19,0]+landmarks[20,0])/2),int((landmarks[19,1]+landmarks[20,1])/2))
                pot_2 = "阳白穴"
                pos_2 = (int((landmarks[19,0]+landmarks[20,0])/2),int((landmarks[19,1]+landmarks[20,1])/2+landmarks[19,1]-landmarks[37,1]))
                pot_3 = "印堂穴"#1
                pos_3 = (int((landmarks[21,0]+landmarks[22,0])/2),int((landmarks[21,1]+landmarks[22,1])/2))
                pot_4 = "丝竹空"
                pos_4 = (landmarks[17,0],landmarks[17,1])
                pot_5 = "承泣穴"
                pos_5 = (int((landmarks[41,0]+landmarks[40,0])/2),int(landmarks[41,1])+(landmarks[41,1]-landmarks[37,1]))
                
                #右眼
                pot_6 = "攒竹穴"
                pos_6 = (landmarks[22,0],int(landmarks[22,1]*1.05))
                pot_7 = "鱼腰穴"
                pos_7 = (int((landmarks[23,0]+landmarks[24,0])/2),int((landmarks[23,1]+landmarks[24,1])/2))
                pot_8 = "阳白穴"
                pos_8 = (int((landmarks[23,0]+landmarks[24,0])/2),int((landmarks[23,1]+landmarks[24,1])/2+landmarks[19,1]-landmarks[44,1]))
                pot_9 = "丝竹空"
                pos_9 = (landmarks[26,0],landmarks[26,1])
                pot_10 = "承泣穴"
                pos_10 = (int((landmarks[47,0]+landmarks[46,0])/2),int(landmarks[47,1])+(landmarks[46,1]-landmarks[44,1]))
                pot_11 = "太阳穴"
                pos_11 = (int((landmarks[45,0]+landmarks[16,0])/2),int((landmarks[45,1]+landmarks[16,1])/2))
                pot_12 = "太阳穴"
                pos_12 = (int((landmarks[36,0]+landmarks[0,0])/2),int((landmarks[36,1]+landmarks[0,1])/2))
                
                #鼻嘴
                pot_13 = "迎香穴"
                pos_13 = (landmarks[31,0],landmarks[31,1]-int((landmarks[30,1]-landmarks[29,1])/2))
                pot_14 = "迎香穴"
                pos_14 = (landmarks[35,0],landmarks[35,1]-int((landmarks[30,1]-landmarks[29,1])/2))
                pot_15 = "水沟穴"
                pos_15 = (int((landmarks[33,0]+landmarks[51,0])/2),int((landmarks[33,1]+landmarks[51,1])/2))
                pot_16 = "兑端穴"
                pos_16 = (int((landmarks[62,0]+landmarks[51,0])/2),int((landmarks[62,1]+landmarks[51,1])/2))
                pot_17 = "承浆穴"
                pos_17 = (landmarks[57,0],landmarks[57,1])
                pot_18 = "颊车穴"
                pos_18 = (landmarks[4,0],landmarks[4,1])
                pot_19 = "颊车穴"
                pos_19 = (landmarks[12,0],landmarks[12,1])
                pot_20 = "大迎穴"
                pos_20 = (landmarks[6,0],landmarks[6,1])
                pot_21 = "大迎穴"
                pos_21 = (landmarks[10,0],landmarks[10,1])
                pot_22 = "地仓穴"
                pos_22 = (landmarks[54,0],landmarks[54,1])
                pot_23 = "地仓穴"
                pos_23 = (landmarks[48,0],landmarks[48,1])
                
    
                pot = [pot_0,pot_1,pot_2,pot_3,pot_4,pot_5,pot_6,pot_7,pot_8,pot_9,pot_10,pot_11,pot_12,pot_13,pot_14,pot_15,pot_16,pot_17,pot_18,pot_19,pot_20,pot_21,pot_22,pot_23]
                pos = [pos_0,pos_1,pos_2,pos_3,pos_4,pos_5,pos_6,pos_7,pos_8,pos_9,pos_10,pos_11,pos_12,pos_13,pos_14,pos_15,pos_16,pos_17,pos_18,pos_19,pos_20,pos_21,pos_22,pos_23]

                for i in range(len(pot)):
                    # print(pot[i],pos[i])
                    # 利用cv2.circle给每个特征点画一个圈，共68个
                    cv2.circle(frame, pos[i], 2, color=(0, 255, 0))
                    # 利用cv2.putText输出1-68
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    frame =cv2ImgAddText(frame,pot[i], pos[i][0],pos[i][1],(0,255,255), 10)
            
            
            
        cv2.imshow("find me", frame)

        #等待10毫秒看是否有按键输入
        k = cv2.waitKey(10)
        #如果输入q则退出循环
        if k & 0xFF == ord('q'):
            break

            
    #释放摄像头并销毁所有窗口
    cap.release()
    cv2.destroyAllWindows()