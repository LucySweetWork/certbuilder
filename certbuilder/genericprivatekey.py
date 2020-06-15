class GenericPrivateKey:

    def __init__(self, algorithm, sign_callback, public_key):
        self.algorithm = algorithm
        self.__sign_callback = sign_callback
        self.public_key = public_key

    def sign_content(self, content):
        return self.__sign_callback(content)
