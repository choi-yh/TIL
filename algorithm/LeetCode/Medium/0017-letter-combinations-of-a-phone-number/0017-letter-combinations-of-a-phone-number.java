class Solution {
    public List<String> answer = new ArrayList();

    public List<String> letterCombinations(String digits) {
        if (digits.isEmpty()) {
            return answer;
        }

        Map<Integer, List<String>> data = Map.of(
            2, List.of("a", "b", "c"),
            3, List.of("d", "e", "f"),
            4, List.of("g", "h", "i"),
            5, List.of("j", "k", "l"),
            6, List.of("m", "n", "o"),
            7, List.of("p", "q", "r", "s"),
            8, List.of("t", "u", "v"),
            9, List.of("w", "x", "y", "z")
        );

        List<List<String>> target = new ArrayList();
        for (int i = 0; i < digits.length(); i++) {
            target.add(data.get(Integer.valueOf(digits.substring(i, i + 1))));
        }
        System.out.println(target);

        createText(target, "", 0, digits.length());

        return answer;
    }

    public void createText(List<List<String>> target, String text, int idx, int end) {
        if (idx == end) {
            answer.add(text);
            return;
        }

        for (String t: target.get(idx)) {
            text += t;
            
            createText(target, text, idx + 1, end);
            
            text = text.substring(0, text.length() - 1);
        }
    }
}