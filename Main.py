import undetected_chromedriver.v2 as uc
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
import imaplib
import re


Data = open('settings.txt', 'r')
data1 = {}
for line in Data.readlines():
    key, val = line.strip().split("=")
    data1[key] = val
emailamazon = data1['emailamazon']
emailgmail = data1['emailgmail']
passwordgmail = data1['passwordgmail']
phones = data1['phone']
name = data1['name']
Data.close()

def OTPmail():
    print(str(emailgmail) + '@gmail.com', str(passwordgmail))
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(str(emailgmail) + '@gmail.com', str(passwordgmail))
    mail.list()
    mail.select("inbox")
    result, data = mail.search(None, "ALL")
    ids = data[0]
    id_list = ids.split()
    latest_email_id = id_list[-1]
    result, data = mail.fetch(latest_email_id, "(RFC822)")

    raw_email = data[0][1]

    import email
    global email_message
    email_message = email.message_from_string(str(raw_email))




email = emailgmail
n= int(input("Gmail +?\n"))
path = r'./webdriver/chromedriver'
while True:
    driver = uc.Chrome()
    driver.get(
        "https://www.amazon.com/ap/register?openid.pape.max_auth_age=1&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
    driver.find_element_by_id("ap_customer_name").send_keys(name)
    account = (email+"+"+str(n)+"@gmail.com")
    driver.find_element_by_id("ap_email").send_keys(email, "+", str(n), "@gmail.com")
    driver.find_element_by_id("ap_password").send_keys(email, "+", str(n), "@gmail.com")
    driver.find_element_by_id("ap_password_check").send_keys(email, "+", str(n), "@gmail.com")
    driver.find_element_by_id("continue").click()
    WebDriverWait(driver, 60).until(EC.presence_of_element_located(
        (By.ID, "cvf-input-code")))
    time.sleep(6)
    OTPmail()
    mailOTP= re.findall('class=3D"otp">(?<!\d)\d{6}(?!\d)</p>', str(email_message))
    mailOTPs= re.findall('(?<!\d)\d{6}(?!\d)+', str(mailOTP))
    driver.find_element_by_id("cvf-input-code").send_keys(mailOTPs)
    print("Your email OTP is:", mailOTPs)
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div/div[1]/form/div[7]/span/span/input").click()
    phone = open("Settings.txt", "r")
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[1]/div/div[2]/div/div[2]/input").send_keys(phones)
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div/div/form/span/span/input").click()
    time.sleep(5)
    otpsms = open("OTP.txt", "r")
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div/form/div[1]/div[5]/input").send_keys(otpsms.read())
    otpsms.close()
    driver.find_element_by_name("cvf_action").click()
    time.sleep(5)
    driver.get("https://www.amazon.com/ap/cnep?openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fyour-account&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
    driver.find_element_by_id("auth-cnep-edit-phone-button").click()
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[4]/div/div/div/div/div/div[1]/div[2]/div[2]/div/form/span/a/button").click()
    driver.find_element_by_id("ap-remove-mobile-claim-submit-button").click()
    file = open("accounts.txt", 'a')
    file.write(str(account))
    file.write(":")
    file.write(str(account) + "\n")
    file.close()



    def addemail():
        global n
        n+=1


    addemail()
