import java.util.ArrayList
import java.util.LinkedList
import java.util.Scanner

fun main(args: Array<String>) {
    val input = Scanner(System.`in`)
    val numStages = input.nextInt()
    val stages = ArrayList<LinkedList<IntArray>>(numStages)
    for (e in stages) {
        val words = input.nextLine().split(" ")
        val numEvents = Integer.parseInt(words[0])
        val stage = LinkedList<IntArray>()
        var i = 1
        while (i <= numEvents) {
            val inicio = Integer.parseInt(words[i])
            val fin = Integer.parseInt(words[i + 1])
            val canciones = Integer.parseInt(words[i + 2])
            stage.add(intArrayOf(inicio, fin, canciones))
            i += 3
        }
        stage.sortBy { event -> event[2] }
    }
    val result = emptyList<IntArray>()
    for (stage:LinkedList<IntArray> in stages){
        for(event:IntArray in stage){
            for (scheduled:IntArray in result){
                var inicioS = scheduled[0];
                var finS = scheduled[0];
            }
        }
    }
}
