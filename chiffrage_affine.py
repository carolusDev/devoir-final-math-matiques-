
def calc(a, b): 
    x,y, u,v = 0,1, 1,0
    while a != 0: 
        q, r = b//a, b%a 
        m, n = x-u*q, y-v*q 
        b,a, x,y, u,v = a,r, u,v, m,n 
        gcd = b 
    return gcd, x, y 

def rev(a, m): 
    gcd, x, y = calc(a, m) 
    if gcd != 1: 
        return None
    else: 
        return x % m 


#on chiffre le texte et on l'affiche
def encr(text,  key_decr): 
    ''' 
    C = (a*P + b) % 26 
    ''' 
    return ''.join([ chr(((  key_decr[0]*(ord(t) - ord('A')) +  key_decr[1] ) % 26) 
                    + ord('A')) for t in text.upper().replace(' ', '') ]) 


#on applique l'affine de cipher et on affiche le texte déchiffré
def decr(aff, key_decr): 
    ''' 
    P = (a^-1 * (C - b)) % 26 
    '''
    return ''.join([ chr((( rev( key_decr[0], 26)*(ord(c) - ord('A') -  key_decr[1])) 
                    % 26) + ord('A')) for c in aff ]) 


#main code 
def main(): 
    # declaring text and key 
    text = input("entrez votre texte : ")
    key1 = int(input("a = "))
    key2 = int(input("b = "))
    key_decr = [key1, key2] 
    
    ask = input("ce texte est il à chiffer (1) ou déchiffer (2) ? ")
    if (ask == "1"):
        encrText = encr(text,  key_decr) 
    
        print('Encrypted Text: {}'.format( encrText )) 

    elif (ask=="2"):
        encrText = encr(text,  key_decr) 
        print('Decrypted Text: {}'.format
        ( decr(encrText,  key_decr) ))
    else :
        print("veuillez recommencer")
        main()



    # start function



if __name__ == '__main__': 
    main() 
