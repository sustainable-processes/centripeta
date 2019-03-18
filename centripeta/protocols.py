from abc import ABC
from commanduino import CommandManager

class Protocol():

    def __init__(self, name, instruments=[]):
        self._name = name
        self._mgr = None
        self._instruments = instruments
    
    @property
    def name(self):
        return self._name

    def add_parameters(self, *args):
        '''Add parameters to the protocol that are defined by a user at runtime'''
        pass

    def add_instruments(self, *args):
        '''Add instruments to the protocol'''
        # check.areinstances(args, Instrument) #At some point add a check that actual instruments are passed
        self._instruments += list(args) 
        pass

    def start(self):
        '''Start the protocol'''
        pass

    def on_stop(self, func):
        '''Define a stopping/shutdown procedure for the protocol'''
        pass

    def stop(self):
        '''Stop the protocol'''




