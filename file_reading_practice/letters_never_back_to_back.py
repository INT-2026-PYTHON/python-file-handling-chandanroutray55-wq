"""
## 2. Alphabets That Never Appear Back-to-Back  *(Medium)*

=================================================
ALPHABETS NEVER IN SEQUENCE
=================================================

Problem Statement:
Read the text file `sowpods.txt` and PRINT
every alphabet letter that:
   - APPEARS at least once in the words of
     the file, AND
   - NEVER appears TWICE IN A ROW (back-to-back)
     in ANY word of the file.

Letters that never appear in the file at all
should NOT be in the answer. Letters that
appear back-to-back at least once (like the
'u' in "vacuum") should also be excluded.

-------------------------------------------------
Input Example (sowpods.txt sample):
aardvark
hello
buzz
moon
puppy

Output Example:
Letters that never appear back-to-back:
['b', 'd', 'e', 'h', 'k', 'm', 'n', 'r', 'u', 'v', 'y']

-------------------------------------------------
Explanation:
Letters seen anywhere in the sample:
   aardvark -> a, r, d, v, k
   hello    -> h, e, l, o
   buzz     -> b, u, z
   moon     -> m, o, n
   puppy    -> p, u, y
   seen    = {a, b, d, e, h, k, l, m, n, o,
              p, r, u, v, y, z}

Letters that ever appear back-to-back:
   aa (aardvark), ll (hello), zz (buzz),
   oo (moon),     pp (puppy)
   doubled = {a, l, z, o, p}

Answer = seen - doubled
       = {b, d, e, h, k, m, n, r, u, v, y}
Sorted -> ['b', 'd', 'e', 'h', 'k', 'm', 'n',
           'r', 'u', 'v', 'y']
=================================================

"""
import string

def find_non_repeating_letters(filename="sowpods.txt"):
    seen_letters = set()
    doubled_letters = set()

    # Read the file line by line
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip().lower()
            
            # Track letters seen and check for consecutive duplicates
            for i, char in enumerate(word):
                if char.isalpha():
                    seen_letters.add(char)
                    # Check if the next character is the same
                    if i < len(word) - 1 and char == word[i + 1]:
                        doubled_letters.add(char)

    # Valid letters = (letters that appear at least once) - (letters that double up)
    valid_letters = seen_letters - doubled_letters
    
    # Sort alphabetically as shown in the example output
    return sorted(list(valid_letters))

# Execute the function
if __name__ == "__main__":
    result = find_non_repeating_letters()
    print(result)
   
