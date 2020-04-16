from LRU import LRUCache
class LRUTest:
    def __init__(self):
        pass
    def testingmethod(self):
        l = LRUCache(4)
        a = [1,2,3,4]
        for i in a:
            l.put(i)
        assert l.get_cache() == [1,2,3,4], "testcase1 failed"
        print("Testcase 1 Passed")
        l1 = LRUCache(6)
        b = [88, 26, 122, 105, 57, 123]
        for i in b:
            l1.put(i)
        assert l1.get_cache() == [88, 26, 122, 105, 57, 123], "testcase2 failed"
        print("Testcase 2 Passed")
        l2 = LRUCache(6)
        c = [35,45,501,507,45,501]
        for i in c:
            l2.put(i)
        assert l2.get_cache() == [35,507,45,501], "testcase 3 failed"
        print("Testcase 3 Passed")
        print("All testcases passed")
        
if __name__=="__main__":
    l1 = LRUTest()
    l1.testingmethod()