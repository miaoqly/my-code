# File ：test_decorate.py
def huan(miao):
    def dada(*args,**kwargs):
        print("\n我在前面")
        miao(*args,**kwargs)
        print("我在后面")
    return dada

@huan
def fun():
    print("我在中间")

def test_demo():
    fun()