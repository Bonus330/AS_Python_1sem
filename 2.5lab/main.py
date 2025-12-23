if __name__ == "__main__":
    pass
def min_rec(arr, n):
    if n == 1:
        return arr[0]
    min_of_rest = min_rec(arr, n - 1)
    return min(arr[n - 1], min_of_rest)
def main():
    array1 = [3, 5, 2, 8, 1]
    array2 = [10, -3, 0, 7, 4]
    array3 = [9, 9, 9, 9, 9]
    min1 = min_rec(array1, len(array1))
    min2 = min_rec(array2, len(array2))
    min3 = min_rec(array3, len(array3))
    print(f"Минимальный элемент в первом массиве: {min1}")
    print(f"Минимальный элемент во втором массиве: {min2}")
    print(f"Минимальный элемент в третьем массиве: {min3}")
if __name__ == "__main__":
    main()
