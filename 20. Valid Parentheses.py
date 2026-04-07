class Solution:
    def isValid(self, s: str) -> bool:
        stek = []
        sl = {"}":"{", "]":"[", ")":"("}
        for i in s:
            if i in "]})":
                if len(stek)>0 and sl[i]!= stek[-1]:
                    return False
                else:
                    if len(stek)>0:
                        del stek[-1]
                    else:
                        return False
            else:
                stek.append(i)
        return len(stek)==0
        