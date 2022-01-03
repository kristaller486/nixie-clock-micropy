import machine
#from .exceptions import *

class Decoder:
    def __init__(self, pins):
        """
        Pins - dict like {'a0': Pin(4), 'a1': Pin(6), 'a2': Pin(7), 'a3': Pin(8)}
        
        """
        if not isinstance(pins['a0'], machine.Pin) or not isinstance(pins['a1'], machine.Pin) or not isinstance(pins['a2'], machine.Pin) or not isinstance(pins['a3'], machine.Pin):
            raise TypeError('Decoder.pins must be machine.Pin!')
        
        self.SYMBOLS = {
            0: {
                'a0': 0,
                'a1': 0,
                'a2': 0,
                'a3': 0,
                },
            1:{
                'a0': 1,
                'a1': 0,
                'a2': 0,
                'a3': 0,
                },
            2: {
                'a0': 0,
                'a1': 1,
                'a2': 0,
                'a3': 0,
                },
            3:{
                'a0': 1,
                'a1': 1,
                'a2': 0,
                'a3': 0,
                },
            4:{
                'a0': 0,
                'a1': 0,
                'a2': 1,
                'a3': 0,
                },
            5:{
                'a0': 1,
                'a1': 0,
                'a2': 1,
                'a3': 0,
                },
            6:{
                'a0': 0,
                'a1': 1,
                'a2': 1,
                'a3': 0,
                },
            7:{
                'a0': 1,
                'a1': 1,
                'a2': 1,
                'a3': 0,
                },
            8:{
                'a0': 0,
                'a1': 0,
                'a2': 0,
                'a3': 1,
                },
            9:{
                'a0': 1,
                'a1': 0,
                'a2': 0,
                'a3': 1,
                },
#            -1: {
#                'a0': 1,
#                'a1': 1,
#                'a2': 1,
#                'a3': 1,
#                },
            }
        
        self.pins = pins
        self.current = {
            'a0': None,
            'a1': None,
            'a2': None,
            'a3': None,
           }
        
    def next_num(self): #TODO
        pass
    
    def prev_num(self,): #TODO
        pass
    
    def reset_nums(self): #TODO
        pass
    
    def reser_num(self, num): #TODO
        pass
    
    def set_num(self, num):
        if num < 0 or num > 9:
            raise TypeError('Decoder.set_num.num must be 0-9')
        if not isinstance(num, int):
            raise TypeError('Decoder.set_num.num must be int')
        
        for i in self.SYMBOLS[num]:
            self.pins[i].value(self.SYMBOLS[num][i])
            self.current[i] = self.SYMBOLS[num][i] #DEBUG
        #print(self.current[])
class NixieDot:
    def __init__(self, dotpin):
        if not isinstance(dotpin, machine.Pin):
            raise TypeError('NixieDot.dotpin must be machine.Pin!')
