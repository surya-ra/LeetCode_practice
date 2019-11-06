class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace('-', '').upper()
        size = len(S)
        prefix = size % K
        ans = [S[i: i+K] for i in range(prefix, (size // K) * K + prefix, K)]

        if prefix == 0:
            ans = '-'.join(ans)
        else:
            ans = '-'.join([S[:prefix]] + ans)

        print(ans)

a = Solution()
a.licenseKeyFormatting('ab-cb-efg-hk', 4)