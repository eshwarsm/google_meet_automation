'''
#1 >> Mention your Chrome Driver path
#2 >> Change the username
#3 >> Change the password
#4 >> Mention your Google Meet Links
#5 >> Schedule links as per your timetable
#6 >> Enjoy!!!
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import schedule
import time

#default_chrome_options
opt=Options()
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")

opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 1,
"profile.default_content_setting_values.media_stream_camera": 1,
"profile.default_content_setting_values.geolocation": 1,
"profile.default_content_setting_values.notifications": 1
})

#gmeet
driver=webdriver.Chrome(chrome_options=opt, executable_path='/your/path/./chromedriver')
driver.get('https://meet.google.com')

#signin_button
SignIn = driver.find_element_by_xpath('/html/body/header/div[1]/div/div[3]/div[1]/div/span[1]/a')
SignIn.click()

#username
username=driver.find_element_by_id('identifierId')
username.click()
username.send_keys('your_username')
next=driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
next.click()
time.sleep(2)

#password
password=driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password.click()
password.send_keys('your_password')
next=driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
next.click()
time.sleep(2)

#mute_and_join
def press():
    camera = driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[2]/div/div')
    camera.click()
    time.sleep(2)

    mic = driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div/div/div')
    mic.click()
    time.sleep(2)

    join = driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span')
    join.click()
    time.sleep(5)

#class_links
def cs():
    cs = driver.get("your_links")

def maths():
    maths = driver.get("your_links")
    press()

def chem():
    chem = driver.get("your_links")
    press()

def eng():
    eng = driver.get("your_links")
    press()

def eg():
    eg = driver.get("your_links")
    press()

def ims():
    ims = driver.get("your_links")
    press()

def chem_lab():
    chem_lab = ("your_links")
    press()

def phy():
    phy = ("your_links")
    press()

def phy_lab():
    phy_lab = driver.get("your_links")
    press()

def twm():
    twm = driver.get("your_links")
    press()

#schedules_as_per_your_timetable
schedule.every().monday.at("09:25").do(eng)
schedule.every().monday.at("10:55").do(chem)
schedule.every().monday.at("13:55").do(cs)
schedule.every().monday.at("15:25").do(cs)

schedule.every().tuesday.at("09:29").do(maths)
schedule.every().tuesday.at("10:55").do(phy)
schedule.every().tuesday.at("13:55").do(eg)
schedule.every().tuesday.at("15:25").do(eg)

schedule.every().wednesday.at("09:25").do(ims)
schedule.every().wednesday.at("10:55").do(chem)
schedule.every().wednesday.at("13:55").do(eng)
schedule.every().wednesday.at("15:25").do(maths)
schedule.every().wednesday.at("16:30").do(twm)

schedule.every().thursday.at("09:25").do(maths)
schedule.every().thursday.at("10:55").do(phy)
schedule.every().thursday.at("13:55").do(maths)
schedule.every().thursday.at("15:25").do(eng)

schedule.every().friday.at("09:25").do(ims)
schedule.every().friday.at("10:55").do(chem)
schedule.every().friday.at("13:55").do(phy_lab)
schedule.every().friday.at("15:25").do(chem_lab)

schedule.every().saturday.at("09:25").do(ims)
schedule.every().saturday.at("10:55").do(phy)
schedule.every().saturday.at("13:55").do(cs)
schedule.every().saturday.at("15:25").do(cs)

while True:
    schedule.run_pending()
    time.sleep(1)
