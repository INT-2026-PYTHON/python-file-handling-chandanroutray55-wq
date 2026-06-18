"""
## 6. Words in sonnet_words.txt but NOT in sowpods.txt  *(Hard)*

=================================================
WORDS UNIQUE TO THE SONNET
=================================================

Problem Statement:
Read the text files `sowpods.txt` and
`sonnet_words.txt`. PRINT every word that
appears in `sonnet_words.txt` but does NOT
appear in `sowpods.txt`.

This problem is about CHOOSING THE RIGHT DATA
STRUCTURE. If you check each sonnet word
against the SOWPODS list with a nested loop,
the work is O(N*M). Using SETS turns the
membership check into O(1), giving you an
overall O(N + M) algorithm.

-------------------------------------------------
Input Example:
sowpods.txt sample:
   thee
   love
   summer
   day
   eyes
   shall
   more

sonnet_words.txt sample:
   shall
   i
   compare
   thee
   to
   a
   summer
   day

Output Example:
Words in sonnet but not in sowpods:
['a', 'compare', 'i', 'to']
Total: 4

-------------------------------------------------
Explanation:
sonnet words -> {'shall', 'i', 'compare',
                 'thee', 'to', 'a', 'summer',
                 'day'}
sowpods set   -> {'thee', 'love', 'summer',
                  'day', 'eyes', 'shall',
                  'more'}
Difference (sonnet - sowpods)
              -> {'i', 'compare', 'to', 'a'}
After sorting -> ['a', 'compare', 'i', 'to'].
=================================================

"""
def find_unique_words(sowpods_file, sonnet_file):
    # Read SOWPODS words and store them in a set for O(1) lookups
    with open(sowpods_file, 'r', encoding='utf-8') as f:
        # strip() removes any trailing newlines or whitespace
        sowpods_set = {line.strip().lower() for line in f if line.strip()}
        
    # Read sonnet words and store them in a set to find unique words
    with open(sonnet_file, 'r', encoding='utf-8') as f:
        sonnet_set = {line.strip().lower() for line in f if line.strip()}
        
    # Find words in sonnet_set but NOT in sowpods_set using set difference
    unique_words_set = sonnet_set.difference(sowpods_set)
    
    # Convert to a sorted list as shown in the example output
    sorted_unique_words = sorted(list(unique_words_set))
    
    # Print the results matching the requested format
    print("Words in sonnet but not in sowpods:")
    print(sorted_unique_words)
    print(f"Total: {len(sorted_unique_words)}")

# Example usage (uncomment to run locally):
# find_unique_words('sowpods.txt', 'sonnet_words.txt')
