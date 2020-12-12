# Python program for implementation of Linear Serach
# Function needs an array and element to be found
def LinearSearch(arr,x): 
    n = len(arr)
    flag = False
    # Traverse through all array elements 
    for i in range(n):
        # Condition to check weather the element is found or not
        
        if arr[i] == x:
            # Return True and the Set pos to index of Element in arr
            return True
    # Return -1 if no elemet found    
    return False   
        
# TEST

def solve(arr):
    LinearSearch(arr,14095505)

