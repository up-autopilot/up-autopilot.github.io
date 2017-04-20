from up.registrar import UpRegistrar


class Registrar(UpRegistrar):
    def __init__(self):
        super().__init__('my_cog')

    def register(self):
        return True
