import sys

def addNumbers(n1,n2):
	return n1+n2

if __name__ == '__main__':
    
    print "__name__:",__name__
    print "__file__:",__file__
    if len(sys.argv) != 3:
        print "Invalid number of arguments"
        print "Syntax is: python main.py <number 1> <number 2>"
    else:

        number1 = int(sys.argv[1])
        number2 = int(sys.argv[2])

        print "Result:",addNumbers(number1,number2)
    
    
