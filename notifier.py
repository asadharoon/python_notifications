from plyer import notification
import time
if __name__=="__main__":
    while True:
        notification.notify(
            title="ABC",
            message="Hello Asad",
            app_icon = "D:\icon.ico", # change address
            timeout=10, # notification timeout is 10seconds
        )
        time.sleep(10) # after every 10 seconds it shows notification