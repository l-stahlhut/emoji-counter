#!usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Laura Stahlhut
# Date: 07.11.2022

"""
Script to count emoji frequency in a txt-file. See README.md for information on how to use the code.
"""


import emoji
from collections import Counter
import argparse
import os

parser = argparse.ArgumentParser(description='Get Beleglisten')
parser.add_argument("-i", "--input", help="Specify the name of your input file.")
parser.add_argument("-o", "--output", help="Specify the name of your output file.")
args = parser.parse_args()


# get list of all emojis
def extract_emojis(s):
  return ''.join(c for c in s if c in emoji.UNICODE_EMOJI['en'])

# count frequency
def get_emoji_freq(s):
	s = extract_emojis(s)
	count = Counter(emoji for string in s for emoji in string)
	return str(count)[8:].rstrip(')')


def main():
	with open(args.input, 'r') as f:
		lines = f.readlines()
		s = ' '.join(lines)
		
	with open(os.path.join('emoji_frequency/', args.output), 'w') as outfile:

		outfile.write(get_emoji_freq(s))


if __name__ == '__main__':
	main()