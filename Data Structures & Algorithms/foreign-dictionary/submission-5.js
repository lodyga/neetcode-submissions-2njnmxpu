class Solution {
   /**
    * Time complexity: O(V + E)
    *     V: unique letters count
    * Auxiliary space complexity: O(V + E)
    * Tags:
    *     DS: array (graph)
    *     A: multi-source DFS, topological sort with cycle detection
    * @param {string[]} words
    * @return {string}
    */
   foreignDictionary(words) {
      const prereqs = new Map();
      for (const word of words) {
         for (const letter of word) {
            if (!prereqs.has(letter)) {
               prereqs.set(letter, [])
            }
         }
      }

      for (let index = 0; index < words.length - 1; index++) {
         const word = words[index];
         const nextWord = words[index + 1];

         for (let index = 0; index < word.length; index++) {
            if (index === nextWord.length) {
               return ''
            }

            const letter = word[index];
            const nextLetter = nextWord[index];
            if (letter === nextLetter) {
               continue
            }

            prereqs.get(nextLetter).push(letter);
            break
         }
      }

      // -1: not visited, 0: visited, 1: in path (detect a cycle)
      const visited = Array(26).fill(-1);

      const dfs = (letter) => {
         const index = letter.charCodeAt(0) - 'a'.charCodeAt(0);
         if (visited[index] !== -1) {
            return visited[index]
         }

         visited[index] = 1;

         for (const prereq of prereqs.get(letter))
            if (dfs(prereq))
               return true

         alienDict.push(letter);
         visited[index] = 0;
         return 0
      };

      const alienDict = [];
      for (const letter of prereqs.keys()) {
         if (dfs(letter))
            return ''
      }

      return alienDict.join('')
   };
}