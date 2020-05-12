from selenium import webdriver
import time

# Going to instagram's website then waiting 3 seconds before continuing
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(3)
# After this it goes to the login page so these next variables are where the login boxes are and it will also enter my login details!

"""Login Page"""
# Getting username box and entering my username
usernameBox = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
usernameBox.send_keys("####")

# Getting password box and entering my password
passwordBox = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
passwordBox.send_keys("#####")

# Getting the login box and clicking, then waiting 3 seconds to continue
loginBox = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div')
loginBox.click()
time.sleep(3)

"""Home Page"""
# Finds the dm button and clicks it, then waits 3 seconds
directMsgBox = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a')
directMsgBox.click()
time.sleep(3)

"""DM Page"""
# Finds the first box and clicks it, waits 1 second
dmBox = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a')
dmBox.click()
time.sleep(1)

# Finds and Clicks on the text area and enters the phrase you want, waits 2 seconds and the clicks send
def sendMsg(phrase):
    textArea = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
    textArea.click()
    textArea.send_keys(phrase)
    time.sleep(0.5)
    clickSend = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')
    clickSend.click()

for i in range(100):
    sendMsg("spam message")
