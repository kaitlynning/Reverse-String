def reverse(msg):
    return msg[::-1]

num = (input('num = '))
reversed_num = reverse(num)
print(reversed_num)

#or 先呼叫reversed進行反轉，會得到含有單一字元的串列（list），再以字串的join結合
reversed_num = ''.join(list(reverse(num)))
print(reversed_num)
'''
num = 123456789 hannah haha
ahah hannah 987654321
ahah hannah 987654321
'''