class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(1)
    * Tags: string, iteration
    * @param {string} word
    * @param {string} abbr
    * @return {boolean}
    */
   validWordAbbreviation(word, abbr) {
      let index = 0;
      let index2 = 0;

      const isDigit = (char) => {
         return char.match(/\d/)
      }

      while (
         index < word.length &&
         index2 < abbr.length
      ) {
         if (word[index] === abbr[index2]) {
            index++;
            index2++;
            continue
         } else if (isDigit(abbr[index2])) {
            if (abbr[index2] === '0') 
               return false
            
            let skip = 0;
            while (index2 < abbr.length && isDigit(abbr[index2])) {
               skip = 10*skip + Number(abbr[index2]);
               index2++;
            }
            index += skip
         } else 
            return false
      }
      return (
         index === word.length && 
         index2 === abbr.length
      )
   };
}