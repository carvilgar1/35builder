class Stat:
    def __init__(self, base, misc = 0, tpm = 0):
        self._base_score = base
        self._base
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
        return self._calculate_mod()

    def _calculate_mod(self, score):
        return score // 2 - 5
    
    def addMiscModifier(self, mod):
        self.misc += mod
    
    def addTmpModifier(self, mod):
        self.tpm += mod
    
    def __str__(self):
        return f"{self.score}({self.mod:+d})"



st = Stat(18)
assert st.mod == 4
st.addMiscModifier(1)
assert st.score == 19
assert st.mod == 4
# start fury
st.addTmpModifier(4)
# getPoisoned
st.addTmpModifier(-2)
assert st.score == 21
assert st.mod == 5
st.addTmpModifier(-2)
assert st.score == 19
assert st.mod == 4
# fury ends
st.addTmpModifier(-4)
assert st.score == 15
assert st.mod == 2
assert st.misc == 1
assert st.tpm == -4