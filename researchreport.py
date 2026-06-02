from typing import Dict,List
class ResearchReport:
    @staticmethod
    def print_header()->None:
        print("="*50)
        print("Interstellar Communication analysis")
        print("="*50)
    @staticmethod
    def print_trial(seq_type:str,length:int,noise_pct:float,metrics:Dict[str,float],original:List[int],encoded:str,corrupted:str,decoded:List[int])->None:
        print(f"\nSequence Type:{seq_type}")
        print(f"Length:{length}")
        print(f"Noise Level:{noise_pct*100:.0f}%")
        print("-"*40)
        print(f"Pattern Preservation Score: {metrics['pattern_preservation']*100:.1f}%")
        print(f"Recognition Probability: {metrics['recognition_probability']*100:.1f}%")
        print(f"Sequence Integrity Score: {metrics['sequence_integrity']*100:.1f}%")
        print(f"Bit Error Rate: {metrics['error_rate']*100:.1f}%")
        print("-"*40)
        print(f"Original : {str(original[:8])}{'...'if len(original)>8 else ''}")
        print(f"Decoded: {str(decoded[:8])}{'...' if len(decoded)>8 else ''}")
    
    @classmethod
    def generate_comparative_report(cls,results:Dict[str,Dict[str,float]]) ->None:
        print("\n"+"="*50)
        print("COMPARATIVE MATHEMATICAL ANALYSIS")
        print("="*50)
        print(f"{'Sequence':<15}|{'recognition_probability':<15}|{'sequence_integerity':<15}")
        print("-"*50)
        for seq, metrics in results.items():
            recog = metrics['recognition_probability']*100
            integ=metrics['sequence_integrity']*100
            print(f"{seq:<15}|{recog:<14.2f}%|{integ:<14.2f}%")
        ranked = sorted(results.items(),key=lambda x:x[1]['recognition_probability'],reverse=True)
        print("\nConclusion:")
        top_seq,top_m=ranked[0]
        print(f" '{top_seq}' sequences demonstrated the highest resilience")
        print(f"under simulated transmission noise with a recognition")
        print(f"probability of {top_m['recognition_probability']*100:.1f}%.")