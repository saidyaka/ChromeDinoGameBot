import pyautogui
import time
import numpy as np 
from PIL import ImageGrab, ImageOps, Image

class coordinates():
    replay = (337,191)
    dinosaur = (336, 420)
#starts the game for you
def restart():
    time.sleep(2)  
    pyautogui.click(coordinates.replay)
    pyautogui.click(coordinates.replay)
def jump():
  
    # pressing Space to overcome Bush 
    pyautogui.keyDown('space') 
  
    # so that Space Key will be recognized easily 
    time.sleep(0.05)  
  
    # printing jump to input
    
    print("jump")         
    time.sleep(0.10) 
  
    # releasing the Space Key  
    pyautogui.keyUp('space')
    time.sleep(0.10)  

    #go down after the jump faster
    pyautogui.keyDown('arrow_down')
    pyautogui.keyUp('arrow_down')
  

def imageGrab():  
    # defining the coordinates of box in front of dinosaur  
    dinosaur = coordinates.dinosaur
    box = (dinosaur[0]+40, dinosaur[1], dinosaur[0]+30, dinosaur[1]+100) 
  
    image = ImageGrab.grab(box) 
    
    #d = ImageGrab.grab(dino) 
    # converting RGB to Grayscale to 
    # make processing easy and result faster  
    grayImage = ImageOps.grayscale(image) 
    
    # using numpy to get sum of all pixels 
    a = np.array(grayImage.getcolors()) 
  
    # returning the sum 
    summothy = a.sum()
    print(summothy)  
    return summothy 

restart()

while True:  
     # the number is the sum of the white pixels, you should change it depending on the number you get without any bushes/birds 
     if(imageGrab()!= 10338 ):    
        jump()   
        # time to recognize the operation performed by above function  
        time.sleep(0.1)      