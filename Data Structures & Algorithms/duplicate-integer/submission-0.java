public class Solution {
  public boolean hasDuplicate(int[] numbers) {
    Set<Integer> uniqueNumbers = new HashSet<>();
    for (int number : numbers) {
      if (uniqueNumbers.contains(number)) {
        return true;
      } else {
        uniqueNumbers.add(number);
      }
    }
    return false;
  }
}