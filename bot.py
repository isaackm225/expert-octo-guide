from Gen import gen
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.proxy import *
from random import randint
import data_stuff
import test_api

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

    def verify_and_create_ad(self,url,title):
        with uc.Chrome() as driver:
            wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException,ElementNotSelectableException,NoSuchElementException])
            driver.get(url)
            post_ad =  wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Post ad")))
            time.sleep(randint(1,5))
            post_ad.click()
            ad_title = wait.until(EC.element_to_be_clickable((By.ID,"AdTitleForm")))
            time.sleep(randint(1,5))
            ad_title.send_keys(title)
            time.sleep(randint(1,5))
            ad_title.send_keys(Keys.RETURN)
            cat_btn1 = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div[2]/div/div/div/div[2]/div/div/div[2]/div[2]/div/ul/li[1]/button")))
            time.sleep(randint(1,5))
            cat_btn1.click()
            cat_btn2 = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div[2]/div/div/div/div[2]/div/div/div[2]/div[2]/div/ul[2]/li[14]/button")))
            time.sleep(randint(1,5))
            cat_btn2.click()
            cat_btn3 = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div[2]/div/div/div/div[2]/div/div/div[2]/div[2]/div/ul[2]/li[1]/button")))
            time.sleep(randint(1,5))
            cat_btn3.click()   

              


if __name__=="__main__":
    wb = WebBot()
    names = wb.get_names()
    name = names[randint(0,len(names)-1)]
    pword = gen((True,True,10))
    eb = test_api.Email_Bot()
    email,t = eb.get()
    wb.create_account(name,email,pword)
    mid = eb.check(email,t)
    print(mid)
    if mid:
        time.sleep(randint(1,10))
        url = eb.read(email,mid)
        title = data_stuff.TITLE[randint(0,len(data_stuff.TITLE)-1)]
        wb.verify_and_create_ad(url, title)
