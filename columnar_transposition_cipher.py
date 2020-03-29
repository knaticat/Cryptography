
import math

#Encryption
def encrypt_message(msg, key):
    cipher = "" # store the chipertext
    k_index = 0 # track key index
    
    msg_list = list(''.join(msg.split()))# make a list of the message characters
    msg_len = len(msg_list)# find length of the message
    key_list = sorted(list(key))# sort the key alphabetically and store in a list
    
    col = len(key) # find the column of the matrix
    row = int(math.ceil(msg_len/col))# find the row of matrix
    
    fill_null = int((col*row)- msg_len)# count required number of trailing spaces
    msg_list.extend(['_']*fill_null)# add special character to the trailing blank spaces 
    
    matrix = [msg_list[i:i+col] for i in range(0, len(msg_list), col)] # create matrix & fill with message 
    
    for _ in range(col):
        current_index = key.index(key_list[k_index]) # return the key index of the sorted (alphabetically) key_list
        cipher += ''.join(row[current_index] for row in matrix)
        k_index+=1
    return cipher
#Decryption
def decrypt_message(cipher,key):
    message= "" # store decrypted message
    k_index = 0 # track key index
    
    ciph_index = 0 # track cipher index
    ciph_len = len(cipher)# length of ciphertext
    ciph_list = list(cipher)# store in list
    
    col = len(key)# column of decipher matrix
    row = int(math.ceil(ciph_len/col))# row of decipher matrix
    key_list = sorted(list(key))# sorting key and storing in alphabetical order
    
    dec_cipher = [] # decipher matrix
    
    for _ in range(row):
        dec_cipher += [[None]*col]# initialize
    
    for _ in range(col):
        current_index = key.index(key_list[k_index]) # return the key index of the sorted (alphabetically) key_list
        
        for j in range(row):
            dec_cipher[j][current_index] = ciph_list[ciph_index]# fill the decipher matrix with entries from the cipher list
            ciph_index+=1
        k_index+=1
        
    message = ''.join(sum(dec_cipher,[]))
    message = message.replace('_','')
    return message
            
    
