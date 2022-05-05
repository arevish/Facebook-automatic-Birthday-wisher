from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
import getpass
# Download and Install The Webdriver Automatically Using WebDriver_Manager Module (pip install webdriver_manager)
try:
	driver = webdriver.Chrome(ChromeDriverManager().install())
except:
	driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
id = input('Enter your Email ID or Phone No. - ')
key = getpass.getpass('Enter your Password - ')
driver.set_page_load_timeout(10)
driver.get("https://facebook.com")
driver.maximize_window()
driver.implicitly_wait(2)
driver.find_element_by_id("email").send_keys(id)
driver.find_element_by_id("pass").send_keys(key)
driver.find_element_by_id("loginbutton").click()
driver.implicitly_wait(1)
if driver.title == "Facebook":
    driver.get("https://www.facebook.com/events/birthdays")
    driver.implicitly_wait(5)
    message = driver.find_elements_by_xpath("//textarea[@class='enter_submit uiTextareaNoResize uiTextareaAutogrow uiStreamInlineTextarea inlineReplyTextArea mentionsTextarea textInput']")
    for textarea in message:
        textarea.send_keys("Happy Birthday")
        textarea.send_keys(Keys.RETURN)
else:
    print("\n\n Invalid Info. Run the program agian.")
    driver.quit()