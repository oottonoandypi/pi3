def merge2SortedArraysInPlace(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
            Given 2 list nums1 with size m+n and nums2 with size n
            Sort 2 lists and merge in place in nums1
        """
        index1=m-1
        index2=n-1
        index=len(nums1)-1
        
        while index1>=0 and index2>=0:
            if nums1[index1]>nums2[index2]:
                nums1[index]=nums1[index1]
                index1-=1
            else:
                nums1[index]=nums2[index2]
                index2-=1
            index-=1
        
        while index2>=0:
            nums1[index]=nums2[index2]
            index-=1
            index2-=1