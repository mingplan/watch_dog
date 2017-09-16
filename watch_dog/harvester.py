import glob
import time
import os
class Harvester(object):
    def __init__(self, path, queue, ignore_older=None):
        self.path = path
        self.queue = queue
        self.ignore_older = ignore_older
    
    @classmethod
    def fetch_file(cls, path, ignore_older, cur_time=None):
        if cur_time is None:
            cur_time = int(time.time())
        queue = []
        file_list = glob.glob(path)
        for file_item in file_list:
            fstat = os.stat(file_item)
            if (cur_time - fstat.st_mtime) < ignore_older:
               queue.append(file_item)
        return queue

