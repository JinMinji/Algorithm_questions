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
		
		for (int i = 0; i < numOfAllPlayers -1; i++) { //자리는 전체인원-1개만큼 존재.
			memberOrder[i] = ++alphabet; // B부터 차례대로 배열에 입력
		}
	
		int[] numOfTagger = new int[numOfAllPlayers];
		for (int i = 0; i < numOfAllPlayers; i++) { //자리는 전체인원-1개만큼 존재.
			numOfTagger[i] = 0; // B부터 차례대로 배열에 입력
		}
		
		// 달리기가 빠른 사람들은, 절대 술래가 되지않으므로 자리를 이동하지 않는다.
		
		int presentPosition = 0; // 시작 위치는 B가 있는 0부터.
		char tagger = 'A';
		numOfTagger[0] += 1; // 첫술래인 A에 1을 더해준다.
		
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
				//빨리달리는 사람 리스트에 있으면, 원래 술래가 다시 술래.
				char a = 'A';
				numOfTagger[tagger-a] += 1;
			}
			else { 
				char tmp;
				tmp = memberOrder[presentPosition];
				memberOrder[presentPosition] = tagger; // 술래가 자리에 앉고,
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
