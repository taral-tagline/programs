from sys import exc_info


try:
    a = int(input("enter the number:- "))
    b = int(input("enter the number:- "))
    c = int(input("enter the number:- "))
except Exception as e:
    # print(e)
    print(exc_info())
    # f = open("exception.txt", "a")
    # f.writelines(e)
    # f.close()
    # raise Exception("Other Exception...")

# if a > b and a > c:
#         print("A is bigger...")
# elif b > c:
#     print("B is greater...")
# else :
#     print("c is greater")