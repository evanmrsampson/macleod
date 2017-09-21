"""
@author Robert Powell
@version 0.0.2

Base class representing what is the object structure of Macleod. General idea
is that the majority of the Logical operations should return new copies of
stuff, alas that doesn't always work so you'll notice some state mutations.
These mutating functions are meant to be called from some other utility
structure that will appropiately copy as needed to keep the original structure
normal
"""


class Logical(object):
    '''
    Represents the base class that all terms will have in common.
    '''

    def __init__(self):

        # Serves as the dynamic storage location for nesting within the object
        # structure. Each Logical type has various restrictions on what can or
        # cannot be placed within this storage. It is the responsibility of the
        # child classes to maintain consistency with their definitions.
        self.terms = []

    def __and__(self, other):
        '''
        Operator overload for the '&' command, to simplify first-order logic
        operations.

        :return Connective.Conjunction()
        '''

        import macleod.logical.Connective as Connective

        return Connective.Conjunction([self, other])

    def __or__(self, other):
        '''
        Operator overload for the '|' command, to simplify first-order logic
        operations.

        :return Connective.Disjunction()
        '''

        import macleod.logical.Connective as Connective

        return Connective.Disjunction([self, other])

    def __invert__(self):
        '''
        Operator overload for the '~' command, to simplify first-order logic
        operations.

        :return Negation.Negation()
        '''

        import macleod.logical.Negation as Negation

        return Negation.Negation(self)

    def remove_term(self, term):
        '''
        Function stub for removal accessor
        '''

        raise NotImplementedError

    def set_term(self, term):
        '''
        Function stub for setter accessor
        '''

        raise NotImplementedError

    def get_term(self):
        '''
        Function stub for getter accessor
        '''

        return self.terms
    
    def is_onf(self):
        '''
        Helper to decide is an element is already in onf form
        '''

        raise NotImplementedError

    def to_onf(self):
        '''
        Our basic modifier, feel like we could do something cool with classes and python mojo here
        '''

        raise NotImplementedError
