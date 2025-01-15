package genericrestrict;

public class Pizza extends Food {
    private String kind;

    public Pizza(String name) {
        this.name = name;
    }

    public Pizza(String name, Integer price, String kind) {
        this.name = name;
        this.price = price;
        this.kind = kind;
    }

    @Override
    public String toString() {
        return "Pizza{" +
                "name='" + name + '\'' +
                '}';
    }
}
