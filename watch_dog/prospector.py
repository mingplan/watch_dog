from watch_dog.harvester import Harvester

if __name__ == '__main__':
    path = ''
    queue = []
    harvester = Harvester(path, queue, 90000)
    harvester.fetch_file()
    for item in queue:
        print item
    
