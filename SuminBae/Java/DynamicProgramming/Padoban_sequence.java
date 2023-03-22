import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Padoban_sequence {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder answer = new StringBuilder();
		int testcase = Integer.parseInt(br.readLine().strip());
		int n = 0;
		
		for (int i = 0; i < testcase; i++) {
			n = Integer.parseInt(br.readLine().strip());
			long[] wave = new long[101];
			
			// default
			wave[1] = 1;  wave[2] = 1;  wave[3] = 1;
			wave[4] = 2;  wave[5] = 2;
			
			// padoban(n)
			for (int j = 4; j <= 100; j++) {
				wave[j] = wave[j-2] + wave[j-3];
			}
			answer.append(wave[n]).append("\n");
		}
		System.out.println(answer);
	}
}