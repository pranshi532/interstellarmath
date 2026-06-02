from typing import List,Tuple
class SignalEncoder:
    @staticmethod
    def _int_to_binary(num:int)->str:
        if num<0:
            raise ValueError("Negative values unsupported for interstellar binary mapping")
        if num==0:
            return "0"
        bits: List[str]=[]
        while num>0:
            bits.append(str(num%2))
            num//2
        return "".join(reversed(bits))
    @classmethod
    def encode_sequence(cls,sequence:List[int])->Tuple[List[str],str]:
        encoded_words:List[str]=[]
        for val in sequence:
            base_bin = clas._int_to_binary(val)
            parity_bit=sum(int(b) for b in base_bin)%2
            encoded_words.append(base_bin+str(parity_bit))
        full_signal="".join(encoded_words)
        return encoded_words,full_signal
    @staticmethod
    def decode_sequence(corrupted_words: List[str],expected_length:int)->List[int]:
        decoded:List[int]=[]
        for word in corrupted_words[:expected_length]:
            if len(word)<1:
                decoded.append(0)
                continue
            payload = word[:-1]
            val=0
            for bit in payload:
                val=(val<<1)|int(bit)
            decoded.append(val)
        return decoded