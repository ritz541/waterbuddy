import threading
import time

def notification():
    while True:
        print("Notification: Your body needs water!")
        time.sleep(120)
        
# notification_thread = threading.Thread(target=notification)
# notification_thread.start()
