import java.util.Stack;

/**
 * 문장에 있는 단어를 공백을 기준으로 하여 뒤집습니다.
 */
public class ShuffleWordInSentence {

    public static String shuffle(String sentence) {
        String[] words = sentence.split(" ");

        Stack<String> stack = new Stack<>();
        for (String word : words) {
            stack.push(word);
        }

        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            String word = stack.pop();
            sb.append(word).append(" ");
        }

        return sb.deleteCharAt(sb.length() - 1).toString();
    }

}
