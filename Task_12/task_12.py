import sys

def add(a,b):
    try:
        sum = float(a)+float(b)
        return sum
    except ValueError : 
        print("Error : Provide numbers as arguments ")
        return None

if __name__=="__main__":
    if len(sys.argv) != 3 :
        print("User : python script_name.py a b")
    else :
        a = sys.argv[1]
        b = sys.argv[2]
        sum = add(a,b)
        if sum is not None:
            print(f"The sum of the 2 numbers {a} and {b} is : {sum} ")
