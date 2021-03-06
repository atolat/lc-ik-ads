# 127. Word Ladder
# Medium

# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list.
# Note:

# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# Example 1:

# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]

# Output: 5

# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
# Example 2:

# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]

# Output: 0

# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        n = len(beginWord)
        # Adjacency list - Intermediate Word::Word
        adjList = collections.defaultdict(list)
        for word in wordList:
            for i in range(n):
                adjList[word[:i]+'*'+word[i+1:]].append(word)
        
        q = collections.deque([(beginWord, 1)])
        visited = set(beginWord)
        
        # BFS
        while q:
            numnodes = len(q)
            for _ in range(numnodes):
                curr, d = q.popleft()
                for i in range(n):
                    intermediate = curr[:i] + '*' + curr[i+1:]
                    for word in adjList[intermediate]:
                        if endWord == word:
                            return d+1
                        if word not in visited:
                            q.append((word, d+1))
                            visited.add(word)
        return 0                        