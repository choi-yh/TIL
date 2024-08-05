import java.lang.Math;

class Solution {
    public int solution(int[] arrayA, int[] arrayB) {
        int aGCD = getArrayGCD(arrayA);
        int bGCD = getArrayGCD(arrayB);
            
        if (check(bGCD, arrayA) || check(aGCD, arrayB)) {
            return Math.max(aGCD, bGCD);
        }
        
        return 0;
    }
    
    public boolean check(int gcd, int[] arr) {
        for (int a: arr) {
            if (a % gcd == 0) {
                return false;
            }
        }

        return true;
    }
    
    public int getArrayGCD(int[] array) {
        int gcd = array[0];
        for (int a: array) {
            gcd = getGCD(gcd, a);
        }
        
        return gcd;
    }
    
    public int getGCD(int a, int b) {
        while (a > 0) {
            int temp = a;
            a = b % a;
            b = temp;
        }
        
        return b;
    }
}