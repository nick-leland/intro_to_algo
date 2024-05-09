def insertion_sort(A, n):
    """Function that performs a simple insertion sort."""
    # A is an array of values to be sorted
    # n is the number of values to sort
    # values occupy positions A[1] through A[n] of the array (A[:n]
    # print(A)
    for i in range(n):
        key = A[i]
        # Insert A[i] into the sorted subarray A[:i-1]
        j = i - 1
        print("key =", str(key) + ", A[j] =", str(A[j])+", while result =", ((j>=0) and (A[j] > key)))
        r = (((j>=0) and (A[j] > key)))
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j = j-1
        # print("A["+str(j+1)+"]=", key)
        A[j+1] = key
        # if r == True:
            # print(A, (i))
    return A

if __name__ == "__main__":
    x = [5, 2, 4, 6, 1, 3]
    y = len(x)
    print(x)
    print(insertion_sort(x, y))
    print()
    x = [5, 7, 0, 1, 8, 3, 3]
    y = len(x)
    print(x)
    print(insertion_sort(x, y))

    
