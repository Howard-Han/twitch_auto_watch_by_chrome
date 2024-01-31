import os, time, json, requests
from datetime import datetime, timedelta
# selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
# twitch_api
from twitch_api import TwitchAPI
# argparse
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--streamer_name", help="streamer name can be seen in the url")
args = parser.parse_args()
STREAMER_NAME = args.streamer_name
# log
LOGGING_PATH = 'streamer_log'
import logging
LOG_FORMAT = '%(asctime)s %(levelname)s: %(message)s'
ts_str = datetime.now().strftime("%Y%m%d%H%M%S")
log_file_path = LOGGING_PATH + '/' + STREAMER_NAME + '/{}.log'.format(ts_str)
if os.path.exists(LOGGING_PATH+'/'+STREAMER_NAME)==False:
    os.makedirs(LOGGING_PATH+'/'+STREAMER_NAME, exist_ok=True)
logging.basicConfig(level=logging.INFO, filename=log_file_path, filemode='a', format=LOG_FORMAT)

### 重要參數
CLIENT_ID = "你的Twitch開發者ID"
CLIENT_SECRET = "你的Twitch開發者SECRET"
api = TwitchAPI()
api.auth(CLIENT_ID, CLIENT_SECRET)
STREAMER_URL = 'https://www.twitch.tv/{}'.format(STREAMER_NAME)
CHROME_PROFILE_PATH = "你的指定chrome profile資料夾位置"
CHROME_PROFILE_NAME = "你的指定chrome profile資料夾名稱"
test_url = "https://api.twitch.tv/helix/streams?user_login={}".format(STREAMER_NAME)

while 1<2:
    try:
        res = requests.get(test_url, headers=api.headers)
        if len(res.json()['data'])==0:
            on_stream = False
            print("{} 目前沒開台".format(STREAMER_NAME))
            logging.info("{} 目前沒開台".format(STREAMER_NAME))
            time.sleep(3600)
        else:
            print("{} 開台中，在線人數{}人".format(res.json()['data'][0]['user_name'], res.json()['data'][0]['viewer_count']))
            logging.info("{} 開台中，在線人數{}人".format(res.json()['data'][0]['user_name'], res.json()['data'][0]['viewer_count']))
            # 自動開啟網頁
            options = Options()
            options.add_argument("user-data-dir="+CHROME_PROFILE_PATH)
            options.add_argument("profile-directory="+CHROME_PROFILE_NAME)
            browser = webdriver.Chrome(options=options)
            browser.get(STREAMER_URL)
            time.sleep(3600)
            # 每30分鐘檢查，一旦關播就關掉網頁
            on_stream = True
            res = requests.get(test_url, headers=api.headers)
            while on_stream:
                print("{} 開台中，在線人數{}人".format(res.json()['data'][0]['user_name'], res.json()['data'][0]['viewer_count']))
                logging.info("{} 開台中，在線人數{}人".format(res.json()['data'][0]['user_name'], res.json()['data'][0]['viewer_count']))
                time.sleep(1800)
                res = requests.get(test_url, headers=api.headers)
                if len(res.json()['data'])==0:
                    on_stream = False
                    break
            print("{} 已經關台了".format(STREAMER_NAME))
            logging.info("{} 已經關台了".format(STREAMER_NAME))
            browser.quit()
    except Exception as e:
        print("")
        message = "發生錯誤，時間: {}, 錯誤: {}".format(datetime.now(), e)
        print(message)
        logging.error(message)
        print("")
        #break
        time.sleep(3600)
    except KeyboardInterrupt:
        print("")
        print("Stop by KeyboardInterrupt")
        print("")
        break

