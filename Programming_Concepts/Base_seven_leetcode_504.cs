public class BaseSeven{
    public string convertToBaseSeven(int num){
        bool isNegative=false;
        if(num<0){
            num=num*-1;
            isNegative=true;
        }
        int testi=num;
        string outi="";
        while(testi!=0){
            outi=(testi%7)+outi;
            testi=testi/7;
        }
        if(isNegative){
            outi="-"+outi;
        }
        return outi==""?"0":outi;
    }
}