import java.util.*;

class  DH
{
    public static void main(String args[])
    {
    System.out.println("***********          ****        ****"
                   + "\n*************        ****        ****" 
                   + "\n****        ***      ****        ****"
                   + "\n****         ****    ****        ****"
                   + "\n****          ****   ****************"
                   + "\n****          ****   ****************"
                   + "\n****         ****    ****        ****"
                   + "\n****        ***      ****        ****"
                   + "\n*************        ****        ****"
                   + "\n***********          ****        ****");
        try{
        int pri_key = Integer.parseInt(args[0]);
        Scanner sc = new Scanner(System.in);
        System.out.println("\nEnter the module");
        int m=sc.nextInt();
        System.out.println("Enter the large random number");
        int n=sc.nextInt();
        int pub_key = (int)Math.pow(m,pri_key)%n;
        if(args.length==1){
        System.out.println("Publick key is   "+ pub_key);
        }

        if(args.length==2){
        int pub_key2 = Integer.parseInt(args[1]);
        int session_key = (int)Math.pow(pub_key2,pri_key)%n;
        System.out.println("Session key is:   " +session_key);
        }
    }
    catch(ArrayIndexOutOfBoundsException e){
        System.out.println("\n\nIf you want to get Public Key You need to provide private key of sender ex : java DH privatekey \n"
        + "If you need to get session key you need to provide private key and public key of reciver ex : java DH privatekey publickey\n");
    }
    catch(Exception e)
    {
        System.out.println("\n\nYou need to provide numerical value\n");
    }
    }
}
