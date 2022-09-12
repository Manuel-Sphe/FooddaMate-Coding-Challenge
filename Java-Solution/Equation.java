public class Equation {
    private String left , right;

    public Equation(String l, String r ){
        this.left = l; this.right = r;
    }


    public String getSign(){
        char [] ch = this.left.toCharArray();

        char sign =' ';
        for(int i = 0 ;i<ch.length;++i){
            if (ch[i]=='-' || ch[i]=='+'){
                sign = ch[i];
                break;
            }
        }

        return ""+sign;
    }

    public String getNum(){
        return this.left.trim().substring(left.indexOf(getSign())+1);
    }

    public void  Eliminate(){
        String result = "";
        String num = getNum();
       
       
        if(getSign().equals("-")){
            System.out.println("Add "+num+" to both sides");
            result  = this.left + " + " + num + " =" +right+" + "+num;
        }
        else if(getSign().equals("+")){
            System.out.println("Substract "+num+" to both sides");
            result = this.left +" - "+num + " = "+ right+" - "+num;
        }

        System.out.println(result);
    }

    public void Simpify(){
        System.out.println("Simplify");
        int rhs = Integer.parseInt(right.trim());
        int ans = rhs + Integer.parseInt(getNum());

        String lhs = left.substring(0,left.indexOf('x')+1);
        
        System.out.println(lhs +" = "+ ans);

        setLeft(lhs);
        setRight(""+ans);

    }

    void Final_Ans(){
        
        String l = getLeft();
        
        String x_coff = l.substring(0, l.indexOf('x'));
        System.out.println("Devide both side by the same factor");
        System.out.println("x = "+getRight()+'/'+x_coff);
    }

    void setLeft( String l){
        this.left = l;
    }
    void setRight(String r){
        this.right = r;
    }

    String getLeft(){
        return this.left;
    }

    String getRight(){
        return this.right;
    }


 
}
