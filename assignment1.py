import argparse
import os
import logging
logging.basicConfig(level=logging.INFO)

_description = 'Measure the relative frequencies of letters ina a text file'

def count_letters(file_path):
    """Main processing method to measure
    the relative frequencies of the letters
    """
    # Basic sanity check: make sure that the file_path points to
    # an existing text file
    assert file_path.endswith('.txt')
    assert os.path.isfile(file_path)
    with open(file_path) as file:
        data = file.read()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    freq_dic = {}
    for ch in letters:
        freq_dic[ch] = 0
    for ch in data.lower():
        if ch in letters:
            freq_dic[ch] += 1
    num_char = float(sum(freq_dic.values()))
    for ch in letters:
        freq_dic[ch] /= num_char
    for ch, freq in freq_dic.items():
        print('{}: {:.3f}%'.format(ch, freq))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=_description)
    parser.add_argument('path', help='argument of the input file')
    args = parser.parse_args()
    count_letters('args.path')
