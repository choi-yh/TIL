import java.lang.Integer;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int[] solution(String[] gems) {
        int[] answer = {1, gems.length};
        
        Set<String> gemSet = new HashSet<>(Arrays.asList(gems));
        
        Set<String> checkSet = new HashSet<>();        
        HashMap<String, Integer> checkMap = new HashMap<>();
        for (String gem: gems) {
            checkMap.put(gem, 0);
        }
        
        checkSet.add(gems[0]);
        checkMap.put(gems[0], 1);
        
        int start = 0;
        int end = 0;
        while (start <= end) {
            if (checkSet.size() == gemSet.size() && end - start < answer[1] - answer[0]) {
                answer[0] = start + 1;
                answer[1] = end + 1;
            }
            
            if (end == gems.length - 1) {
                checkMap.put(gems[start], checkMap.get(gems[start]) - 1);
                if (checkMap.get(gems[start]) == 0) {
                    checkSet.remove(gems[start]);
                }
                
                start++;
                continue;
            }
            
            if (checkSet.size() < gemSet.size()) {
                end++;
                
                checkMap.put(gems[end], checkMap.get(gems[end]) + 1);
                checkSet.add(gems[end]);
            } else {
                checkMap.put(gems[start], checkMap.get(gems[start]) - 1);
                if (checkMap.get(gems[start]) == 0) {
                    checkSet.remove(gems[start]);
                }
                
                start++;
            }
        }
        
        return answer;
    }
}