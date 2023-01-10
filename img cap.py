import cv2
import os
import keyboard
import csv

path = r'C:\Users\Zharb\Documents\GitHub\Image-capture\IMG'
cam = cv2.VideoCapture(0)
img_counter = 0
video = 'video'
angle = 0
#t_end = time.time() + 60 * 0.5
#while time.time() < t_end:
while True:

    result, image = cam.read()
    Cat = ['center','left','right', 'steering', 'throttle', 'reverse', 'speed']

    if result:
        cv2.imshow(video, image)
        if keyboard.is_pressed('c'):
            print("c is pressed")
            img_name=f'center_{img_counter}.png'
            file = os.path.join(path, img_name)
            cv2.imwrite(file, image)
            img_counter += 1
            #angle=current_angle
            dict ={"center": file,"left":'null',"right":'null', "steering": angle, "throttle":'null', "reverse":'null', "speed":'null'}
            with open('demo.csv', 'a') as csv_file:
                dict_object = csv.DictWriter(csv_file, fieldnames = Cat) 
                dict_object.writerow(dict)

            
        if keyboard.is_pressed('q'):
            break
        
        cv2.waitKey(20)

cam.release()
cam.destroyAllWindows()