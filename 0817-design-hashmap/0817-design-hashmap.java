import java.util.HashMap;
class MyHashMap {
    private HashMap<Integer,Integer> h;
    public MyHashMap() {
        h=new HashMap<>();
        
    }
    
    public void put(int key, int value) {
        h.put(key,value);
        
    }
    
    public int get(int key) {
        if(h.containsKey(key))
        {
        return h.get(key);
        }
        return -1;
        
    }
    
    public void remove(int key) {
        if(h.containsKey(key)){
        h.remove(key);
        }
        
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */