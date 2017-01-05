PLAYERS_CONFIG = [{"no":1, "name":"Joey", "defence":8},
{"no":2, "name":"Nick", "defence":8},
{"no":3, "name":"Russel", "defence":7},
{"no":4, "name":"Vivek", "defence":7},
{"no":5, "name":"Pritam", "defence":6},
{"no":6, "name":"Amit", "defence":6},
{"no":7, "name":"Chandler", "defence":5},
{"no":8, "name":"Colwin", "defence":5}]




class Player:
    def __init__(self, kwargs):
        self.no = kwargs.get('no')
        self.name = kwargs.get('name')
        self.defence = kwargs.get('defence')
