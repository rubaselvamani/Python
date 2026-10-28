class StrVowelReverser:
   def  __init__(self, text: str) -> str :
       # initializing the constructor
       self.text = text
       self.vowel = 'aeiouAEIOU'

   def get_vowels(self):
        vowels_only = "".join(i for i in self.text if i in self.vowel)
        return vowels_only[::-1]

   def reverse_vowels_only(self,reversed_vowels):
        vowels_index =0
        vowels_reversed_str = ''
        for index,value in enumerate(self.text):
            if value in self.vowel:
                vowels_reversed_str = vowels_reversed_str + reversed_vowels[vowels_index]
                vowels_index +=1
            else:
               vowels_reversed_str = vowels_reversed_str + value
        return vowels_reversed_str

   def vowel_reversed_str(self):
       reversed_vowels = self.get_vowels()
       vowel_reversed_str = self.reverse_vowels_only(reversed_vowels)

       return vowel_reversed_str


if __name__ == "__main__":
    str_input = input("enter the string: ")
    vr = StrVowelReverser(str_input)
    reversed_text = vr.vowel_reversed_str()
    print(f"Given text: {vr.text}")
    print(f"Vowel reversed string: {reversed_text}")


