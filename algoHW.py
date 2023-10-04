'''Name: Sydney Christenson                             Date: Tue Oct 3
   Net ID: sac771                                       Assignment: Algorithms Homework 1

   References:
    * Alg05Sorting.pdf                                  * JavaTPoint.com
    * matplotlib Docs
'''

import time
import random
import matplotlib.pyplot as plot

# Arrays to store the runtimes of all the sorting algorithms, will be used to plot into graph
selectTimes = []
quickTimes = []
hybridTimes = []

# Function will grab the time at which the sorting starts, call the algorithm with array size, record the time the sorting ends, 
# then takes the difference and converts it to microseconds
def measureTime(algorithm, arr):
    start = time.time()
    algorithm(arr)
    end = time.time()
    return (end - start) * 1e6

# Used Selection Sort Pseudocode from class
def selectionSort(arr):
    n = len(arr)
    for i in range(n): 
        min = i # smallest element in array
        for j in range(i+1, n): 
            if arr[j] < arr[min]: # do if i < smallest array
                min = j # then smallest
        arr[i], arr[min] = arr[min], arr[i] # exchanging


# I used JavaTPoint.com and Class Notes
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quickSort(left) + middle + quickSort(right)

# Hybrid Algorithm
def sydSort(arr, threshold): 
# If less than 60, will use Selection Sort
    if len(arr) < threshold: 
        n = len(arr)
        for i in range(n): 
            min = i
            for j in range(i+1, n): 
                if arr[j] < arr[min]: 
                    min = j
            arr[i], arr[min] = arr[min], arr[i]
# If greater than 60, will use Quicksort
    else:
        if len(arr) <= 1: # Array of 1 is already sorted
            return arr
        pivot = arr[len(arr) // 2] # Using the middle element as a pivot
        left = [x for x in arr if x < pivot] 
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quickSort(left) + middle + quickSort(right)


inputSizes = [10, 20, 30, 40, 50, 55, 56, 57, 58, 59, 60, 65, 70, 80, 90, 100]
threshold = 60 # Found after experiemnts

for size in inputSizes:
    arr = [random.randint(1, 1000) for _ in range(size)] # Generating random array
    print(f"Random array of size {size}: {arr}") 

    # Measures the time for each algorithm
    selectTime = measureTime(selectionSort, arr.copy())
    quickTime = measureTime(quickSort, arr.copy())
    hybridTime = measureTime(lambda x: sydSort(x, threshold), arr.copy())

    # Appends times to time arrays for plotting
    selectTimes.append(selectTime)
    quickTimes.append(quickTime)
    hybridTimes.append(hybridTime)

    print(f"----------------------For size {size}:----------------------")
    #print(f"   Selection Sort time = {selectTime} microseconds\n   Quicksort time = {quickTime} microseconds\n")
    print(f"   Selection Sort time = {selectTime} microseconds\n   Quicksort time = {quickTime} microseconds\n   SydSort time = {hybridTime} microseconds")

    '''if selectTime < quickTime:
        print(f"\nSelection Sort Faster For Size {size}\n")
    else:
        print(f"\nQuicksort Faster For Size {size}\n")'''
    
    # for my own sanity
    if selectTime < quickTime and selectTime < hybridTime:
        print(f"\nSelection Sort Faster For Size {size}\n")
    if quickTime < selectTime and quickTime < hybridTime:
        print(f"\nQuicksort Faster For Size {size}\n")
    if hybridTime < selectTime and hybridTime < quickTime:
        print(f"\nSydSort is Faster For Size {size}\n")
    if hybridTime == selectTime and hybridTime < quickTime:
        print(f"\nSydSort and Selection Sort are Faster For Size {size}\n")


# Plotting points with time arrays declared at top
plot.figure(figsize=(10,6))
plot.plot(inputSizes, selectTimes, '-o', label="Selection Sort")
plot.plot(inputSizes, quickTimes, '-o', label="Quicksort")
plot.plot(inputSizes, hybridTimes, '-o', label="SydSort")
plot.title("Sorting Algorithm Time Comparisons")
plot.xlabel("Input Size")
plot.ylabel("Time (microseconds)")
plot.legend()
plot.grid(True)
plot.show()



