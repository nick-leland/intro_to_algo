def insertion_sort(A, n):
    """Function that performs a simple insertion sort."""
    for i in range(n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = key
    return A

if __name__ == "__main__":
    x = [5, 2, 4, 6, 1, 3]
    y = len(x)
    print(x)
    print(insertion_sort(x, y))
    x = [5, 7, 0, 1, 8, 3, 3]
    y = len(x)
    print(x)
    print(insertion_sort(x, y))

    
