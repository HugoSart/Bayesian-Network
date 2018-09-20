from carv.car import Evaluator

def __main__():

    evaluator = Evaluator()
    evaluator.parse_data_csv('data/car.csv')
    evaluator.create_network()
    evaluator.print()


__main__()
