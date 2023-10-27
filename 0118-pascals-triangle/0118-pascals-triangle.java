class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res=new ArrayList<>();
        ArrayList<Integer> temp=new ArrayList<>();
        temp.add(1);
        res.add(temp);
        for(int i=0;i<numRows-1;i++)
        {
            ArrayList<Integer> curr=new ArrayList<>();
            curr.add(1);
            for(int j=0;j<temp.size()-1;j++)
            {
                curr.add(temp.get(j)+temp.get(j+1));

            }
            curr.add(1);
            res.add(curr);
            temp=curr;
        }
        return res;
    }
}