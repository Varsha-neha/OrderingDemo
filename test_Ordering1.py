import pytest

class TestOrderDemo:
    @pytest.mark.second #customized markers
    def testB(self):
        print("this is B")

    @pytest.mark.forth
    def testD(self):
        print("this is D")

    @pytest.mark.first
    def testA(self):
        print("this is A")

    @pytest.mark.third
    def testC(self):
        print("this is C")