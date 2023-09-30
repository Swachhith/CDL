import re
import string
import matplotlib.pyplot as plt

def count_letters_regex(filename):
  with open(filename, "r") as f:
    contents = f.read()

  letters = {}
  for letter in string.ascii_lowercase:
    letters[letter] = 0

  pattern = r"[a-zA-Z]"
  matches = re.findall(pattern, contents)

  for match in matches:
    letters[match.lower()] += 1

  return letters

def main():
  letters = count_letters_regex(r"Job33/data.txt")
  f = open(r"Job33/data.txt","r")
  txt = f.read()
  contents=0
  for match in re.findall(r"\w",txt):
    contents+=1
  frequencies = {}
  for letter, count in letters.items():
    frequencies[letter] = count / contents * 100

  plt.figure(figsize=(10, 6))
  plt.bar(letters.keys(), frequencies.values())
  plt.xlabel("Letter")
  plt.ylabel("Percentage")
  plt.title("Percentage of Letter Appearance in data.txt")
  plt.show()

if __name__ == "__main__":
  main()
