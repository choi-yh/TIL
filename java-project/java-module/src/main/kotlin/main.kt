fun main() {
    // 1. Hello world
    println("Hello World!")

    // val is read-only variables
    val popcorn: Long = 5
    val hotdog: Float = 7f
    val isEnabled: Boolean = true

    // var is mutable variables
    var customers = 10

    customers = 8
    println(customers)

    // 2. Basic types
    val a: Int = 1000
    val b: String = "log message"
    val c: Double = 3.14
    val d: Long = 100_000_000_000_000
    val e: Boolean = false
    val f: Char = '\n'

    // 3. Collections

    // List
    // Read only list
    val readOnlyShapes: List<String> = listOf("triangle", "square", "circle")
    println(readOnlyShapes)
    println("The first item in the list is ${readOnlyShapes[0]}")
    println("The last item in the list is ${readOnlyShapes.last()}")

    // Mutable list
    val shapes: MutableList<String> = mutableListOf("triangle", "square", "circle")
    println(shapes)

    // Set & Map
    // Read-only map
    val readOnlyJuiceMenu = mutableMapOf("apple" to 100, "kiwi" to 190, "orange" to 100)
    println(readOnlyJuiceMenu)
    println("The value of apple juice is: ${readOnlyJuiceMenu["apple"]}") // map 에 접근하기 위해서는 파이썬과 비슷
    readOnlyJuiceMenu.remove("melon") // 없는 키 값을 지우면 아무 일도 일어나지 않는다.
    println(readOnlyJuiceMenu)

    // Exercise 2
    val SUPPORTED = setOf("HTTP", "HTTPS", "FTP")
    val requested = "smtp"
    val isSupported: Boolean = requested.uppercase() in SUPPORTED // Write your code here
    println("Support for $requested: $isSupported")

    // Exercise 3
    val number2word = mapOf(1 to "one", 2 to "two", 3 to "three") // Write your code here
    val n = 2
    println("$n is spelt as '${number2word[2]}'")
}