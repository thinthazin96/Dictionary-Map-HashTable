#Two Sum with given array

arr1 = [1,3,5,6]
target1 = 8

arr2 = [4,7,2,6]
target2 = 12

def two_sum(arr,target):

    values = dict()

#Loop each element using indexies in array.
    for i, elem in enumerate(arr):
        comp = target - elem

#if the two sum add up to target value, return that value.
#if not, 
        if comp in values:

            return[values[comp], i]

        values[elem] = i

    return[]

list1 = two_sum(arr1,target1)
print(list1)

list2 = two_sum(arr2, target2)
print(list2)

