# a rudimentry implementation of quicksort
import random


def quicksort(array):
    nbr_elements = len(array)
    # base case
    if nbr_elements <= 1:
        return array
    # recursive calls
    else:
        idx = random.randint(0, nbr_elements - 1)
        pivot = array.pop(idx)

        L = list(filter(lambda e: e <= pivot, array))
        R = list(filter(lambda e: e > pivot, array))

        return quicksort(L) + [pivot] + quicksort(R)


if __name__ == "__main__":
    rand_array = [random.randrange(-10, 10, 1) for i in range(100)]
    print("\n{}\n".format(rand_array))
    srtd = quicksort(rand_array)
    print("\n{}\n".format(srtd))
