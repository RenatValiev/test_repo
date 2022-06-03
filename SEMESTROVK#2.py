def InsertionSort(arr, begin, end):
    """
    Основная функция сортировки данных с использованием алгоритма сортировки вставкой
    """
    left = begin
    right = end

    for i in range(left + 1, right + 1):
        key = arr[i]

        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key