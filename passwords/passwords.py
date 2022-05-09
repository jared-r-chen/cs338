
import hashlib
import binascii


words = [line.strip().lower() for line in open('words.txt')]

#  ==========
# || Part 1 ||
#  ==========

# hash_to_word = {}
# username_to_hash = {}
# passwords1_file = open('passwords1.txt', 'r') 
# for line in passwords1_file:
#     cur_line = line.split(':')
#     username_to_hash[cur_line[0]] = cur_line[1]

# passwords1_file.close()

# cracked1 = open("cracked1.txt", "w")

# for word in words:
#     password = word # type=string
#     encoded_password = password.encode('utf-8') # type=bytes
#     hasher = hashlib.sha256(encoded_password)
#     digest = hasher.digest() # type=bytes
#     digest_as_hex = binascii.hexlify(digest) # weirdly, still type=bytes
#     digest_as_hex_string = digest_as_hex.decode('utf-8') # type=string
    
#     hash_to_word[digest_as_hex_string] = word

# for key in username_to_hash.keys():

#     cracked1.write(key + ':' + hash_to_word[username_to_hash[key]] + '\n')

# cracked1.close()

#  ==========
# || Part 2 ||
#  ==========

# passwords2 = {}
# counter = 0
# passwords2_file = open('passwords2.txt', 'r') 
# for line in passwords2_file:
#     cur_line = line.split(':')
#     passwords2[cur_line[1]] = cur_line[0]

# passwords2_file.close()

# # print(passwords2)

# cracked2 = open("cracked2.txt", "w")

# for i in range(len(words)):
#     for j in range(len(words)):
#         print(counter)
#         password = words[i] + words[j] # type=string
#         # print(password)
#         encoded_password = password.encode('utf-8') # type=bytes
#         hasher = hashlib.sha256(encoded_password)
#         digest = hasher.digest() # type=bytes
#         digest_as_hex = binascii.hexlify(digest) # weirdly, still type=bytes
#         digest_as_hex_string = digest_as_hex.decode('utf-8') # type=string
#         counter += 1
#         if digest_as_hex_string in passwords2:
#             cracked2.write(passwords2[digest_as_hex_string] + ':' + password + '\n')
            
# cracked2.close()

#  ==========
# || Part 3 ||
#  ==========

passwords3 = {}
hex = "0123456789abcdef"
counter = [0,0,0,0,0,0,0,0]
hash_counter = 0

passwords3_file = open('passwords3.txt', 'r') 
for line in passwords3_file:
    cur_line = line.split(':')
    passwords3[cur_line[1]] = cur_line[0]

passwords3_file.close()

cracked3 = open("cracked3.txt", "w")

while(len(counter) < 9):
    salt = hex[counter[0]] + hex[counter[1]] + hex[counter[2]] + hex[counter[3]] + hex[counter[4]] + hex[counter[5]] + hex[counter[6]] + hex[counter[7]]


    for word in words:
        hash_counter += 1
        print(hash_counter)
        password =  salt + word # type=string
        encoded_password = password.encode('utf-8') # type=bytes
        hasher = hashlib.sha256(encoded_password)
        digest = hasher.digest() # type=bytes
        digest_as_hex = binascii.hexlify(digest) # weirdly, still type=bytes
        digest_as_hex_string = digest_as_hex.decode('utf-8') # type=string

        salt_hash = '$5$' + salt + '$' + digest_as_hex_string
        if salt_hash in passwords3:
            cracked3.write(passwords3[digest_as_hex_string] + ':' + password + '\n')


    counter[0] += 1
    # print(salt)
    for i in range(len(counter)):
        if counter[i] > 15:
            counter[i] = 0
            counter[i + 1] += 1
    

cracked3.close()

