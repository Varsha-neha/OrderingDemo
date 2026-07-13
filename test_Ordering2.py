import pytest

class TestOrderMethod2:
    @pytest.mark.run(order=2)
    def testB(self):
        print("this is B")

    @pytest.mark.run(order=4)
    def testD(self):
        print("this is D")

    @pytest.mark.run(order=1)
    def testA(self):
        print("this is A")

    @pytest.mark.run(order=3)
    def testC(self):
        print("this is C")