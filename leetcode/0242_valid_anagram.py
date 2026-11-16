class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict={}
        tdict={}
        for sh in s:
            if sh not in sdict:
                sdict[sh]=1 
            else:
                sdict[sh]+=1
        for th in t:
            if th not in tdict:
                tdict[th]=1 
            else:
                tdict[th]+=1
        if sdict==tdict:
            return True
        else:
            return False