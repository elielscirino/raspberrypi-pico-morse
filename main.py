import machine
import utime

led_onboard = machine.Pin(25, machine.Pin.OUT)

latin_alphabet = [
    'a','b','c','d','e','f','g',
    'h','i','j','k','l','m','n',
    'o','p','q','r','s','t','u',
    'v','w','x','y','z']

morse_alphabet = [
    '.-','-...','-.-.','-..','.','..-.','--.',
    '....','..','.---','-.-','.-..','--','-.',
    '---','.--.','--.-','.-.','...','-','..-',
    '...-','.--','-..-','-.--','--..',]

msg = 'Hello World'
msg_converted = list()

for word in msg:
    for letter in word.lower():
        if letter in latin_alphabet:
            msg_converted.append(morse_alphabet[latin_alphabet.index(letter)])


for morse_letter in msg_converted:
    print(f'{latin_alphabet[morse_alphabet.index(morse_letter)]}: {morse_letter}')
    for x in morse_letter:
        if x == '-':
            led_onboard.value(1)
            utime.sleep(2)
        else:
            led_onboard.value(1)
            utime.sleep(0.5)

        led_onboard.value(0)
        utime.sleep(0.5)