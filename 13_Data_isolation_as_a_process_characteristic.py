import multiprocessing


my_list = []

def write_data():
    for i in range(5):
        my_list.append(i)
        print(f"写入数据：{i}")

    print(f"写入完成，当前列表：{my_list}")

def read_data():
    print(f"读取数据，当前列表：{my_list}")



print(f"我是main外资源，我执行了几遍")


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=write_data)
    p2 = multiprocessing.Process(target=read_data)

    p1.start()
    p1.join()  # 等待p1进程完成后再执行p2
    p2.start()
    p2.join()