"""Burrows-Wheeler Transform (BWT) & Move-To-Front (MTF) Transform.
100% Python Standard Library.
"""

class BWTCoder:
    """BWT block sorter and MTF symbol locality transformer."""
    STX = "\x02"
    ETX = "\x03"

    @classmethod
    def bwt_transform(cls, s: str) -> str:
        s = cls.STX + s + cls.ETX
        n = len(s)
        table = sorted(s[i:] + s[:i] for i in range(n))
        return "".join(row[-1] for row in table)

    @classmethod
    def bwt_inverse(cls, r: str) -> str:
        n = len(r)
        table = [""] * n
        for _ in range(n):
            table = sorted(r[i] + table[i] for i in range(n))
        for row in table:
            if row.startswith(cls.STX) and row.endswith(cls.ETX):
                return row[1:-1]
        return ""

    @staticmethod
    def mtf_encode(s: str) -> list:
        alphabet = [chr(i) for i in range(256)]
        out = []
        for ch in s:
            idx = alphabet.index(ch)
            out.append(idx)
            alphabet.pop(idx)
            alphabet.insert(0, ch)
        return out
