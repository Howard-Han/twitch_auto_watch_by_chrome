# twitch_auto_watch_by_chrome
運用Python selenium套件與Twitch API，實現用Chrome自動看指定Twitch實況主的實況

### 我用 Windows + Python 3.9.10 + Chromedriver 114.0.5735.90 操作的，其他作業系統跟程式版本沒測試過

### 前置作業:
1. 申請Twitch開發者金鑰(註冊一個APP): 需要CLIENT_ID和CLIENT_SECRET才能使用Twitch API，詳見 [此文章最前段](https://medium.com/@s1k2y37st/linebot%E7%B3%BB%E5%88%97-%E4%B8%89-%E4%B8%B2%E8%81%AFtwitch-api-39820d52be8c)
2. 利用已經有登入自己Twitch帳號的Chrome user，在桌面建立捷徑
3. 去硬碟中chrome的資料夾，記錄位置(CHROME_PROFILE_PATH)和user名稱(CHROME_PROFILE_NAME)，以我自己為例，前者是 "C:\\Users\\user\\AppData\\Local\\Google\\Chrome\\User Data"，後者是 "Default"
(2和3請參照 https://stackoverflow.com/questions/73927843/cant-login-on-twitch-with-selenium)

### 所需python套件:
1. datetime
2. requests
3. selenium

### 操作步驟:
1. 下載所有的資料夾與py檔
2. 將 auto_watch_stream.py 內的 CLIENT_ID, CLIENT_SECRET, CHROME_PROFILE_PATH, CHROME_PROFILE_NAME 按前置作業中的設定改換
3. 依所需python套件建立虛擬環境
4. 開啟命令提示字元(cmd)，進入該虛擬環境並執行 auto_watch_stream.py --streamer_name 實況主名稱 *(註: 實況主名稱就是該實況主url中，最後一個斜線後面的那串，通常會是該實況主的頻道名稱*

### 備註:
1. 程式碼中我讓其在預設路徑(D槽)讀取Chromedriver，如有更動Chromedriver執行檔的位置，可直接改`browser = webdriver.Chrome(options=options)`這行
2. 製作這程式的最大原因在於**我一定得要用Chrome自動開指定的Twitch實況台**，如果是Twitch其他用Oauth認證後去互動的操作，就不會需要selenium做開啟瀏覽器的動作了
3. print在cmd內的內容，我也有自動寫成log了 (可以在streamer_log資料夾中找到
4. twitch_api.py 內的東西非我原創，但我也找不到來源了


