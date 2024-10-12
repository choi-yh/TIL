import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.HashMap;
import java.util.Map;

public class Http {

    public static void main(String[] args) {
        Map<String, Integer> body = Map.of("problem", 1);
        Map response = http("POST", "/start", body, HashMap.class);
        System.out.println(response);
    }

    private static final String BASE_URL = "";

    public static <T> T http(String method, String path, Object body, Class<T> responseType) {
        try {
            HttpURLConnection connection = getHttpURLConnection(method, path);

            // Connect to the server
            connection.connect();

            // TODO: 필요하다면 json 라이브러리 구현이 필요
            ObjectMapper objectMapper = new ObjectMapper();

            if (body != null) {
                // Make JsonInputString
                String jsonInputString = objectMapper.writeValueAsString(body);

                // Write the JSON body to the output stream
                try (OutputStream os = connection.getOutputStream()) {
                    byte[] input = jsonInputString.getBytes("utf-8");
                    os.write(input, 0, input.length);
                }
            }

            // Read the response from the server
            BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            StringBuilder response = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                response.append(line);
            }
            reader.close();

            System.out.println(response);

            connection.disconnect();

            // Convert JSON response to the desired type using custom deserializer
            return objectMapper.readValue(response.toString(), responseType);
        } catch (IOException e) {
            e.printStackTrace();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }

        return null;
    }

    private static HttpURLConnection getHttpURLConnection(String method, String path) throws IOException {
        URL url = new URL(BASE_URL + path);

        // Open a connection to the URL using the HttpURLConnection class
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();

        // Set the request method to GET
        connection.setRequestMethod(method);

        // Add any headers you want to send with the request
        connection.setRequestProperty("Content-Type", "application/json");

        // Set any other options you want to set on the connection
        connection.setDoOutput(true);
        connection.setDoInput(true);

        return connection;
    }

}
