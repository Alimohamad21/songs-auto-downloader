import json
import time

from selenium import webdriver


def close_tab(n):
    while True:
        if len(driver.window_handles) == n:
            driver.switch_to.window(driver.window_handles[-1])
            driver.close()
            driver.switch_to.window(driver.window_handles[n - 2])
            break


data = json.load(open('D:\passwords.json'))
password = data['anghami_password']
username = data['anghami_username']

driver = webdriver.Edge('/Users/Mohamed/Downloads/msedgedriver')
driver.get("https://play.anghami.com/home")
window_before = driver.window_handles[0]
while True:
    try:
        driver.find_element_by_class_name("login-btn").click()
        break
    except:
        pass
driver.find_elements_by_class_name("login-btn-txt")[1].click()
while True:
    try:
        window_after = driver.window_handles[1]
        break
    except:
        pass
driver.switch_to.window(window_after)
while True:
    try:
        driver.find_element_by_tag_name("input").send_keys(username)
        break
    except:
        pass
driver.find_element_by_class_name("VfPpkd-RLmnJb").click()
while True:
    try:
        driver.find_element_by_xpath('//input[@type = "password"]').send_keys(password)
        break
    except:
        pass
driver.find_element_by_class_name("VfPpkd-RLmnJb").click()
driver.switch_to.window(window_before)
while True:
    try:
        driver.find_element_by_xpath("//*[text()='Your Library']").click()
        break
    except:
        pass
while True:
    try:
        # driver.find_element_by_xpath("//*[text()=' Shuffle ']").click()
        break
    except:
        pass
start_time = time.time()
song_names = []
for i in range(17):
    songs = driver.find_elements_by_class_name("cell-title")
    for song in songs:
        song_names.append(song.text)
    driver.execute_script("window.scrollBy(0,1000)")
song_names = list(dict.fromkeys(song_names))
for i in range(len(song_names)):
    song_name = song_names[i].split()
    song_uri = ""
    for i in range(len(song_name)):
        if i != len(song_name) - 1:
            song_uri += song_name[i] + "+"
        else:
            song_uri += song_name[i]
    url = "https://www.youtube.com/results?search_query="
    url += song_uri
    driver.get(url)
    download_link = driver.find_element_by_id("video-title").get_attribute("href")
    driver.get("https://ytmp3.cc/en13/")
    while True:
        try:
            driver.find_element_by_id("input").send_keys(download_link)
            break
        except:
            pass
    driver.find_element_by_id("submit").click()
    while True:
        try:
            driver.find_element_by_xpath("//*[text()='Download']").click()
            break
        except:
            pass
    if len(driver.window_handles) == 2:
        close_tab(2)
