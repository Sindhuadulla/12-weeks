def intersection2sortedarrays(a, b):
    ans = []
    i, j = 0, 0
    m, n = len(a), len(b)
    while i < m and j < n:
        if a[i] == b[j]:
            ans.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return ans

if __name__ == "__main__":
    m, n = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = intersection2sortedarrays(a, b)
    print(*ans)