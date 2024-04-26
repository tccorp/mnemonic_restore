from mnemonic import Mnemonic


def check_mnemonic_validity(words):

  mnemo = Mnemonic("english")

  # words = mnemo.generate(strength=256)


  try:
    entropy = mnemo.to_entropy(words)
    return True
  except (ValueError, Exception) as e:
    print (e)
    return False

if __name__ == '__main__':

  words = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about"
  print(check_mnemonic_validity(words))
