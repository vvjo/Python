from selenium import webdriver as wb
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from apscheduler.schedulers.blocking import BlockingScheduler

def play():
    wbd.get("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    sleep(3)
    wbd.find_element_by_xpath("/html/body/ytd-app/ytd-popup-container/paper-dialog/yt-upsell-dialog-renderer/div/div[3]/div[1]/yt-button-renderer/a/paper-button/yt-formatted-string").click()
    wbd.find_element_by_xpath("/html/body/div/c-wiz/div[2]/div/div/div/div/div[2]/form/div/span/span").click()
    sleep(120)

wbd = wb.Chrome('chromedriver.exe')

kpl = 0
f = open("sites.txt", "r")
try:
    wbd.get(f.readline())
    sleep(1)
    wbd.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/button").click()
except:
    print("NoSuchElement")
try:
    n = wbd.find_elements_by_xpath("/html/body/div[1]/div[1]/div/div/main/div[1]/div[6]/div/ol[1]/li[*]")
    print("Verkkokauppa: ", wbd.current_url)
    for i in n:
        try:
            if "Heti" in i.text:
                kpl += 1
                name = i.find_element_by_xpath(".//div/div[1]/div/a").text
                print(name)
        except:
            print("NoSuchElement")
except(NoSuchElementException):
    print("NoSuchElement")
print(kpl, " tulosta.")

kpl = 0
try:
    wbd.get(f.readline())
    sleep(1)
    n = wbd.find_elements_by_xpath("/html/body/div[3]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/div[*]")
    print("Jimms: ", wbd.current_url)
    for y in n:
        try:
            if "1-4 työpäivää" in y.text:
                name = y.find_element_by_xpath(".//div[3]/div[1]/a/span").text
                if "3080" in name:
                    kpl += 1
                    print(name)
        except:
            print("NoSuchElement")
except(NoSuchElementException):
    print("NoSuchElement")
print(kpl, " tulosta")

kpl = 0
try:
    wbd.get(f.readline())
    sleep(1)
    wbd.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/button[2]").click()
except:
    print("NoSuchElement")
try:
    print("Gigantti: ", wbd.current_url)
    n = wbd.find_elements_by_xpath("/html/body/div[3]/main/section/div[4]/div[1]/div[*]")
    for i in n:
        try:
            if "Keskusvarastossa" in i.text:
                name = i.find_element_by_xpath(".//div/div/div[1]/div[2]/div[2]/div[2]/a/span/span").text
                print(name)
                kpl += 1
        except:
            print("NoSuchElement")
except(NoSuchElementException):
    print("NoSuchElement")
print(kpl, " tulosta")

kpl = 0
try:
    wbd.get(f.readline())
    sleep(1)
    wbd.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div[1]/button[3]").click()
except:
    print("Error")
try:
    print("Power: ", wbd.current_url)
    n = wbd.find_elements_by_xpath("/html/body/pwr-main/div[1]/pwr-page-entry/pwr-search-result-page/pwr-product-list/div/section/div/div[2]/div[2]/div/div[*]")
    for i in n:
        try:
            state = i.find_element_by_xpath(".//pwr-product-list-item/pwr-product-item/div/div/div[2]/div[1]/pwr-product-stock-label/span").text
            if "VARASTOSSA" == state or "Toimitus myymälöistä" == state:
                name = i.find_element_by_xpath(".//pwr-product-list-item/pwr-product-item/div/a/div[2]/span").text
                print(name)
                kpl += 1
        except:
            print("NoSuchElement")
except(NoSuchElementException):
    print("NoSuchElement")
print(kpl, " tulosta.")

#/html/body/pwr-main/div[1]/pwr-page-entry/pwr-search-result-page/pwr-product-list/div/section/div/div[2]/div[2]/div/div[*]
#/html/body/pwr-main/div[1]/pwr-page-entry/pwr-search-result-page/pwr-product-list/div/section/div/div[2]/div[2]/div/div[9]/pwr-product-list-item/pwr-product-item/div/div/div[2]/div[1]/pwr-product-stock-label/span/text()

f.close()
wbd.close()