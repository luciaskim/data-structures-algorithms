"""
Quick Sort in Python
Adapted from Youtube codebasics 
Title: "Quick Sort - Data Structures & Algorithms Tutorial Python #15"
https://youtu.be/5iSZ7mh_RAk
"""

def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    start = pivot_index + 1

    while start < end:
        while start < len(elements) and elements[start] <= pivot: # Checks start is in range
            start += 1
        while elements[end] > pivot:
            end -= 1
        if start < end:   # Swaps only if start is less than end, otherwise exists loop
            elements[start], elements[end] = elements[end], elements[start]
    elements[pivot_index], elements[end] = elements[end], elements[pivot_index]
    return end

def quicksort(elements, start, end):
    if start < end:
        partition_index = partition(elements, start, end)
        quicksort(elements, start, partition_index - 1)
        quicksort(elements, partition_index + 1, end)

if __name__ == '__main__':
    data1 = [11, 9, 29, 7, 2, 15, 28]
    data2 = data1.copy()
    quicksort(data2, 0, len(data2) - 1)
    # print(data1)
    print(data2)
