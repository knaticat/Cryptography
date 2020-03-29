import string

def vignere_tableau(key):
    std_matrix = list(string.ascii_lowercase)# create a list storing lowercase English alphabets
    key_index = [std_matrix.index(key[i]) for i in range(len(key))]# store the indices of each alphabet of the key
    std_len = len(std_matrix) # length of Standard matrix i.e. 26
    
    vig_tab = {std_matrix[i]:std_matrix[i:std_len]+std_matrix[0:i-std_len] for i in range(std_len)}# create the vignere tableau
    return vig_tab, key_index # return the table and key indices list

# Encryption
def encrypt_message(msg, key):
    cipher= "" # store the ciphertext
    vig_table,key_index = vignere_tableau(key)
    msg_list = list(''.join(msg.split()))# make a list of the message characters
    msg_len = len(msg_list)# find length of the message
    
    for j in range(msg_len):
        cipher_letter = vig_table[msg_list[j]][key_index[j%len(key_index)]]# Access the value of message character from the Vignere table
        cipher+=''.join(cipher_letter)
    return cipher    

# Decryption
def decrypt_message(cipher, key):
    std_plain_matrix = list(string.ascii_lowercase) # create a list storing the English alphabets
    msg = "" # store the plaintext message
    vig_table,key_index = vignere_tableau(key)
    for k in range(len(cipher)):
        msg_list = vig_table[key[k%len(key_index)]] # access the row corresponding to the key index
        msg_let_index = msg_list.index(cipher[k])# find the index of the ciphertext letter and then store it
        msg+=''.join(std_plain_matrix[msg_let_index])# find the column(plaintext) letter and join it to get our message
    return msg
    
# Driver Program
def main():
    msg = "the alphabet is changing"
    key = "key"
    cipher = encrypt_message(msg,key)
    plaintext = decrypt_message(cipher,key)
    print(cipher)
    print(plaintext)
if __name__ == "__main__":
    main()
         
