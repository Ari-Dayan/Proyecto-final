import mediapipe as mp
import cv2
from PIL import Image
import imutils

cap = cv2.VideoCapture(0)



#las variables necesarias para la deteccion de manos
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils



#las variables usads para crear el cuadrado
hand_points = []
Top_x = 0
Top_y = 0
Low_x = 99999
Low_y = 99999
contador = 0


#las variables para recortar las fotos
recorte = 0
imAux = 0
numFotos = 0
strFotos = ""
for i in range (21):
    hand_points.append(0)

#una clase en la que le daremos a una lista las coordenadas de los 20 landmarks
class ScreenPoints():
    def __init__(self, lm_x, lm_y, lm_z):
        HEIGHT, WIDTH, CHANNEL = img.shape
        self.x = int(lm_x * WIDTH)
        self.y = int(lm_y * HEIGHT)
        self.z = lm_z
      
with mpHands.Hands(min_detection_confidence = 0.8, min_tracking_confidence = 0.4) as hands:

    while True:

    
        succes, img = cap.read()
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)


        HEIGHT, WIDTH, CHANNEL = img.shape
        Top_x = 3
        Top_y = 3
        Low_x = WIDTH
        Low_y = HEIGHT
#____________________________________________________________________________________________________________________________________________________________________________________________________
    #esto es para ahorrrarnos una conversion del color de la imagen, detecta las posiciones en la imagen RGB, pero las dibuja en la otra
        if results.multi_hand_landmarks:

            for handLms in results.multi_hand_landmarks:

            #en este loop sacaremos los x e y de los landmark
                for id, lm in enumerate(handLms.landmark):                
                    hand_points[id] = ScreenPoints(lm.x, lm.y, lm.z)
                

                    if hand_points[id].x > Top_x:
                        Top_x = hand_points[id].x
                
                    if hand_points[id].y > Top_y:
                        Top_y = hand_points[id].y

                            
                    if hand_points[id].x < Low_x:
                        Low_x = hand_points[id].x
                
                    if hand_points[id].y < Low_y:
                        Low_y = hand_points[id].y
                    #cv2.circle(img,(hand_x[id], hand_y[id]), 10, (134,82,43), cv2.FILLED)
#____________________________________________________________________________________________________________________________________________________________________________________________________
    


            #aca dibujo en la imagen los puntos y las conexiones
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

        HEIGHT, WIDTH, CHANNEL = img.shape
        #dibujamos un rectangulo al rededor de la mano
        cv2.rectangle(img, (Low_x -10, Low_y -10), (Top_x +10, Top_y +10), (255, 0, 0),2)

        

        #recorto el rectangulo
        imAux = img.copy()

       # recorte = imAux.crop(Top_x, Top_y, Low_x, Low_y)
    
        img = cv2.flip(img, 1)
        if Top_x<=0 :
            Top_x = 1

        if Top_y<=0 :
            Top_y = 1


        if Low_x<=0 :
           Low_x = 1

        if Low_y<=0 :
            Low_y = 1
        recorte = imAux[Low_y:Top_y, Low_x:Top_x]
   
        sized_img = imutils.resize(recorte, width=200, height=300)

        if results.multi_hand_landmarks:
            strFotos = str(numFotos)
            numFotos = numFotos +1
            #cv2.imwrite(strFotos, recorte)
            

        #reseteamos las variables

        if results.multi_hand_landmarks:
            cv2.imshow("deteccion de manos", sized_img)
            cv2.waitKey(1)
