class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        List<String> repeat = new ArrayList<>();
        if (s.length() <= 10) return repeat;

        Set<Integer> once = new HashSet<>(), multiple = new HashSet<>();

        Map<Character, Integer> map = new HashMap<>(Map.of(
            'A', 0, 'C', 1, 'G', 2, 'T', 3));

        int hash = 0;
        for (int i = 0; i < s.length(); i++) {
            hash = (hash << 2) + map.get(s.charAt(i));

            if (i >= 9) {
                hash = ((1 << 20) - 1) & hash;

                if (once.contains(hash)) {
                    if (!multiple.contains(hash)) {
                        repeat.add(s.substring(i - 9, i + 1));
                        multiple.add(hash);
                    }
                }

                else {
                    once.add(hash);
                }
            } 
        }
        return repeat;
    }
}