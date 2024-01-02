import cv2
import mediapipe as mp
import time
import pyfirmata

Nfing = 5
cap = cv2.VideoCapture(0)

#Call hand pipe line module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        # print("Input is an integer number. Number = ", val)
        bv = True
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            # print("Input is a float  number. Number = ", val)
            bv = True
        except ValueError:
            # print("No.. input is not a number. It's a string")
            bv = False
    return bv

cport = input('Enter the camera port: ')
while not (check_user_input(cport)):
    print('Please enter a number not string')
    cport = input('Enter the camera port: ')

comport = input('Enter the arduino board COM port: ')
while not (check_user_input(comport)):
    print('Please enter a number not string')
    comport = input('Enter the arduino board COM port: ')

board=pyfirmata.Arduino('COM'+comport)
led_1=board.get_pin('d:13:o') #Set pin to output
led_2=board.get_pin('d:12:o')
led_3=board.get_pin('d:11:o')
led_4=board.get_pin('d:10:o')
led_5=board.get_pin('d:9:o')

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    Nfing = 0
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                
                if id == 12:
                    id12 = int(id)
                    cy12 = cy
                if id == 11:
                    id11 = int(id)
                    cy11 = cy
                if id == 16:
                    id16 = int(id)
                    cy16 = cy
                if id == 15:
                    id15 = int(id)
                    cy15 = cy
                if id == 20:
                    id20 = int(id)
                    cy20 = cy
                if id == 19:
                    id19 = int(id)
                    cy19 = cy
                if id == 8:
                    id8 = int(id)
                    cy8 = cy
                if id == 7:
                    id7 = int(id)
                    cy7 = cy
                
                if id == 3:
                    id3 = int(id)
                    cx3 = cx
                if id == 4:
                    id4 = int(id)
                    cx4 = cx
                if id == 5:
                   id5 = int(id)
                   cx5 = cx
                if id == 17 :
                   id17 = int(id)
                   cx17 = cx


            
            
            fing = ["Thumb","Index", "Midele" , "Ring", "Pinkle"]
        
            if cy20 < cy19:
                    Nfing += 1
                    cv2.putText(img, fing[4], (10, 450), cv2.FONT_HERSHEY_PLAIN, 3,
                (0, 204, 255), 3)
                    led_5.write(1)
            else: led_5.write(0)
                 
            if cy16 < cy15:
                    Nfing += 1
                    cv2.putText(img, fing[3], (10, 400), cv2.FONT_HERSHEY_PLAIN, 3,
                (0, 204, 255), 3)
                    led_4.write(1)
            else: led_4.write(0)

            if cy12 < cy11 :
                    Nfing += 1
                    cv2.putText(img, fing[2], (10, 350), cv2.FONT_HERSHEY_PLAIN, 3,
                (0, 204, 255), 3)
                    led_3.write(1)
            else : led_3.write(0)
            if cy8 < cy7 :
                    Nfing += 1
                    cv2.putText(img, fing[1], (10, 300), cv2.FONT_HERSHEY_PLAIN, 3,
                (0, 204, 255), 3)
                    led_2.write(1)
            else : led_2.write(0)
            if cx4 > cx3 :
                    Nfing += 1
                    cv2.putText(img, fing[0], (10, 250), cv2.FONT_HERSHEY_PLAIN, 3,
                (0, 204, 255), 3)
                    led_1.write(1)
            else : led_1.write(0)
            
            if cx4 > cx3 and cy8 < cy7 and cy20 < cy19 and cy12 > cy11 and cy16 > cy15 :
                 cv2.putText(img, "I LOVE U <3", (300, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (0, 204, 255), 3)
            if cx4 < cx3 and cy8 < cy7 and cy20 < cy19 and cy12 > cy11 and cy16 > cy15 :
                 cv2.putText(img, "Rock n Roll", (300, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (0, 204, 255), 3)
            if cx4 > cx3 and cy8 > cy7 and cy20 < cy19 and cy12 > cy11 and cy16 > cy15 :
                 cv2.putText(img, "Carabao", (400, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (0, 204, 255), 3)

            

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
        

    cv2.putText(img, str(int(Nfing)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (0, 204, 255), 3)
    
    cv2.putText(img, "PAWARIT", (400, 450), cv2.FONT_HERSHEY_PLAIN, 3,
                (0, 204, 255), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
#Closeing all open windows
#cv2.destroyAllWindows()