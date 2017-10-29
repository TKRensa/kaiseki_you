# encoding=utf8  
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import re

options = webdriver.ChromeOptions()
options.add_argument("chromeのユーザーデータ")

driver = webdriver.Chrome("./chromedriver.exe", chrome_options=options) # さっきDLしたchromedriver.exeを使う
driver.implicitly_wait(5)

#団のIDここにおいてくんやで
ID = [100, 200]

#detailかmemberで切り替え
lists = ["detail", "member"]
for guild_id in (ID):

    rn = random.uniform(1.0,1.5)
    urls = "http://game.granbluefantasy.jp/#guild/" + "detail" + "/" + str(guild_id)
    driver.get(urls)
    time.sleep(rn)
