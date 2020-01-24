class Servant():
        def __init__(self,  img: str):
            self.image = img

        def __eq__(self, value: str):
            return value == self.img

class Servants():
    def __init__(self, svs: list = []):
        self.servants = svs

    def get_seravnts(self):
        pass
