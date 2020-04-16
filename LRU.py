class LRUCache:
    def __init__(self,size):
        self.lrucache = []
        self.size = 6
    def put(self,item):
        if item not in self.lrucache:
            if(len(self.lrucache)<self.size):
                self.lrucache.append(item)
            else:
                self.lrucache.pop(0)
                self.lrucache.append(item)        
        else:
            # m1 = self.lrucache.remove(item)
            index = self.lrucache.index(item)
            m1 = self.lrucache.pop(index)
            self.lrucache.append(m1)
    def get(self):
        return self.lrucache[0]
    def get_cache(self):
        return self.lrucache