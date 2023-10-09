public class Main {

    public static double FuncForDoubl(double a){
        double f;
        f = 14 * (1 - Math.cos(17* a)) / Math.pow(a,2);
        return f;
    }
    public static float FuncForFloat(float b){
        float f;
        f = 14 * (1 - (float)Math.cos(17* b)) / (float)Math.pow(b,2);
        return f;
    }
    public static void For3a(){
        for (int i = 0; i < 22 ; i++) {
            double k;
            k = Math.pow(10, -i);
            System.out.println(FuncForDoubl(k));
        }
    }
    public static void For3A(){
        for (int i = 0; i < 22 ; i++) {
            float k;
            k = (float) Math.pow(10, -i);
            System.out.println(FuncForFloat(k));
        }
    }

    public static void main(String[] args) {

        System.out.println("==Double Precision==");
        For3a();
        System.out.println("==Single Precision==");
        For3A();
    }
}