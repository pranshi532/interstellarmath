import random
from typing import List
class NoiseSimulator:
    def __init__(self,noise_level:float):
        if not (0.0<=noise_level<=1.0):
            raise ValueError("Noise level must be between [0.0 and 1.0]")
        self.noise_level=noise_level
    
    def apply_noise(self,bitstrings:List[str])->List[str]:
        corrupted:List[str]=[]
        for word in bitstrings:
            flipped_word=[]
            for bit in word:
                if random.random()<self.noise_level:
                    flipped_word.append('1' if bit =='0' else'0')
                else:
                    flipped_word.append(bit)
            corrupted.append("".join(flipped_word))
        return corrupted