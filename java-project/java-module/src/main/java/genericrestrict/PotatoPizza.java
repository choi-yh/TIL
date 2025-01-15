package genericrestrict;

public class PotatoPizza extends Pizza {
    // 부모 생성자를 따라간다.
    public PotatoPizza(String name) {
        super(name);
    }

    // 부모 생성자를 따라간다.
    public PotatoPizza(String name, Integer price, String kind) {
        super(name, price, kind);
    }

    @Override
    public String toString() {
        return "PotatoPizza{" +
                "name='" + name + '\'' +
                '}';
    }
}
