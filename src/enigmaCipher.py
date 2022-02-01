from enigma.machine import EnigmaMachine

def initEnigma(wheelOrder, ringSettings, reflector, plugboardSettings):
    machine = EnigmaMachine.from_key_sheet(
        rotors = wheelOrder,
        ring_settings = ringSettings,
        reflector = reflector,
        plugboard_settings = plugboardSettings
    )
    return machine

def enigma(machine, initPosition, messageKey, encryptedText):
    machine.set_display(initPosition)
    messageKey = machine.process_text(messageKey)
    machine.set_display(messageKey)

    text = machine.process_text(encryptedText, replace_char='Z')

    return text

def rotorPosition(machine):
    return machine.get_display()

# machine = initEnigma('II IV V', [2, 18, 7], 'B', 'AV BS CG DL FU HZ IN KM OW RX')
# print(enigma(machine, 'WXC', 'KCH', 'RKBNUTBJUIFAIYKLERJ'))