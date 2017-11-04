
import add
import sys

print sys.argv

def addList(inlist,sysargs):
    print inlist
    print sysargs
    
    add(inlist[0],inlist[1],sysargs)
    
addList([1,2],sys.argv)
    
