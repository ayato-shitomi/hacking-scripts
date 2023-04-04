
enc = input("encrypt message : ")
law = input("law message     : ")

try:
    assert len(enc) == len(law)
    list(zip(enc, law))
    [ord(e)-ord(p) for e,p in zip(enc, law)]
    [(ord(e)-ord(p))%26 for e,p in zip(enc, law)]
    [(ord(e)-ord(p))%26 + ord('a') for e,p in zip(enc, law)]
    print()
    print([chr((ord(e)-ord(p))%26 + ord('a')) for e,p in zip(enc, law)])
except:
    print("Error")