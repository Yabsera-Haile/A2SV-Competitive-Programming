class Solution: 
    def select(self, arr, i):
        for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    i = j
        return i
            
    
    def selectionSort(self, arr,n):
        for i in range(0,n):
            j=self.select(arr=arr,i=i)
            arr[i],arr[j]=arr[j],arr[i]