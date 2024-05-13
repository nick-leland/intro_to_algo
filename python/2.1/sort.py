def insertion_sort(A, n):
    """Function that performs a simple insertion sort."""
    try:
        y = A.copy()
        for i in range(1, n):
            key = A[i]
            j = i - 1
            count = 0
            while j >= 0 and A[j] > key:
                A[j+1] = A[j]
                j = j-1
            A[j+1] = key

            if sorted(A) != sorted(y):
                raise ValueError        
    except ValueError:
        print("List is missing a value.")
        print(A)
        print(y)
    return A

if __name__ == "__main__":
    x = [5, 2, 4, 6, 1, 3]
    y = len(x)
    print(x, y)
    print(insertion_sort(x, y))
    x = [5, 7, 0, 1, 8, 3, 3]
    y = len(x)
    # print(x)
    # print(insertion_sort(x, y))

    
