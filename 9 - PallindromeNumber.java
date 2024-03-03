class Solution {
    public boolean isPalindrome(int x) {
        int temp = x;
        int y = 0;
        
        if(x < 0)
            { return false;}
        while(temp != 0){
            y = y * 10;
            y += temp % 10;
            temp = temp / 10;
        }

        return x == y || x == y/10;

    }
}

