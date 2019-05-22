from selenium import webdriver

# Gets the webdriver
browser = webdriver.Chrome(executable_path='C:\\Program Files\\chromedriver\\chromedriver.exe')

# Url to use, gets the page
url = 'https://cdcs.ur.rochester.edu/'
browser.get(url)

# Make requests to cdcs for necessary courses...
