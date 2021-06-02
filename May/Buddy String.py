def swap(i, j, arr):
    if i != j:
        arr[i], arr[j] = arr[j], arr[i]
    return arr


def Buddy_strings(a, b):
    st1 = set(a)
    st2 = set(b)


    for i in range(1, len(st1)):
        key = st1[i]
        j = i - 1
        while j >= 0 and key != st1[j]:
            if swap(i,j,st1) == st2:
                return True
            else:
                swap(i,j,st1)
            j = j - 1
        while j >= 0 and key == st1[j]:
            if swap(i, j, st1) == st2:
                return True
            j = j-1


    return False

if __name__ == '__main__':
    a = "abcd"
    b = "acbd"
    print(Buddy_strings(a,b))