from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
# 페이지 로딩을 기다리는데에 사용할 time 모듈 import
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
# ActionChains 모듈 import
from selenium.webdriver.common.action_chains import ActionChains
# driver.implicitly_wait(10)


# 크롬드라이버 실행
def get_driver():
    driver = webdriver.Chrome()
    driver.get('https://ship.freightos.com/')
    return driver

# login
def login(driver, id, password):
    login_buttion = driver.find_element(By.XPATH, '//*[@id="app-container"]/header/div/div[2]/div/div[1]/button')
    driver.implicitly_wait(10)
    login_buttion.click()
    id_box = driver.find_element(By.CLASS_NAME, 'ant-input.ant-input-lg')
    driver.implicitly_wait(10)
    id_box.send_keys(id)
    driver.implicitly_wait(10)
    password_box = driver.find_element(By.XPATH, '//*[@id="authUILogIn_password"]')

    driver.implicitly_wait(10)
    password_box.send_keys(password)
    driver.find_element(By.XPATH, '/html/body/div[12]/div/div[2]/div/div[2]/div/div/div[1]/div/form/button').click()

# 검색요건1(origin)
def search_origin(driver, country, address):
    origin_button = driver.find_element(By.XPATH, '//*[@id="app-container"]/main/div/div[1]/div[2]/div/div/div[1]/p')
    driver.implicitly_wait(10)
    origin_button.click()
    #type 선택
    origin_type = driver.find_element(By.XPATH, '//*[@id="app-container"]/main/div/div[1]/div[2]/div/div/div[5]/div/div/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div/span/div/div/div/div')
    driver.implicitly_wait(10)
    origin_type.click()
    driver.find_element(By.XPATH,'/html/body/div[12]/div/div/div/ul/li[1]').click()
    #country 선택
    origin_country = driver.find_element(By.XPATH, '//*[@id="app-container"]/main/div/div[1]/div[2]/div/div/div[5]/div/div/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/span/div/div/div/div')
    driver.implicitly_wait(10)
    origin_country.click()
    driver.find_element(By.XPATH, '/html/body/div[2]/section/main/div/div[1]/div[2]/div/div/div[5]/div/div/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/span/div/div/div/div/div[3]/div/input').send_keys(country)
    target = driver.find_element(By.XPATH, '/html/body/div[2]/section/main/div/div[1]/div[2]/div/div/div[5]/div/div/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/span/div/div/div/div/div[3]/div/input')
    #.location
    action = ActionChains(driver)
    action.move_to_element(target).move_by_offset(90, 45).click().perform()
    
    origin_address = driver.find_element(By.XPATH, '//*[@id="app-container"]/main/div/div[1]/div[2]/div/div/div[5]/div/div/div/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/span/div/div/div')
    driver.implicitly_wait(10)
    origin_address.click()
    driver.find_element(By.XPATH, '/html/body/div[2]/section/main/div/div[1]/div[2]/div/div/div[5]/div/div/div/div/div/div[1]/div[1]/div[2]/div[2]/div/div[2]/div/span/div/div/div/div[2]/div/input').send_keys(address)
    target = driver.find_element(By.XPATH, '/html/body/div[2]/section/main/div/div[1]/div[2]/div/div/div[5]/div/div/div/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/span/div/div/div/div[2]/div/input')
    action = ActionChains(driver)
    action.move_to_element(target).move_by_offset(90, 45).click().perform()

# 검색요건2(destination)
def search_destination(driver, country, address):
    destination_button = driver.find_element(By.CSS_SELECTOR, '[data-test-id="CategoryWrapper-destination"]')
    driver.implicitly_wait(10)
    destination_button.click()
    # type 선택
    destination_type = driver.find_element(By.CSS_SELECTOR, '[data-test-id="destination-type"]')
    driver.implicitly_wait(10)
    destination_type.click()
    action = ActionChains(driver)
    action.move_to_element(destination_type).move_by_offset(90, 45).click().perform()
    #country 선택
    destination_country = driver.find_element(By.CSS_SELECTOR, '[data-test-id="destination-country-select"]')
    driver.implicitly_wait(10)
    destination_country.click()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[@id="app-container"]/main/div/div[1]/div[2]/div/div/div[6]/div/div/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/span/div/div/div/div/div[3]/div/input').send_keys(country)
    driver.implicitly_wait(10)
    target = driver.find_element(By.XPATH, '//*[@id="app-container"]/main/div/div[1]/div[2]/div/div/div[6]/div/div/div/div/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/span/div/div/div/div/div[3]/div/input')
    action = ActionChains(driver)
    action.move_to_element(target).move_by_offset(90, 45).click().perform()
    
    destination_address = driver.find_element(By.CSS_SELECTOR, '[data-test-id="destination-address-select"]')
    driver.implicitly_wait(10)
    destination_address.click()
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[@id="app-container"]/main/div/div[1]/div[2]/div/div/div[6]/div/div/div/div/div/div[1]/div[1]/div[2]/div[2]/div/div[2]/div/span/div/div/div/div[2]/div/input').send_keys(address)
    target = driver.find_element(By.XPATH, '//*[@id="app-container"]/main/div/div[1]/div[2]/div/div/div[6]/div/div/div/div/div/div[1]/div[1]/div[2]/div[2]/div/div[2]/div/span/div/div/div/div[2]/div/input')
    action = ActionChains(driver)
    action.move_to_element(target).move_by_offset(90, 45).click().perform()
    
# 검색요건3(Load)
def search_load(driver):
    load_button = driver.find_element(By.XPATH, '//*[@id="app-container"]/main/div/div[1]/div[2]/div/div/div[3]')
    driver.implicitly_wait(10)
    load_button.click()
    driver.find_element(By.XPATH, '//*[@id="app-container"]/main/div/div[1]/div[2]/div/div/div[7]/div/div/div/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[1]/div[2]/span').click()
    # add goods 40ft
    add_button = driver.find_element(By.XPATH, '//*[@id="app-container"]/main/div/div[1]/div[2]/div/div/div[7]/div/div/div/div/div/div/div[2]/button[1]')
    driver.implicitly_wait(10)
    add_button.click()
    # add goods 20ft
    #driver.find_element(By.XPATH, '/html/body/div[2]/section/main/div/div[1]/div[2]/div/div/div[7]/div/div/div/div/div/div/div[1]/div[3]/div/div[2]/div[2]/div[2]/div/div[2]/div/span/div/label[1]/span[1]').click()
    target = driver.find_element(By.XPATH, '//*[@id="app-container"]/main/div/div[1]/div[2]/div/div/div[7]/div/div/div/div/div/div/div[2]/button[2]')
    action = ActionChains(driver)
    action.move_to_element(target).move_by_offset(-252, -115).click().perform()
    add_button.click()

    driver.find_element(By.XPATH, '//*[@id="app-container"]/main/div/div[1]/div[2]/div/div/div[7]/div/div/div/div/div/div/div[2]/button[2]').click()

# 검색요건4(Goods)
def search_goods(driver, value):
    goods_button = driver.find_element(By.XPATH, '//*[@id="app-container"]/main/div/div[1]/div[2]/div/div/div[4]')
    driver.implicitly_wait(10)
    goods_button.click()
    # goods value 입력
    driver.find_element(By.XPATH, '/html/body/div[2]/section/main/div/div[1]/div[2]/div/div/div[8]/div/div/div/div/div/div/div[1]/div[1]/div[2]/div/span/span/span/input').send_keys(value)
    # ready
    driver.find_element(By.XPATH, '//*[@id="app-container"]/main/div/div[1]/div[2]/div/div/div[8]/div/div/div/div/div/div/div[1]/div[3]/div[2]/div/span/div/div/div/div').click()
    
    target = driver.find_element(By.XPATH, '//*[@id="app-container"]/main/div/div[1]/div[2]/div/div/div[8]/div/div/div/div/div/div/div[1]/div[3]/div[2]/div/span/div/div/div/div')
    action = ActionChains(driver)
    action.move_to_element(target).move_by_offset(10, 40).click().perform()
    
    driver.find_element(By.XPATH, '//*[@id="app-container"]/main/div/div[1]/div[2]/div/div/div[8]/div/div/div/div/div/div/div[2]/button').click()

# Done !
def search_done(driver):
    search_button = driver.find_element(By.XPATH, '//*[@id="app-container"]/main/div/div[1]/div[2]/div/div/button')
    driver.implicitly_wait(10)
    search_button.click()
    singleBond_button = driver.find_element(By.XPATH, '/html/body/div[12]/div/div/div/div[2]/div[2]/div/div[3]/div[2]/ul[2]/li/div[4]/label[1]')
    driver.implicitly_wait(10)
    singleBond_button.click()
    result_button = driver.find_element(By.XPATH, '/html/body/div[12]/div/div/div/div[2]/div[3]/div/button[2]')
    driver.implicitly_wait(10)
    result_button.click()

# best offer 선택
def select_offer(driver):
    offer_button = driver.find_element(By.XPATH, '//*[@id="results-view"]/section/section/main/div[1]/div/div')
    driver.implicitly_wait(10)
    offer_button.click()

    fee40 = driver.find_element(By.XPATH, '//*[@id="results-view"]/section/section/main/div[1]/div/div[2]/div/div[1]/div[3]/div[6]/span/span[2]')
    fee20 = driver.find_element(By.XPATH, '//*[@id="results-view"]/section/section/main/div[1]/div/div[2]/div/div[1]/div[4]/div[6]/span/span[2]')
    print("OCEAN 20' :", fee20.text)
    print("OCEAN 40' :", fee40.text)
    #driver.find_element(By.XPATH, '/html/body/div[2]/section/main/div/div[1]/div[2]/div/div/div[2]/div/div/div/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div/div[2]/div/span/div/div/div/div/div[3]/div/input').send_keys('Best Offer')
    #target = driver.find_element(By.XPATH, '/html/body/div[2]/section/main/div/div[1]/div[2]/div/div/div[2]/div/div/div/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div/div[2]/div/span/div/div/div/div/div[3]/div/input')
    #action = ActionChains(driver)
    #action.move_to_element(target).move_by_offset(90, 45).click().perform()
    #driver.find_element(By.XPATH, '/html/body/div[2]/section/main/div/div[1]/div[2]/div/div/div[2]/div/div/div/div/div/div/div[2]/button').click()

if __name__ == "__main__":
    driver = get_driver()
    time.sleep(2)
    login(driver, '4840sss@kookmin.ac.kr', 'Bok18864jae!')
    time.sleep(2)
    search_origin(driver, 'Korea, Republic of', 'KRPUS')
    time.sleep(2)
    search_destination(driver, 'United States', 'USLGB')
    time.sleep(2)
    search_load(driver)
    time.sleep(2)
    search_goods(driver, "100000")
    time.sleep(2)
    search_done(driver)
    time.sleep(8)
    select_offer(driver)
    time.sleep(10)
