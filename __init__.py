class RC4:
    def __init__(self, key):
        self.state = self.init(key)

    def init(self, key):
        state = []
        for i in range(256):
            state.append(i)
        j = 0
        for i in range(256):
            j = (j + state[i] + ord(key[i % len(key)])) % 256
            state[i], state[j] = state[j], state[i]
        return state

    def crypt(self, inbuf):
        j = i = 0
        cipher_text = ""
        for x in range(len(inbuf)):
            i = (i + 1) % 256
            j = (j + self.state[i]) % 256
            self.state[i], self.state[j] = self.state[j], self.state[i]
            k = self.state[(self.state[i] + self.state[j]) % 256]
            cipher_text += chr(k ^ ord(inbuf[x]))
        return cipher_text
