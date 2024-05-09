from timeit import default_timer as timer
import random

def insertion_sort(A, n):
    """Function that performs a simple insertion sort."""
    for i in range(n):
        key = A[i]
        j = i - 1
        r = (((j>=0) and (A[j] > key)))
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = key
    return A

if __name__ == "__main__":
    iterations = 1000
    total = 0
    for _ in range(iterations):
        faster = False
        z = 1
        while faster == False: 
            digits = 5
            x = [random.randint(0,((digits*10)-1)) for i in range(z)]
            y = len(x)

            start = timer()
            end = timer()
            time_algo= (f'{abs(start - end):.20f}')

            start = timer()
            end = timer()
            time_built = (f'{abs(start - end):.20f}')

            if time_algo < time_built:
                # print(f"Algo wins at {time_algo}, converges at {z}")
                faster = True
                total += z        
            # else:
                # print(f"Built wins at {time_built}")
            z += 1
        print(total)
    print(f"Average convergences is {total/iterations}")
