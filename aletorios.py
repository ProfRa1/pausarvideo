import cv2
import mediapipe as mp
import pyautogui

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue
    
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            hand_landmarks_list = []
            for landmark in hand_landmarks.landmark:
                hand_landmarks_list.append((landmark.x, landmark.y))
            
            # Calcula a distância entre os pontos da ponta do polegar e a ponta do dedo médio
            thumb_tip = hand_landmarks_list[4]
            index_tip = hand_landmarks_list[8]
            distance = ((thumb_tip[0] - index_tip[0])**2 + (thumb_tip[1] - index_tip[1])**2)**0.5
            
            # Se a distância for menor que um valor arbitrário, pausa o vídeo
            if distance < 0.1:  # Você p ode ajustar este valor conf  
                pyautogui.press('space')
    
    cv2.imshow('Hand Detection', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
