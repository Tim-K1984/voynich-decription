import json
import sys
from utils import load_text, save_text

with open("data/mappings.json", "r", encoding="utf-8") as f:
    mapping = json.load(f)

def decrypt(text):
    return "".join(mapping.get(ch, ch) for ch in text)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python src/decrypt.py <inputfile>")
        sys.exit(1)
    voynich_text = load_text(sys.argv[1])
    clear_text = decrypt(voynich_text)
    save_text("examples/sample_output.txt", clear_text)
    print(clear_text)
