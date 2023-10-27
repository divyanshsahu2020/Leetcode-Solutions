class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> ans= new ArrayList();

        List<Integer> prevRow= new ArrayList();

        prevRow.add(1);

        ans.add(prevRow);

        for(int i=0; i< numRows-1; i++)
        {
            List<Integer> currRow= new ArrayList();

            currRow.add(1);

            for(int j=0; j< prevRow.size()-1; j++)
            {
                currRow.add(prevRow.get(j) + prevRow.get(j+1));
            }

            currRow.add(1);

            ans.add(currRow);

            prevRow=currRow;
        }
        return ans;
    }
}