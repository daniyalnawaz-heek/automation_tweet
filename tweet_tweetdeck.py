from selenium import webdriver
import time
import pyautogui
path="D:/Downloads/chromedriver_win32/chromedriver.exe"
driver=webdriver.Chrome(executable_path=path)
driver.get("http://google.com")
driver.maximize_window()
driver.get("https://mobile.twitter.com/login?hide_message=true&redirect_after_login=https%3A%2F%2Ftweetdeck.twitter.com%2F%3Fvia_twitter_login%3Dtrue")
time.sleep(5)
mypass=open("tpass.txt","r")
time.sleep(5)
pyautogui.typewrite("daniyalnawaz.heek@gmail.com")
pyautogui.press("tab")
pyautogui.typewrite(str(mypass.read()))
pyautogui.press("enter")
time.sleep(15)
pyautogui.keyDown("ctrl")
pyautogui.keyDown("l")
pyautogui.keyUp("l")
pyautogui.keyUp("ctrl")
time.sleep(3)
for i in range(0,6):
  pyautogui.press("tab")
glock=open("tweet_spam.txt","r")  
for word in glock:
  pyautogui.typewrite(word)  
  pyautogui.keyDown("ctrl")
  pyautogui.keyDown("enter")
  pyautogui.keyUp("enter")
  pyautogui.keyUp("ctrl")
  time.sleep(3)

print("done tweeting")
driver.close()



