def my_levenshtein(s1:str,s2:str)->int:
    comp=0
    if len(s1)!=len(s2):
        return -1
    if s1==s2=="":
        return 0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            comp+=1
        return comp
