class Test1:
    def __init__(self):
        ''' Constructor for this class. '''
        self.world = ['Earth', 'Mars']

    def printHello(self):
        for world in self.world:
            print('Hello %s!' % world)

    def printGoodbye(self):
        for world in self.world:
            print('Goodbye %s!' % world)
