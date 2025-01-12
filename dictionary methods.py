ep1 = {33: 22,232:22,556:23,212: 446,22:1}
ep2= {22: 12, 34: 22, 120:33, 21: 2}

ep1.update(ep2)
# ep1.clear()
print(ep1)
ep1.pop(21)
print(ep2)
print(ep2.popitem())