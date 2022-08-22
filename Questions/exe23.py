"""
<<<<<<< HEAD
Want to try some string methods yourself? Give it a go!
Fill in the gaps in the initials function so that it returns the initials of the words contained in the phrase received, in upper case. For example:
"Universal Serial Bus" should return "USB"; "local area network" should return "LAN”.
"""

def initials(phrase):
    words = phrase.title()
    result = ""
    for word in words:
        if word.isupper(): 
            result += word
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS
=======
Modify the double_word function so that it returns the same word repeated twice, followed by the
length of the new doubled word. For example, double_word("hello") should return hellohello10.
"""

def double_word(word):
    aux = "{0}{1}".format((word * 2), str(len(word * 2)))
    return aux

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0
>>>>>>> a59a59bbf31f35306e14af1a068a3447b55f7c09
