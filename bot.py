from selenium import webdriver




options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/benn/AppData/Local/Google/Chrome/User Data")
driver = webdriver.Chrome('chromedriver.exe',chrome_options=options)
driver.get("https://web.whatsapp.com/")