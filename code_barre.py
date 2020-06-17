#on déclare notre fonction principale
def main():
    binary = input("entrez le code barre : ")
    binary_change = binary


    test = len(binary_change)

    letters = ''

    numbers = ''

    pair=0
    impair=0

    #on cherche le code pour commencer 
    if  binary_change.startswith('101'):
        binary_change =  binary_change.replace('101','',1)
        for i in range(test):

            #on vérifie pour la lettre A
            if binary_change.startswith('0001101'):
                letters = letters+"A"
                numbers = numbers+"0"
                pair = pair+0
                binary_change =  binary_change.replace('0001101','',1)

            if binary_change.startswith('0011001'):
                letters = letters+"A"
                numbers = numbers+"1"
                impair = impair + 1
                binary_change =  binary_change.replace('0011001','',1)

            if binary_change.startswith('0010011'):
                letters = letters+"A"
                numbers = numbers+"2"
                pair = pair+2
                binary_change =  binary_change.replace('0010011','',1)

            if binary_change.startswith('0111101'):
                letters = letters+"A"
                numbers = numbers+"3"
                impair = impair+3

                binary_change =  binary_change.replace('0111101','',1)

            if binary_change.startswith('0100011'):
                letters = letters+"A"
                numbers = numbers+"4"
                pair = pair+4
                binary_change =  binary_change.replace('0100011','',1)

            if binary_change.startswith('0110001'):
                letters = letters+"A"
                numbers = numbers+"5"
                impair = impair+5
                binary_change =  binary_change.replace('0110001','',1)


            if binary_change.startswith('0101111'):
                letters = letters+"A"
                numbers = numbers+"6"
                pair = pair+6
                binary_change =  binary_change.replace('0101111','',1)

            if binary_change.startswith('0111011'):
                letters = letters+"A"
                numbers = numbers+"7"
                impair = impair+7
                binary_change =  binary_change.replace('0111011','',1)

            if binary_change.startswith('0110111'):
                letters = letters+"A"
                numbers = numbers+"8"
                pair = pair+8
                binary_change =  binary_change.replace('0110111','',1)

            if binary_change.startswith('0001011'):
                letters = letters+"A"
                numbers = numbers+"9"
                impair = impair+9
                binary_change =  binary_change.replace('0001011','',1)


    #on vérifie pour la lettre B
            if binary_change.startswith('0100111'):
                letters = letters+"B"
                numbers = numbers+"0"
                pair = pair+0
                binary_change =  binary_change.replace('0100111','',1)

            if binary_change.startswith('0110011'):
                letters = letters+"B"
                numbers = numbers+"1"
                impair = impair+1
                binary_change =  binary_change.replace('0110011','',1)

            if binary_change.startswith('0011011'):
                letters = letters+"B"
                numbers = numbers+"2"
                pair = pair+2
                binary_change =  binary_change.replace('0011011','',1)

            if binary_change.startswith('0100001'):
                letters = letters+"B"
                numbers = numbers+"3"
                impair = impair+3
                binary_change =  binary_change.replace('0100001','',1)

            if binary_change.startswith('0011101'):
                letters = letters+"B"
                numbers = numbers+"4"
                pair = pair+4
                binary_change =  binary_change.replace('0011101','',1)

            if binary_change.startswith('0111001'):
                letters = letters+"B"
                numbers = numbers+"5"
                impair = impair+5
                binary_change =  binary_change.replace('0111001','',1)


            if binary_change.startswith('0000101'):
                letters = letters+"B"
                numbers = numbers+"6"
                pair = pair+6
                binary_change =  binary_change.replace('0000101','',1)

            if binary_change.startswith('0010001'):
                letters = letters+"B"
                numbers = numbers+"7"
                impair = impair+7
                binary_change =  binary_change.replace('0010001','',1)

            if binary_change.startswith('0001001'):
                letters = letters+"B"
                numbers = numbers+"8"
                pair = pair+8
                binary_change =  binary_change.replace('0001001','',1)

            if binary_change.startswith('0010111'):
                letters = letters+"B"
                numbers = numbers+"9"
                impair = impair+9
                binary_change =  binary_change.replace('0010111','',1)

    #on passe au séparateur
            if binary_change.startswith('01010'):
                letters = letters+" "
                numbers = numbers+" "
                binary_change =  binary_change.replace('01010','',1)

    #on vérifie pour la partie C
            if binary_change.startswith('1110010'):
                letters = letters+"C"
                numbers = numbers+"0"
                pair = pair+0
                binary_change =  binary_change.replace('1110010','',1)

            if binary_change.startswith('1100110'):
                letters = letters+"C"
                numbers = numbers+"1"
                impair = impair+1
                binary_change =  binary_change.replace('1100110','',1)

            if binary_change.startswith('1101100'):
                letters = letters+"C"
                numbers = numbers+"2"
                pair = pair+2
                binary_change =  binary_change.replace('1101100','',1)

            if binary_change.startswith('1000010'):
                letters = letters+"C"
                numbers = numbers+"3"
                impair = impair+3
                binary_change =  binary_change.replace('1000010','',1)

            if binary_change.startswith('1011100'):
                letters = letters+"C"
                numbers = numbers+"4"
                pair = pair+4
                binary_change =  binary_change.replace('1011100','',1)

            if binary_change.startswith('1001110'):
                letters = letters+"C"
                numbers = numbers+"5"
                impair = impair+5
                binary_change =  binary_change.replace('1001110','',1)


            if binary_change.startswith('1010000'):
                letters = letters+"C"
                numbers = numbers+"6"
                pair = pair+6
                binary_change =  binary_change.replace('1010000','',1)

            if binary_change.startswith('1000100'):
                letters = letters+"C"
                numbers = numbers+"7"
                impair = impair+7
                binary_change =  binary_change.replace('1000100','',1)

            if binary_change.startswith('1001000'):
                letters = letters+"C"
                numbers = numbers+"8"
                pair = pair+8
                binary_change =  binary_change.replace('1001000','',1)

            if binary_change.startswith('1110100'):
                letters = letters+"C"
                numbers = numbers+"9"
                impair = impair+9
                binary_change =  binary_change.replace('1110100','',1)

    #maintenant on s'occupe du chiffre du pays

        if letters.startswith('AAAAAA'):
            numbers = "0 "+numbers
            pair = pair+0

        if letters.startswith('AABABB'):
            numbers = "1 "+numbers
            impair = impair+1

        if letters.startswith('AABBAB'):
            numbers = "2 "+numbers
            pair = pair+2

        if letters.startswith('AABBBA'):
            numbers = "3 "+numbers
            impair = impair+3

        if letters.startswith('ABAABB'):
            numbers = "4 "+numbers
            pair = pair+4

        if letters.startswith('ABBAAB'):
            numbers = "5 "+numbers
            impair = impair+5

        if letters.startswith('ABBBAA'):
            numbers = "6 "+numbers
            pair = pair+6

        if letters.startswith('ABABAB'):
            numbers = "7 "+numbers
            impair = impair+7

        if letters.startswith('ABABBA'):
            numbers = "8 "+numbers
            pair = pair+8

        if letters.startswith('ABBABA'):
            numbers = "9 "+numbers
            impair = impair+9
        #on vérifie que le code donné est bon
        if ((pair+3)*impair)%10==0:
            print("\""+binary+"\""+" a pour code : "+numbers)

        else:
            print("votre code n'est pas valide")
            main()

    else:
        print("votre code n'est pas valide")
        main()


if __name__ == '__main__':
    main()


