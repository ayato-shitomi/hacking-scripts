import hashlib

tmp = input("変換したい文字列を入力してください:	")

def p(s):
	print()
	print('\033[31m' + s + '\033[0m')
	print("\tmd5 hash:\t", hashlib.md5(s.encode()).hexdigest())
	print("\tsha256:\t\t", hashlib.sha256(s.encode()).hexdigest())

p(tmp)
p(tmp.upper())
p(tmp.lower())
p(tmp.title())
