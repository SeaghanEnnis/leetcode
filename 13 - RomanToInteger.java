class Solution {
    
    Map<Character,Integer> romanMap = new HashMap<>() {{
        put('I', 1);
        put('V', 5);
        put('X', 10);
        put('L', 50);
        put('C', 100);
        put('D', 500);
        put('M', 1000);
    }};
    
    public int romanToInt(String s) {
        
        int n = s.length();
        
        int num = 0;
        int prev = 0;
        
        for(int i = n-1; i >= 0; i--) {
            
            int curr = romanMap.get( s.charAt(i) );
            
            if( curr >= prev ) {
                num += curr;
            } 
            else {
                num -= curr;
            }
            
            prev = curr;
        }
        
        return num;
    }
}