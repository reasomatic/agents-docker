# this file will be overriden (via COPY in the Dockerfile) if the user creates a "processor.py" in their HF space

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import datetime

##################

def prepare_llama_cpp_model(model_path):
    from llama_cpp import Llama

    print(f'defining the model (at {datetime.datetime.now()})...')
    # Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
    llm = Llama(
        model_path=model_path,  # Download the model file first
        n_ctx=512,#2048,  # The max sequence length to use - note that longer sequence lengths require much more resources
        #n_threads=2,            # The number of CPU threads to use, tailor to your system and the resulting performance
        n_gpu_layers=0         # The number of layers to offload to GPU, if you have GPU acceleration available
    )
    print(f'done with defining the model (at {datetime.datetime.now()})...')


model_path = "./phi-2.Q4_K_M.gguf" ## remember to download this in the Dockerfile
prepare_llama_cpp_model(model_path)


##################

def process_input_llama_cpp(input_str: str):
    # Phi-2-GGUF
    # Simple inference example
    prompt = f"Instruct: {input_str}\nOutput:"
    output = llm(
        prompt, # Prompt
        max_tokens=512,  # Generate up to 512 tokens
        stop=["</s>"],   # Example stop token - not necessarily correct for this specific model! Please check before using.
        echo=True        # Whether to echo the prompt
    )
    return output['choices'][0]['text'][len(prompt):]


def process_input(input_str: str) -> str:
    # Placeholder function to be implemented

    # output_str = "just suppose we have process this input:" + input_str  # Modify this to perform actual processing
    
    # llama_cpp models
    output_str = process_input_llama_cpp(input_str)

    return output_str



