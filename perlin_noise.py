from noise import pnoise2
import numpy as np
from math import floor, ceil
import random

def perlin_array(shape = (1200, 600), amplitude = 1,
			scale = 30, octaves = random.randint(3, 5),
                        persistence = .35,
                        lacunarity= 2.5, 
			seed = None, norm = "standard"):

    
       

    if seed is None:
        seed = random.randint(0, 100)
    print(">>> seed was se{}_sc{}_o{}_p{}_L{}".format(seed, scale, octaves, round(persistence,2), round(lacunarity, 1)))

    arr = np.zeros(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            arr[i][j] = pnoise2(i / scale,
                                        j / scale,
                                        octaves=octaves,
                                        persistence=persistence,
                                        lacunarity=lacunarity,
                                        repeatx=1024,
                                        repeaty=1024,
                                        base=seed)

    max_arr = np.max(arr)
    min_arr = np.min(arr)

    if norm == "normalized":
        norm = lambda x: (x-min_arr)/(max_arr - min_arr)
        
    if norm == "standard":
        
        norm = lambda x: (x-min_arr)/(max_arr - min_arr)*(amplitude)
        

    if norm == "ziggurat":
        norm = lambda x: floor((x-min_arr)/(max_arr - min_arr)*amplitude) -0.1

    if norm == "flatland":
        norm = lambda x: floor((x-min_arr)/(max_arr - min_arr)*2*amplitude)/2 -0.1

    if norm == "binary":
        norm = lambda x: int((x-min_arr)/(max_arr - min_arr) +0.5)

    if norm == "ternary":
        norm = lambda x: int((x-min_arr)/(max_arr - min_arr)*3)

    if norm == "grade8":
        norm = lambda x: int((x-min_arr)/(max_arr - min_arr)*8)
    if norm == "grade20":
        norm = lambda x: int((x-min_arr)/(max_arr - min_arr)*20)

        

    norm = np.vectorize(norm)
    arr = norm(arr)
    return arr

if __name__ == "__main__":
    pass
    
