import java.util.Scanner;

public class N10818 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] n = new int[sc.nextInt()]; // 배열 크기 입력 받음

        int small = 1000000, large = -1000000; // 가장 작은 수, 가장 큰 수를 설정
        int get = 0; // 입력 받아 비교할 수

        for (int i = 0; i < n.length; i++) {  // 배열 크기 만큼 반복
            get = sc.nextInt(); // 비교 할 수 입력
            if(get < small){  // 입력 받은 수가 현재 제일 작은 수 보다 작을 경우
                small = get;
            }
            else if(get > large){ // 입력 받은 수가 현재 제일 큰 수 보다 클 경우
                large = get;
            }
        }
        System.out.println(small + " " + large); //입력 받은 수 중 제일 작은 수
    }
}
