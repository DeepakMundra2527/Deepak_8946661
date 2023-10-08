# Importing required libraries


# pip install selenium


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()
driver.maximize_window()

time.sleep(5)

# Navigating to the nike.ca homepage
driver.get("https://www.nike.com/ca/")
time.sleep(5)


# Mouse hover on Men menu
men_menu = driver.find_element("xpath",
                                  "/html/body/div[3]/div/div[3]/header/div[1]/div[2]/nav/div[2]/div/ul/li[2]/a")
a = ActionChains(driver)
a.move_to_element(men_menu).perform()
time.sleep(3)

# Clicking on Teens collections from the Men menu
teens_collection = driver.find_element("xpath",
                                  "/html/body/div[3]/div/div[3]/header/div[1]/div[2]/nav/div[2]/div/ul/li[2]/div/div/div[1]/a[4]")

teens_collection.click()
time.sleep(3)

# Selecting an item from the list
select_item = driver.find_element("xpath",
                                  "/html/body/div[4]/div/div/div[2]/div[4]/div/div[5]/div[2]/main/section/div/div[1]/div/figure/a[2]/div/img")
select_item.click()
time.sleep(3)

# Selecting shoe size
select_size = driver.find_element("xpath",
                                  "/html/body/div[4]/div/div/div[2]/div/div[4]/div[2]/div[2]/div/div/div[3]/form/div[1]/fieldset/div/div[6]/label")
select_size.click()
time.sleep(3)

# Click on Favourites
add_to_favourites = driver.find_element("xpath",
                                  "/html/body/div[4]/div/div/div[2]/div/div[4]/div[2]/div[2]/div/div/div[3]/form/div[2]/div/div/button[2]/span[1]")
add_to_favourites.click()
time.sleep(3)

driver.close()
