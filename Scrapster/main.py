
def scroll_to_bottom(nooftimes):
    html = driver.find_element(By.TAG_NAME,'html')
    
    for i in range(nooftimes):
        html.send_keys(Keys.END)
        time.sleep(5)
    
    # when internet is slow uncomment the code block below
    try:
        # click on the show more button
        driver.find_element(By.XPATH,'//input[contains(@value,"Show more results")]').click()
        time.sleep(5)       
    except:
        print("No more results button")
        pass

def make_new_dir(query):
    cwd = os.getcwd()
    print(cwd) 
    new_dir_path = os.path.join(cwd,query)
    if os.path.exists(new_dir_path):
        shutil.rmtree(new_dir_path)
    os.mkdir(new_dir_path)
    print("Directory '% s' created" % query)
    return new_dir_path


def get_images_from_google():
    
    query = 'solar panels'
    driver.get('https://images.google.com/')

    search_box = driver.find_element(By.XPATH,'//input[contains(@title,"Search")]')
    search_box.send_keys(query)
    search_box.send_keys(Keys.ENTER)

    new_dir_name = query.strip('"') 
    new_dir_path = make_new_dir(new_dir_name)
    
    # for loading whole page
    time.sleep(2)
    
    scroll_to_bottom(NO_OF_TIMES)
    time.sleep(10)
    
    for i in range(START_INDEX,LIMIT):
        try:
            img = driver.find_element(By.XPATH,f'//*[@id="islrg"]/div[1]/div[{i}]/a[1]/div[1]/img')
            img.click()
            full_img =  driver.find_element(By.XPATH,'//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img')
            # to load image
            time.sleep(3)
            # Enter the location of folder in which
            # the images will be saved
            full_img.screenshot(f"{new_dir_path}/{query}-{i}.png")
            # Each new screenshot will automatically
            # have its name updated
    
            # Just to avoid unwanted errors
            time.sleep(0.2)
            print(f"{query}-{i}.png downloaded")
        except:
            # if we can't find the XPath of an image,
            # we skip to the next image
            print("Can't find X-Path")

    
if __name__ == "__main__":
    import os
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    import time
    import shutil
    
    PATH = "D:/webdrivers/chromedriver.exe"
    LIMIT = 100
    NO_OF_TIMES = 5
    START_INDEX = 0

    options = Options()
    # options.binary_location = r"D:\webdrivers\chromedriver"
    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome(options=options,service=Service(PATH))
    
    print("Starting....")

    # Maximize the screen
    driver.maximize_window()

    get_images_from_google()
    driver.quit()
