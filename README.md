# hacking-scripts
ハッキングやセキュリティ関連のスクリプト

## ascii decoddr

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