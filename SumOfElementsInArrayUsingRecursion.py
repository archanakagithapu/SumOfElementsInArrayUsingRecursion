'''Sum of all the elements in array using array'''

def s_arr(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + s_arr(arr[1:])

arr=list(map(int,input().split()))
result=s_arr(arr)
print(result)
