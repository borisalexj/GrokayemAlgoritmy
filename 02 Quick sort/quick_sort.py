
def quickSort(array):
    if len(array) <2:
        return array
    else:
        pivot = array[0]
        print("pivot - ", pivot)
        less = [i for i in array[1:] if i <= pivot]
        print("less - ", less)
        greater = [i for i in array[1:] if i > pivot ]
        print("greater - ", greater)
        return quickSort(less) + [pivot] + quickSort(greater)

print(quickSort([10,5,2,3]))