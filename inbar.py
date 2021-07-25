# list=[1,2,3,5,5,6,7]


def containsDuplicate(nums):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if i == j:
                continue
            else:
                if nums[i] == nums[j]:
                    return True
    return False

def again(nums):
    dic={}
    for i in range(len(nums)):
        if nums[i] not in dic:
            dic[nums[i]]=nums[i]
        else:
            return True
    return False


# print(containsDuplicate(list))
# print(again(list))
# print(max(list))
# nums=[4,1,2,1,2]

def singleNumber(nums):
    dic = {}
    for i in nums:
        if i not in dic:
            dic[i]=1
        else:
            dic[i] += 1
    for i in dic:
        if dic[i] == 1:
            return i

# print(singleNumber(nums))
nums=[0,0,1]
def moveZeroes(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            for j in range(i, len(nums) - 1):
                x = nums[j + 1]
                nums[j + 1] = nums[j]
                nums[j] = x
    return nums

# print(moveZeroes(nums))
# def isValidSudoku(board):
#     for i in range(len(board)):
#         for j in range(len(board[0])-1):
#             for k in range(j+1,len(board[0])):
#                 if board[i][j]==board[i][k]
#                     return False
#     for i in range(len(board[0])):
#         for j in range(len(board)-1):
#             for k in range(j,len(board)):
#                 if board[j][i]==board[k][i]:
#                     return False
#     return True

def reverse(x):
    if x >= 0:
        y = True
    else:
        y = False
        x=(-x)
    count = 0
    num = x
    while num != 0:
        count = count + 1
        num = num // 10
    num = 0
    count = count - 1
    while x != 0:
        num = num + (10 ** count) * (x % 10)
        count = count - 1
        x = x // 10
    if not y:
        return -num
    else:
        return num
# print(reverse(-123))
# print(-1//10)


needle="ll"
haystack="hello"
def strStr(haystack, needle):
    n = len(needle)
    count=0
    for i in haystack:
        if i == needle[0]:
            for j in range(n):
                if str(needle[j])==str(haystack[j+i]):
                    count=count+1
            if count==n:
                return i
            count=0
    return -1
print(strStr(haystack,needle))
