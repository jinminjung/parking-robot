#!/usr/bin/env python3

import os
import subprocess
import sys

def run_python_script(script_name):
    """주어진 파이썬 스크립트를 실행하는 함수"""
    subprocess.run(["python3", script_name])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 node_sequence.py <choice>")
        sys.exit(1)

    choice = sys.argv[1]

    # 현재 작업 디렉토리 변경
    current_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_dir)

    # 실행할 파이썬 스크립트 파일들의 이름 리스트
    python_scripts_default = [
        "send_command_U.py",
        "straight1.py",
        "rotate_r.py",
        "straight2.py",
        "send_command_D.py",
        "back2.py",
        "rotate_l.py",
        "back1.py"
        # "1.py",
        # "2.py"
    ]

    python_scripts_alternative = [
        "send_command_U.py",
        "straight3.py",
        "rotate_r.py",
        "straight2.py",
        "send_command_D.py",
        "back2.py",
        "rotate_l.py",
        "back3.py"
        # "1.py",
        # "3.py"
    ]

    if choice == '전기차':
        python_scripts = python_scripts_alternative
    else:
        python_scripts = python_scripts_default

    # 각 스크립트를 순차적으로 실행
    for script in python_scripts:
        run_python_script(script)
