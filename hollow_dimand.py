def demo(n):
    for row in range(1,n):
        for space in range(n,row,-1):
            print(end=" ")
        for column in range(1,row * 2):
            if column == 1 or column == row * 2 - 1 :
                print("*",end="")
            else:
                print(' ',end="")
        print("\r")

    for row in range(n-2,0,-1):
        for space in range(n,row,-1):
            print(end=" ")
        for column in range(1,row * 2):
            if column == 1 or column == row * 2 - 1 :
                print("*",end="")
            else:
                print(' ',end="")
        print("\r")

n= input("enter the number:- ")
demo(int(n)+1)