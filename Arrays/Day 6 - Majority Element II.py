class Solution:
    def findMajority(self, arr):
        n = len(arr)
        ele1, ele2 = -1, -1
        cnt1, cnt2 = 0, 0

        for ele in arr:
            if ele == ele1:
                cnt1 += 1
            elif ele == ele2:
                cnt2 += 1
            elif cnt1 == 0:
                ele1 = ele
                cnt1 = 1
            elif cnt2 == 0:
                ele2 = ele
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1, cnt2 = 0, 0
        for ele in arr:
            if ele == ele1:
                cnt1 += 1
            elif ele == ele2:
                cnt2 += 1

        res = []
        if cnt1 > n / 3:
            res.append(ele1)
        if cnt2 > n / 3:
            res.append(ele2)

        res.sort()
        return res