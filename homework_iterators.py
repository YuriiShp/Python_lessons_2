class MyRange:

    def __init__(self, limit, start=None, step=None):
        self.limit = limit
        self.start = 0 if not start else start
        self.step = 1 if not step else step
        self.count = 0
        self.current = self.start

    def __next__(self):
        if (self.current < self.limit and self.step > 0) or\
           (self.current > self.limit and self.step < 0):
            res = self.current
            self.current += self.step
            return res
        else:
            raise StopIteration

    def __iter__(self):
        return self


# for i in MyRange(-10, 4, -1):
#     print(i)


def myrange(limit, start=None, step=None):
    start = 0 if not start else start
    step = 1 if not step else step
    j = start

    if step > 0:
        while True:
            i = j
            j += step
            if (i >= limit and step > 0) or\
               (i <= limit and step < 0):
                break
            yield i
# 
# for i in myrange(-10, 4, -1):
#     print(i)
