import time
from threading import Thread

class MyThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.i = 5
        
    def run(self):
        while True:
            print('hello from thread # %i' % self.i) 
            time.sleep(.25)

def start():
	m1 = MyThread()
	m2 = MyThread()
	m1.start()
	m2.start()
	time.sleep(2)
	m1.stop()
	m2.stop()

if __name__ == '__main__':
    start()