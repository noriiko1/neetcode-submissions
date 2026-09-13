class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs: # if list is empty, return empty
            return ""
        sizes, res = [], [] # creates the list
        for s in strs:
            sizes.append(len(s)) # takes the length of each string in the list and adds the length to the size ex: "apple" would append 5 into sizes
        for sz in sizes: 
            res.append(str(sz)) # appends a string version of the indexes for how many items there are in sizes
            res.append(",") # adds a comma in between each
        res.append("#") # adds a hashtag at the end
        res.extend(strs) # adds all the original list to the end of res
        return "".join(res) # returns everything into one string

    def decode(self, s: str) -> List[str]:
        if not s: # if string is empty, return empty
            return []
        sizes, res, i = [], [], 0 # creates two lists and a counter
        while s[i] != "#": # checks if the char at index is a hashtag
            j = i # creates index that is same as i
            while s[j] != ",": # checks if the char at index is a comma
                j += 1 # moves second pointer further
            sizes.append(int(s[i:j])) # appends the string from beginning until there is a comma
            i = j + 1 # moves onto the next word onto the comma
        i += 1 # moves past the comma
        for sz in sizes: # for each index in the new index, add the words
            res.append(s[i:i + sz]) # combine all the words
            i += sz
        return res