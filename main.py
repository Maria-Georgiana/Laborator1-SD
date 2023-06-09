from Entity import Car
from operations import Search_Maria, Search_Diana, Sort_Maria, Sort_Diana

cars = []
f = open("Cars.txt", "r")
line = f.readline().strip("\n")
while line != "":
    cars_list = line.split(" ")
    modelCar = cars_list[0]
    brandCar = cars_list[1]
    tokenCar = cars_list[2]
    buyingpriceCar = int(cars_list[3])
    sellingpriceCar = int(cars_list[4])
    car = Car(modelCar, brandCar, tokenCar, buyingpriceCar, sellingpriceCar)
    # print(car)
    cars.append(car)
    line = f.readline().strip("\n")
f.close()


def menu():
    false = False
    while not false:
        print("      MENU    \n"
              "1) Search car\n"
              "2) Sort cars"
              )
        choice = int(input())
        if choice == 1:
            search()
        elif choice == 2:
            sort()
        else:
            false = True


#                                               SEARCH

def search():
    Sort_Maria(cars, 1).bubble_sort()
    token = input("Please enter token of the brand you search for: \n")
    print(Search_Maria(cars, token).binary_search())
    print(Search_Diana(cars, token).secventail_search())


#                                                   SORT

def sort():
    is_true = True
    while is_true:
        print(
            "1. Sort by car token\n"
            "2. Sort by car brand and model\n"
            "3. Sort by car car brand, model and token\n"
            "4. Sort by profit\n"
            "5. Exit\n"
        )
        condition = int(input())
        if condition == 5:
            is_true = False
        else:
            Sort_Maria(cars, condition).bubble_sort()
            Sort_Diana(cars, condition).merge_sort(cars)
            for carrr in cars:
                print(carrr)
        print("\n")


menu()
