class Room(object):
    room_count = 0
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
        self.__class__.room_count += 1

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)