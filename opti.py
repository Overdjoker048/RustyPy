from sys import stdout, dont_write_bytecode, stderr
stdout.reconfigure(encoding='utf-8')
dont_write_bytecode = True
del dont_write_bytecode
stdout.write(f"x est 10\nAddition: 12 + 7 = 22\nSoustraction: 12 - 7 = 8\nMultiplication: 12 × 7 = 105\nDivision: 12 ÷ 7 = {(15 / 7):.2f}\nPuissance: 12² = 225\nModulo: 12 % 7 = 1\nDivision entière: 12 // 7 = 2\nMoyenne de 12, 7, 3.5 = {8.5:.2f}\n12\n")
stdout.write(f"{complex(12)}\n")
del stdout, stderr
