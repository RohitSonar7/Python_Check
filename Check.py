def By5(a):
    if a % 5 == 0:
        return True
    else:
        return False

def By7(a):
    if a % 7 == 0:
        return True
    else:
        return False

def By9(a):
    if a % 9 == 0:
        return True
    else:
        return False

def By11(a):
    if a % 11 == 0:
        return True
    else:
        return False


if __name__ =="__main__":
    num = int(input("Enter the Number"))
    result = By5(num)
    print(result)
    result = By7(num)
    print(result)
    result = By9(num)
    print(result)
    result = By11(num)
    print(result)