from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import subprocess
from PIL import Image as cut
import pygetwindow as closeWin
import schedule
from idle_time import IdleMonitor
import pyautogui as gui


load_dotenv()
options = Options()

class Hours:
    @staticmethod
    def get_hours():
        agora = datetime.now()
        return agora.strftime("%m/%Y/%d %H:%M:%S")




class CutImage:
    
    @staticmethod
    def cutImage(path):
        
      fsImageCut =  cut.open(path)
     
      image = fsImageCut.crop((0, 100, 900, 600))


      image.save("fs.png")
      
      
      
class Browser:
    driver = None
    actions = None
    @staticmethod
    def open_browser():
        print("Iniciando processo....")
        # options.add_argument("--headless")  
        options.add_argument("--window-size=1920,1080")

        Browser.driver = webdriver.Chrome(options=options)



        Browser.driver.get(os.getenv("URLSECRET"))
        time.sleep(10)
        Browser.escribeText(os.getenv("EMAILSECRET"))
        time.sleep(10)
        Browser.escribeText(os.getenv("PASSWORLD"))
        time.sleep(15)
        Browser.okKespass()
        time.sleep(40)
        Browser.screenShotAndZoom()
        

    @staticmethod
    def escribeText(text):
      Browser.actions = ActionChains(Browser.driver)
      Browser.actions.send_keys(text + Keys.ENTER)
      Browser.actions.perform()
      
      
    @staticmethod
    def okKespass():
        Browser.actions = ActionChains(Browser.driver)
        Browser.actions.send_keys(Keys.ENTER)
        Browser.actions.perform()
          
          
    @staticmethod
    def screenShotAndZoom():
    
      Browser.driver.execute_script("document.body.style.zoom='50%'")
      
      time.sleep(15)
      
      Browser.driver.save_screenshot("fs.png")
      Browser.driver.quit()
      time.sleep(10)
      CutImage.cutImage("fs.png")
      time.sleep(5)
      subprocess.run([
          "node",
          "bot.js"
      ])
      

class IdleScreen:
    
    @staticmethod
    
    def screenIdle():
        durationTimeMonitor = IdleMonitor.get_monitor()
       
        while True:
            if durationTimeMonitor.get_idle_time() == 180000:
             gui.click()
             time.sleep(30)
             
            
          
class CroonJoob:
    @staticmethod
    
    def jobStart():
        schedule.every(5).minutes.do(Browser.open_browser)
        
        while True:
            schedule.run_pending()
            time.sleep(1)
      
          
CroonJoob.jobStart()
IdleScreen.screenIdle()


