from typing import List
class SequenceGenerator:
    @staticmethod
    def _is_prime(num: int) -> bool:
        if num <2:
            return False
        if num==2:
            return True
        if num%2==0:
            return False
        for i in range(3,int(num**0.5)+1,2):
            if num%i == 0:
                return False
        return True
    @classmethod
    def generate_primes(cls,length:int)->List[int]:
        if length <=0:
            raise ValueError("Sequence Length must be a positive integer")
        primes:List[int]=[]
        candidate=2
        while len(primes)<length:
            if cls._is_prime(candidate):
                primes.append(candidate)
            candidate+=1
        return primes
    
    @staticmethod
    def generate_fibonacci(length:int) -> List[int]:
        if length <=0:
            raise ValueError("Sequence length must  be a positive integer")
        seq: List[int]=[1,1]
        while len(seq)<length:
            seq.append(seq[-1]+seq[-2])
        return seq[:length]
    
    @staticmethod
    def generate_squares(length:int)->List[int]:
        if length<=0:
            raise ValueError("Sequence length must be a positive integer")
        return[i**2 for i in range(1,length+1)]
    
    @staticmethod
    def generate_triangular(length:int)->List[int]:
        if length <=0:
            raise ValueError("Sequence length must  be a postive integer")
        return[i*(i+1)//2 for i in range(1,length+1)]
                

        
