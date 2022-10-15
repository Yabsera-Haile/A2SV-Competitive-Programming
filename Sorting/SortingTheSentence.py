class Solution:
    def sortSentence(self, s: str) -> str:
        sentence = s.split()
        sentence.sort(key=lambda word: int(word[-1]))
        sentence = list(map(lambda word: word[:len(word)-1], sentence))
        return " ".join(sentence)
