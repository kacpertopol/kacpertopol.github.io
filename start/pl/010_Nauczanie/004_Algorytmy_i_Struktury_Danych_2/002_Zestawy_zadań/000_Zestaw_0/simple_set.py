from rec import *

N = 10

def vis_bool_table(b):
    if N <= 10:
        return "".join([str(i) for i in range(N)]) + "\n" + \
                "".join(["#" if x else " " for x in b])
    else:
        return "".join(["T" if x else "F" for x in b])

def insert(b , x):
    b[x] = True

def remove(b , x):
    b[x] = False

def is_in(b , x):
    return b[x]

def intersection(b1 , b2):
    return [b1[i] and b2[i] for i in range(N)]

def union(b1 , b2):
    return [b1[i] or b2[i] for i in range(N)]

a = [False for _ in range(N)]
b = [False for _ in range(N)]
c = [False for _ in range(N)]

r = recorder("a" , "b" , "c" , visualization_functions = 
             {"a" : vis_bool_table , 
              "b" : vis_bool_table ,
              "c" : vis_bool_table})

with r:
    r.record(step = "INITIAL VALUES" , getcontext = 5)
    insert(a , 1)
    insert(a , 3)
    r.record(step = "INSERTED TO A" , getcontext = 5)
    insert(b , 3)
    insert(b , 5)
    c = intersection(a , b)
    r.record(step = "INTERSECTION A , B" , getcontext = 5)
    c = union(a , b)
    r.record(step = "UNION A , B" , getcontext = 5)

r.play()

