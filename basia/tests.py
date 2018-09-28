from basia.bayesian_network import BayesianNetwork

FALSE = 0
TRUE = 1


def asia_test():
    evaluator = BayesianNetwork()
    evaluator.create_network()
    evaluator.asia.observe(TRUE)
    evaluator.run_inference()
    b = evaluator.asia.get_moments()[0][TRUE]
    return round(b, 4) == TRUE


def tub_asia_test():
    evaluator = BayesianNetwork()
    evaluator.create_network()
    evaluator.asia.observe(TRUE)
    evaluator.run_inference()
    b = evaluator.tub.get_moments()[0][TRUE]
    return round(b, 4) == 0.05


def either_lug_tub_test():
    evaluator = BayesianNetwork()
    evaluator.create_network()
    evaluator.lung.observe(TRUE)
    evaluator.tub.observe(TRUE)
    evaluator.run_inference()
    b = evaluator.either.get_moments()[0][TRUE]
    return round(b, 4) == 1.0


def either_lug_tub_test():
    evaluator = BayesianNetwork()
    evaluator.create_network()
    evaluator.lung.observe(FALSE)
    evaluator.tub.observe(TRUE)
    evaluator.run_inference()
    b = evaluator.either.get_moments()[0][TRUE]
    return round(b, 4) == 1.0


def either_lug_tub_test2():
    evaluator = BayesianNetwork()
    evaluator.create_network()
    evaluator.lung.observe(FALSE)
    evaluator.tub.observe(FALSE)
    evaluator.run_inference()
    b = evaluator.either.get_moments()[0][TRUE]
    return round(b, 4) == 0


def either_lug_tub_test3():
    evaluator = BayesianNetwork()
    evaluator.create_network()
    evaluator.lung.observe(TRUE)
    evaluator.tub.observe(TRUE)
    evaluator.run_inference()
    b = evaluator.either.get_moments()[0][TRUE]
    return round(b, 4) == 1


def run_all_tests():

    at = asia_test()
    tat = tub_asia_test()
    eltt = either_lug_tub_test()
    eltt2 = either_lug_tub_test2()
    eltt3 = either_lug_tub_test3()

    print("test1 = " + str(at))
    print("test2 = " + str(tat))
    print("test3 = " + str(eltt))
    print("test4 = " + str(eltt2))
    print("test5 = " + str(eltt3))
