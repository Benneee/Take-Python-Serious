# A static method is basically an helper method. It doesn't rely on the class.

class WeatherForecast():
    def __init__(self, temperatures):
        self.temperatures = temperatures

    # The static method
    @staticmethod
    def convert_from_fahrenheit_to_celsius(fahrenheit: int):
        calculation = (5/9) * (fahrenheit - 32)
        return round(calculation, 3)

    
    def in_celsius(self):
        # Using list comprehension, we return the temperatures converted from fahrenheit to celsius
        # Because the conversion process is a bit of a stretch, we can outsource that process to an helper function
        # This is where our static method becomes useful
        return [self.convert_from_fahrenheit_to_celsius(temp) for temp in self.temperatures]


wf = WeatherForecast([100, 90, 80, 70, 60])
print(wf.in_celsius());
