class Solution:
    def removeDuplicates(self, arr):
        """
        Removes duplicates from sorted array in-place
        Time: O(n) | Space: O(1)
        Returns new length of array

        Example: [1,1,2,2,3,4,4] -> 4, arr = [1,2,3,4,...]
        """
        if not arr:
            return 0

        j = 0 # Pointer for unique elements

        for i in range(1, len(arr)):
            if arr[i]!= arr[j]:
                j += 1
                arr[j] = arr[i]

        return j + 1 # New length
class Solution:
    # Function to rotate an array by k elements to the right
    def rotateArr(self, arr, k):
        n = len(arr)
        k = k % n # Important: k > n ka case handle
        if k == 0:
            return

        # Step 1: Reverse whole array
        # [1,2,3,4,5] -> [5,4,3,2,1]
        self.reverse(arr, 0, n - 1)

        # Step 2: Reverse first k elements
        # [5,4,3,2,1] -> [4,5,3,2,1]
        self.reverse(arr, 0, k - 1)

        # Step 3: Reverse remaining n-k elements
        # [4,5,3,2,1] -> [4,5,1,2,3]
        self.reverse(arr, k, n - 1)

    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
