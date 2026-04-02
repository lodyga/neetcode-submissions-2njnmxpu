class Solution {
   /**
    * Time complexity: O(n)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: stack, string
    *     A: iteration
    * @param {string} text
    * @return {}
    */
   calculate(text) {
      const stack = [];
      let num = 0;
      let isDigit = false;

      // Convert string numbers to int numbers and push numbers and operators to stack.
      for (const char of text + ' ') {
         if (char >= '0' && char <= '9') {
            num *= 10;
            num += Number(char);
            isDigit = true;
         } else if (isDigit) {
            stack.push(num);
            isDigit = false;
            num = 0;
         }

         if ('+-*/'.includes(char)) {
            stack.push(char);
         }
      }

      const equations = [];
      // Handle // and * operators.
      let index = 0
      while (index < stack.length) {
         const char = stack[index];

         if (char === '*' || char === '/') {
            index += 1

            if (char === '/') {
               equations.push(Math.floor(equations.pop() / stack[index]))
            } else {
               equations.push(equations.pop() * stack[index])
            }
         } else {
            equations.push(char);
         }
         index += 1
      }

      let res = 0;
      index = 0;
      // Handle + and - operators.
      while (index < equations.length) {
         const char = equations[index];

         if (char === '+' || char === '-') {
            index += 1;

            if (char === '+') {
               res += equations[index];
            } else {
               res -= equations[index];
            }
         } else {
            res += char;
         }

         index += 1
      }

      return res
   };
}


const calculate = new Solution().calculate;