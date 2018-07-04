class Queue(object):
    def __init__(self):
        self.queue = []

    def insert(self,e):
        self.queue.append(e)

    def remove(self):
        try:
            print self.queue[0]
            self.queue.remove(self.queue[0])
        except:
            raise ValueError()

s = Queue()
s.insert(2)
s.insert(3)
s.insert([2,4])
print s
s.remove()
print s
s.remove()
print s
s.remove()
s.remove()