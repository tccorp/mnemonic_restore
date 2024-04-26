def check_mnemonic_validity(words):

    from mnemonic import Mnemonic

    mnemo = Mnemonic("english")

    # words = mnemo.generate(strength=256)

    try:
        entropy = mnemo.to_entropy(words)
        return True
    except (ValueError, Exception) as e:
        # print (e)
        return False
