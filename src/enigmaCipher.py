# Enigma Cipher dengan 3-rotor (26 huruf alfabet)

from enigma.machine import EnigmaMachine

def initEnigma(wheelOrder, ringSettings, reflector, plugboardSettings):
    machine = EnigmaMachine.from_key_sheet(
        rotors = wheelOrder,
        ring_settings = ringSettings,
        reflector = reflector,
        plugboard_settings = plugboardSettings
    )
    return machine

def enigma(machine, initPosition, messageKeyUnprocessed, encryptedText):
    machine.set_display(initPosition)
    messageKey = machine.process_text(messageKeyUnprocessed)
    machine.set_display(messageKey)

    text = machine.process_text(encryptedText, replace_char='Z')

    return text

def rotorPosition(machine):
    return machine.get_display()

def saveEncryption(string):
    file = open("./text/enigmaCipher.txt", "w")
    file.write(string)
    file.close()

# machine = initEnigma('II IV V', [2, 18, 7], 'B', 'AV BS CG DL FU HZ IN KM OW RX')
# saveEncryption(enigma(machine, 'WXC', 'KCH', 'SAYA KE ITB KEMARIN!!'))
# print(enigma(machine, 'WXC', 'KCH', 'RKBNUTBJUIFAIYKLERJAT'))