import java.util.Collections;
import java.util.PriorityQueue;

class Solution {
    public long solution(int n, int[] works) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for(int work: works) {
            pq.add(work);
        }
        
        for (int i = 0; i < n; i++) {
            int work = pq.poll();
            if (work == 0) {
                return 0;
            }
            
            work -= 1;
            pq.add(work);
        }
                
        long answer = 0;
        for (int remain: pq) {
            answer += Math.pow(remain, 2);
        }
        
        return answer;
    }
}