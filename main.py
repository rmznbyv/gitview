from selenium import webdriver

browser = webdriver.Chrome()
y=input("Your Github page link:")
browser.get(y)
x=2
while x>1:
    browser.refresh();

    
