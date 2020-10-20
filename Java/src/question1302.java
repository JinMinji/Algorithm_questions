import java.util.*;

public class question1302 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();

        String[] books = new String[num];

        for(int i = 0;i<num;i++)
        {
            books[i] = scan.next();
        };

        Map<String, Integer> book_count = new HashMap<String, Integer>();

        for(int i = 0; i<num; i++)
        {
            if(Arrays.asList(book_count.keySet()).contains(books[i]))
            {
                book_count.put(books[i], book_count.get(books[i])+1);
            }
            else
            {
                book_count.put(books[i], 1);
            }
        }


        System.out.printf("");
    }

}

