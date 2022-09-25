import time
import random
import pyautogui

from selenium import webdriver
from selenium.common.exceptions import NoSuchWindowException

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome import options

# Main

opt = webdriver.ChromeOptions()
opt.add_extension("D:\\Python Workshop\\AutoUpload\\MetaMask.crx")

driver = webdriver.Chrome(options=opt)
driver.get("https://www.google.com/")
driver.maximize_window()

driver.switch_to.window(driver.window_handles[0])

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/button")))
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/button").send_keys(Keys.RETURN)
    print("Element found and clicked!")

except TimeoutError:
    print("Page timeout!")
    driver.quit()
    exit(-1)


try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button")))
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button").send_keys(Keys.RETURN)
    print("Element found and clicked!")

except TimeoutError:
    print("Page timeout!")
    driver.quit()
    exit(-1)


try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[2]")))
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[2]").send_keys(Keys.RETURN)
    print("Element found and clicked!")

except TimeoutError:
    print("Page timeout!")
    driver.quit()
    exit(-1)


try:
    PASSPHRASE = "problem empower dice oak used angry survey destroy oyster rural labor dash"
    wordList = list(PASSPHRASE.split(" "))

    xpathList = ["/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[1]/div[1]/div/input",
                 "/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[2]/div[1]/div/input",
                 "/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[3]/div[1]/div/input",
                 "/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[4]/div[1]/div/input",
                 "/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[5]/div[1]/div/input",
                 "/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[6]/div[1]/div/input",
                 "/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[7]/div[1]/div/input",
                 "/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[8]/div[1]/div/input",
                 "/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[9]/div[1]/div/input",
                 "/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[10]/div[1]/div/input",
                 "/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[11]/div[1]/div/input",
                 "/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div[12]/div[1]/div/input"]

    for i in range(12):
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpathList[i])))
            driver.find_element(By.XPATH, xpathList[i]).send_keys(wordList[i])
            print(wordList[i] + " was inputted.")

        except EC.NoSuchElementException:
            print("Element not found!")
            driver.quit()
            exit(-2)

except TimeoutError:
    print("Could not fill out passphrase!")
    driver.quit()
    exit(-1)


try:
    PASSWORD = "j/Y`X?2\\?{$eHwQe_&^57g\"gn*?McvxC'7_A>Zn+7Y*P\"PcgefR~8kDWjW]h%r4#"

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[2]/div[1]/div/input")))
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[2]/div[1]/div/input").send_keys(PASSWORD)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[2]/div[2]/div/input")))
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[2]/div[2]/div/input").send_keys(PASSWORD)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[3]/input")))
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[3]/input").send_keys(Keys.SPACE)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/form/button")))
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[2]/form/button").send_keys(Keys.RETURN)

except TimeoutError:
    print("Page timeout!")
    driver.quit()
    exit(-1)


try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/button")))
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/button").send_keys(Keys.RETURN)

except TimeoutError:
    print("Page timeout!")
    driver.quit()
    exit(-1)

driver.close()

driver.switch_to.window(driver.window_handles[0])

driver.get("https://rarible.com/create/start/ethereum")

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/button")))
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/button").send_keys(Keys.RETURN)

except EC.NoSuchElementException:
    print("No such element!")
    driver.quit()
    exit(-2)


try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div[1]/button")))
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div[1]/button").send_keys(Keys.RETURN)

except EC.NoSuchElementException:
    print("No such element!")
    driver.quit()
    exit(-2)

time.sleep(5)

driver.switch_to.window(driver.window_handles[1])

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[3]/div[2]/button[2]")))
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[3]/div[2]/button[2]").send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]")))
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]").send_keys(Keys.RETURN)


except EC.NoSuchElementException:
    print("No such element!")
    driver.quit()
    exit(-2)

time.sleep(3)

driver.switch_to.window(driver.window_handles[0])


parentDirectory = "E:\\metadata\\"
i = 935
j = 0
while i <= 1000:

    try:

        array = []

        with open(parentDirectory + "Geode #" + str(i) + "_data.txt", 'r') as file:

            for line in file.readlines():
                array.append(line)

            file.close()
            pass

        imagePath = array[0].strip()
        name = array[1].strip()
        description = array[2].strip()
        bgColor = array[3].strip()
        rockColor = array[4].strip()
        facePaint = array[5].strip()
        eyeLid = array[6].strip()
        eyeAcc = array[7].strip()
        hatAcc = array[8].strip()
        faceAcc = array[9].strip()
        prop = array[10].strip()

        if j == 0:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/button[2]")))
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/button[2]").send_keys(Keys.RETURN)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div/input")))
        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div/input").send_keys(imagePath)

        #bid = 0.02
        #fixed = 0.06

        z = 1
        x = 2

        # Bid
        if z == x:
            time.sleep(2)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[4]/div/div/button[2]")))
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[4]/div/div/button[2]").send_keys(Keys.RETURN)

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[6]/div/div[2]/div/button[2]")))
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[6]/div/div[2]/div/button[2]").send_keys(Keys.RETURN)

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[8]/div/div[2]/div/input")))
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[8]/div/div[2]/div/input").send_keys(name)

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[9]/div/div[2]/div/textarea")))
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[9]/div/div[2]/div/textarea").send_keys(description)

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[11]/button")))
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[11]/button").send_keys(Keys.RETURN)

        # Fixed
        else:
            time.sleep(2)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[5]/div/div[2]/div[1]/input")))
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[5]/div/div[2]/div[1]/input").send_keys("0.06")

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[7]/div/div[2]/div/button[2]")))
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[7]/div/div[2]/div/button[2]").send_keys(Keys.RETURN)

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[9]/div/div[2]/div/input")))
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[9]/div/div[2]/div/input").send_keys(name)

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[10]/div/div[2]/div/textarea")))
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[10]/div/div[2]/div/textarea").send_keys(description)

            #/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[11]/div/div[2]/div[2]/div/input
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[11]/div/div[2]/div[2]/div/input")))
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[11]/div/div[2]/div[2]/div/input").send_keys("1")

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/button")))
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/button").send_keys(Keys.RETURN)

            ####################################################

            # Background
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[1]/div/input")))
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[1]/div/input").send_keys("Background Color")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[2]/div/input")))
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[2]/div/input").send_keys(bgColor)

            # Rock Color
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[3]/div/input")))
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[3]/div/input").send_keys("Rock Color")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[3]/div/input")))
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[4]/div/input").send_keys(rockColor)

            # Face Paint
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[3]/div/input")))
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[5]/div/input").send_keys("Face Paint")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[3]/div/input")))
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[6]/div/input").send_keys(facePaint)

            # Eye Lid
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[3]/div/input")))
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[7]/div/input").send_keys("Eye Lid")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[3]/div/input")))
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[8]/div/input").send_keys(eyeLid)

            # Eye Accessory
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[3]/div/input")))
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[9]/div/input").send_keys("Eye Accessory")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[3]/div/input")))
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[10]/div/input").send_keys(eyeAcc)

            # Hat Accessory
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[3]/div/input")))
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[11]/div/input").send_keys("Hat Accessory")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[3]/div/input")))
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[12]/div/input").send_keys(hatAcc)

            # Face Accessory
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[3]/div/input")))
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[13]/div/input").send_keys("Face Accessory")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[3]/div/input")))
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[14]/div/input").send_keys(faceAcc)

            # Prop
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[3]/div/input")))
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[15]/div/input").send_keys("Prop")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[3]/div/input")))
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[16]/div/input").send_keys(prop)

            # Create Item
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[13]/div/div/button")))
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[13]/div/div/button").send_keys(Keys.SPACE)

            timeout = 0
            while True:

                windows = driver.window_handles

                if timeout != 30:

                    if len(windows) > 1:

                        time.sleep(1)
                        driver.switch_to.window(driver.window_handles[1])
                        break

                    timeout += 1
                    time.sleep(1)
                else:

                    print("Window timed out!")
                    driver.quit()
                    exit(-3)

            driver.maximize_window()
            time.sleep(1)
            pyautogui.click(1133, 740)

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[4]/button[2]")))
            driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[4]/button[2]").send_keys(Keys.RETURN)

            time.sleep(2)

            timeout = 0
            while True:

                windows = driver.window_handles

                if timeout != 30:

                    if len(windows) > 1:

                        time.sleep(2)
                        driver.switch_to.window(driver.window_handles[1])
                        break

                    timeout += 1
                    time.sleep(1)

            driver.maximize_window()
            time.sleep(1)
            pyautogui.click(1133, 740)

            #/html/body/div[1]/div/div[2]/div/div[4]/button[2]
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[4]/button[2]")))
            driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[4]/button[2]").send_keys(Keys.RETURN)

            time.sleep(1)

            driver.switch_to.window(driver.window_handles[0])

            driver.get("https://rarible.com/create/start/ethereum")

            #/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/button[2]
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/button[2]")))
            driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/div/button[2]").send_keys(Keys.RETURN)

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/button")))
            driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div/button").send_keys(Keys.RETURN)

            i += 1
            j = 1

    except EC.NoSuchElementException:
        print("No such element!")
        driver.quit()
        exit(-2)

    i = i + 1

print(driver.title)
