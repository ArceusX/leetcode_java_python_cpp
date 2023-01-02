public class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        List<String> repeat = new ArrayList<String>();
        if (s.length() <= 10) return repeat;

        Set<String> once = new HashSet<>(), multiple = new HashSet<>();

        for (int i = 0; i < s.length() - 9; i++) {
            String subStr = s.substring(i, i + 10);

            if (once.contains(subStr)) {
                if (!multiple.contains(subStr)) {
                    multiple.add(subStr);
                    repeat.add(subStr);
                }
            }
            else {
                once.add(subStr);
            }

        }
        return repeat;
    }
}