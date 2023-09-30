def is_identical(str1, str2):
  """Returns True if the two strings are identical with wildcards, False otherwise."""

  i = 0
  j = 0
  while i < len(str1) and j < len(str2):
    if str1[i] != str2[j] and str2[j] != '*':
      return False
    elif str2[j] == '*':
      j += 1
      while j < len(str2) and str2[j] == '*':
        j += 1
      if j == len(str2):
        return True
    else:
      i += 1
      j += 1

  return i == len(str1) and j == len(str2)


def main():
  """Prompts the user for two strings and checks if they are identical with wildcards."""

  str1 = input("Enter the first string: ")
  str2 = input("Enter the second string: ")

  if is_identical(str1, str2):
    print("1")
  else:
    print("0")


if __name__ == "__main__":
  main()
