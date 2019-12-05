# Selenium
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class Codeforce:
    def __init__(self, handle, pword):
        if (handle and pword):
            self.handle = handle
            self.pword = pword
        else:
            print("Insufficient information provided.")
    
        self.driverPath = "../chromedriver.exe"
        self.chrome = webdriver.Chrome(self.driverPath)

    def openPage(self, link):
        # Open link
        self.chrome.get(link)

    def isLoggedIn(self):
        try:
            enter = self.chrome.find_element_by_link_text("Enter")
        except:
            return True
        return False

    def inputDetails(self):
        # Handle
        handle = self.chrome.find_element_by_id("handleOrEmail")
        handle.send_keys(self.handle)

        password = self.chrome.find_element_by_id("password")
        password.send_keys(self.pword)

        login = self.chrome.find_element_by_class_name("submit")
        login.click()

    def register(self):
        try: 
            registerLink = self.chrome.find_element_by_partial_link_text("Register now")
            registerLink.click()

            time.sleep(2)

            register = self.chrome.find_element_by_class_name("submit")
            register.click()
        except:
            print("[Codeforce] Already registered or no contest open. Try again later.")
            

    def screenshot(self):
        self.chrome.save_screenshot(self.handle + "_screenshot.png")
    
    def run(self):
        # Start the script
        print("[Codeforce] Opening contests page.")
        self.openPage("https://codeforces.com/contests")

        if not self.isLoggedIn():
            self.openPage("https://codeforces.com/enter")
            self.inputDetails()

        print("[Codeforce] Registering.")
        self.register()

        print("[Codeforce] Taking screenshot. (" + handle + "_screenshot.png)")
        self.screenshot()

        self.chrome.close()
        # Done
        print("[Codeforce] Finished.")


print("Please input the handle or email and password.")
handle = input("Handle or email: ")
pword = input("Password: ")

print("[Codeforce] Starting Script.")
print("Handle: " + handle + "; Password: " + pword)
input("Press enter to continue or ctrl + z to cancel.")

Codeforce(handle=handle, pword=pword).run()
