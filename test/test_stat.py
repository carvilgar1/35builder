from src.stats import Stat


def test_stat_modifiers_sequence():
    st = Stat(18)
    assert st.mod == 4
    st.addMiscModifier(1)
    assert st.score == 19
    assert st.mod == 4
    st.addTmpModifier(4)
    st.addTmpModifier(-2)
    assert st.score == 21
    assert st.mod == 5
    st.addTmpModifier(-2)
    assert st.score == 19
    assert st.mod == 4
    st.addTmpModifier(-4)
    assert st.score == 15
    assert st.mod == 2
    assert st.misc == 1
    assert st.tpm == -4
