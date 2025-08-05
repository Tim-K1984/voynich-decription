def load_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def save_text(filepath, text):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
