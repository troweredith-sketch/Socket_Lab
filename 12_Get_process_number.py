import multiprocessing
import time
import os

def coding(name, num):
    for i in range(1, num + 1):
        print(f"{name} 正在敲第 {i} 行代码...")
        time.sleep(0.5)
    print(f"p1的进程号是：{os.getpid()}, {multiprocessing.current_process().pid},, 父进程号是：{os.getppid()}")

def music(name, num):
    for i in range(1, num + 1):
        print(f"{name} 正在听第 {i} 首歌......")
        time.sleep(0.5)
    print(f"p2的进程号是：{os.getpid()}, {multiprocessing.current_process().pid},  父进程号是：{os.getppid()}")


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=coding, args=("张三", 10))
    p2 = multiprocessing.Process(target=music, kwargs={"num": 10, "name": "李四"})

    p1.start()
    p2.start()

    print(f"main的进程号是：{os.getpid()}, {multiprocessing.current_process().pid},, 父进程号是：{os.getppid()}")