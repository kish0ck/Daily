var x = 5


fun main() {
    println("Hello, world!!!")
    
    x += 1
    
    println(x)
    
    val a : Int = 1
    
    val b = 1
    
    val c : Int
    c = 3
    
    val d : Int //지연 할당 을 사용할땐 type 필수적으로 선언
    d = 123
    
    // val(value)    readOnly
    // var(variable) 재할당이 가능
    
    var e : String = "Hello"
    e = "World"
    
    /*
    var f = 123
    f = "hi"
    // 최초 타입 Int타입 이기때문에 String으로 변경하게 되면 컴파일 오류
    */
    
    
}
