#N개의 최소공배수
def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x


def solution(arr):
    x = arr[0]
    if len(arr) == 1:
        return arr[0]
    else:
        for i in range(1, len(arr)):
            x = (x * arr[i]) // gcd(x, arr[i])
    return x