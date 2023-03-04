input_file = input("TXT形式にエクスポートしたファイル:	")

mode = "a"
chlis = ["y", "n", "Y", "N"]
while mode not in chlis:
	mode = input("POSTFAILを表示するか y/n:	")

newmap = {
2: "PostFail",
4: "a",
5: "b",
6: "c",
7: "d",
8: "e",
9: "f",
10: "g",
11: "h",
12: "i",
13: "j",
14: "k",
15: "l",
16: "m",
17: "n",
18: "o",
19: "p",
20: "q",
21: "r",
22: "s",
23: "t",
24: "u",
25: "v",
26: "w",
27: "x",
28: "y",
29: "z",
30: "1",
31: "2",
32: "3",
33: "4",
34: "5",
35: "6",
36: "7",
37: "8",
38: "9",
39: "0",
40: "Enter",
41: "esc",
42: "del",
43: "tab",
44: "space",
45: "-",
47: "[",
48: "]",
56: "/",
57: "CapsLock",
79: "RightArrow",
80: "LetfArrow"
}

ch = ""

def put(l):
	rtn = ""
	bytesArray = bytearray.fromhex(l.strip())
	#print "l Number: " + str(i)
	for byte in bytesArray:
		if byte != 0:
			keyVal = int(byte)
			if keyVal in newmap:
				if mode == "n" and keyVal == 2:
					print("Value map : " + str(keyVal) + "-> " + newmap[keyVal])
				else:
					print("Value map : " + str(keyVal) + "-> " + newmap[keyVal])
					rtn = newmap[keyVal]
			else:
				print("No map found for this value: " + str(keyVal))
				rtn = "*"
	return rtn


with open(input_file) as f:
	for line in f:
		if line.split(":")[0] == "Leftover Capture Data":
			#print(line.split(":")[1].replace("\n", "").replace(" ", ""))
			ch += put(line.split(":")[1].replace("\n", "").replace(" ", ""))
print(ch)
