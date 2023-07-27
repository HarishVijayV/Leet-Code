class Solution {
    public boolean isValid(String s) {
        Stack<Character> my = new Stack<>();
        for(char x:s.toCharArray()){
            if ((x=='{')||(x=='(')||(x=='[')){
                my.push(x);}
            if(!my.empty()){
                if(x=='}'){
                    if (my.peek()=='{'){
                        my.pop();
                    }
                    else{
                        my.push(x);
                    }
                }
                else if(x==')'){
                    if (my.peek()=='('){
                        my.pop();
                    }
                    else{
                        my.push(x);
                    }
                }
                else if(x==']'){
                    if (my.peek()=='['){
                        my.pop();
                    }
                    else{
                        my.push(x);
                    }
                }
            }else{
                my.push(x);
            }
        } 
        if (my.empty()){
            return true;
        }
        return false;
    }
    
}