# 10進数への変換を行い、ASCIIに変換もする

import sys

def put_arr(arr):
	for i in arr:
		print(i, end="")
	print()

base	= input("元の進数	:	")
arr	= input("数の配列	:	")
split	= input("区切り文字	:	")

arr = arr.replace(" ", "")
arr = arr.split(split)

tmp = []
for i in arr:
	try:
		tmp.append(int(i, int(base)))
	except:
		tmp.append("?")

print()
print(tmp)

ascii_tmp = []
for i in tmp:
	if i == "?":
		ascii_tmp.append("<CAN NOT DECODE>")
	ascii_tmp.append(chr(int(i)))

print(ascii_tmp)
put_arr(ascii_tmp)
