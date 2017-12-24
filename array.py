'''
Given an array of non-negative integers. Our task is to find minimum number of elements such that their sum should be greater than the sum of rest of the elements of the array.
'''

array = [8,2,3,4,5,6,7,1]
print("Input Array: {}".format(array))


def findArray(array):
    array.sort(reverse=True)
    print("Sorted Array: {}".format(array))
    for i in range(0,len(array)):
        if sum(array[:i]) > sum(array[i+1:]):
            return array[:i]
    return None

try:
    result = findArray(array)
    if result != None:
        print("The expected set of numbers: {}".format(result))
    else:
        print("Unable to get the result")

except Exception as e:
    print("Exception caught: {}".format(e))

