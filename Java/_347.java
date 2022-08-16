class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        
        // Default is min. reverseOrder changes to max
        Queue<Pair<Integer, Integer>> pQueue = new PriorityQueue<>(
        	nums.length, Collections.reverseOrder());
        int[] ret = new int[k];

        // If key not found, give default val 1.
        for (int num : nums) {
        	map.merge(num, 1, (a, b) -> a + 1);
        }

        for (var entry : map.entrySet()) {
        	pQueue.add(new Pair(entry.getValue(), entry.getKey()));
        }

        while (k-- != 0) ret[k] = pQueue.poll().second;
        return ret;
    }
}

class Pair<F extends Comparable<F>, S extends Comparable<S>>
    implements Comparable<Pair<F, S>> {
    
    public F first;
    public S second;
    public Pair(F first, S second){
        this.first = first;
        this.second = second;
    }

    @Override
    public int compareTo(Pair<F, S> o) {
        int retVal = first.compareTo(o.first);
        if (retVal != 0) return retVal;
        return second.compareTo(o.second);
    }
}