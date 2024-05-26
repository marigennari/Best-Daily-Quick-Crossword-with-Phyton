from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


driver_path = 'C:/Users/marig/chromedriver.exe'  # Please update this path to your current path


service = Service(driver_path)

driver = webdriver.Chrome(service=service)

try:
   
    driver.get('https://www.gamelab.com/games/daily-quick-crossword')
    
    
    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it(
            (By.XPATH, '//iframe[contains(@src, "ams.cdn.arkadiumhosted.com/advertisement/video/alpha/h5/frames/interstitial.html")]')
        )
    )
    
   
    WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it(
            (By.ID, 'google_ads_iframe_/100151972/www.gamelab.com/h5_0')
        )
    )
    
    # Closes the AD
    dismiss_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'dismiss-button'))
    )
    dismiss_button.click()
    
    
    driver.switch_to.default_content()
    
    
    time.sleep(2)
    
   
    driver.maximize_window()
    time.sleep(1)  
    
    # Play
    x, y = 856, 899
    pyautogui.moveTo(x, y)
    pyautogui.click()
    logger.info("Clicked on Play")

    time.sleep(1)

    # Check
    x, y = 1301, 445
    pyautogui.moveTo(x, y)
    pyautogui.click()
    logger.info("Clicou no Check")

    time.sleep(1)

    # Autocheck on
    x, y = 1249, 613
    pyautogui.moveTo(x, y)
    pyautogui.click()
    logger.info("Autocheck is on")

    time.sleep(2)

    square_x, square_y = 633, 533
    reveal_x, reveal_y = 1415, 458
    revealpuzzle_x, revealpuzzle_y = 1409, 560

    # Testing each alphabet letter in a square
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        
        pyautogui.moveTo(square_x, square_y)
        pyautogui.click()
      
        pyautogui.press(letter)
        logger.info(f"the letter '{letter}' was pressed")

        time.sleep(0.5)  

    
    #Revealing the puzzle
    pyautogui.moveTo(reveal_x, reveal_y)
    pyautogui.click()

    time.sleep(2)   

    pyautogui.moveTo(revealpuzzle_x, revealpuzzle_y)
    pyautogui.click()

    time.sleep(4)    

    logger.info("Puzzle revealed")

    # Screenshot
    screenshot_path = 'C:/Users/marig/screenshot.png' # Adjust this to your current path
    driver.save_screenshot(screenshot_path)
    logger.info(f"Screenshot saved: {screenshot_path}")

finally:
    
    driver.quit()
