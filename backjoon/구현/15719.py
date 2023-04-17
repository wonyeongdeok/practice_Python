'''1. 메모리 초과'''

# n = int(input())
# nums = list(map(int, input().split()))
# nums.sort()
#
# for i in range(1, n):
#     if nums[i] == nums[i-1]:
#         print(nums[i])
#
'''2. 시간초과'''
# n = int(input())
# nums = input()
#
# total_sum = 0
# tmp_num = ''
# for i, num in enumerate(nums):
#     if i == 0:
#         tmp_num += num
#     else:
#         if num == ' ':
#             total_sum += int(tmp_num)
#             tmp_num = ''
#         else:
#             tmp_num += num
# else:
#     total_sum += int(tmp_num)
#
# n_list = [i for i in range(1, n)]
# n_sum = sum(n_list)
#
# print(total_sum - n_sum)


'''3. 시간초과'''
# import sys
#
# n = int(input())
# nums = sys.stdin.read()
#
# total_sum = 0
# tmp_num = ''
# for num in nums:
#     if num.isdigit():
#         tmp_num += num
#     else:
#         total_sum += int(tmp_num)
#         tmp_num = ''
# total_sum += int(tmp_num)
#
# n_sum = n * (n - 1) // 2
#
# print(total_sum - n_sum)


'''4. 메모리 초과'''
# import sys
# from collections import Counter
# n = int(input())
# # nums = input()
# # n = 10
# # nums = '1 2 2 5 6 4 3 7 8 9'
# nums = sys.stdin.read()
# dict = {}
# total_sum = 0
# tmp_num = ''
# for num in nums:
#     if num.isdigit():
#         tmp_num += num
#     else:
#         if not tmp_num in dict.keys():
#             dict[tmp_num] = 0
#             dict[tmp_num] += 1
#             tmp_num = ''
#         else:
#             dict[tmp_num] += 1
#             tmp_num = ''
# dict[tmp_num] = 0
# dict[tmp_num] += 1
#
# for k, v in dict.items():
#     if v == 2:
#         print(k)



import sys
n = int(input())
nums = sys.stdin.read()
total_sum = 0

tmp_num = ''

for num in nums:
    if num.isdigit():
        tmp_num += num
    elif num == ' ':
        total_sum += int(tmp_num)
        tmp_num = ''

total_sum += int(tmp_num)

n_sum = n * (n - 1) // 2
print(total_sum - n_sum)
