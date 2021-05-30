package codingtests;

import java.util.ArrayList;

public class Test2 {

	public ArrayList bracket(int index, char[] order) {
		ArrayList inCharArr = new ArrayList();
		
		while (order[index] != ')') {
			if (order[index] != '(') {
				inCharArr.add(order[index]);
			}
		}
		
		return inCharArr;
	}
	
	public ArrayList operator(int index, char[] order) {
		for (int i = 0 ; i < order.length; i++) {
			order[index];
		}
	}
	
	public boolean isin(char a) {
		return false;
	}

	public static void main(String[] args) {

		int numOfOrder = 2;
		String[] orderArr = {"B2(RG)","3(R2(GB))"};
		
		
	
		
		String[] resultOrder = new String[numOfOrder];
		
		char[] numArr = {'0','1','2','3','4','5','6','7','8','9'};
		
		for (int i = 0; i < numOfOrder; i++) {
			ArrayList charList = new ArrayList();
			
			char[] charArr = null;
			charArr = orderArr[i].toCharArray();
			for (int j = 0; j < charArr.length; j++) {
				
				boolean inout = false; // 괄호가 열려있는지 확인
				boolean isnum = false; // 숫자인지 확인
				for (int n = 0 ; n < 10 ; n++) {
					if (numArr[n] == charArr[j]) {
						isnum = true;
					}
				}
				if (charArr[j] =='(') {
					inout = true;
					charList.add(charArr[j]);
				}
				else if (charArr[j] == ')') {
					inout = false;
				}
			}
			
			for (int j = 0 ; j < charList.size(); j++) {
				System.out.printf("%c",charList.get(j));		
			}	
			System.out.println();
		}
	}
}
