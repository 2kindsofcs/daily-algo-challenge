
public class Solution {

	public int hammingDistance(int x, int y) {
		int len = (x > y) ? Integer.toBinaryString(x).length() : Integer.toBinaryString(y).length();
		int cnt = 0;
		String xStr = Integer.toBinaryString(x);
		String yStr = Integer.toBinaryString(y);

		while (xStr.length() < len) {
			xStr = "0" + xStr;
		}
		while (yStr.length() < len) {
			yStr = "0" + yStr;
		}

		char[] xcStr = xStr.toCharArray();
		char[] ycStr = yStr.toCharArray();

		for (int i = 0; i < len; i++) {
			if (xcStr[i] != ycStr[i])
				cnt++;
		}
		return cnt;
	}

	public static void main(String[] args) {
		Solution s = new Solution();

		System.out.println(s.hammingDistance(1, 4));
	}
}