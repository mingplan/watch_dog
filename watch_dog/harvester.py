import glob
import time
import os
class Harvester(object):
    def __init__(self, path, queue, ignore_older=None):
        self.path = path
        self.queue = queue
        self.ignore_older = ignore_older

    def fetch_file(self, cur_time=None):
        if cur_time is None:
            cur_time = int(time.time())
        file_list = glob.glob(self.path)
        for file_item in file_list:
            fstat = os.stat(file_item)
            if (cur_time - fstat.st_mtime) < self.ignore_older:
                self.queue.append(file_item)

