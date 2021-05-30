package codingtests;

import java.util.ArrayList;

public class Test {
	
	public static void main(String[] args) {
		
		int numOfAllPlayers = 17;
	    int numOfQuickPlayers = 5;
	    char[] namesOfQuickPlayers = {'B','D','I','M','P'};
	    int numOfGames = 11;
	    int[] numOfMovesPerGame = {3, -4, 5, 6, -7,-8, 10, -12, -15, -20, 23};
		
		char[] memberOrder = new char[numOfAllPlayers];
		
		char alphabet = 'A';
		
		for (int i = 0; i < numOfAllPlayers -1; i++) { //�ڸ��� ��ü�ο�-1����ŭ ����.
			memberOrder[i] = ++alphabet; // B���� ���ʴ�� �迭�� �Է�
		}
	
		int[] numOfTagger = new int[numOfAllPlayers];
		for (int i = 0; i < numOfAllPlayers; i++) { //�ڸ��� ��ü�ο�-1����ŭ ����.
			numOfTagger[i] = 0; // B���� ���ʴ�� �迭�� �Է�
		}
		
		// �޸��Ⱑ ���� �������, ���� ������ ���������Ƿ� �ڸ��� �̵����� �ʴ´�.
		
		int presentPosition = 0; // ���� ��ġ�� B�� �ִ� 0����.
		char tagger = 'A';
		numOfTagger[0] += 1; // ù������ A�� 1�� �����ش�.
		
		for (int i = 0; i < numOfGames; i++) {
			presentPosition = (presentPosition + numOfMovesPerGame[i]) % (numOfAllPlayers-1);
			if (presentPosition < 0) {
				presentPosition = numOfAllPlayers-1+presentPosition;
			}
			
			boolean isFast = false;
			
			for (int j = 0; j< numOfQuickPlayers; j++) {
				if (memberOrder[presentPosition] == namesOfQuickPlayers[j]) {
					isFast = true;
					break;
				}		
			}
			
			if (isFast){
				//�����޸��� ��� ����Ʈ�� ������, ���� ������ �ٽ� ����.
				char a = 'A';
				numOfTagger[tagger-a] += 1;
			}
			else { 
				char tmp;
				tmp = memberOrder[presentPosition];
				memberOrder[presentPosition] = tagger; // ������ �ڸ��� �ɰ�,
				tagger = tmp;
				char a = 'A';
				numOfTagger[tagger-a] += 1;
			}
		}
		char a = 'A';
		for (int i = 0; i < numOfAllPlayers-1; i++) {
			System.out.println(memberOrder[i] + " " + numOfTagger[memberOrder[i]-a]);
		}
		System.out.println(tagger + " " + numOfTagger[tagger-a]);
	}
}
