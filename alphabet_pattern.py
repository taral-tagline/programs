def demo(n):
    inc = 65
    for row in range(0,n):
        for space in range(n,row,-1):
            print(end=" ")
        for item in range(0,row):
            print(chr(inc),end=" ")
            inc = inc + 1
        print("\r")

n= input("enter the number:- ")
demo(int(n)+1)