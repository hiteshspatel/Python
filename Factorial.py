def example_fac(i):
    ans = 1
    if i == 1 or i == 0:
        return 1

    while(True):
        if i > 1:
            ans = ans * i
            i = i - 1
        else:
            break
    return ans


if __name__ == '__main__':
    n = example_fac(10)
    print(n)