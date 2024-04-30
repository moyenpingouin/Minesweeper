import numpy as np
from multiprocessing import Pool
import time

nbThread=8
nbCalculs=600

def func1(x:int)->int:
    """Fonction qui renvoi la somme des carrés de 0 à x**2"""
    #time.sleep(0.1)
    S=0
    for i in range(x**2):
        S=S+i*i
    return S

def func2(n, parallel=False):
    """Cacul le resultat de func1 pour des valeurs de 1 à n parallélement ou non"""
    my_array = np.zeros((n))

    # Parallelized version:
    if parallel:
        pool = Pool(processes=nbThread)
        ####### HERE COMES THE CHANGE ####### 
        results = [pool.apply_async(func1, [val]) for val in range(1, n+1)]
        for idx, val in enumerate(results):
            my_array[idx] = val.get()
        ####### 
        pool.close()
    # Not parallelized version:
    else:
        for i in range(1, n+1):
            my_array[i-1] = func1(i)

    return my_array

def main():
    start = time.time()
    my_array = func2(nbCalculs)
    end = time.time()

    print("Normal time: {}\n".format(end-start))

    start_parallel = time.time()
    my_array_parallelized = func2(nbCalculs, parallel=True)
    end_parallel = time.time()

    print("Time based on multiprocessing: {}".format(end_parallel-start_parallel))

if __name__ == '__main__':
    main()