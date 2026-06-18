"""
## 4. Find All Palindrome Words  *(Medium)*

=================================================
PALINDROME WORDS
=================================================

Problem Statement:
Read the text file `sowpods.txt` and PRINT
every PALINDROME word (a word that reads the
same forwards and backwards).

Write a helper FUNCTION called `is_palindrome`
that takes a single word and returns True if
it is a palindrome, else False. Pass every
word in the file to this function ONE AT A
TIME.

-------------------------------------------------
Input Example (sowpods.txt sample):
level
radar
hello
noon
civic
python
deified
racecar
banana

Output Example:
level
radar
noon
civic
deified
racecar
Total palindromes: 6

-------------------------------------------------
Explanation:
- "level"    reversed -> "level"   -> palindrome
- "radar"    reversed -> "radar"   -> palindrome
- "hello"    reversed -> "olleh"   -> not
- "noon"     reversed -> "noon"    -> palindrome
- "civic"    reversed -> "civic"   -> palindrome
- "python"   reversed -> "nohtyp"  -> not
- "deified"  reversed -> "deified" -> palindrome
- "racecar"  reversed -> "racecar" -> palindrome
- "banana"   reversed -> "ananab"  -> not
=================================================

"""
def is_palindrome(word):
    """
    Helper function to check if a word reads the same forwards and backwards.
    """
    # Clean the word by removing whitespace and converting to lowercase
    cleaned_word = word.strip().lower()
    return cleaned_word == cleaned_word[::-1]

def find_all_palindrome_words(filename="sowpods.txt"):
    """
    Reads the text file and prints every palindrome word along with the total count.
    """
    palindrome_count = 0
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Get the word and strip trailing newlines/spaces
                word = line.strip()
                
                # Skip empty lines if any exist in the file
                if not word:
                    continue
                
                # Check if the word is a palindrome using the helper function
                if is_palindrome(word):
                    print(word)
                    palindrome_count += 1
                    
        print(f"Total palindromes: {palindrome_count}")
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Please ensure it is in the same directory.")

# Execute the function
if __name__ == "__main__":
    find_all_palindrome_words()
