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

if __name__ == "__main__":
    sys.exit(lists())