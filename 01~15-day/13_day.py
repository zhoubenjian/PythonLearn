'''
进程和线程
'''
from multiprocessing import Process
from random import randint
from threading import Thread
from time import time, sleep


def download_task(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成！耗时%d秒' % (filename, time_to_download))
    

# 单线程（顺序执行）
def main1():
    start = time()
    download_task('从入门到入土.pdf')
    download_task('Nozomi Kitano.avi')
    end = time()
    print('总共耗时%.2f' % (end - start))


# 多线程（交替执行）
def main2():
    start = time()
    p1 = Process(target=download_task, args=('Maeda Kaori.avi',))
    p1.start()
    p2 = Process(target=download_task, args=('Nozomi Kitano.avi',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('耗时%.2f' % (end - start))
    
    
class DownloadTask(Thread):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename
        
    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成！耗时%d秒！' % (self._filename, time_to_download))
        
        
def main3():
    start = time()
    t1 = DownloadTask('Nozomi Kitano.avi')
    t1.start()
    t2 = DownloadTask('Maeda Kaori.avi')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('共耗时%.2f秒' % (end - start))
    
    
if __name__ == '__main__':
    # main1()
    
    # main2()
    
    main3()
    