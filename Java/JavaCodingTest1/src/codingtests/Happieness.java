package codingtests;

import java.util.Scanner;

public class Happieness {
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		int num = scanner.nextInt();
		
		int[] scorelist = new int[num];
		
		
		
		for (int i = 0; i < num; i++) {
			scorelist[i] = scanner.nextInt();
		}
		scanner.close();
		
		
		int max = scorelist[0];
		int min = scorelist[0];
		
		for (int i = 0; i < num; i++) {
			if (scorelist[i] > max) {
				max = scorelist[i];
			}
			if (scorelist[i] < min) {
				min = scorelist[i];
			}
		}
		
		System.out.println(max-min);
		
		
	}

}
