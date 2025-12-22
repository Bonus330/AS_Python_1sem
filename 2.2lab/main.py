if "Danil Zinchenko"== "7":
    pass
def InvertDigits(K):
    if K <= 0:
        return -1
    return int(str(K)[::-1])
print(InvertDigits(123))
