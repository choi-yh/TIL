import java.util.*;

/*
    stack 에서 사용가능한 메서드
        1. append : 스택의 끝에 원소를 추가
        2. pop : 스택의 끝에 있는 원소를 반환하고 제거
        3. size : 스택의 길이
        4. isEmpty : 비어있는지 여부 확인

    queue 에서 필요한 메서드는
        1. append : 큐의 가장 끝에 원소를 삽입
        2. pop : 큐의 가장 맨 앞 원소를 반환하고 제거
        3. size : 큐의 길이
        4. isEmpty : 비어있는지 여부 확인

    length vs length() vs size
        - length : 배열의 길이 (int[], double[], String[])
        - length() : 문자열의 길이 (String, StringBuilder)
        - size : Collection Object (ArrayList, Set, etc, ...)
 */
class Stack2Queue {
    public static void main(String[] args) {
        Stack2Queue q = new Stack2Queue(Arrays.asList(1, 2));
        q.print();

        System.out.println(q.isEmpty());

        q.append(4);
        q.print();

        System.out.println(q.pop());
        System.out.println(q.pop());
        System.out.println(q.pop());

        System.out.println(q.isEmpty());
    }

    private final Stack<Integer> stack1 = new Stack<>();
    private final Stack<Integer> stack2 = new Stack<>();

    public Stack2Queue(Collection<Integer> queue) {
        for (Integer e: queue) {
            stack1.push(e);
        }
    }

    public List<Integer> getQueue() {
        List<Integer> list = new ArrayList<>(stack2);
        Collections.reverse(list);
        list.addAll(stack1);
        return list;
    }

    public void append(Integer e) {
        stack1.push(e);
    }

    public Integer pop() {
        if (stack1.isEmpty() && stack2.isEmpty()){
            throw new RuntimeException("Queue is Empty");
        }

        while (!stack1.isEmpty()) {
            stack2.add(stack1.pop());
        }

        return stack2.pop();
    }

    public int size() {
        return stack1.size() + stack2.size();
    }

    public boolean isEmpty() {
        return stack1.isEmpty() && stack2.isEmpty();
    }

    public void print() {
        System.out.println(this.getQueue());
    }
}