package genericrestrict;

public class Water extends Food {

    public Water(String name) {
        this.name = name;
    }

    public Water(String name, Integer price) {
        this.name = name;
        this.price = price;
    }

    @Override
    public String toString() {
        return "Water{" +
                "name='" + name + '\'' +
                '}';
    }
}
