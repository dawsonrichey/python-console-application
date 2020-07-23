import random


class Thief:
    sneaky = True

    def pickpocket(self):
        if self.sneaky:
            return bool(random.randint(0,1))
        return False
