import string

# Encrypt function definition which takes arguments str and int
def encrypt(str, addNum):
    ''' This function will take a text and encrypt it by adding addNum shifts'''
    if addNum == 0:
        return str
    encryptStr = ""

    # Shift Lowercase
    for i in range(len(str)):
        if str[i] in string.ascii_lowercase:
            for j in range(len(string.ascii_lowercase)):
                # find index of match
                if str[i] == string.ascii_lowercase[j]:
                    newLower = j + addNum
                    if newLower > 25:
                        newLower = newLower % 26
                    elif newLower < 0:
                        newLower = newLower % 26
                    encryptStr += (string.ascii_lowercase[newLower])

        # Uppercase Shift 
        elif str[i] in string.ascii_uppercase:
            for k in range(len(string.ascii_uppercase)):
                if str[i] == string.ascii_uppercase[k]:
                    newUpper = k + addNum
                    if newUpper > 25:
                        newUpper = newUpper % 26
                    elif newUpper < 0:
                        newUpper = newUpper % 26
                    
                    encryptStr += (string.ascii_uppercase[newUpper])
 
        # Non-char (no change)
        else:
            encryptStr += str[i]
    
    return encryptStr

def decrypt(string, key):
    x = 0
    for i in range(0, 26):
        mixed = encrypt(string, -i)
        if key in mixed:
            x = 1
            return [mixed, i]
    if x == 0:
        return ("ERROR")

def test_encrypt(word, shift, expected):
    assert encrypt(word, shift) == expected

def test_decrypt(word, keyword, expected_word, expected_shift):
    if expected_word == "ERROR":
        assert decrypt(word, keyword) == "ERROR"
    else:
        assert decrypt(word, keyword) == [expected_word, expected_shift]


if __name__ == "__main__":
    usrChoice = int(input("OPTION> "))
    
    if usrChoice == 1:
        inpStr = input("MESSAGE> ")
        inpShift = int(input("SHIFT> "))
        encryptedMessage = encrypt(inpStr, inpShift)
        print(f'OUTPUT {encryptedMessage}')
    
    elif usrChoice == 2:
        inpStr = input("MESSAGE> ")
        inpKey = input("KEY> ")
        decrypted = decrypt(inpStr, inpKey)
        if "ERROR" not in decrypted:
            print(f'OUTPUT {decrypted[0]}')
            print(f'OUTPUT {decrypted[1]}')
        else:
            print(f'OUTPUT {decrypted}')

    elif usrChoice == 3:
        test_encrypt("quizzes", 1, "rvjaaft")
        test_encrypt("Hellva Engineer", 2023, "Czggqv Zibdizzm")
        test_encrypt("VTEC JUST KICKED IN!", 5, "AYJH OZXY PNHPJI NS!")
    
        test_decrypt("rvjaaft", "quizzes", "quizzes", 1)
        test_decrypt("Z34 Asgtqvm OBZ", "GTR", "R34 Skyline GTR", 8)
        test_decrypt("DT bu Njoft", "CS", "CS at Mines", 1)
        test_decrypt("pink", "love", "ERROR", 0)