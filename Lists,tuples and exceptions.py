import sys


def lists():
    l = list()
    print(l,type(l))
    print(len(l))#length of list
    l1 = [5,6,7,8]
    print(l1,len(l1))
    print(dir(l1))#dir show attributes on objects ie.in a list
    print(6 in l1)
    print(11 not in l1)
    print(not 11 in l1)
    a = list()
    b = a + [7,8,9]
    print(f"a = {a}")
    print(f"b = {b}")
    u = [1,2,3]
    v = u
    print(f"u = {u}")
    print(f"v = {v}")
    v += [4,5,6]
    print(f"u = {u}")
    print(f"v = {v}")
    v1= u.copy()#Use copy and not assignment to make a copy
    print(v)
    print(id(a))#Shows unique identity of an object
    print(id(v))
    print(id(u))
    print(id(v1))
    #Mean and Max
    print(min(v1))
    print(max(v1))
    #Indexing with Lists
    print(f" v1 = {v1}")
    print(f"The first item is {v1[0]}")
    print(f"The second item is {v1[1]}")
    print(f"The last item is {v1[-1]}")
    print(f"The second last item is {v1[-2]}")
    #Finding the position of an item we know of
    print(f"6th is at {v1.index(5)}")
    #Multiplication operator on lists
    d  = [3] * 20
    print(d,"of length ",len(d))
    #This gives an error aswe cannot multiply a list with another list
    #e = [2]* [4]
    #print(e)

    e = 20 * [5]
    print(e)
     #Counting items in list
    v = [3] * 10 + [5,6,7]
    print(v)
    print(f"There are {v.count(3)} instances in list v")

    print("f"* 10)
    #Tracing index in a list
    s = "This is a good sentence to work with"
    print(s[8])
    #Range of indexes
    print(s[1:7])
    #Rnge function
    r = list(range(20))
    print(r[3:10])
    #Range with step
    print(r[3:10:2])
    #Range with a start value
    l = list(range(15,20))
    w = list(range(15, 20,2))
    print(l)
    print(w)
    k = list(range(12, 100, 3))
    print(k)
    print(k[-10:-1])
    print(k[-10:-1:2])
    print(k[-1:-10:-2])
    #Slicing
    print(k)
    print(k[::2])
    print(k[:12:])

 #Methods associated with lists
    #Replace using indexes
    k[12] = 1000
    print(F"New k = {k}")
    k[14:20] = [77] * 4
    print(k, len(k))
    del k[17]
    print(k,len(k))
    k.append(6)
    print(k)

    #Tuples
    t = tuple()
    print(t,type(t))
    print(len(t))
    s = ()
    print(s,type(s))
    s = ("car")
    print(s,type(s))
    #Creation of single item tuple
    t = (0,)
    print(t,type(t))
    u = 5,6
    print(u,type(u))
    t = (5,6,7,8,9,10)
    print(f"t[0] = {t[0]}")
    print(f"t[1:3] = {t[1:3]}")
    #Tuples do not item assignment(Immutability)
    #t[3] = 12 This will throw an error message since you cannot change the existing tuple









if __name__ == "__main__":
    sys.exit(lists())