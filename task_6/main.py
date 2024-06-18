# 1. შექმენი ქვეყნის აბსტრაქტული კლასი. რომელსაც
# ექნება მინიმუმ სამი აბსტრაქტული მეთოდი.
# 2. შექმენი მისგან საქართველოს კლასი, რომელსაც ექნება
# public, protected და private ცვლადები (მაგალითად
# ბიუჯეტი, მოსახლეობა და ა.შ.).
# 3. შექმენი საქართველოს ობიექტი და გამოიყენე
# ზემოხსენებული მეთოდები.



from abc import ABC, abstractmethod


class Country(ABC):

    @abstractmethod
    def show_capital(self):
        """Show the capital of the country."""
        pass


    @abstractmethod
    def population_density(self):
        """Calculate and return the population density."""
        pass

    @abstractmethod
    def show_official_language(self):
        """Show the official language of the country."""
        pass



class Georgia(Country):
    def __init__(self, name, capital, population, area, official_language):
        self.name = name
        self._capital = capital
        self.population = population
        self.area = area
        self.__official_language = official_language

    def show_capital(self):
        return f"The capital of {self.name} is {self._capital}"
    

    def population_density(self):
        """Calculate and return the population density (people per square kilometer)."""

        density = self.population / self.area
        return f'Population density is {density:.2f} people per sq km'
    

    def show_official_language(self):
        return f'Official language is {self.__official_language}'
    

    def __str__(self) -> str:
        return (f"Country: {self.name}\n"
                f"Capital: {self._capital}\n"
                f"Population: {self.population}\n"
                f"Area: {self.area} sq km\n"
                f"Official Language: {self.__official_language}\n")




georgia = Georgia('Georgia', 'Tbilisi', 3713804, 69700, 'Georgian')
print(georgia.show_capital())
print(georgia.show_official_language())
print(georgia.population_density())
print(georgia)
