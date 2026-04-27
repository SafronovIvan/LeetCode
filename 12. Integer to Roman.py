class Solution:
    def intToRoman(self, num: int) -> str:
        st = str(num)
        ans = ""
        if len(st)>0 and num >= 1000:
            ans += "M"*int(st[0])
            st = st[1:]
        if len(st)>0 and int(st) >= 900:
            ans += "CM"
            st = st[1:]
        elif len(st)>0 and int(st) >= 500:
            ans += "D"
            ans += "C"*(int(st[0])-5)
            st = st[1:]
        elif len(st)>0 and int(st) >= 400:
            ans += "CD"
            st = st[1:]
        elif len(st)>0 and int(st) >= 100:
            ans += "C"*(int(st[0]))
            st = st[1:]
        if len(st)>0 and st[0] == "0":
            st = st[1:]
        if len(st)>0 and int(st) >= 90:
            ans += "XC"
            st = st[1:]
        elif len(st)>0 and int(st) >= 50:
            ans += "L"
            ans += "X"*(int(st[0])-5)
            st = st[1:]
        elif len(st)>0 and int(st) >= 40:
            ans += "XL"
            st = st[1:]
        elif len(st)>0 and int(st) >= 10:
            ans += "X"*(int(st[0]))
            st = st[1:]
        if len(st)>0 and st[0] == "0":
            st = st[1:]
        if len(st)>0 and int(st) >= 9:
            ans += "IX"
            st = st[1:]
        elif len(st)>0 and int(st) >= 5:
            ans += "V"
            ans += "I"*(int(st[0])-5)
            st = st[1:]
        elif len(st)>0 and int(st) >= 4:
            ans += "IV"
            st = st[1:]
        elif len(st)>0 and int(st)>=1:
            ans += "I"*(int(st[0]))
            st = st[1:]
        return(ans)
            

        



        