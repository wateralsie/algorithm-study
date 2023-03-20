import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Fibonacci_function {
	
	static Integer[][] fibo = new Integer[41][2];

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int testCase = Integer.parseInt(bf.readLine());
		int n= 0;
		StringBuilder answer = new StringBuilder();
		
		for (int i = 0; i < testCase; i++) {
			n = Integer.parseInt(bf.readLine());
			
			// fibonacci(0)
			fibo[0][0] = 1;		// 0이 몇 번
			fibo[0][1] = 0;		// 1이 몇 번
			// fibonacci(1)
			fibo[1][0] = 0;
			fibo[1][1] = 1;
			
			fibonacci(n);
			answer.append(fibo[n][0] + " " + fibo[n][1]).append("\n");
		}
		System.out.println(answer);

	}
	
	public static Integer[] fibonacci(int N) {
		for (int i = 2; i <= N; i++) {
			fibo[i][0] = fibo[i-1][0] + fibo[i-2][0];
			fibo[i][1] = fibo[i-1][1] + fibo[i-2][1];
		}
		return fibo[N];
	}
}