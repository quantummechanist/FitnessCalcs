#!python3
""" Some basic calculation methods for nutritional information"""

# from Measures import Inch, Pound

class Person():

    internal_props = ('mass', 'height')
    sex_options = ('male', 'female')
    hamwi_base_height = 60*0.025

    def __init__(self, *args, **kwargs):
        """A person has atrributes of mass and height, set optionally and in that order"""

        self.mass = None
        self.height = None
        self.sex = None
        self.name = None
        self.hamwi_mass = None

        # pull relevant keys from kwargs
        for prop in self.internal_props:
            if prop in kwargs.keys():
                self.__setattr__(prop, kwargs[prop])

        if len(args) >= 1:
            if isinstance(args[0], str) and args[0] in self.sex_options:
                self.sex = args[0]
            else:
                raise TypeError("Specify sex on first argument, either 'male' or 'female'")

        if len(args) >= 2:
            self.height = args[1]

        if len(args) >= 3:
            self.mass = args[2]

        if len(args) >= 4:
            raise ValueError("Cannot yet understand more than three initial arguments")

    def __str__(self):
        return "Person: sex={}, height={}, mass={}, name={}".format(
            self.sex, self.height, self.mass, self.name)

    def hamwi_ideal_mass(self):
        """Calculates the ideal person mass based on the hamwi method"""

        if self.hamwi_mass is not None:
            return self.hamwi_mass

        for name in ("height", "sex"):
            test = self.__getattribute__(name)
            if test is None:
                raise ValueError("Require that property '{0}' be set"
                                 " before calling hamwi_ideal_mass".format(name)) 

        # hamwi mass depends on your sex
        if self.sex == 'male':
            self.hamwi_base_mass = 106*0.454
        elif self.sex == 'female':
            self.hamwi_base_mass = 100*0.454
        else:
            self.hamwi_base_mass = 103*0.454

        # if height is greater than excess (it will be unless super midget)
        if self.height >= self.hamwi_base_height:
            floor_mass = self.hamwi_base_mass
            excess_height = self.height - self.hamwi_base_height
        else:
            # to handle a linear falloff to base case
            excess_height = 0
            floor_mass = self.hamwi_base_mass * (self.height / self.hamwi_base_height)

        excess_mass = (excess_height / 0.025) * (6 * 0.454)

        self.hamwi_mass = excess_mass + floor_mass
        return self.hamwi_mass

    def excess_from_hamwi(self):
        """ Calculate the amount of excess weight present versus Hamwi method weight"""
        
        if self.mass is None:
            raise ValueError("Require that mass property be set")

        self.mass_excess = self.mass - self.hamwi_ideal_mass()
        return self.mass_excess
        

if __name__ == '__main__':

    bob = Person('female', 1.65, 65)
    print(bob)
    print(bob.hamwi_ideal_mass())
    print(bob.excess_from_hamwi())