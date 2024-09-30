import java.lang.reflect.Field;

public class Json {

    public static String toJson(Object obj) throws IllegalAccessException {
        StringBuilder json = new StringBuilder();
        Class<?> objClass = obj.getClass();
        json.append("{");

        Field[] fields = objClass.getDeclaredFields();
        for (int i = 0; i < fields.length; i++) {
            Field field = fields[i];
            field.setAccessible(true); // private 필드 접근 가능하게 설정
            String key = field.getName();
            Object value = field.get(obj);

            json.append("\"").append(key).append("\":");

            // 값을 처리 (문자열, 숫자, 논리형에 따라 다르게 처리)
            if (value instanceof String) {
                json.append("\"").append(value).append("\"");
            } else {
                json.append(value); // 숫자 또는 논리형(boolean)은 그대로 추가
            }

            if (i < fields.length - 1) {
                json.append(","); // 마지막 요소가 아니면 쉼표 추가
            }
        }

        json.append("}");
        return json.toString();
    }

    public static <T> T fromJson(String jsonString, Class<T> clazz) throws Exception {
        T obj = clazz.getDeclaredConstructor().newInstance();

        jsonString = jsonString.replace("{", "").replace("}", "").trim();
        String[] keyValuePairs = jsonString.split(",");

        for (String pair : keyValuePairs) {
            String[] keyValue = pair.split(":");
            String key = keyValue[0].replace("\"", "").trim(); // 필드명
            String value = keyValue[1].replace("\"", "").trim(); // 필드 값

            Field field = clazz.getDeclaredField(key);
            field.setAccessible(true);

            // 필드의 타입에 맞게 값을 변환하여 할당
            if (field.getType() == int.class) {
                field.set(obj, Integer.parseInt(value));
            } else if (field.getType() == boolean.class) {
                field.set(obj, Boolean.parseBoolean(value));
            } else {
                field.set(obj, value); // 기본적으로 문자열로 처리
            }
        }

        return obj;
    }

}
