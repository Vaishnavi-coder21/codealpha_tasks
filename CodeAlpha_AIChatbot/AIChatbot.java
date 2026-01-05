import java.util.Scanner;

public class SimpleChatbot {

    public static String getResponse(String input) {
        input = input.toLowerCase();

        if (input.contains("hello") || input.contains("hi")) {
            return "Hello! How can I assist you today?";
        } else if (input.contains("how are you")) {
            return "I'm just a program, but I'm doing great!";
        } else if (input.contains("bye") || input.contains("exit")) {
            return "Goodbye! Have a nice day.";
        } else {
            return "Sorry, I don't understand that yet.";
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Chatbot: Hi! Type something to start chatting (type 'exit' to quit).");

        while (true) {
            System.out.print("You: ");
            String userInput = scanner.nextLine();
            String response = getResponse(userInput);
            System.out.println("Chatbot: " + response);
            if (userInput.toLowerCase().contains("exit")) break;
        }
        scanner.close();
    }
}
