import tokenize
import token
from sys import stdout, argv, exit as sexit

instruction = 0
passed = 0

if len(argv) != 2:
    print("Usage : python3 list_tokens.py <fichier.py>")
    sexit(1)

filtered_lines = []
with open(argv[1], "r", encoding="utf-8") as f:
    for _, line in enumerate(f, start=1):
        if "assert" in line:
            passed += 1
            continue
        filtered_lines.append(line)

code = "".join(filtered_lines).encode("utf-8")

line_generator = iter(code.splitlines(keepends=True)).__next__

for tok in tokenize.tokenize(line_generator):
    tok_type = token.tok_name.get(tok.type, tok.type)

    if tok_type == "OP" and tok.string == ";":
        passed += 1
        continue
    if tok.string == "    ":
        instruction += 1
        stdout.write(f"[{tok.start[0]:<2}] {tok.type:<14} '\\t'\n")
    if tok_type not in ("COMMENT", "NL"):
        instruction += 1
        stdout.write(f"[{tok.start[0]:<2}] {tok_type:<14} {repr(tok.string)}\n")
    else:
        passed += 1

stdout.write(f"\nInstructions comptées : {instruction}\nTokens ignorés : {passed}\nTotals Tokens: {passed+instruction}\n")

#reconvertir en code
#convertir les print en sys.write.stdout et formatter l entré
#degager le typage et docstrings et valeur inutile

