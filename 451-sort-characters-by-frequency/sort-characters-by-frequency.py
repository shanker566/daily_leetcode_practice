class Solution:
    def frequencySort(self, s: str) -> str:
        # Step 1: Count the frequencies of each letter
        counts = {}
        for letter in s:
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1
        
        # Step 2: Sort the characters based on their counts (highest to lowest)
        # counts.items() gives pairs like ('e', 3). 
        # key=lambda x: x[1] tells Python to sort using the count (index 1).
        # reverse=True makes it descending (highest counts first).
        sorted_characters = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        
        # Step 3: Rebuild the string
        result = []
        for letter, count in sorted_characters:
            result.append(letter * count)  # e.g., 'e' * 3 becomes "eee"
            
        return "".join(result)
