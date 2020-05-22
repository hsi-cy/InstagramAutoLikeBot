from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.keys import Keys
import timeit


class InstagramBot:
    def __init__(self, username, password):
        """Create an InstagramBot object with your username and password. set the webdrive run in backgroud"""
        self.username = username
        self.password = password
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        self.bot = webdriver.Chrome(ChromeDriverManager().install())#, options=chrome_options)
    
    def login(self):
        """login your account"""
        bot = self.bot
        
        bot.get("https://www.instagram.com/")
        sleep(1)
        bot.find_element_by_name('username').send_keys(self.username)
        bot.find_element_by_name('password').send_keys(self.password + Keys.RETURN)
        
        
#     def searchHashtag(self, hashtag):
#         bot = self.bot
#         bot.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        
    def likePhotos(self, hashtag, amount):
        """Input a list of hashtags(list type), how many times to press like btn (int). If the first try fails
        (sometimes it runs too fast), it will try again."""
        bot = self.bot
        wait = WebDriverWait(bot, 10)
        try:
            bot.get("https://www.instagram.com/explore/tags/" + hashtag + "/")

            # find the first picture
            bot.find_element_by_class_name("eLAPa").click()

            i = 1

            while i <= amount:
                sleep(2)
                wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "wpO6b ")))
                bot.find_element_by_class_name("wpO6b ").click()
                sleep(0.5)
                bot.find_element_by_class_name("wpO6b ").send_keys(Keys.ARROW_RIGHT)
                i += 1
            print('Done! I have pressed ' + str(i) + ' likes')


        except Exception as exc:
            print(exc)
            print('Failed to complete the first time!' + ' Only proccessed '  + str(i))
            
            try:
                bot.get("https://www.instagram.com/explore/tags/" + hashtag + "/")

                # find the first picture
                bot.find_element_by_class_name("eLAPa").click() 

                i = 1

                while i <= amount:
                    sleep(2)
                    wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "wpO6b ")))
                    bot.find_element_by_class_name("wpO6b ").click()
                    sleep(0.5)
                    bot.find_element_by_class_name("wpO6b ").send_keys(Keys.ARROW_RIGHT)
                    i += 1
                print('Done! I have pressed ' + str(i) + ' likes')


            except Exception as exc:
                print(exc)
                print("It's beyond repaired" + ' Only proccessed '  + str(i))
                            
          


            
            
    def closeBrowser(self):
        """close the browser in case you change the code to show the browser"""
        bot = self.bot
        bot.close()
    
    def reload(self):
        """this function was written for testing purpose"""
        bot = self.bot
        bot.refresh()