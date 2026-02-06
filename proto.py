from sys import stdout, argv
from platform import system


def parse_arguments(args: list[str]) -> dict:
    flags = {
        "path": None,
        "gui": False,
        "doc": False,
        "asr": False,
        "nogc": False,
        "output": None,
        "icon": None,
    }

    if not args:
        return flags

    flags["path"] = args[0]
    expect_value = None

    for arg in args[1:]:
        lower = arg.lower()

        if expect_value:
            flags[expect_value] = arg
            expect_value = None
            continue

        if lower == "-gui":
            flags["gui"] = True
        elif lower == "-doc":
            flags["doc"] = True
        elif lower == "-asr":
            flags["asr"] = True
        elif lower == "-nogc":
            flags["nogc"] = True
        elif lower == "-o":
            expect_value = "output"
        elif lower == "-icon":
            expect_value = "icon"
        else:
            stdout.write(f"Warning: unknown argument ignored: {arg}\n")

    if expect_value:
        stdout.write(f"Warning: missing value for option: -{expect_value}\n")

    return flags


def main():
    if len(argv) < 2:
        stdout.write("Usage: python main.py <python path> [-doc] [-gui] [-asr] [-icon <icon path>] [-nogc] [-o <output name>]\n")
        return

    flags = parse_arguments(argv[1:])

    if not flags["path"]:
        stdout.write("Usage: python main.py <python path> [-doc] [-gui] [-asr] [-icon <icon path>] [-nogc] [-o <output name>]\n")
        return

    base = flags["path"].rsplit(".", 1)[0]
    ext = ".exe" if system() == "Windows" else ""
    flags["output"] = flags["output"] or (base + ext)

    header = [
        "from sys import stdout, dont_write_bytecode",
        "stdout.reconfigure(encoding='utf-8')",
        "dont_write_bytecode = True",
        "del stdout, dont_write_bytecode",
    ]

    if flags["nogc"]:
        header.extend([
            "from gc import disable",
            "disable()",
            "del disable",
        ])

    if flags["gui"]:
        header.extend([
            "from sys import stdout, stderr, stdin",
            "def __nothing(s: str) -> None: pass",
            "stdout.write = __nothing",
            "stderr.write = __nothing",
            "stdin.write = __nothing",
            "del stderr, stdout, stdin",
        ])