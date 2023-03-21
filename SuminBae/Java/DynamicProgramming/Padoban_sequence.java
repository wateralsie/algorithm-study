import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Padoban_sequence {
	
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int testcase = Integer.parseInt(bf.readLine().strip());
		int n = 0;
		StringBuilder answer = new StringBuilder();
		
		for (int i = 0; i < testcase; i++) {
			n = Integer.parseInt(bf.readLine().strip());
			ArrayList<Long> wave = new ArrayList<Long>();
			
			// default
			wave.add(0, 0L);
			wave.add(1, 1L);  wave.add(2, 1L);  wave.add(3, 1L);
			wave.add(4, 2L);  wave.add(5, 2L);
			
			// padoban(n)
			for (int j = 6; j <= n; j++) {
				wave.add(j, wave.get(j-5) + wave.get(j-1));
			}
			
			answer.append(wave.get(n)).append("\n");
		}
		System.out.println(answer);
	}
}
