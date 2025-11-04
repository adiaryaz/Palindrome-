def palindrome_arr(arr):
    if not arr:
        return False
    
    left = 0
    right = len(arr) - 1
    palindrome = True
    while left < right:
        if arr[left] != arr[right]:
            palindrome = False
        left +=  1 
        right -= 1

    return palindrome

arr = input()
eval_arr = eval(arr)
x = palindrome_arr(eval_arr)
print(x)