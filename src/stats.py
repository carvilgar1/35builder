class Stat:
    def __init__(self, base, misc=0, tpm=0):
        self._base_score = base
        self._total_score = base
        self.misc = misc
        self.tpm = tpm

    @property
    def base(self):
        return self._base_score

    @property
    def score(self):
        return self.base + self.misc + self.tpm

    @property
    def mod(self):
        return self._calculate_mod(self.score)

    def _calculate_mod(self, score):
        return score // 2 - 5

    def addMiscModifier(self, mod):
        self.misc += mod

    def addTmpModifier(self, mod):
        self.tpm += mod

    def __str__(self):
        return f"{self.score}({self.mod:+d})"
