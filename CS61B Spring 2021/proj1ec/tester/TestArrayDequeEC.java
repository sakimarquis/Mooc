package tester;

import static org.junit.Assert.*;
import org.junit.Test;
import student.StudentArrayDeque;
import edu.princeton.cs.introcs.StdRandom;

public class TestArrayDequeEC {
    @Test
    public void randomizedTest() {
        StringBuilder sb = new StringBuilder();
        StudentArrayDeque<Integer> student = new StudentArrayDeque<>();
        ArrayDequeSolution<Integer> solution = new ArrayDequeSolution<>();

        for (int i = 0; i < 1000; i++) {
            int operationNumber = StdRandom.uniform(0, 4);
            if (operationNumber == 0) {
                student.addFirst(i);
                solution.addFirst(i);
                sb.append("addFirst(").append(i).append(")").append("\n");
                assertEquals(sb.toString(), student.get(0), solution.get(0));
            } else if (operationNumber == 1) {
                student.addLast(i);
                solution.addLast(i);
                sb.append("addLast(").append(i).append(")").append("\n");
                assertEquals(sb.toString(), student.get(student.size() - 1), solution.get(solution.size() - 1));
            } else if (operationNumber == 2 && !student.isEmpty()) {
                Integer actual = student.removeFirst();
                Integer expected = solution.removeFirst();
                sb.append("removeFirst()").append("\n");
                assertEquals(sb.toString(), expected, actual);
            } else if (operationNumber == 3 && !student.isEmpty()) {
                Integer actual = student.removeLast();
                Integer expected = solution.removeLast();
                sb.append("removeLast()").append("\n");
                assertEquals(sb.toString(), expected, actual);
            }
        }

    }
}
