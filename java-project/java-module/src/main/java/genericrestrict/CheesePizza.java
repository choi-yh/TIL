package genericrestrict;

public class CheesePizza extends Pizza {
    public CheesePizza(String name) {
        super(name);
    }

    public CheesePizza(String name, Integer price, String kind) {
        super(name, price, kind);
    }

    @Override
    public String toString() {
        return "CheesePizza{" +
                "name='" + name + '\'' +
                '}';
    }
}
