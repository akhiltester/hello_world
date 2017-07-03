def reverse(text):
    length= len(text)
    print ("The length of the string is: ",length) #text added
    y=0
    rv=""
    
    while length-1>=0:
        rv=rv+text[length-1]
        length=length-1
    print (rv)    
        
   
   
    
rn="akhil" 
reverse(rn)
