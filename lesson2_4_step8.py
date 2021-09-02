from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

LINK = 'http://suninjuly.github.io/explicit_wait2.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

def main():
    try:
        browser = webdriver.Chrome()
        browser.get(LINK)
        WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
        browser.find_element_by_css_selector('#book').click()
        print('test1')

        x = browser.find_element_by_css_selector('#input_value').text
        answer_input = browser.find_element_by_css_selector('#answer')
        answer_input.send_keys(calc(x))
        browser.find_element_by_css_selector('[type="submit"]').click()

        print(browser.switch_to.alert.text)
    except Exception as e:
        print(f'Error: {e.__repr__()}')
    finally:
        browser.quit()

if __name__=='__main__':
    main()

    
