def isAnagramString_dict(self, s: str, t: str) -> bool:
    # runtime O(s+t)
    if len(s)!=len(t):
            return False
        
        count={}
        
        for c in s:
            if c not in count:
                count[c]=1
            else:
                count[c]+=1
        
        for c in t:
            if c not in count:
                return False
            elif count[c]==1:
                del count[c]
            else:
                count[c]-=1
        
        return len(count)==0

def isAnagramString_list(self, s: str, t: str) -> bool:
    # runtime O(s+t+26)
    if len(s)!=len(t):
            return False
        
        count=[0]*26
        
        for c in s:
            count[ord(c)-97]+=1
        for c in t:
            count[ord(c)-97]-=1
        
        for i in count:
            if i!=0:
                return False
        
        return True


