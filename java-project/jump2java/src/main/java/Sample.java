abstract class Predator extends Animal{
    abstract String getFood();
}

interface Barkable {
    void bark();
}

class Animal {
    String name;

    public void setName(String name) {
        this.name = name;
    }
}

class Tiger extends Predator implements Barkable {
    public String getFood() {
        return "tiger food";
    }

    public void bark() {
        System.out.println("어흥");
    }
}

class Lion extends Predator implements Barkable {
    public String getFood() {
        return "lion food";
    }

    public void bark() {
        System.out.println("으르렁");
    }
}

class ZooKeeper {
    void feed(Predator predator) {
        System.out.println(predator.getFood() + " feeding");
    }
}

class Bouncer {
    void barkAnimal(Barkable animal) {
        animal.bark();
    }
}

class Dog extends Animal {
    // 디폴트 생성자
    Dog() {

    }

    void sleep() {
        System.out.println(this.name + " sleep");
    }
}

class HouseDog extends Dog {
    // 생성자: 메서드명이 클래스명과 동일하고 리턴 자료형을 정의하지 않는 메서드
    // 생성자 오버로딩
    HouseDog(String name) {
        this.setName(name);
    }

    void sleep() { // 메서드 오버라이딩
        System.out.println(this.name + " sleep in house");
    }

    void sleep(int hour) { // 메서드 오버로딩
        System.out.println(this.name + " zzz in house for " + hour + " hours");
    }
}

public class Sample {
    public static void main(String[] args) {
        ZooKeeper zooKeeper = new ZooKeeper();

        Tiger tiger  = new Tiger();
        Lion lion = new Lion();

        Bouncer bouncer = new Bouncer();
        bouncer.barkAnimal(tiger);
        bouncer.barkAnimal(lion);
    }
}
