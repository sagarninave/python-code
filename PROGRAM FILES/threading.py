import threading

class threadManager(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

x = threadManager(name="start")
y = threadManager(name="end")

x.start()
y.start()