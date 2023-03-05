import os
import datetime
import base64


def	run_cmd(cmd):
	print(cmd)
	os.system(cmd)

i = input("画像ファイルを選択:	")

path = (str(datetime.datetime.now()) + "_" + i).replace(".","-").replace(":","-").replace(" ", "_")

print()
cmd = "mkdir ./" + path
run_cmd(cmd)
cmd = "strings " + i + " > ./" + path + "/strings.txt"
run_cmd(cmd)
cmd = "exiftool " + i + " > ./" + path + "/exiftool.txt"
run_cmd(cmd)
print()

# if mode == 1, display all
def ch_flag(s1, s2, mode):
	if ("CTF" in str(s2)) or ("ctf" in str(s2)):
		print("\033[31m\033[1m", s1, "\t", s2, "\033[0m")
	else:
		if mode == 1:
			print("\033[1m", s1, "\033[0m\t", s2)

def	from_base64_exif(p):
	print("=== plain text and base64 decode on exif command ===")
	with open(p) as fi:
		n = 0
		for i in fi:
			tmp = i.split(": ")[1].replace("\n", "")
			ch_flag(p + ":" + str(n), tmp, 0)
			try:
				ch_flag(p + ":" + str(n) + " '" + tmp + "' -> ", base64.b64decode(tmp), 1)
			except:
				pass
			n = n + 1
	print()

def from_base64_string(p):
	print("=== plain text and base64 on strings command ===")
	with open(p) as fi:
		for i in fi:
			n = 0
			tmp = i.replace("\n", "")
			ch_flag(p + ":" + str(n), tmp, 0)
			try:
				ch_flag(p + ":" + str(n) + " '" + tmp + "' -> ", base64.b64decode(tmp), 0)
			except:
				pass
			n = n + 1
	print()

from_base64_string("./" + path + "/strings.txt")
from_base64_exif("./" + path + "/exiftool.txt")
