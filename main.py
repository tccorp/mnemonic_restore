from utils import check_mnemonic_validity as cmv

def txt2list(fname):
    with open(fname, 'r') as f:
        return [line.strip() for line in f]

# Assumes BIP39 and BIP44
def main(phrase, missing_notation='?', verbose=True):
    mnemonic_dictionary = txt2list('bip39_words_english.txt')
    phrase_list = phrase.split(' ')
    if verbose:
        print('Phrase given:')
        print(phrase)

    num_missing_word = sum(1 if _ == missing_notation else 0 for _ in phrase_list)
    if num_missing_word > 1:
        raise Exception('Multiple missing words is not supported yet.')

    pos_missing_word = phrase_list.index(missing_notation)
    for guess_word in mnemonic_dictionary:
        phrase_list[pos_missing_word] = guess_word
        phrase_printable = ' '.join(phrase_list)
        print ('.', flush=True, end='')

        if cmv(phrase_printable):
            if verbose:
                # print('\nFound correct phrase:')
                print('\n', phrase_printable)
                # break
                continue
            else:
                if verbose:
                    print('\nNot found!')
    print()


if __name__ == '__main__':
    # phrase = 'school antique detect emotion pepper weasel topic arm shoulder ? chapter deny' # an example
    # phrase = 'install fresh conduct boss coyote tragic erase follow fence talent hint dish' # an example
    # phrase = 'install fresh conduct boss coyote tragic erase follow fence talent ? dish' # an example
    phrase = 'abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon ?' # an example

    main(phrase)
