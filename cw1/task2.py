import csv


class Persona:

    def __init__(self, name, higth, weigth, age):
        self.name = name
        self.higth = higth
        self.weigth = weigth
        self.age = age

    def eat_smthg(self, name_of_food, count):
        self.menu_of_one_person = [self.name, name_of_food, count]
        return self.menu_of_one_person


class UserData:
    def __init__(self, name_of_user):
        self.name_of_user = name_of_user

    def write(self, all_menu_of_eating):
        with open("cw2.csv", "w") as csvfile:
            fieldnames = ["Персонаж", "Что скушал", "Количество"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_menu_of_eating)


if __name__ == "__main__":
    all_menu_of_eating = []
    people_1 = Persona("Renat", "180", "90", "18")
    list_ = people_1.eat_smthg("apple", 5)
    all_menu_of_eating.append({"Персонаж": people_1.menu_of_one_person[0], "Что скушал": people_1.menu_of_one_person[1],
                               "Количество": people_1.menu_of_one_person[2]})
    people_2 = Persona("Marat", "170", "60", "17")
    list_ = people_2.eat_smthg("mango", 10)
    all_menu_of_eating.append({"Персонаж": people_2.menu_of_one_person[0], "Что скушал": people_2.menu_of_one_person[1],
                               "Количество": people_2.menu_of_one_person[2]})
    user = UserData("Renat")
    user.write(all_menu_of_eating)