import csv
from collections import defaultdict

class Car:

    def __init__(self, buying, main, doors, persons, lug_boot, safety, acceptability):
        self.buying = buying
        self.maint = main
        self.doors = doors
        self.persons = persons
        self.lug_boot = lug_boot
        self.safety = safety
        self.acceptability = acceptability

    buying = ''
    maint = ''
    doors = ''
    persons = ''
    lug_boot = ''
    safety = ''
    acceptability = '' 


class Evaluator:

    __knowledge = []
    __network = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    __count = defaultdict(lambda: defaultdict(int))

    def parse_data_csv(self, path):
        car_reader = csv.reader(open(path, 'r'))
        for row in car_reader:
            car = Car(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            self.__knowledge.append(car)

    def create_network(self):

        total = len(self.__knowledge)

        for car in self.__knowledge:
            self.__count['buying'][car.buying] += 1
            self.__count['maint'][car.maint] += 1
            self.__count['doors'][car.doors] += 1
            self.__count['persons'][car.persons] += 1
            self.__count['lug_boot'][car.lug_boot] += 1
            self.__count['safety'][car.safety] += 1

        for car in self.__knowledge:
            self.__network['buying'][car.buying][car.acceptability] += 1 / self.__count['buying'][car.buying]
            self.__network['maint'][car.maint][car.acceptability] += 1 / self.__count['maint'][car.maint]
            self.__network['doors'][car.doors][car.acceptability] += 1 / self.__count['doors'][car.doors]
            self.__network['persons'][car.persons][car.acceptability] += 1 / self.__count['persons'][car.persons]
            self.__network['lug_boot'][car.lug_boot][car.acceptability] += 1 / self.__count['lug_boot'][car.lug_boot]
            self.__network['safety'][car.safety][car.acceptability] += 1 / self.__count['safety'][car.safety]

    def print(self):
        for attribute in self.__network:
            print(attribute + ":")
            for value in self.__network[attribute]:
                print("    " + value + ":")
                for acceptability in self.__network[attribute][value]:
                    print("      " + acceptability + ":   \t" +
                          str(round(self.__network[attribute][value][acceptability] * 100, 2)) + "%")


    def evaluate(self, car):
        acceptability = 'test'
        car.acceptability = acceptability
        return acceptability



