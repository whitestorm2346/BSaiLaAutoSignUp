import threading
from tkinter import *
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import chromedriver_autoinstaller

def get_url_from_gui():
    """
    開啟 Tkinter 輸入介面，輸入完比賽網址後回傳字串
    """
    result = {"url": None}

    def submit():
        result["url"] = entry_url.get()
        root.quit()      # 結束 mainloop，但不會馬上銷毀 Tk
        root.destroy()   # 關閉視窗

    root = Tk()
    root.title("比賽網址輸入")
    root.geometry("400x150")

    label_url = Label(root, text="比賽網址：", font=("Arial", 12))
    label_url.pack(pady=10)

    entry_url = Entry(root, width=40, font=("Arial", 12))
    entry_url.pack()

    btn_submit = Button(root, text="提交", command=submit, font=("Arial", 12))
    btn_submit.pack(pady=10)

    root.mainloop()
    return result["url"]


if __name__ == "__main__":
    chrome_option = chromeOptions()
    chrome_option.add_argument('--log-level=3')
    chrome_option.add_argument('--start-maximized')
    chromedriver_autoinstaller.install()

    driver = webdriver.Chrome(options=chrome_option)
    url = get_url_from_gui()

    driver.get(url)

    

    driver.close()

