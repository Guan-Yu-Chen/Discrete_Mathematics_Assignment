import time
import random

class Arc:
    def __init__(self, head, tail, length):
        self.head = head
        self.tail = tail
        self.len = length

N = 100000
arcs = [Arc(0, random.randint(0, 10000), 1) for _ in range(N)]

# 方法1: append + sort
lst1 = []
start = time.time()
for arc in arcs:
    lst1.append(arc)
lst1.sort(key=lambda a: a.tail)
print("append + sort:", time.time() - start)

# 方法2: 每次插入排序
lst2 = []
start = time.time()
for arc in arcs:
    i = 0
    while i < len(lst2) and lst2[i].tail < arc.tail:
        i += 1
    lst2.insert(i, arc)
print("manual insert:", time.time() - start)
