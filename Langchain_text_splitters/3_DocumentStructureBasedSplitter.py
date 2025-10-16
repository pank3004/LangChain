from langchain.text_splitter import RecursiveCharacterTextSplitter, Language


splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, 
    chunk_size=500, 
    chunk_overlap=0
)

text='''
    # main.py

def calculate_car_age(car_year):
    from datetime import datetime
    current_year = datetime.now().year
    return current_year - car_year


class Car:
    def __init__(self, make, model, year):
        # These are instance attributes
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Information: {self.year} {self.make} {self.model}")

    def get_age(self):
        # Calling the standalone function from within a class method
        age = calculate_car_age(self.year)
        print(f"The car is {age} years old.")


# This is the main execution block
if __name__ == "__main__":
    # Create an instance (object) of the Car class
    my_car = Car("Ford", "Mustang", 2022)

    # Call the methods of the my_car object
    my_car.display_info()
    my_car.get_age()

    print("\n--- Another Car ---")

    # Create another instance of the Car class
    your_car = Car("Honda", "Civic", 2019)
    your_car.display_info()
    your_car.get_age()
    '''



result=splitter.split_text(text)



print(result)

print(type(result))
print(len(result))


for i in range(len(result)): 
    print("---------------------------------------------")
    print(result[i])
    print("---------------------------------------------")


