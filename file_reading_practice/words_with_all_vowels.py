"""
## 3. Words Containing All Five Vowels  *(Medium)*

=================================================
WORDS WITH ALL VOWELS
=================================================

Problem Statement:
Read the text file `sowpods.txt` and PRINT
every word that contains ALL FIVE vowels
('a', 'e', 'i', 'o', 'u') at least once.
The order of the vowels does NOT matter, and
the check should be case-insensitive.


-------------------------------------------------
Input Example (sowpods.txt sample):
education
sequoia
facetious
hello
audio
unequivocal

Output Example:
education
sequoia
facetious
unequivocal
Total words with all vowels: 4

-------------------------------------------------
Explanation:
- "education" contains a, e, i, o, u -> yes
- "sequoia"   contains a, e, i, o, u -> yes
- "facetious" contains a, e, i, o, u -> yes
- "hello"     missing a, i, o, u     -> no
- "audio"     missing e               -> no
- "unequivocal" contains a,e,i,o,u   -> yes
=================================================

"""
def find_words_with_all_vowels(filename="sowpods.txt"):
    # Define the set of all five vowels
    vowels = {"a", "e", "i", "o", "u"}
    match_count = 0

    try:
        # Open and read the text file line by line
        with open(filename, "r") as file:
            for line in file:
                # Remove whitespace and newlines, then convert to lowercase
                word = line.strip()
                word_lower = word.lower()

                # Convert the word to a set of characters
                word_chars = set(word_lower)

                # Check if all vowels are a subset of the word's characters
                if vowels.issubset(word_chars):
                    print(word)
                    match_count += 1

        # Print the total count of matching words
        print(f"\nTotal words with all vowels: {match_count}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")


# Run the function
if __name__ == "__main__":
    find_words_with_all_vowels()
  
