def reverse(text):
    length= len(text)
    print (length)
    y=0
    rv=""
    
    while length-1>=0:
        rv=rv+text[length-1]
        length-=1
    print (rv)    
        
   
   
    
rn="akhil" 
reverse(rn)