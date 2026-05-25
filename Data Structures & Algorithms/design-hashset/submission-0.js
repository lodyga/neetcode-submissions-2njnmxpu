class ListNode {
   constructor(val = null, next = null) {
      this.val = val;
      this.next = next;
   }
}


class LinkedList {
   constructor() {
      this.head = new ListNode();
   }

   add(val) {
      let node = this.head;

      while (node.next) {
         if (node.next.val === val) {
            return;
         }
         node = node.next;
      }

      node.next = new ListNode(val);
   }

   has(val) {
      let node = this.head;

      while (node.next) {
         if (node.next.val === val) {
            return true;
         }

         node = node.next;
      }

      return false;
   }

   discard(val) {
      let node = this.head;

      while (node.next) {
         if (node.next.val === val) {
            node.next = node.next.next;
            return;
         }

         node = node.next;
      }
   }

}

class MyHashSet {
   /**
    * Time complexity:
    *     constructor: O(CAPACITY)
    *     add: O(1)
    *     contains: O(1)
    *     remove: O(1)
    * Auxiliary space complexity: O(n)
    * Tags:
    *     DS: linked list, hash set
    *     A: iteration
    */
   CAPACITY = 10 ** 4;

   constructor() {
      this.buckets = Array.from({ length: this.CAPACITY }, () => new LinkedList());
   }

   /**
    * @param {number} val
    * @returns {number}
    */
   #getHashCode(val) {
      return val % this.CAPACITY;
   }

   /**
    * @param {number} val
    * @returns {LinkedList}
    */
   #getLinkedList(val) {
      return this.buckets[this.#getHashCode(val)];
   }

   /**
    * @param {number} val 
    * @returns {void}
    */
   add(val) {
      const linkedList = this.#getLinkedList(val);
      linkedList.add(val);
   }

   /**
    * @param {number} val 
    * @returns {boolean}
    */
   contains(val) {
      const linkedList = this.#getLinkedList(val);
      return linkedList.has(val);
   }

   /**
    * @param {number} val 
    * @returns {void}
    */
   remove(val) {
      const linkedList = this.#getLinkedList(val);
      linkedList.discard(val);
   }
}


/**
 * Your MyHashSet object will be instantiated and called as such:
 * var obj = new MyHashSet()
 * obj.add(key)
 * obj.remove(key)
 * var param_3 = obj.contains(key)
 */
