import java.util.ArrayDeque;
import java.util.Deque;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean isChangable(String src, String dst) {
        int cnt = 0;
        for (int i = 0; i < src.length(); i++) {
            if (src.charAt(i) != dst.charAt(i)) {
                cnt++;
            }
        }
        
        return cnt == 1;
    }
    
    public int solution(String begin, String target, String[] words) {
        Map<String, Integer> dist = new HashMap<>();
        for (String word: words) {
            dist.put(word, 999);
        }
        dist.put(begin, 0);
        
        Deque<String> q = new ArrayDeque<>();
        q.addFirst(begin);
        while (q.size() > 0) {
            String w = q.pollFirst();
            if (w.equals(target)) {
                return dist.get(w);
            }
            
            for (String word: words) {
                if (isChangable(w, word) && dist.get(word) > dist.get(w)) {
                    
                    q.addLast(word);
                    dist.put(word, dist.get(w) + 1);
                }
            }
        } 
        
        return 0;
    }
}