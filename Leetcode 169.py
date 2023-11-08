class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = None
        count = 0

        for num in nums:
            if count == 0:
                ans = num
            count += (1 if num == ans else -1)         
        return ans
    

    
class Solution {
    public int majorityElement(int[] nums) {
        Arrays.sort(nums);
        return nums[nums.length/2];
    }
}


class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap();
        for(int num : nums){
            if(!map.containsKey(num))
                map.put(num, 1);
            else{
                map.put(num, map.getOrDefault(num, 1) + 1);
            }  
        }

        int max = 0;
        int result = 0;
        for (Map.Entry<Integer, Integer> e : map.entrySet()) {
            int key = e.getKey();
            int value = e.getValue();
            if(max < value){
                max = value;
                result = key;
            }
        }        
        return result;
    }
}