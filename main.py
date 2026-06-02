import sys
from typing import Dict,List
from sequencegenerator import SequenceGenerator
from signalencoder import SignalEncoder
from noisesimulator import NoiseSimulator
from patternanalyzer import PatternAnalyzer
from researchreport import ResearchReport

def _input_valid_choice(prompt: str , options:List[str]) ->str:
    while True:
        
            val= input(prompt).strip().lower()
            if val in options:
                return val
            print(f"Invalid choice. Please choose from:{', ' .join(options)}.")

def _input_int(prompt:str,low:int,high:int)->int:
    while True:
        try:
            user_text = input(prompt).strip()
            val=int(user_text)
            if low <= val <=high:
                return val
            print(f"Please enter a whole number between{low}and {high}.")
        except ValueError:
            print("Invalid input.Please enter a whole number.")


def _run_trial(seq_type:str , length:int,noise_pct:float)->Dict[str,float]:
    if seq_type=="prime":
        original = SequenceGenerator.generate_primes(length)
    elif seq_type =="fibonacci":
        original = SequenceGenerator.generate_fibonacci(length)
    elif seq_type =="squares":
            original = SequenceGenerator.generate_squares(length)
    elif seq_type=="triangular":
        original = SequenceGenerator.generate_triangular(length)
    else:
        raise ValueError("Unsupported sequence type")

    encoded_list,full_encoded=SignalEncoder.encode_sequence(original)
    noise_sim= NoiseSimulator(noise_pct/100.0)
    corrupted_list=noise_sim.apply_noise(encoded_list)
    full_corrupted="".join(corrupted_list)
    decoded=SignalEncoder.decode_sequence(corrupted_list,length)
    metrics=PatternAnalyzer.analyze(original,decoded,encoded_list,corrupted_list)

    ResearchReport.print_trial(
        seq_type.capitalize(),length,noise_pct/100.0,metrics,original,full_encoded,full_corrupted,decoded
    )
    return metrics

def main() -> None:
    ResearchReport.print_header()
    print("\n[PARAMETERS]")
    seq_type=_input_valid_choice("Sequence type (prime/fibonacci/squares/triangular):",["prime","fibonacci","squares","triangular"])
    length=_input_int("Sequence length(5-50):",5,50)
    noise_pct=_input_int("Noise level(0/5/10/20/30):",0,30)
    trials=_input_int("Trials per type(1-3):",1,3)
    print("\n[EXECUTING SIMULATIONS]")
    comparative={}
    types=["prime","fibonacci","squares","triangular"]
    for st in types:
        print(f"\n>>Evaluating{st.upper()}...")
        metrics_list=[]
        for t in range(trials):
            print(f" Trial{t+1}/{trials}")
            metrics_list.append(_run_trial(st,length,noise_pct))
        
        avg={k:sum(m[k] for m in metrics_list)/len(metrics_list) for k in metrics_list[0]}
        comparative[st.capitalize()]=avg
    ResearchReport.generate_comparative_report(comparative)
    print("\n[Mathematical Verification Complete]")
    print("Ready for peer review or deep space transmission modeling")
if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSimulation halted.")
        sys.exit(0)
    except Exception as e:
        print(f"\nError:{e}")
        sys.exit(1)