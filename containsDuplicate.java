import java.util.HashSet;
import java.util.Set;

public class containsDuplicate {

    public boolean containsDup(int[] nums) {

        Set<Integer> set = new HashSet<>();
        
        for (int i: nums) {
            set.add(i);
        }

        if (set.size() < nums.length) {
            return true;
        }

        return false;
    }

    public static void main(String[] args) {
      
    }
}
    
