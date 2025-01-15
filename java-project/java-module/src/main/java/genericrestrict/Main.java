package genericrestrict;

import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {

        List<Pizza> pizzaList = new ArrayList<>();
        pizzaList.add(new Pizza("pizza"));
        printExtends(pizzaList); // Pizza{name='pizza'}
        printSuper(pizzaList); // Pizza{name='pizza'}

        System.out.println();

        List<PotatoPizza> potatoPizzas = new ArrayList<>();
        potatoPizzas.add(new PotatoPizza("potato"));
        printExtends(potatoPizzas); // PotatoPizza{name='potato'}
//        printSuper(potatoPizzas); // <? super Pizza> 는 Pizza 의 부모만 되기 때문에 불가능

        List<Water> waterList = new ArrayList<>();
        waterList.add(new Water("Water1"));
        waterList.add(new Water("Water2"));

        // print_ 메서드는 Pizza 의 부모 혹은 자식이어야 하기 때문에 water 는 불가능
//        printExtends(waterList);
//        printSuper(waterList);

    }

    private static void printExtends(List<? extends Pizza> list) {
        for (Pizza obj : list) {
            System.out.println(obj);
        }
    }

    private static void printSuper(List<? super Pizza> list) {
        for (Object obj : list) {
            System.out.println(obj);
        }
    }
}
