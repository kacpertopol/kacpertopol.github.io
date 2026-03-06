from rec import recorder
import copy

def to_str(l):
    if len(l) == 0:
        return "[]"
    elif len(l) == 1:
        return "[...]"
    elif len(l) == 2:
        return "[" + str(l[0]) + " , ...]"

def to_str_nice(l , p , c , tab = 0 , spaces = 13 , p_comment = " <- previous" , c_comment = " <- current"):
    description = ""
    if l == p:
        description = p_comment
    if l == c:
        description = c_comment
    res = []
    if len(l) == 0:
        return "[]"
    elif len(l) == 1:
        return " " * tab + "(" + " \u2577 )".rjust(spaces - 1) + description + "\n" + \
                to_str_nice(l[0] , p , c , tab = tab + spaces , spaces = spaces , p_comment = p_comment , c_comment = c_comment)
    elif len(l) == 2:
        if l[1] is None:
            return " " * (tab - 3) + "\u2570\u2500\u2500" + "[" + (str(l[0]) + ", x ]").rjust(spaces - 1) + description + "\n"
        else:
            return " " * (tab - 3) + "\u2570\u2500\u2500" + "[" + (str(l[0]) + ", \u2577 ]").rjust(spaces - 1) + description + "\n" + \
                    to_str_nice(l[1] , p , c , tab = tab + 13 , spaces = spaces , p_comment = p_comment , c_comment = c_comment)

def add(l , x):
    """
    Adds x to set l. Modifies l.
    """
    r = recorder(
            {
                ("l" , "previous" , "current") : lambda l , p , c : "l =\n" + to_str_nice(l , p , c) ,
                "new" : lambda n : "new = " + (to_str(n) if n is not None else "")
             } , raise_error = False)
    with r:
        r.record(step = "INITIAL STATE")
        if len(l) == 0:
            new = [x , None]
            l.append(new)
            r.record(step = "ADDING FIRST ELEMENT")
        else:
            previous = l
            current = l[0]
            while True:
                r.record(step = "STARTING SEARCH")
                val , nxt = current
                if val >= x:
                    new = [x ,  current]
                    r.record(step = "INSERTING NEW")
                    if len(previous) == 1:
                        previous[0] = new
                        r.record(step = "UPDATING STRUCTURE")
                    else:
                        previous[1] = new
                        r.record(step = "UPDATING STRUCTURE")
                    break
                if nxt is None:
                    r.record(step = "INSERTING NEW ON TOP")
                    new = [x ,  None]
                    current[1] = new
                    r.record(step = "UPDATING STRUCTURE")
                    break
                previous = current
                current = nxt
    return r

def remove(l , x):
    """
    Removes x from set l. Modifies l.
    """
    r = recorder(
            {
                ("l" , "previous" , "current") : lambda l , p , c : "l =\n" + to_str_nice(l , p , c)
             } , raise_error = False)
    with r:
        r.record(step = "INITIAL STATE")
        if len(l) > 0:
            previous = l
            current = l[0]
            while True:
                r.record(step = "STARTING SEARCH")
                val , nxt = current
                if val == x:
                    r.record(step = "FOUND " + str(x))
                    if len(previous) == 1:
                        previous[0] = nxt
                    else:
                        previous[1] = nxt
                    r.record(step = "UPDATED STRUCTURE")
                    break
                if val > x:
                    break
                if nxt is None:
                    break
                previous = current
                current = nxt
    return r

def intersection(l1 , l2):
    """
    Calculates the intersection of sets l1 and l2. Returns new set.
    """
    r = recorder(
            {
                "l1l2" : lambda l : "l1l2 =\n" + to_str_nice(l , None , None) ,
                ("l1" , "previous1" , "current1") : 
                    lambda l , p , c : 
                        "l1 =\n" + \
                            to_str_nice(l , p , c , p_comment = " <- previous1" , c_comment = " <- current1") ,
                ("l2" , "previous2" , "current2") : 
                    lambda l , p , c : 
                        "l2 =\n" + \
                            to_str_nice(l , p , c , p_comment = " <- previous2" , c_comment = "<- current2") ,
                "new" : lambda n : "new = " + (to_str(n) if n is not None else "")
             } , raise_error = False)
    with r:
        l1l2 = []
        top = None
        r.record(step = "INITIAL STATE")
        if len(l1) == 0:
            l1l2 = copy.deepcopy(l2)
            r.record(step = "FINISHED")
            return r , l1l2
        if len(l2) == 0:
            l1l2 = copy.deepcopy(l1)
            r.record(step = "FINISHED")
            return r , l1l2
        else:
            previous1 = l1
            current1 = l1[0]
            previous2 = l2
            current2 = l2[0]
            while True:
                r.record(step = "STARTING SEARCH")
                val1 , nxt1 = current1
                val2 , nxt2 = current2
                if val1 == val2:
                    new = [val1 , None]
                    if top == None:
                        l1l2.append(new)
                        top = new
                    else:
                        top[1] = new
                        top = new

                    r.record(step = "ADDING TO NEW LIST")
                if nxt1 is None or nxt2 is None:
                    break
                if val2 > val1:
                    previous1 = current1
                    current1 = nxt1
                else:
                    previous2 = current2
                    current2 = nxt2
        r.record(step = "FINISHED")
    return r , l1l2

if __name__ == "__main__":
    m = [] # empty set
    r = add(m , 1.0)
 #   r.play(title = "adding to empty")
    add(m , 4.0)
    add(m , 3.0)
    add(m , 2.0)

    r = add(m , 2.2)
#    r.play(title = "adding 2.2")
    
    r = remove(m , 3.0)
#    r.play(title = "removing 3.0")
    
    r = remove(m , 1.0)
#    r.play(title = "removing 1.0")

#    a = []
#    b = []
#    r , _ = intersection(a , b)
#    r.play()

    a = []
    add(a , 3.0)
    add(a , 2.0)
    add(a , 0.0)
    b = []
    add(b , 0.1)
    add(b , 0.0)
    add(b , 3.1)
    add(b , 2.0)
    add(b , 10.0)

    r , _ = intersection(a , b)
    r.play(title = "calculating intersection")


