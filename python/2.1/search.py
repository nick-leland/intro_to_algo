# This currently loops infinitely, fix it kekl

def search(A, n):
    """Searches list 'A' for a value 'n'"""
    counter = 0
    key = A[counter]
    while key != n and counter <= len(A):
        counter + 1
        key = A[counter]
        print(key)
    if counter > len(A):
        return "NIL"
    else:
        return counter + 1
if __name__ == "__main__":
    x = [3, 1, 6, 9, 10]
    y = 3
    print(search(x, y))
    x = [3, 1, 6, 9, 10]
    y = 6
    print(search(x, y))
    x = [3, 1, 6, 9, 10]
    y = 10
    print(search(x, y))
