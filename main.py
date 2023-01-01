import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)
#user inputs
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text,shift,direction):
  end_text=""
  if direction=="decode":
    shift*=-1
  for i in range(len(text)):
    for position in alphabet:
      #the variable 'x' gives the index of each letter in the alphabet
      x=alphabet.index(position)
      #the variable 'y' gives final index that the shifted letter becomes
      y=x+shift
      #for shift numbers greater than the last index of the alphabet the modulo function loops around the alphabet list
      if y>25:
        y%=len(alphabet)
      #when the text letter at the index and the alphabet letter are a match the shifted alphabet letter is added to the empty string end_text
      if text[i]==position:
        end_text+=alphabet[y]
    #if spaces or symbols in the text, the spaces and symbols will remain untouched.
    if not text[i] in alphabet:
      end_text+=text[i]
        
  print(f"The {direction}d text is {end_text}\n")
 

caesar(text,shift,direction)
go_again=input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
#allows for user to reuse the cipher 
while go_again == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text,shift,direction)
  