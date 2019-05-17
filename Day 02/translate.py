#Translate Function


def translate(inp_str):
    consonants = 'bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'
    final_list = []

    for element in inp_str:
        if element in consonants: 
            final_list.append(element+"o"+element)
        else:
            final_list.append(element)

    return "".join(final_list)

actual_input = input("Enter string to Translate: ")

print (translate(actual_input))


