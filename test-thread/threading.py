import _thread
import logging
import threading
from time import sleep, ctime
# 日志输出等级设置为info，info级别日志就可以打印和输出
logging.basicConfig(level=logging.INFO)

loops = [2,4]
class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        # 主动调用init
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name
    # 重写run方法
    def run(self):
        self.func(*self.args)
def loop(nloop,nsec):
    # nloop是数值，需要强制转换成字符串再进行拼接
    logging.info("start loop " + str(nloop) + " at " + ctime())
    sleep(nsec)
    logging.info("end loop " + str(nloop) + " at " + ctime())

def main():
    logging.info("start all at " + ctime())
    # threading虽然设置了Thread但不会立马执行，需要用list把所有线程包起来
    threads = []
    # 几个loop取决于上方设置的loops有几个值，即长度len
    nloops = range(len(loops))
    for i in nloops:
        # 用自己的方法调用，参数为函数名，参数，函数名
        t = MyThread(loop, (i, loops[i]),loop.__name__)
        # 追加线程
        threads.append(t)
    # 依次取出线程判断锁是否被锁,解锁后跳出死循环
    for i in nloops:
        # 调用start方法才会执行loop函数
        threads[i].start()
    # 虽然不用锁了，但是要加入join方法，它会等loop0结束才会结束阻塞
    for i in nloops:
        threads[i].join()
    logging.info("end all at " + ctime())
# 如果运行的函数名字是main，就执行main方法
if __name__ == '__main__':
    main()




