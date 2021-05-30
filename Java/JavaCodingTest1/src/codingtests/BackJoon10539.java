package codingtests;

import java.util.Scanner;

public class BackJoon10539 {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		
		int len = scanner.nextInt();
		
		int[] arr = new int[len];
		
		for (int i = 0; i < len; i++) {
			arr[i] = scanner.nextInt();
		}
		scanner.close();
		
		int[] result = new int[len];
		
		int sum = 0;
		
		for (int i = 0; i < len; i++) {
			result[i] = (i+1)*arr[i] - sum;
			sum += result[i];
			System.out.print(result[i]+" ");
		}
		
	}
	
}
