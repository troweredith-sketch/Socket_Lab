import threading
import time

def coding(name, num):
    for i in range(1, num + 1):
        print(f"{name} 正在敲第 {i} 遍代码...")
        time.sleep(0.5)

def music(name, num):
    for i in range(1, num + 1):
        print(f"{name} 正在听第 {i} 遍音乐...")
        time.sleep(0.5)


if __name__ == "__main__":
    t1 = threading.Thread(target=coding, args=("张三", 10))
    t2 = threading.Thread(target=music, kwargs={"num": 10, "name": "李四"})

    t1.start()
    t2.start()