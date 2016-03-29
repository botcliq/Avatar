l = []
def anagram(s1,s2):
    c1= [0]*26
    c2= [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos]+1
    print c1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] +1
    print c2

    j = 0
    still_ok = True

    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j=j+1
        else:
            still_ok = False
    return still_ok

print (anagram("apple","pleap"))
print (anagram("apple","plaa"))

def test1(): l = []
for i in range(1000): l = l + [i]
def test2():
    l = []
    for i in range(1000):
        l.append(i)
def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

#import timeit
from timeit import Timer
t1 = Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "milliseconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "milliseconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")