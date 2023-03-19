class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode() # instantiate Trie data structure

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
		    # add a character to the children of node if it doesn't already exist in the children dictionary, then traverse to this child node
            node = node.children.setdefault(char, TrieNode()) 
        node.is_word = True
        
    def search(self, word: str) -> bool:
        queue = [self.root]
        for char in word: 
            tmp = [] # append new nodes to this temporary queue
            for node in queue: # for a sinlge char, bfs over the possible nodes (due to the wildcard '.')
                if char == '.': # if the char is a wildcard, append all child nodes into a queue to bfs at next iteration.
                    for child in node.children:
                        tmp.append(node.children[child])
                elif node.children.get(char): # if the char is found, keep going deeper into its children
					# Keep adding to tmp array when wildcard '.' results in nodes with the same char appearing. 
					# e.g., suppose adding two words 'abc' and 'cbd'. When searching for '.bc', 
					# both word nodes will be appended as candidates at the node.children['b']
                    tmp.append(node.children[char]) 
            queue = tmp # the newly appended queue to bfs over in the next iteration
        return any([node.is_word for node in queue])
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)