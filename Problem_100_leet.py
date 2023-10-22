list1 = [1,2,3]
list2 = [3,4,5]

def checker(nums1, nums2):
    x = True
    if len(nums1) == len(nums2):
        for i in range(len(nums1)):
            if nums1[i] != nums2[i]:
                x = False
    else:
        print("The trees are  not of the same length")
        x = False


    if x == True:
        print("The binary trees are the same")
    else:
        print("The binary trees are not the same")

checker(list1, list2)