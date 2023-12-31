> https://gmlwjd9405.github.io/2018/07/06/design-pattern.html

# 디자인 패턴 구조
| Context                                                            | Problem                                                                            | Solution                                                                                                                  |
|--------------------------------------------------------------------|------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| - 문제가 발생하는 상황 기술 (패턴이 적용될 수 있는 상황) <br/> - 경우에 따라서는 패턴이 유용하지 못한 상황 | - 패턴이 적용되어 해결될 필요가 있는 여러 디자인 이슈들을 기술<br/> - 이때, 여러 제약 사항과 영향력도 문제 해결을 위해서 고려해야 한다. | - 문제를 해결하도록 설계를 구성하는 요소들과 그 요소들 사이의 관계, 책임, 협력 관계를 기술 <br/> - 해결은 반드시 구체적인 구현 방법이나 언어에 의존적이지 않으며 다양한 상황에 적용할 수 있는 일종의 템플릿 |


# 디자인 패턴 종류
| Creational Pattern                                                                                                     | Structural Pattern                                                                                                                    | Behavioral Pattern                                                                                                                                                                                                                         |
|------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| - 객체 생성에 관련된 패턴<br/> - 객체의 생성과 조합을 캡슐화 -> 특정 객체가 생성되거나 변경되어도 프로그램 구조에 영향을 크게 받지 않도록 유연성 제공                             | - 클래스나 객체를 조합해 더 큰 구조를 만드는 패턴<br/> - 서로 다른 인터페이스를 지닌 2개의 객체를 묶어 단일 인터페이스를 제공하거나 객체들을 서로 묶어 새로운 기능을 제공하는 패턴                            | - 객체나 클래스 사이의 알고리즘이나 책임 분배에 관련된 패턴<br/> - 한 객체가 혼자 수행할 수 없는 작업을 여러 개의 객체로 어떻게 분배하는지, 이렇게 작업하면서 객체 사이의 결합도를 최소하하는 것에 중점을 둔다.                                                                                                                |
| Abstract Factory (추상 팩토리) <br/>Builder (빌더) <br/>Factory Methods (팩토리 메서드) <br/>Prototype (프로토타입) <br/>Singleton (싱글턴) | Adapter (어댑터) <br/>Bridge (브리지) <br/>Composite (컴퍼지트) <br/>Decorator (데코레이터) <br/>Facade (퍼사드)<br/>Flyweight (플라이웨이트)<br/>Proxy (프록시) | Chain of Responsibility (책임 연쇄)<br/> Command (커맨드) <br/> Interpreter (인터프리터) <br/>Iterator (이터레이터) <br/> Mediator (미디에이터) <br/> Observer (옵저버) <br/>State (스테이트) <br/>Strategy (스테레이티지) <br/> Template Method (템플릿 메서드) <br/>Visitor (비지터) |


---
> https://refactoring.guru/ko/design-patterns/creational-patterns

