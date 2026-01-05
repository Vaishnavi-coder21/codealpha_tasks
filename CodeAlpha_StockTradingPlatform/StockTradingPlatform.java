import java.util.*;

class Stock {
    String symbol;
    double price;

    public Stock(String symbol, double price) {
        this.symbol = symbol;
        this.price = price;
    }
}

class User {
    String name;
    Map<String, Integer> portfolio = new HashMap<>(); // symbol -> quantity
    double cash;

    public User(String name, double cash) {
        this.name = name;
        this.cash = cash;
    }

    public void buyStock(Stock stock, int quantity) {
        double cost = stock.price * quantity;
        if (cost > cash) {
            System.out.println("Not enough cash to buy.");
            return;
        }
        cash -= cost;
        portfolio.put(stock.symbol, portfolio.getOrDefault(stock.symbol, 0) + quantity);
        System.out.println("Bought " + quantity + " shares of " + stock.symbol);
    }

    public void sellStock(Stock stock, int quantity) {
        int owned = portfolio.getOrDefault(stock.symbol, 0);
        if (quantity > owned) {
            System.out.println("You don't own enough shares.");
            return;
        }
        portfolio.put(stock.symbol, owned - quantity);
        cash += stock.price * quantity;
        System.out.println("Sold " + quantity + " shares of " + stock.symbol);
    }

    public void printPortfolio() {
        System.out.println("Portfolio for " + name + ":");
        portfolio.forEach((symbol, qty) -> System.out.println(symbol + ": " + qty + " shares"));
        System.out.println("Cash: $" + cash);
    }
}

public class StockTradingPlatform {
    public static void main(String[] args) {
        Stock apple = new Stock("AAPL", 150.0);
        Stock google = new Stock("GOOG", 2800.0);

        User user = new User("Alice", 10000);

        user.buyStock(apple, 50);
        user.buyStock(google, 2);
        user.sellStock(apple, 10);
        user.printPortfolio();
    }
}
