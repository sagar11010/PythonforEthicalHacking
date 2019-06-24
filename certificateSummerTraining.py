import pyautogui
import time
import pyperclip

def generateme(courseList):
    # Switch to excel
    pyautogui.hotkey('alt','tab')
    time.sleep(2)
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('left')
    time.sleep(1)
    pyautogui.press('left')
    time.sleep(1)
    pyautogui.hotkey('ctrl','c')
    time.sleep(1)
    # Switch to Photoshop
    pyautogui.hotkey('alt','tab')
    time.sleep(2)
    # Click on certificate ID
    id = pyperclip.paste()
    id = id[:-2]
    pyautogui.click(481,160)
    time.sleep(2)
    pyautogui.hotkey('ctrl','a')
    time.sleep(2)
    pyautogui.hotkey('ctrl','v')
    time.sleep(2)
    pyautogui.hotkey('ctrl','enter')
    time.sleep(2)
    # Switch to excel
    pyautogui.hotkey('alt','tab')
    time.sleep(2)
    pyautogui.press('right')
    time.sleep(1)
    pyautogui.hotkey('ctrl','c')
    # Switch to photoshop
    pyautogui.hotkey('alt','tab')
    time.sleep(2)
    # Click on name
    name = pyperclip.paste()
    name = name[:-2]
    pyautogui.click(553,472)
    time.sleep(1)
    pyautogui.hotkey('ctrl','a')
    time.sleep(1)
    pyautogui.hotkey('ctrl','v')
    time.sleep(1)
    pyautogui.hotkey('ctrl','enter')
    time.sleep(2)
    # Switch to excel
    pyautogui.hotkey('alt','tab')
    time.sleep(2)
    pyautogui.press('right')
    time.sleep(1)
    pyautogui.hotkey('ctrl','c')
    time.sleep(1)
    # Switch to photoshop
    pyautogui.hotkey('alt','tab')
    time.sleep(2)
    cloudCource = "Cloud Specialization in Amazon Web Services (AWS), Microsoft Azure, Docker, Ansible, with Python & Redhat Enterprise Linux"
    dataAnal = "Data Analytics Specialization in Big Data, Databricks with AWS, Docker, Ansible, Python & Redhat Enterprise Linux"
    dataSci = "Data Science Specialization in Machine Learning, Deep Learning, Neural Networks & AI with AWS, Azure, Docker, Ansible, Python and Red Hat Enterprise Linux"
    fullStack = "Full Stack Web Developer in Python - Django Framework, Javascript with AWS, Ansible, Docker & Red Hat Enterprise Linux"
    clip = pyperclip.paste()
    clip = clip[:-2]

    # Click on the course
    if clip == cloudCource:
        pyautogui.click(courseList[0],courseList[1])        
    elif clip == dataAnal:
        pyautogui.click(courseList[2],courseList[3])
    elif clip == dataSci:
        pyautogui.click(courseList[4],courseList[4])
    elif clip == fullStack:
        pyautogui.click(courseList[6],courseList[5])
    
        
    time.sleep(2)
    pyautogui.hotkey('ctrl','shift','s')
    time.sleep(2)
    pyautogui.typewrite(name)
    pyautogui.typewrite(" ")
    pyautogui.typewrite(id)
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(6)
    pyautogui.press('enter')
    time.sleep(14)

    # UnClick on the course
    if clip == cloudCource:
        pyautogui.click(courseList[0],courseList[1])        
    elif clip == dataAnal:
        pyautogui.click(courseList[2],courseList[3])
    elif clip == dataSci:
        pyautogui.click(courseList[4],courseList[4])
    elif clip == fullStack:
        pyautogui.click(courseList[6],courseList[5])
    
    time.sleep(2)


# Set tab index
pyautogui.hotkey('alt','tab')
time.sleep(1)
pyautogui.click(240,752)
time.sleep(1)
#---------------------------------------------------------------

courseList = []
courseList[0] = 1140 # Cloud
courseList[1] = 250
courseList[2] = 1139 # DataAnal
courseList[3] = 326
courseList[4] = 1141 # DataSci
courseList[5] = 287
courseList[6] = 1142 # fullStack
courseList[7] = 210

#---------------------------------------------------------------
i = 0
while i<39:
    generateme(courseList)
    i=i+1
