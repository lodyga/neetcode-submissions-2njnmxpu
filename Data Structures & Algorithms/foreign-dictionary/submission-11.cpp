class Solution {
public:
   string foreignDictionary(const vector<string>& words) {
      unordered_map<char, vector<char>> prevLetters;
      unordered_set<char> letters;
      // -1: not visited, 0: visited, 1: in path (detect a cycle)
      vector<int> visited(26, -1);
      vector<char> res;

      for (const string& word : words) {
         for (char letter : word) {
            letters.insert(letter);
         }
      }

      auto compareWords = [&](const string& word1, const string& word2) -> bool {
         for (int idx = 0; idx < max(word1.size(), word2.size()); ++idx) {
            if (idx == word2.size()) {
               return false;  // incorrect
            }
            else if (idx == word1.size()) {
               return true;  // ok
            }
            else if (word1[idx] != word2[idx]) {
               prevLetters[word2[idx]].push_back(word1[idx]);
               break;
            }

         }
         return true;
         };

      auto dfs = [&](auto&& self, char letter) -> bool {
         int idx = letter - 'a';

         if (visited[idx] != -1) {
            return visited[idx];
         }

         visited[idx] = 0;

         for (char prevLetter : prevLetters[letter])
            if (self(self, prevLetter) == false) {
               return false;
            }

         res.push_back(letter);
         visited[idx] = 1;
         return true;
         };

      for (int idx = 0; idx < words.size() - 1; ++idx) {
         if (compareWords(words[idx], words[idx + 1]) == false) {
            return "";
         }
      }

      for (char letter : letters) {
         if (dfs(dfs, letter) == false) {
            return "";
         }
      }

      return string(res.begin(), res.end());
   }
};

