def findBitonicPoint(arr):
    """
    :type n: int
    :type trust: List[List[int]]
    :rtype: int
    """
    l = 0
    m = len(arr)/2
    r = len(arr) - 1
    while(true):
        if arr[m]>arr[m-1] and arr[m] < arr[m+1]:
            return m
        elif arr[m] > arr[l]:


a = [3, 9, 10, 11, 13, 20, 17, 5, 1]
b = 12


