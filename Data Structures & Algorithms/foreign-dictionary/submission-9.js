class Solution {
   /**
    * Time complexity: O(V + E)
    *     V: unique letter count
    * Auxiliary space complexity: O(V + E)
    * Tags:
    *     DS: array
    *     A: multi-source DFS, topological sort with cycle detection
    *     Model: graph
    * @param {string[]} words
    * @return {string}
    */
   foreignDictionary(words) {
      const compareWords = (word1, word2) => {
         for (let idx = 0; idx < Math.max(word1.length, word2.length); idx++) {
            if (idx === word2.length) {
               return false;  // incorrect
            }
            else if (idx === word1.length) {
               return true;  // ok
            }
            else if (word1[idx] !== word2[idx]) {
               // prevLetters.get(word2[idx]).add(word1[idx]);
               prevLetters.get(word2[idx]).push(word1[idx]);
               break;
            }

         }
         return true;
      };

      const dfs = (letter) => {
         const idx = letter.charCodeAt(0) - 'a'.charCodeAt(0);

         if (visited[idx] !== -1) {
            return Boolean(visited[idx]);
         }

         visited[idx] = 0;

         for (const prevLetter of prevLetters.get(letter))
            if (dfs(prevLetter) === false) {
               return false;
            }

         res.push(letter);
         visited[idx] = 1;
         return true;
      };

      const prevLetters = new Map();

      for (const word of words) {
         for (const letter of word) {
            if (!prevLetters.has(letter)) {
               // prevLetters.set(letter, new Set());
               prevLetters.set(letter, []);
            }
         }
      }

      for (let idx = 0; idx < words.length - 1; idx++) {
         for (let jdx = idx + 1; jdx < words.length; jdx++) {
            if (compareWords(words[idx], words[jdx]) === false) {
               return "";
            }
         }
      }

      // -1: not visited, 0: visited, 1: in path (detect a cycle)
      const visited = Array(26).fill(-1);
      const res = [];

      for (const letter of prevLetters.keys()) {
         if (dfs(letter) === false) {
            return "";
         }
      }

      return res.join("");
   }
}

