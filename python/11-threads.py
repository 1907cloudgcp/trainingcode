#!/usr/bin/env python3

'''
Threads

Includes: Multi-threading, Custom Threads, Synchronization

-> Threads allow you to perform tasks in parallel starting from a main process.
-> This can use the full extent of your CPU and allow programs to continue
regardless a subsection of it hasn't completed yet.
-> Leverage Synchronization when the order of your operations matters.
'''

import threading
from threading import Thread
import time
import random

#Global threading Lock to be acquired for synchronization
lock = threading.Lock()

def main():
    input('Press any key to start Asynchronous Thread race...')
    threads = []
    for x in range(5):
        thread = AsyncThread(name = 'Thread-{}'.format(x + 1))
        thread.start()
        threads.append(thread)
        time.sleep(1)

    input('Press any key to start Synchronous Thread race...')
    threads = []
    for x in range(5):
        thread = SynchroThread(name = 'SynchroThread-{}'.format(x + 1))
        thread.start()
        threads.append(thread)
        time.sleep(1)

class AsyncThread(Thread):
    #Override run method
    def run(self):
        print('{} started at time {}'.format(self.getName(), str(time.time())))
        time.sleep(random.randint(1,5))
        print('{} ended at time {}'.format(self.getName(), str(time.time())))

class SynchroThread(Thread):
    #Override run method
    def run(self):
        lock.acquire()
        print('{} started at time {}'.format(self.getName(), str(time.time())))
        time.sleep(random.randint(1,5))
        print('{} ended at time {}'.format(self.getName(), str(time.time())))
        lock.release()

if __name__ == '__main__':
    main()