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

    public void  Eliminate(){
        String result = "";
        String num = this.left.trim().substring(left.indexOf(getSign())+2);
       
       
        if(getSign().equals("-")){
            System.out.println("Add "+num+" to both sides");
            result  = this.left + "+ " + num + " =" +right+" + "+num;
        }
        else if(getSign().equals("+")){
            System.out.println("Substract "+num+" to both sides");
            result = this.left +"- "+num + " ="+ right+" - "+num;
        }

        System.out.println(result);
    }

    public void Simpify(String l, String r){

    }

    void setLeft( String l){
        this.left = l;
    }
    void setRight(String r){
        this.right = r;
    }


 
}
