#hashlist by using the dictonary 
s="azyxyyzaaaajbjfdhdfvdfvvbcxvxchjxfastyuyasdfrjgrhvdnvjrvjvkdhfhjadcfklsdjfmsdvfbsdjkfklasdfjsvxhasioawxd"
q=["d","a","y","x","k"]
hash_list=[0]*26
for ch in s:
    asci_value=ord(ch)
    index=asci_value-97
    hash_list[index]+=1
for ch in q:
    asci_value=ord(ch)
    index=asci_value-97
    print(ch,"=",hash_list[index])