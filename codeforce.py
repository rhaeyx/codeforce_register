# Selenium
import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class Codeforce:
    def __init__(self, handle, email, pword):
        if (handle and email and pword):
            self.handle = handle
            self.email = email
            self.pword = pword
        else:
            print("Insufficient information provided.")
    
        self.driverPath = "../chromedriver.exe"

    def openPage(self):
        self.chrome = webdriver.Chrome(self.driverPath)

        # Open Registration Page
        self.chrome.get("https://codeforces.com/register")

    def inputDetails(self):
        # Handle
        handle = self.chrome.find_element_by_name("handle")
        handle.send_keys(self.handle)

        email = self.chrome.find_element_by_name("email")
        email.send_keys(self.email)

        password = self.chrome.find_element_by_name("password")
        password.send_keys(self.pword)

        passwordConfirmation = self.chrome.find_element_by_name("passwordConfirmation")
        passwordConfirmation.send_keys(self.pword)

        submit = self.chrome.find_element_by_class_name("submit")
        submit.click()

    def screenshot(self):
        self.chrome.save_screenshot(self.handle + "_screenshot.png")
    
    def run(self):
        # Start the script
        print("[Codeforce] Opening page.")
        self.openPage()

        print("[Codeforce] Typing in details.")
        self.inputDetails()

        print("[Codeforce] Taking screenshot.")
        self.screenshot()

        # Done
        print("[Codeforce] Finished.")

print("Please input the handle, email and password.")
handle = input("Handle (Username): ")
email = input("Email: ")
pword = input("Password: ")

print("[Codeforce] Starting Script.")
print("Handle: " + handle + "; Email: " + email + "; Password: " + pword)
input("Press enter to continue or ctrl + z to cancel.")

Codeforce(handle=handle, email=email, pword=pword).run()
