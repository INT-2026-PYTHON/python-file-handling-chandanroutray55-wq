"""
## 5. Longest Palindrome in the File  *(Hard)*

=================================================
LONGEST PALINDROME
=================================================

Problem Statement:
Read the text file `sowpods.txt` and find the
LONGEST PALINDROME word in the file.

If multiple palindromes share the maximum
length, print ALL of them.

-------------------------------------------------
Input Example (sowpods.txt sample):
level
radar
noon
civic
deified
racecar
rotator
malayalam

Output Example:
Longest palindrome length: 9
malayalam

-------------------------------------------------
Explanation:
Lengths of the palindromes in the sample:
   level    -> 5
   radar    -> 5
   noon     -> 4
   civic    -> 5
   deified  -> 7
   racecar  -> 7
   rotator  -> 7
   malayalam -> 9
The longest is "malayalam" with 9 characters.
=================================================

"""
def find_longest_palindromes(filename="sowpods.txt"):
    try:
        max_length = 0
        longest_palindromes = []

        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                # Clean up whitespace and newlines
                word = line.strip()

                # Skip empty lines
                if not word:
                    continue

                # Check if the word is a palindrome
                if word == word[::-1]:
                    word_len = len(word)

                    # Found a strictly longer palindrome
                    if word_len > max_length:
                        max_length = word_len
                        longest_palindromes = [word]
                    # Found another palindrome of the same maximum length
                    elif word_len == max_length:
                        longest_palindromes.append(word)

        # Print results matching the requested format
        if longest_palindromes:
            print(f"Longest palindrome length: {max_length}")
            for palindrome in longest_palindromes:
                print(palindrome)
        else:
            print("No palindromes found in the file.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")


# Run the function
if __name__ == "__main__":
    find_longest_palindromes()
   
