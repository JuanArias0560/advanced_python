def mayus(func):
    def envelope(text):
        return func(text).upper()
    return envelope

@mayus
def message(name):
    return f'{name}, you received a message'

print(message('Juan '))

