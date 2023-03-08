from Gen import gen
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.proxy import *
from random import randint, choice
import data_stuff
import test_api
from selenium.webdriver.common.action_chains import ActionChains
import os

class WebBot:
    def __init__(self) -> None:
        self.website = 'https://www.kijiji.ca/t-user-registration.html'

    def get_names(self):
        #with statement
        try: 
            with open('randomNames.txt','x') as f:
                with uc.Chrome() as driver:
                    #wait statement
                    wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])
                    driver.get("https://1000randomnames.com/")
                    name_elems = driver.find_elements(By.TAG_NAME, 'li') #list of all the web elements. The name is inside the text prop i.e: name = self.name_elems[0].text
                    for name_elem in name_elems:
                        f.write(f'{name_elem.text} \n')
        except:
                pass
        finally:
                with open('randomNames.txt','r') as f:
                    names = f.readlines()
                    names = list(map(str.strip,names))
        return names

    def create_account(self,name,email,pword):
        with uc.Chrome() as driver:
            #driver.desired_capabilities['proxy']={}
            wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])
            driver.get(self.website)

            #landing on register page
            name_field = wait.until(EC.element_to_be_clickable((By.ID, 'profileName')))
            time.sleep(randint(1,5))
            name_field.send_keys(name)

            email_field = wait.until(EC.element_to_be_clickable((By.ID,"email")))
            time.sleep(randint(1,5))
            email_field.send_keys(email)

            pass1 =  wait.until(EC.element_to_be_clickable((By.ID,"password")))
            time.sleep(randint(1,5))
            pass1.send_keys(pword)

            pass2 =  wait.until(EC.element_to_be_clickable((By.ID,"passwordConfirmation")))
            time.sleep(randint(1,5))
            pass2.send_keys(pword)
            time.sleep(randint(1,5))
            pass2.send_keys(Keys.RETURN)

    def verify_and_create_ad(self,url,title,b):
        with uc.Chrome() as driver:
            wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException,TimeoutException])
            driver.get(url)
            post_ad =  wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Post ad")))
            time.sleep(randint(1,5))
            post_ad.click()
            ad_title = wait.until(EC.element_to_be_clickable((By.ID,"AdTitleForm")))
            time.sleep(randint(1,5))
            ad_title.send_keys(title)
            time.sleep(randint(1,5))
            ad_title.send_keys(Keys.RETURN)
            time.sleep(randint(1,5))

            btns = driver.find_elements(By.TAG_NAME,"button")
            for btn in btns:
                if btn.text == 'Buy & Sell':
                    btn.click()
                    break
            
            time.sleep(5)
            btns = driver.find_elements(By.TAG_NAME,"button")
            for btn in btns:
                if btn.text == 'Furniture':
                    btn.click()
                    break
                
            time.sleep(5)
            btns = driver.find_elements(By.TAG_NAME,"button")
            for btn in btns:
                if btn.text == 'Beds & Mattresses':
                    btn.click()
                    break
            
            time.sleep(5)
            try:
                if wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "select-location"))):
                    ontario2_lnk = driver.find_element(By.PARTIAL_LINK_TEXT, "Ontario (M - Z)")
                    ontario2_lnk.click()
                    time.sleep(5)
                    ottawa1_lnk = driver.find_element(By.PARTIAL_LINK_TEXT, "Ottawa")
                    ottawa1_lnk.click()
                    time.sleep(5)
                    ottawa2_lnk = driver.find_element(By.LINK_TEXT, "Ottawa")
                    ottawa2_lnk.click()
                    time.sleep(5)
                    go_btn = driver.find_element(By.ID,"LocUpdate")
                    go_btn.click()
            except:
                pass   
            time.sleep(randint(1,5))
            chkboxs = driver.find_elements(By.TAG_NAME,"label")
            for chkbox in chkboxs:
                if chkbox.text == "Business" and b:
                    chkbox.click()
                if chkbox.text == "Willing to drop-off / deliver":
                    chkbox.click()
                if chkbox.text == "Willing to ship the item":
                    chkbox.click()
                if chkbox.text == "Offer curbside pick up":
                    chkbox.click()
                if chkbox.text == "Offer cashless payment":
                    chkbox.click()
                if chkbox.text == "Cash accepted":
                    chkbox.click()
            
            #select_elem = driver.find_element(By.ID, "condition_s")

                     

            time.sleep(randint(1,5))
            txt_area = driver.find_element(By.ID, 'pstad-descrptn')
            txt_area.send_keys(data_stuff.DESCRIPTIONS[randint(0,len(data_stuff.DESCRIPTIONS))])

            #time.sleep(randint(1,5))
            #tag_tfield = driver.find_element(By.XPATH, '//*[@id="pstad-tagsInput"]')
            #for i in range(0,5):
            #    tag_tfield.send_keys(data_stuff.TAGS[randint(0,len(data_stuff.TAGS))])
            #tag_tfield.send_keys(Keys.ENTER)

            time.sleep(randint(1,5))
            img_fields = driver.find_elements(By.TAG_NAME, "input")
            for img_field in img_fields:
                if img_field.get_attribute('type') == "file":
                    for img in os.listdir(r"./Pics/"):
                        img_field.send_keys(os.getcwd()+r"/Pics/"+img)

            time.sleep(randint(1,5))
            location = driver.find_element(By.ID, "location")
            location.send_keys(data_stuff.ZIP)
            time.sleep(5)
            location.send_keys(Keys.DOWN)
            time.sleep(5)
            location.send_keys(Keys.ENTER)           

            time.sleep(randint(1,5))
            price_field = driver.find_element(By.ID, "PriceAmount")
            price_field.send_keys(data_stuff.PRICES[randint(0,len(data_stuff.PRICES)-1)])

            time.sleep(randint(1,5))
            phone_field = driver.find_element(By.ID, "PhoneNumber")
            phone_field.send_keys(choice(data_stuff.PHONES))

            btns = driver.find_elements(By.TAG_NAME, "button")
            for btn in btns:
                if btn.text == "Post Your Ad":
                    btn.click()

            print("Done!")
            time.sleep(50)


if __name__=="__main__":
    wb = WebBot()
    names = wb.get_names()
    name = names[randint(0,len(names)-1)]
    pword = gen((True,True,10))
    eb = test_api.Email_Bot()
    email,t = eb.get()
    wb.create_account(name,email,pword)
    mid = eb.check(email,t)
    business = bool(randint(0,1))
    data_stuff.log(name,email,t,pword,business)
    if mid:
        time.sleep(randint(1,10))
        url = eb.read(email,mid)
        title = data_stuff.TITLE[randint(0,len(data_stuff.TITLE)-1)]
        wb.verify_and_create_ad(url, title,business)

