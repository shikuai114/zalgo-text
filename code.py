import random

def zalgo_text(text, intensity=10):#The number here is adjustable,Depends on how scary you want him to be
       combining_chars = [chr(i) for i in range(0x0300, 0x036F)]
       zalgo_text = []
       for char in text:
           zalgo_text.append(char)
           for _ in range(intensity):
               zalgo_text.append(random.choice(combining_chars))
       return ''.join(zalgo_text)
       
use_input = input("text here:")

result = zalgo_text(use_input)

#end
print(result)
