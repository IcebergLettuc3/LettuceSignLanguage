import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils



  imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  results = hands.process(imgRGB)
  # print(results.multi_hand_landmarks)

  if results.multi_hand_landmarks:
    for handLms in results.multi_hand_landmarks:
      for id, lm in enumerate(handLms.landmark):
        # print(id, lm)
        h, w, c = img.shape
        cx, cy = int(lm.x*w), int(lm.y*h)
        # print(id, cx, cy)
        if id == 12:
          cv2.circle(img, (cx, cy), 20, (255, 0, 255), cv2.FILLED) #this line highlights the tip of the middle finger

      mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

  
  

def main():
  pTime = 0
  cTime = 0
  while True:
    success, img = cap.read()

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 40), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 32, 49), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)


if __name__ == "__main__":
