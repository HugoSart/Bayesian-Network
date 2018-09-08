import csv


class Car:

    def __init__(self, buying, main, doors, persons, lug_boot, safety, acceptability):
        self.buying = buying
        self.maint = main
        self.doors = doors
        self.persons = persons
        self.lug_boot = lug_boot
        self.safety = safety
        self.acceptability = acceptability

    buying = 0
    maint = 0
    doors = ''
    persons = ''
    lug_boot = ''
    safety = ''
    acceptability = ''


class Evaluator:

    __knowledge = []

    def evaluate(self, car):
        print('car')

    def parse_data_csv(self, path):
        car_reader = csv.reader(open(path, 'r'))
        for row in car_reader:
            car = Car(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            self.__knowledge.append(car)
