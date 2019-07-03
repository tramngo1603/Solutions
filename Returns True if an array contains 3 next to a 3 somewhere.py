#FIND 33:Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def array_contains3 (mylist):
    for a in range(0, len(mylist)):
        if mylist[a] == 3 and mylist[a+1] == 3:
            print(True)

array_contains3([3,5,3,3,4])
