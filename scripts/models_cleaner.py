"""
Script to clean model files.
"""
import os
import re

from pathlib import Path


MODEL_FILES = [
    "../chsdi/models/vector/are.py",
    "../chsdi/models/vector/bafu.py",
    "../chsdi/models/vector/bak.py",
    "../chsdi/models/vector/dritte.py",
    "../chsdi/models/vector/edi.py",
    "../chsdi/models/vector/evd.py",
    "../chsdi/models/vector/lubis.py",
    "../chsdi/models/vector/stopo.py",
    "../chsdi/models/vector/uvek_solarkataster.py",
    "../chsdi/models/vector/uvek.py",
    "../chsdi/models/vector/vbs.py",
    "../chsdi/models/vector/zeitreihen.py"
]


def clean_register_lines(file_path, output_path=None):
    """ Replace BOD IDs in register lines with <object name>.__bodId__ """
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    output_lines = []
    for line in lines:
        match = re.match(r"register\(\s*'([^']+)'\s*,\s*([A-Za-z0-9_]+)\s*\)", line)
        if match:
            bod_id, obj_name = match.groups()
            output_lines.append(f"register({obj_name}.__bodId__, {obj_name})\n")
        else:
            output_lines.append(line)

    target_path = output_path if output_path else file_path
    with open(target_path, "w", encoding="utf-8") as f:
        f.writelines(output_lines)


def ensure_single_blank_line_before_register(file_path, output_path=None):
    """ Ensure there is only a single blank line before the register lines. """
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    output_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if re.match(r"\s*register\(", line):
            blank_lines_count = 0
            j = len(output_lines) - 1
            while j >= 0 and output_lines[j].strip() == "":
                blank_lines_count += 1
                j -= 1

            prev_nonblank_line = output_lines[j] if j >= 0 else ""

            if re.match(r"\s*register\(", prev_nonblank_line):
                output_lines = output_lines[:j+1]
            else:
                if blank_lines_count == 0:
                    output_lines.append("\n")
                elif blank_lines_count > 1:
                    output_lines = output_lines[:j+2]

            output_lines.append(line)
            i += 1
        else:
            output_lines.append(line)
            i += 1

    target_path = output_path if output_path else file_path
    with open(target_path, "w", encoding="utf-8") as f:
        f.writelines(output_lines)


def clean_class_lines(file_path, output_path=None):
    """ Clean class definitions from unnecessary spaces. """
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    output_lines = []
    for line in lines:
        match = re.match(r"^(\s*)class\s+(\w+)\s*\(([^)]*)\)\s*:", line)
        if match:
            indent, class_name, bases = match.groups()
            base_list = ", ".join(part.strip() for part in bases.split(","))
            clean_line = f"{indent}class {class_name}({base_list}):\n"
            output_lines.append(clean_line)
        else:
            output_lines.append(line)

    target_path = output_path if output_path else file_path
    with open(target_path, "w", encoding="utf-8") as f:
        f.writelines(output_lines)


def main():
    """ Main function to process all model files. """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    for file in MODEL_FILES:
        folder = os.path.dirname(file)
        base = os.path.splitext(os.path.basename(file))[0]
        cleaned_filename = f"{base}.py"
        output_path = os.path.join(folder, cleaned_filename)
        clean_register_lines(output_path)
        ensure_single_blank_line_before_register(output_path)
        clean_class_lines(output_path)


if __name__ == "__main__":
    main()
