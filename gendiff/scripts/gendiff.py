#!/usr/bin/env python3
from gendiff.cli import parsing_args1
import argparse


def parsing_args():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()


def main():
    parsing_args1()


if __name__ == '__main__':
    main()
