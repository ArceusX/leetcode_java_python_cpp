// 049: Group Anagrams
// Use sorted of chars of str as key to get list to which to 
// add anagram. sorted, being == for anagrams, makes ideal key

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        // new sorted equiv -> [unsorted equivs in strs]s
        Map<String, List<String>> map = new HashMap<>();

        for (String str : strs) {
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            String sorted = new String(chars);

            // if key sorted doesn't exist, assign it list
            if (map.get(sorted) == null) {
                map.put(sorted, new ArrayList<String>());
            }
            map.get(sorted).add(str);
        }

        return new ArrayList<List<String>>(map.values());
    }
}