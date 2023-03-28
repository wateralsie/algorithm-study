import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Finding_number {
	
	public static int[] arr;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		StringBuilder sb = new StringBuilder();
		
		// n과 n개의 정수
		int n = Integer.parseInt(br.readLine());
		arr = new int[n];
		
		for (int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(arr);
		
		// m과 탐색 대상 숫자
		int m = Integer.parseInt(br.readLine());
		st = new StringTokenizer(br.readLine(), " ");
		
		for (int i = 0; i < m; i++) {
			// 탐색 값 있을 때 1
			if (binarySearch(Integer.parseInt(st.nextToken())) >= 0) {
				sb.append(1).append("\n");
			}
			// 없을 때 0
			else {
				sb.append(0).append("\n");
			}
		}
		System.out.println(sb);
	}
	

	public static int binarySearch(int target) {
		// mid 구하기
		int start = 0;
		int end = arr.length - 1;
		
		// mid & tmp 비교
		while (start <= end) {
			int mid = (start + end) / 2;
			
			if (target < arr[mid]) {
				end = mid - 1;
			}
			else if (target > arr[mid]) {
				start = mid + 1;
			}
			else {
				return mid;
			}
		}
		// 찾는 값이 없을 때
		return -1;
	}
}
