import time
import multiprocessing

def work():
    for i in range(10):
        print(f"正在工作... {i}")
        time.sleep(0.5)

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=work, name='WorkerProcess')
    p1.start()
    
    time.sleep(1)  # 主进程等待一段时间，确保子进程已经开始工作
    print("main进程结束了，但子进程还在工作...")