"""input number eg.5, print string on the console 12345,
constraint is 1<=n<=150"""
if __name__ == '__main__':
    n = int(input())
    l = []
    if n>=1 and n<=150:
        for i in range(1,n+1):
            l.append(str(i))
        print("".join(l))