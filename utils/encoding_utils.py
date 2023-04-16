import base64

def base16_encode(message):
    msg_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(msg_bytes)
    key = base64_bytes.decode('ascii')
    return key

def base16_decode(key):
    base64_bytes = key.encode('ascii')
    msg_bytes = base64.b64decode(base64_bytes)
    message = msg_bytes.decode('ascii')
    return message

def rot13_encode(message):
    encoded_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                encoded_message += chr((ord(char) - 65 + 13) % 26 + 65)
            else:
                encoded_message += chr((ord(char) - 97 + 13) % 26 + 97)
        else:
            encoded_message += char
    return encoded_message


def rot13_decode(key):
    return rot13_encode(key)

def rle_encode(message):
    key = ""
    current_char = ""
    count = 0
    for char in message:
        if char != current_char:
            if count > 0:
                key += str(count) + current_char
            current_char = char
            count = 1
        else:
            count += 1
    if count > 0:
        key += str(count) + current_char
    return key


def rle_decode(key):
    message = ""
    count = ""
    for char in key:
        if char.isdigit():
            count += char
        else:
            message += char * int(count)
            count = ""
    return message

def lzw_encode(message):
    dictionary = {chr(i): i for i in range(256)}
    result = []
    current_sequence = ""
    for symbol in message:
        new_sequence = current_sequence + symbol
        if new_sequence in dictionary:
            current_sequence = new_sequence
        else:
            result.append(dictionary[current_sequence])
            dictionary[new_sequence] = len(dictionary)
            current_sequence = symbol
    result.append(dictionary[current_sequence])
    return str(result)


def lzw_decode(key):
    key = eval(key)
    dictionary = {i: chr(i) for i in range(256)}
    result = ""
    previous_code = key.pop(0)
    result += dictionary[previous_code]
    previous_sequence = dictionary[previous_code]
    for code in key:
        if code in dictionary:
            sequence = dictionary[code]
        elif code == len(dictionary):
            sequence = previous_sequence + previous_sequence[0]
        else:
            raise ValueError("Invalid code in encoded message")
        result += sequence
        dictionary[len(dictionary)] = previous_sequence + sequence[0]
        previous_sequence = sequence
    return result

def delta_encode(message):
    key = [ord(message[0])]
    for i in range(1, len(message)):
        key.append(ord(message[i]) - ord(message[i-1]))
    return str(key)


def delta_decode(key):
    key = eval(key)
    message = chr(key[0])
    for i in range(1, len(key)):
        message += chr(key[i] + ord(message[i-1]))
    return message