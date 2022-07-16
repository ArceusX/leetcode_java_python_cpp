class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {

        Set<String> set = new HashSet<>(wordList);
        if (!set.contains(endWord)) return 0;

        Set<String> lookSet = new HashSet<>();
        Set<String> checkSet = new HashSet<>();

        lookSet.add(beginWord);
        checkSet.add(endWord);

        int dist = 2;

        while (!lookSet.isEmpty()) {
            Set<String> newLookSet = new HashSet<>();

            for (String str : lookSet) {
                char[] word = str.toCharArray();

                for (int i = 0; i < word.length; i++) {
                    char prevC = word[i];

                    for (char c = 'a'; c <= 'z'; c++) {
                        if (c == str.charAt(i)) continue;
                        word[i] = c;

                        String newWord = new String(word);
                        if (checkSet.contains(newWord)) return dist;

                        if (set.contains(newWord)) {
                            newLookSet.add(newWord);
                            set.remove(newWord);
                        }
                    }
                    word[i] = prevC;
                }
            }
            dist++;
            lookSet = newLookSet;

            if (checkSet.size() < lookSet.size()) {
                Set<String> temp = lookSet;
                lookSet = checkSet;
                checkSet = temp;
            }

        }
        return 0;
    }
}