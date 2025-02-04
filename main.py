import multiprocessing


def cpu_stress():
    while True:
        pass


if __name__ == "__main__":
    # 시스템의 모든 CPU 코어 수 가져오기
    num_cores = multiprocessing.cpu_count()
    processes = []

    for _ in range(num_cores):
        p = multiprocessing.Process(target=cpu_stress)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
