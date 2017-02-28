'''
After you come inside gmail

click on menu: com.google.android.gm:id/mail_toolbar
get elements and click 1rst one.


going to settings: resource_id: android:id/list
then click at id 'com.google.android.gm:id/drawer_footer_text'

'''


from appium import webdriver
from time import sleep
from get_name import fields
from pymongo import MongoClient
from get_name import fields, randint
import deathbycaptcha



username_dbc = 'grownout'
password_dbc = 'grownout123'
client = deathbycaptcha.SocketClient(username_dbc, password_dbc)

print client.get_balance()

def get_captcha(filename):
    sleep(2)
    print 'finding captcha'
    # client = deathbycaptcha.SocketClient(username, password)
    captcha = client.decode(filename)
    print "CAPTCHA %s solved: %s" % (captcha["captcha"], captcha["text"])
    # capcha = raw_input('Enter capcha:')
    return captcha["text"]


# print get_captcha("adityavadia3960022.png")
# exit()


collection = MongoClient()['gmail_accounts'].data

desired_caps = {}
# desired_caps['deviceName'] = 'Titanium_S15'
# desired_caps['deviceName'] = 'Google Nexus 4 - 4.4.4 -API 19 - 786x1280'
desired_caps['deviceName'] = 'mod2'
desired_caps['platformVersion'] = '4.4'
desired_caps['platformName'] = 'Android'
desired_caps['app'] = '/home/tamta/Downloads/ConnectBot-1.8.6.apk'   #App location


# 9718921964

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
print 'ho gya'
# driver.get_screenshot_as_png()
# sleep(10)
#to go to main menu
# driver.press_keycode(4)
print 'wapas chala gya'




from bson import ObjectId

# first_name, last_name, email, password, mongo_id = (u'Batra', u'Arpit', u'arpitbatra2743234', 'CKcypgMePA', ObjectId('5770d1b1f99ce66113c1ab4c'))

def write_to_mongo(first_name, last_name, email, password, mongo_id):
    collection.update({'_id':mongo_id},{"first_name":first_name,"last_name":last_name,"email":email+'@gmail.com',"password":password})
    print email+'@gmail.com'
# write_to_mongo(first_name, last_name, email, password, mongo_id)
# exit()
def start_automating():
    first_name, last_name, email, password, mongo_id = fields()
    while True:
        x = driver.find_elements_by_class_name("android.widget.TextView")
        if len(x)>0:
            if x[0].text == 'Gmail':
                print 'gmail mil gya'
                x[0].click()
                break
            else:
                driver.press_keycode(4)

    while True:
        x = driver.find_elements_by_xpath("//android.widget.ImageButton")
        if len(x) > 0:
            x[0].click()
            break


    while True:
        x = driver.find_elements_by_xpath("//android.widget.ImageButton")
        if len(x) > 0:
            y = driver.find_elements_by_id('com.google.android.gm:id/account_list_button')
            print 'y:',len(y)
            if len(y)>0:
                z = driver.find_elements_by_id('com.google.android.gm:id/account_address')
                z1 = driver.find_elements_by_id('com.google.android.gm:id/add_account_text')
                print 'z:',len(z),'z1:',len(z1)
                if len(z)==1 and len(z1)==0:
                    y[0].click()
                else:
                    break
            else:
                x[0].click()
            # break

    while True:
        x = driver.find_elements_by_id("com.google.android.gm:id/add_account_text")
        if len(x) > 0:
            x[0].click()
            break


    while True:
        x = driver.find_elements_by_id("com.google.android.gm:id/google_option")
        if len(x) > 0:
            x[0].click()
            break
    while True:
        x = driver.find_elements_by_id("com.google.android.gm:id/suw_layout_content")
        if len(x) > 0:
            x[0].click()
            break


    while True:
        x = driver.find_elements_by_id("com.google.android.gsf.login:id/create_button")
        if len(x) > 0:
            x[0].click()
            break

    while True:
        x = driver.find_elements_by_id("com.google.android.gsf.login:id/first_name_edit")
        if len(x) > 0:
            x[0].send_keys(first_name)
            break


    while True:
        x = driver.find_elements_by_id("com.google.android.gsf.login:id/last_name_edit")
        if len(x)>0:
            x[0].send_keys(last_name)
            break


    while True:
        x = driver.find_elements_by_id("com.google.android.gsf.login:id/next_button")
        if len(x)>0:
            x[0].click()
            break
    # email = 'mohittamta1'
    flag = False
    while True:
        x = driver.find_elements_by_id("com.google.android.gsf.login:id/username_edit")
        if len(x)>0:
            x[0].send_keys(email)
            y = driver.find_elements_by_id("com.google.android.gsf.login:id/next_button")
            if len(y) > 0:
                y[0].click()

                while True:
                    z = driver.find_elements_by_id("com.google.android.gsf.login:id/title")
                    if len(z)> 0:
                        if 'Checking availability' in z[0].text:
                            continue
                        elif 'Change username' in z[0].text:
                            #press try again, and aso press backspace
                            start_automating()
                            return
                        elif 'Choose username' in z[0].text:
                            raw_input('Inside the loop of choose username, press next in emulator and then press enter.')
                        else:
                            flag = True
                            break
                if flag: break

    print 'email: ', email
    print 'password:', password
    # while True:


    # com.google.android.gsf.login:id / title
    # Checking availability

    while True:
        x = driver.find_elements_by_id("com.google.android.gsf.login:id/password_edit")
        if len(x)>0:
            x[0].send_keys(password)
            break

    while True:
        x = driver.find_elements_by_id("com.google.android.gsf.login:id/confirm_password_edit")
        if len(x)>0:
            x[0].send_keys(password)
            break

    while True:
        x = driver.find_elements_by_id("com.google.android.gsf.login:id/next_button")
        if len(x) > 0:
            x[0].click()
            break

    while True:
        x = driver.find_elements_by_id("com.google.android.gsf.login:id/no")
        if len(x) > 0:
            x[0].click()
            break

    while True:
        x = driver.find_elements_by_id("com.google.android.gsf.login:id/next_button")
        if len(x) > 0:
            x[0].click()
            break

    while True:
        x = driver.find_elements_by_id("com.google.android.gsf.login:id/yes_button")
        if len(x) > 0:
            x[0].click()
            break


    while True:
        x = driver.find_elements_by_id("com.google.android.gsf.login:id/captcha_image_view")
        if len(x) > 0:
            x = driver.get_screenshot_as_png()
            fo = open(email+'.png','w')
            fo.write(x)
            fo.close()
            capcha = get_captcha(email+'.png')
            break

    # capcha.get_attribute

    while True:
        x = driver.find_elements_by_id("com.google.android.gsf.login:id/captcha_answer_edit")
        if len(x)>0:
            x[0].send_keys(capcha)
            break

    while True:
        x = driver.find_elements_by_id("com.google.android.gsf.login:id/next_button")
        if len(x) > 0:
            x[0].click()
            break

    while True:
        x = driver.find_elements_by_id('com.google.android.gsf.login:id/title')
        if len(x) > 0:
            if 'successful' in x[0].text:
                break
            elif 'Saving account' in x[0].text:
                continue
            else:
                print x[0].text
                print 'error occoured, I quit'
                exit()

    while True:
        x = driver.find_elements_by_id("com.google.android.gsf.login:id/next_button")
        if len(x) > 0:
            x[0].click()
            break

    write_to_mongo(first_name, last_name, email, password, mongo_id)
    # while True:
    #     x =
# from bson import ObjectId

# first_name, last_name, email, password, mongo_id = (u'Sunny', u'Taneja', u'sunnytaneja7211609', 'APliPlNLIT', ObjectId('5770d1b1f99ce66113c1ab4b'))


    # x = driver.find_elements_by_xpath("//android.widget.ImageButton")
    # x[0].click()

    # password = 'gdadhklvh'

# if __name__ == '__main__':

# write_to_mongo('ravi', 'ram', 'raviram67259', 'sanIjk99q')