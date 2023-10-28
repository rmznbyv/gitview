from selenium import webdriver

browser = webdriver.Chrome()
y=input("Your Github page link:")
browser.get(y)
while True:
    browser.refresh();

    
