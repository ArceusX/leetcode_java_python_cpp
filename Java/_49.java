class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

    	Map<String, List<String>> map = new HashMap<String, List<String>>();
        List<List<String>> ret;
        for (String str : strs) {
        	char[] temp = str.toCharArray();
            Arrays.sort(temp);
        	String sorted = new String(temp);
        	map.computeIfAbsent(sorted, k -> new ArrayList<String>()).add(str);
        }

        ret = new ArrayList<List<String>>(map.size());
        for (List<String> group : map.values()) {
        	ret.add(group);
        }

        return ret;
    }
}