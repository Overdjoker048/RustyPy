import tokenize
import token
from sys import stdout, argv, exit as sexit

COL = {
    "KEYWORD": "\033[38;5;176m",
    "NAME": "\033[38;5;117m",
    "NUMBER": "\033[38;5;151m",
    "STRING": "\033[38;5;173m",
    "OP": "\033[38;5;252m",
    "DEFAULT": "\033[38;5;250m"
}

if len(argv) != 2:
    print("Usage : python3 rewrite_tokens.py <fichier.py>")
    sexit(1)

with open(argv[1], "rb") as f:
    tokens = list(tokenize.tokenize(f.readline))

lines = {}
indent_level = 0
removed = 0

REDUCED = {"NAME", "NUMBER", "STRING", "OP", "KEYWORD"}

def classify(tok_type, tok_string):
    if tok_type == "NAME" and tok_string in {
        "def","return","if","else","elif","for","while","class","import",
        "from","as","try","except","finally","with","lambda","pass","break",
        "continue","yield","in","is","and","or","not","global","nonlocal",
        "assert","raise","del"
    }:
        return "KEYWORD"
    return tok_type

for tok in tokens:
    tok_type = token.tok_name.get(tok.type, tok_type := token.tok_name.get(tok.type, tok.type))

    if tok_type in ("ENCODING", "ENDMARKER"):
        continue
    if tok_type == "OP" and tok.string == ";":
        removed += 1
        continue
    if tok_type == "INDENT":
        indent_level += 1
        continue
    if tok_type == "DEDENT":
        indent_level = max(0, indent_level - 1)
        continue
    if tok_type in ("NL", "NEWLINE"):
        removed += 1
        continue

    tok_type = classify(tok_type, tok.string)
    if tok_type not in REDUCED:
        removed += 1
        continue

    line_no = tok.start[0]
    lines.setdefault(line_no, {"indent": indent_level, "tokens": []})

    color = COL.get(tok_type, COL["DEFAULT"])
    colored = f"{color}{tok_type}({repr(tok.string)})\033[0m"

    lines[line_no]["tokens"].append((tok_type, colored))

filtered = {}
for ln, data in lines.items():
    if not data["tokens"]:
        continue
    first_type = data["tokens"][0][0]
    if first_type in ("KEYWORD", "NAME"):
        filtered[ln] = data
    else:
        removed += len(data["tokens"])

for ln in sorted(filtered.keys()):
    indent = "    " * filtered[ln]["indent"]
    colored_tokens = [c for _, c in filtered[ln]["tokens"]]
    stdout.write(f"[{ln:<2}] {indent}{' '.join(colored_tokens)}\n")

stdout.write(f"Removed: {removed}\nConserve: {len(tokens) - removed}\nAll: {len(tokens)}\n")

#reconvertir en code
#convertir les print en sys.write.stdout et formatter l entré
#degager le typage et docstrings et valeur inutile
#supprimer tout ce qui e entre -> et :
#supprimer tout ce qui se trouve apres un : jusqu'au prochaine operateur
#ajouter la gestion des options/header