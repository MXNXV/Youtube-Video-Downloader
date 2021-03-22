from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

link = input("Enter youtube link : ")
choice = input("Enter 1 to download video(mp4)\nEnter 2 to download audio(mp3)\n")
PATH = "E:\\Projects\\Python\\msedgedriver.exe"
driver = webdriver.Edge(PATH)


def downloader(choice, link):
    if choice == '1':
        driver.get("https://en.savefrom.net/18/")
        time.sleep(2)
        search = driver.find_element_by_name('sf_url')
        search.send_keys(link)
        search.send_keys(Keys.RETURN)
        time.sleep(3)
        download = driver.find_element_by_xpath('//*[@id="sf_result"]/div/div/div[2]/div[2]/div[1]/a')
        download.send_keys(Keys.RETURN)
        time.sleep(10)

    elif choice == '2':
    
        driver.get("https://ytmp3.cc/youtube-to-mp3/")
        time.sleep(2)
        search = driver.find_element_by_name('video')
        search.send_keys(link)
        search.send_keys(Keys.RETURN)
        time.sleep(3)
        download = driver.find_element_by_xpath('//*[@id="buttons"]/a[1]')
        download.send_keys(Keys.RETURN)
        time.sleep(10)
    else :
        print("Invalid Choice!!!")

downloader(choice,link)