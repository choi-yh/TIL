import com.fasterxml.jackson.databind.ObjectMapper;
import org.junit.jupiter.api.Test;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Map;

public class HttpTest {

    @Test
    public void post() throws IOException {
        final String POST = "POST";
        final String BASE_URL = "https://7zszxecwra.execute-api.ap-northeast-2.amazonaws.com/api";
        final String X_AUTH_TOKEN = "X-Auth-Token";
        final String token = "7dcaaa0ef3df87db76585287eb15857d";
        final Map<String, Integer> body = Map.of("problem", 1);

        URL url = new URL(BASE_URL + "/start");

        // connection
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();

        // connection setting
        connection.setRequestMethod(POST);

        connection.setRequestProperty("Content-Type", "application/json");
        connection.setRequestProperty("X-Auth-Token", "7dcaaa0ef3df87db76585287eb15857d");

        connection.setDoOutput(true); // output 데이터 (body) 값이 있는지 여부

        // body to jsonString
        ObjectMapper objectMapper = new ObjectMapper();
        String jsonString = objectMapper.writeValueAsString(body);

        DataOutputStream outputStream = new DataOutputStream(connection.getOutputStream());
        outputStream.writeBytes(jsonString);
        outputStream.flush();
        outputStream.close();

        // get response
        int responseCode = connection.getResponseCode();

        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
        StringBuilder stringBuffer = new StringBuilder();
        String inputLine;

        while ((inputLine = bufferedReader.readLine()) != null) {
            stringBuffer.append(inputLine);
        }
        bufferedReader.close();

        Map data = objectMapper.readValue(stringBuffer.toString(), Map.class);

        System.out.println("responseCode = " + responseCode + "\ndata = " + data);
    }

}
