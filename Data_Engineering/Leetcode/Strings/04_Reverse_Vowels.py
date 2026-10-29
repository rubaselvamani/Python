'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower
and upper cases, more than once.

Example 1:

Input: s = "IceCreAm"
Output: "AceCreIm"
Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

'''


#reverse vowels in  a string
def get_vowels(str_1):
    vowels = 'aeiouAEIOU'
    str_vowels = "".join([i for i in str_1 if i in vowels])
    #print(str_vowels[::-1])
    return str_vowels[::-1]

def get_vowel_reversed_word(str_1,reversed_vowels):
    vowel_index = 0
    new_str =''

    for index,value in enumerate(str_1):
        if str_1[index] in 'aeiouAEIOU':
          new_str = new_str + reversed_vowels[vowel_index]
          vowel_index +=1
        else:
            new_str = (new_str + value)
                       #str_1[index])
    return new_str


def main():
    str_1 = "IceCreAm"
    reversed_vowels = get_vowels(str_1)
    print(reversed_vowels)

    vowel_reversed_word =  get_vowel_reversed_word(str_1,reversed_vowels)
    print(f"Vowel reversed string:{vowel_reversed_word} ")

if __name__ == "__main__":
    main()


