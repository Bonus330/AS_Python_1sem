def rle_encode(s):
    res = ""
    i = 0
    n = len(s)

    while i < n:
        cnt = 1
        while i + cnt < n and s[i] == s[i + cnt]:
            cnt += 1
        res += s[i] + str(cnt)
        i += cnt

    return res


while True:
    try:
        line = input()
        print(rle_encode(line))
    except EOFError:
        break
