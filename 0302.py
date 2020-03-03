def reverse(msg):
    return msg[::-1]
#0301int cannot reverse; needa be str
num = int(input('num = '))
num_in_str = str(num)
reversed_num = reverse(num_in_str)
print(reversed_num)
#or 先呼叫reversed進行反轉，會得到含有單一字元的串列（list），再以字串的join結合
reversed_num = ''.join(list(reversed(num_in_str)))
print(reversed_num)

'''
num = 12345678
87654321
87654321
'''