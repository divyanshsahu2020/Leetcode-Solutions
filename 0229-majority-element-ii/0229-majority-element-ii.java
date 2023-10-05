class Solution {
    public List<Integer> majorityElement(int[] nums) {
        int n=nums.length;
        ArrayList<Integer> res=new ArrayList<>();
        HashMap<Integer,Integer> freq=new HashMap<>();
        for(int x:nums)
        {
            if(freq.containsKey(x))
            {
                freq.put(x,freq.get(x)+1);
            }
            else
            {
                freq.put(x,1);
            }

        }
        for(int key:freq.keySet())
        {
            if(freq.get(key)>(n/3))
            {
                res.add(key);
            }

        }
        return res;
        
    }
}