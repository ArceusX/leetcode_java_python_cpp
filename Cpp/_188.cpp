// 188: Max Profit on k Pairs of Buys and Sells (see _123.cpp)

// Dynamic programming: O(nk) time; k is const
// Maximize sell profit up to today by solving 
// subproblem to minimize buy price up to yesterday
// Minimize buy  = price - max of prior sell
// Maximize sell = price - min of prior buy

class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {

        // Create, set 0th entry for sells == 0 so buys[1]
        // can refer to sells[1 - 1]. buys[0] is unused 
    	vector<int> buys (k + 1, 1001);
    	vector<int> sells(k + 1, 0);
        
        for (int price : prices) {
        	for (int i = 1; i <= k; i++) {
        		buys [i] = min(buys [i], price - sells[i - 1]);
        		sells[i] = max(sells[i], price - buys [i   ]);
        	}
        }

        return sells.back(); // Profit of final (kth) sell
    }
};