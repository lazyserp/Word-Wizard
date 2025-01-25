from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)


def writemeaning(word,meaning):
    try:
        with open("Word_Meaning.txt","a+") as wm:
            wm.write(f'{word}-{meaning}\n')

    except FileNotFoundError:
        print("ERROR")


try:
    with open("words.txt","r") as w:
        read = w.readlines()
        words_extracted_from_file  = [i.strip("\n") for i in read]
       
except FileNotFoundError:
    print("FILE NOT FOUND.")


driver = webdriver.Chrome(options=chrome_options)
list_of_word_meaning =[]

for word in words_extracted_from_file:
    driver.get(f"https://www.dictionary.com/browse/{word}")
    wait = WebDriverWait(driver, 10)
    try:
        word_meaning = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="NZKOFkdkcvYgD3lqOIJw"]')))
        list_of_word_meaning.append(word_meaning.text)
    except:
        print(f"Could not find meaning for {word}")

    writemeaning(word,word_meaning.text)


driver.quit()
