MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
              '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
              '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
              '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
              '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
              '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
              '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1',
              '..---': '2', '...--': '3', '....-': '4', '.....': '5',
              '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.',
              '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/',
              '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':', '-.-.-.': ';',
              '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"',
              '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}


def morse_code_decoder(morse_code):
    output = ''
    for word in morse_code.strip().split('   '):
        for letter in word.split(' '):
            output += MORSE_CODE[letter]
        output += ' '

    return(output).rstrip(' ')



print(morse_code_decoder('   .... . -.--   .--- ..- -.. .'))
