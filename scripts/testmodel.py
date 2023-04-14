import json
import argparse

from llama_cpp import Llama

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--model", type=str, default="./models/13B/ggml-alpaca-13b-q4.bin")
args = parser.parse_args()

llm = Llama(model_path=args.model, n_ctx=2056)
messages = []

while True:
    prompt = input("enter prompt: ")
    if prompt=="exit":
        break
    messages.append({"system":"answer questions","role":"user","content":prompt+" answer:"})
    output = llm.create_chat_completion(
        messages,
    )
    messages.append({"system":"","role":output["choices"][0]["message"]["role"],"content":output["choices"][0]["message"]["content"]})
    print(json.dumps(output, indent=2))