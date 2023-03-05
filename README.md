# hacking-scripts
ハッキングやセキュリティ関連のスクリプト

## ascii_decoddr

任意の進数から10進数への変換を行い、ASCIIへの変換もする

```
元の進数        :       16
数の配列        :       0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f 
区切り文字      :       ,

[85, 110, 67, 104, 95, 48, 102, 95]
['U', 'n', 'C', 'h', '_', '0', 'f', '_']
UnCh_0f_
```

## usb_input_pcap_to_string

WiresharkのUSBの入力キャプチャをStringに変換する。
実行した際に`PostFail`が表示されることがある。
これは環境依存なので注意すること。（例えばSHIFTキーに割当たってるなど）

```
TXT形式にエクスポートしたファイル:      a.txt
POSTFAILを表示するか y/n:       n
Value map : 33-> 4
Value map : 31-> 2
Value map : 6-> c
Value map : 23-> t
＜中略＞
Value map : 34-> 5
Value map : 4-> a
Value map : 17-> n
Value map : 32-> 3
Value map : 2-> PostFail
Value map : 2-> PostFail
Value map : 48-> ]
Value map : 2-> PostFail
42ctf[XXX]
```

## easy_letter_changer

簡単な文字チェンジャー、大文字にしたり小文字にしたりする。さらに、それぞれのMD5とSHA256を求める。

```
換したい文字列を入力してください:     42CTF{you're_ready_for_the_real_world}

42CTF{you're_ready_for_the_real_world}
        md5 hash:        d5fc4dac1f976732a02e42f47f6b5be1
        sha256:          2c7eb90ca60a6cfb5830ddf0d2685c87a6a89aa55d258d0eab0fe2b9cdf3130b

42CTF{YOU'RE_READY_FOR_THE_REAL_WORLD}
        md5 hash:        318bad1566e6fa84e2590194f0042d37
        sha256:          1fd1ff1e14363528ac6beeeafc9aa79460246780214395082fb185a67a580b2a

42ctf{you're_ready_for_the_real_world}
        md5 hash:        45c0521242a6a744751257a007605eec
        sha256:          306d2d6a6d68b7e7cc37e3c7c67b75f1381baee93b77e6872413b21049b1461f

42Ctf{You'Re_Ready_For_The_Real_World}
        md5 hash:        5f376ab0c9a3a3f7ccb6530fe70b5bf0
        sha256:          4b59e9ecbd67ce5a4cb99c59c1b887289171cad11b90102f4345e0f9196df027
```

## basic_picture_forensic

簡易的に画像ファイルなどからstringsとexif情報を取得してBase64でデコードする。文字検索が行われるのでみやすい。

```
画像ファイルを選択: cat.jpg
mkdir ./2023-03-04_23-46-00-996052_cat-jpg
strings cat.jpg >> ./2023-03-04_23-46-00-996052_cat-jpg/strings.txt
exiftool cat.jpg >> ./2023-03-04_23-46-00-996052_cat-jpg/exiftool.txt

=== plain text and base64 on strings command ===
 ./2023-03-04_23-06-01-592408_cat-jpg/strings.txt:0      PicoCTF 
 ./2023-03-04_23-06-01-592408_cat-jpg/strings.txt:0          <rdf:li xml:lang='x-default'>PicoCTF</rdf:li> 

=== plain text and base64 decode on exif command ===
 ./2023-03-04_23-06-01-592408_cat-jpg/exiftool.txt:0 '12.54' ->          b'\xd7nx'
 ./2023-03-04_23-06-01-592408_cat-jpg/exiftool.txt:2 '.' ->      b''
 ./2023-03-04_23-06-01-592408_cat-jpg/exiftool.txt:7 '-rw-r--r--' ->     b'\xaf\n\xeb'
 ./2023-03-04_23-06-01-592408_cat-jpg/exiftool.txt:8 'JPEG' ->           b'$\xf1\x06'
 ./2023-03-04_23-06-01-592408_cat-jpg/exiftool.txt:12 'None' ->          b'6\x89\xde'
 ./2023-03-04_23-06-01-592408_cat-jpg/exiftool.txt:15 '7a78f3d9cfb1ce42ab5a3aa30573d617' ->      b'\xed\xae\xfc\x7fw}q\xf6\xf5q\xee6i\xbeZ\xdd\xa6\xb7\xd3\x9e\xf7w\xad{'
 ./2023-03-04_23-06-01-592408_cat-jpg/exiftool.txt:16    PicoCTF 
 ./2023-03-04_23-06-01-592408_cat-jpg/exiftool.txt:19 'cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9' ->          b'picoCTF{the_m3tadata_1s_modified}' 
 ./2023-03-04_23-06-01-592408_cat-jpg/exiftool.txt:20    PicoCTF 
 ./2023-03-04_23-06-01-592408_cat-jpg/exiftool.txt:21 '2560' ->          b'\xdb\x9e\xb4'
 ./2023-03-04_23-06-01-592408_cat-jpg/exiftool.txt:22 '1598' ->          b'\xd7\x9f|'
 ./2023-03-04_23-06-01-592408_cat-jpg/exiftool.txt:23 'Baseline DCT, Huffman coding' ->          b'\x05\xab\x1e\x96)\xde\x0c$\xc7\xb9\xf7\xe6jw(v)\xe0'
```