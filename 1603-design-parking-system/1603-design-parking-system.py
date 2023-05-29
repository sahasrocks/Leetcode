class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.__slots = {
            1: big,
            2: medium,
            3: small
        }

    def addCar(self, car_type: int) -> bool:
        if not self.__slots.get(car_type):
            return False

        self.__slots[car_type] -= 1
        return True
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)