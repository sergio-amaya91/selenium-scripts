from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
PATH = "C:\\Users\iamda\\OneDrive\\Desktop\\selenium scripts\\chromedriver.exe"
driver = webdriver.Chrome(PATH)


driver.get("https://www.bestbuy.com/")

search = driver.find_element(By.ID, "gh-search-input")
search.clear()
search.send_keys("Playstation 5")
search.send_keys(Keys.RETURN)


link = driver.find_element(By.LINK_TEXT, "Sony - PlayStation 5 Console")
link.click()
try:
    
    available = driver.find_element(By.CSS_SELECTOR, 'div.fulfillment-fulfillment-summary')                                            
                                           
    
    print(f"Playstation 5 is: {available.text}")
    
    
except:
    "something went wrong"    




search = driver.find_element(By.ID, "gh-search-input")
search.clear()
search.send_keys("Nintendo Switch")
search.send_keys(Keys.RETURN)


link = driver.find_element(By.LINK_TEXT, "Nintendo Switch – OLED Model w/ White Joy-Con - White")
link.click()
try:
    
    available = driver.find_element(By.CSS_SELECTOR, 'div.fulfillment-fulfillment-summary')                                            
                                           
    
    print(f"Nintendo switch is: {available.text}")

    driver.quit()
    
    
except:
    "something went wrong"    

