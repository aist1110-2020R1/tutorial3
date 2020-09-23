#ex1

# text = "\A[a-z0-9!#$%&'*+/=?^_‘{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_‘{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\z"
# text = text.replace('\\', '\\') # actually not necessary as "" bracket already sanitizes the text
# print(text)

#ex2

# w, h = map(int, input().split()) # expect valid input
# for i in range(h):
#     range_list = [0, w-1] + list(range(1, w-1))*(1 - (i % (h-1)))
#     for j in range(w):
#         if j in range_list: print('*', end = '')
#         else: print(' ', end = '')
#     print()

#ex3

# def happy(num):
#     original = int(''.join(map(str, num)))
#     x = lambda y: y ** 2
#     repeated = []
#     while True:
#         num = list(map(x, num))
#         cou = sum(num)
#         if cou == 1: return True
#         elif cou in repeated: return False
#         repeated.append(cou)
#         num = list(map(int, list(str(cou))))
#
# num = list(map(int, list(input())))
# print(happy(num))

#ex4

# def cont_dupl(nums):
#     snums = sorted(nums)
#     for k, i in enumerate(snums):
#         if k == 0: continue
#         if i == snums[k-1]: return True
#     return False
#
# lis_by_inp = list(map(int, input().split())) # input the list in the format 'x1 x2 x3' etc
# lis_by_df = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2] # input the list by defining it
# print(cont_dupl(lis_by_inp)) # or lis_by_df
