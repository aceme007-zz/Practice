# sort

# Selection Sort
# get the min elem index and put it in front
def selectionSort(A):
  for i in range(len(A)-1):
    imin = i
    for j in range(i+1, len(A)):
      if A[j] < A[imin]:        
        imin = j
    temp = A[i]
    A[i] = A[imin]
    A[imin]= temp
    
# Bubble Sort
# sort highest to end
def bubbleSort(A):
    for j in range(len(A)-1):
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                temp = A[i+1]
                A[i+1] = A[i]
                A[i] = temp
                
# Insertion Sort
# assume 1st is sorted and then insert in hole
def insertionSort(A):
    for i in range(1, len(A)):
        value = A[i]
        hole = i
        while hole>0 and A[hole-1]>value:
            A[hole] = A[hole-1]
            hole = hole - 1
        A[hole] = value
        
        
# Merge Sort
# divide and recursive
def merge(left, right, arr):
    i = j = k = 0
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1
        k = k + 1
    while i<len(left):
        arr[k] = left[i]
        k = k + 1
        i = i + 1
    while j<len(right):
        arr[k] = right[j]
        k = k + 1
        j = j + 1

def mergeSort(A):
    L = len(A)
    if L < 2:
        return
    else:
        mid = int(L/2)
        left = A[:mid]
        right = A[mid:]
        mergeSort(left)
        mergeSort(right)
        merge(left, right, A)
        
A = [2, 4, 1, 6, 8, 5, 3, 7]
mergeSort(A)

# Quick sort
# this is in place sort
def Partition(arr, start, end):
    pivot = arr[end]
    pindex = start
    for i in range(start, end):
        if arr[i] < pivot:
            arr[i], arr[pindex] = arr[pindex], arr[i]
            pindex = pindex + 1
    arr[pindex], arr[end] = arr[end], arr[pindex]
    return pindex

def quickSort(arr, start, end):
    if start < end:
        Pindex = Partition(arr, start, end)
        quickSort(arr, start, Pindex-1)
        quickSort(arr, Pindex+1, end)
    

        
A = [2, 4, 1, 6, 8, 7, 12, 17, 9, 3, 5]
quickSort(A, 0, len(A)-1)