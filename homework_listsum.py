def list_sum(arr, sum=0):

    for el in arr:
        if isinstance(el, list):
            sum = list_sum(el, sum)
        if isinstance(el, int):
            sum += el
        print(sum)
    return sum


my_list = [1, 2, [4, 6], [[7, 8], 4, [11, 2]],[9, 3, [4, [8, 6]]]]
# sum = 75
print(list_sum(my_list))
