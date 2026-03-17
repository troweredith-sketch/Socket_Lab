import multiprocessing
import time

def coding():
    for i in range(1, 11):
        
        print(f"正在敲第 {i} 遍代码！")
        time.sleep(0.5)
        


def music():
    for i in range(1, 11):
        
        print(f"正在听第 {i} 遍音乐！")
        time.sleep(0.5)
        

if __name__ == '__main__':

    p1 = multiprocessing.Process(target=coding)
    p2 = multiprocessing.Process(target=music)

    p1.start()
    p2.start()