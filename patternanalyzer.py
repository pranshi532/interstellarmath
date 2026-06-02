from typing import List,Dict
class PatternAnalyzer:
    @staticmethod
    def _bit_error_rate(original_bits:List[str],corrupted_bits:List[str])->float:
        total_bits=0
        flipped=0
        for orig, corr in zip(original_bits, corrupted_bits):
            for o,c in zip(orig,corr):
                total_bits+=1
                if o!=c:
                    flipped +=1
        return flipped / max(total_bits,1)
    @staticmethod
    def _pattern_preservation_score(original:List[int],received:List[int])->float:
        if len(original)<2 or len(recieved)<2:
            return 0.0
        orig_diffs = [ original[i+1]-original[i] for i in range(len(original)-1)]
        recv_diffs = [recieved[i+1]-recieved[i] for i  in range(len(recieved)-1)]
        min_len = min(len(orig_diffs),len(recv_diffs))
        orig_diffs=orig_diffs[:min_len]
        recv_diffs=recv_diffs[:min_len]

        diff_deviation = sum(abs(r-o) for o , r in zip(orig_diffs,recv_diffs))
        mean_dev=diff_deviation / min_len
        mean_orig_mag=sum(abs(d) for d in orig_diffs)/min_len
        return max(0.0,1.0-(mean_dev/mean_orig_mag+1e-9))
    
    @classmethod
    def analyze(cls,original:List[int],recieved:List[int],
                orig_bits:List[str],corr_bits:List[str])->Dict[str,float]:
        er=cls._bit_error_rate(orig_bits,corr_bits)
        pps=cls._pattern_preservation_score(original,recieved)
        sis=sum(1 for o , r  in zip(original,recieved)if o ==r)/max(len(original),1)
        rp= min(1.0, sis*(0.5+0.5*pps))
        return{
            "error_rate":round(er,4),
            "pattern_preservation":round(pps,4),
            "sequence_integrity":round(sis,4),
            "recognition_probability":round(rp,4)
            
        }