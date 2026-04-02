class Solution {
   /**
    * Time complexity: O(V + E)
    *     V: unique letters count
    * Auxiliary space complexity: O(V + E)
    * Tags: dfs, recursion, graph, topological sort
    * @param {string[]} words
    * @return {string}
    */
   foreignDictionary(words) {
      const prereqs = new Map();
      for (const word of words) {
         for (const letter of word) {
            prereqs.set(letter, new Set())
         }
      }

      for (let index = 0; index < words.length - 1; index++) {
         const word = words[index];
         const nextWord = words[index + 1];

         for (let j = 0; j < Math.max(word.length, nextWord.length); j++) {
            if (j === word.length)
               break
            else if (j === nextWord.length)
               return ''
            else if (word[j] !== nextWord[j]) {
               prereqs.set(nextWord[j], prereqs.get(nextWord[j]).add(word[j]));
               break
            }
         }
      }

      const alienDict = [];
      // null: not visited, false: visited, true: on current patch (detect cycle)
      const visited = Array(26).fill(null);

      const dfs = (letter) => {
         if (visited[letter.charCodeAt(0) - 'a'.charCodeAt(0)] !== null)
            return visited[letter.charCodeAt(0) - 'a'.charCodeAt(0)]

         visited[letter.charCodeAt(0) - 'a'.charCodeAt(0)] = true;

         for (const prereq of prereqs.get(letter))
            if (dfs(prereq))
               return true

         visited[letter.charCodeAt(0) - 'a'.charCodeAt(0)] = false;
         alienDict.push(letter);
         return false
      };

      for (const letter of prereqs.keys()) {
         if (dfs(letter))
            return ''
      }

      return alienDict.join('')
   };
}