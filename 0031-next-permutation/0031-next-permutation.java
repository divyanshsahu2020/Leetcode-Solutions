class Solution {
    public void nextPermutation(int[] nums) {
        int check[]=nums.clone();
        for(int i=nums.length-1;i>=0;i--)
        {
            int temp=101;
            for(int j=i+1;j<nums.length;j++)
            {
                if(nums[i]<nums[j] && nums[j]<temp)
                {
                    temp=nums[j];
                }
            }
            if (temp!=101)
            {
                ArrayList <Integer>temp1=new ArrayList<>();
                for(int x=i;x<nums.length;x++)
                {
                    temp1.add(nums[x]);
                }
                nums[i]=temp;
                int inde=temp1.indexOf(temp);
                temp1.remove(inde);
                Collections.sort(temp1);
                int count=0;
                for(int x=i+1;x<nums.length;x++)
                {
                    nums[x]=temp1.get(count);
                    count++;
                }
                break;
            }

            
        }
        if(Arrays.equals(nums,check))
            {
               for(int i=0;i<nums.length;i++)
               {
                   nums[i]=check[nums.length-1-i];
               }
            }
    }
}