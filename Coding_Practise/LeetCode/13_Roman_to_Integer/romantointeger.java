import java.util.*;

public class romantointeger{
    public static void main(String[] args){
        // System.out.println("Working");
        Scanner scanner=new Scanner(System.in);
        // String inp=scanner.next();
        String inp="MCMXCIV";
        HashMap<String,Integer> map=new HashMap<>();
        map.put("I", 1);
        map.put("V", 5);
        map.put("X", 10);
        map.put("L", 50);
        map.put("C", 100);
        map.put("D", 500);
        map.put("M", 1000);
        String[] splitData=inp.split("");
        int outi=0;
        for(int i=splitData.length-1;i>=0;i--){
            if(i<splitData.length-1 && map.get(splitData[i+1])>map.get(splitData[i])){
                outi-=map.get(splitData[i]);
            }else{
                outi+=map.get(splitData[i]);
            }
        }
        System.out.println(outi);
    }
}