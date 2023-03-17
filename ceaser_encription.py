t = input("Enter the text to be encrypted : ")
out_str = ''
for i in t:
  if (ord(i) in range(65, 91)):  #big alphabetic characters
    ordi = ord(i)

    #-----------VERSION 1-----------
    #out_str+=chr((((ordi-64)+3)%26)+64)
    """ Problem with this was that when giving the input A-Z it was gving result of each no. correct ecept for 'W'->@
            ABCDEFGHIJKLMNOPQRSTUVWXYZ
            DEFGHIJKLMNOPQRSTUVWXY@ABC

            This was bcoz of problem in moduls sign Eg. 'A'->65->65-64->1->1+3->4->4%26->4->4+64->68->'D' ,
                                                        : 
                                                        'Z'->90->90-64->26->26+3->29->29%26->3->3+64->67->'C'
                                                        but
                                                        'W'->87->87-64->23->23+3->26->26%26->0->0+64->64->'@' #problem bcoz of modulus of 26 by 26 is 0 but we wanted it to be 26

            So in the new version we are subrating [1] before modulus function and then adding it later [+1] 
            i.e now 'A'->1+3->4->4[-1]->3->3%26->3->3[+1]->4...4+64('D')
                     :
                    'W'->23+3->26->26[-1]->25->25%26->25->25[+1]->26...('Z')
                    'Z'->26+3->29->29[-1]->28->28%26->2->2[+1]->3...('C')
                                                        
            """

    #__________-vERSION 2------------------
    """"""
    out_str += chr(((((ordi - 64) + 3) - 1) % 26) + 64 + 1)
    #print(chr((((ordi-64)+3)%26)+64),end="")
  elif (ord(i) in range(97, 123)):  #small alphabetic characters
    ordi = ord(i)
    #out_str += chr((((ordi-96)+3)%26)+96)
    out_str += chr(((((ordi - 96) + 3) - 1) % 26) + 96 + 1)
    #print(chr((((ordi-96)+3)%26)+96),end="")
  else:
    #print(i)
    out_str += i
print("Encrypted text :", out_str)


def decrypt(text):
  out_str = ''
  for i in text:
    ordi = ord(i)
    
    if (ordi in range(65, 91)):  #big alphabetic characters
      
      out_str += chr(((((ordi - 64) - 3) - 1) % 26) + 64 + 1)
      #print(chr((((ordi-64)+3)%26)+64),end="")
    elif (ordi in range(97, 123)):  #small alphabetic characters
      #out_str += chr((((ordi-96)+3)%26)+96)
      out_str += chr(((((ordi - 96) - 3) - 1) % 26) + 96 + 1)
      #print(chr((((ordi-96)+3)%26)+96),end="")
    else:
      #print(i)
      out_str += i
  return(out_str)  
  

print("Decrypted text",decrypt(out_str))
