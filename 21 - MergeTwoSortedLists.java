class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode newHead = new ListNode(-1);
        ListNode newList = newHead;
        ListNode tempL = list1;
        ListNode tempR = list2;
        
        
        
        while(tempL != null && tempR != null){
            if(tempL.val <= tempR.val){
                newList.next = tempL;
                tempL = tempL.next;
            } else{
                newList.next = tempR;
                tempR = tempR.next;
            }
            newList = newList.next;
        }
        
        newList.next = tempL == null ? tempR : tempL;
        
        return newHead.next;
    }
}