from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium_stealth import stealth

import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def prepare_browser():
    chrome_options = webdriver.ChromeOptions()
    proxy = "server:port"
    #chrome_options.add_argument(f'--proxy-server={proxy}')
    chrome_options.add_argument("start-maximized")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation","enable-logging"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options= chrome_options)
    stealth(driver,
        user_agent= 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36',
        languages= ["en-US", "en"],
        vendor=  "Google Inc.",
        platform=  "Win32",
        webgl_vendor=  "Intel Inc.",
        renderer=  "Intel Iris OpenGL Engine",
        fix_hairline= False,
        run_on_insecure_origins= False,
        )
    return driver
urls = 'https://socketgames-kube.evoplay.games/gamepage/crash?user_id=10051044595&session_token=250_5344_7b2230223a223130303531303434353935222c2231223a2231222c2232223a2231222c2273223a223766343162303838633765633336656134653838343932663062656631366539227d&currency=DEM&denomination=1&callback_version=2&language=en&game_name=crash&backurl=&cashurl=&s=28e50280ad52c39e36e7a83758540eae&hosts%5B0%5D=https%3A%2F%2Fsocketgames-kube.evoplay.games%2Fgamepage%2F&hide_currency=0'
def dealer(url):
    driver = prepare_browser()  
    driver.get("" + url)
    time.sleep(2)
    
    history = driver.find_element(By.XPATH,value = '//*[@id="app"]/div/div[1]/div[5]').text
    return history


print(dealer(urls))