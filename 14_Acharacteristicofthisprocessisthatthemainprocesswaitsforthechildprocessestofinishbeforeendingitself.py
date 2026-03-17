import time
import multiprocessing

def work():
    for i in range(10):
        print(f"正在工作... {i}")
        time.sleep(0.5)

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=work, name='WorkerProcess')
    p1.daemon = True   # 设置p1为守护进程

    p1.start()
    
    time.sleep(1)  # 主进程等待一段时间，确保子进程已经开始工作
    print("主进程原本准备结束，但由于使用了 join()，现在会等待子进程执行完毕...")

    p1.join()  # 阻塞主进程，直到 p1 执行完毕
    