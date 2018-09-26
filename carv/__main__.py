from carv.bayesian_network import BayesianNetwork
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--asia",   type=int)
    parser.add_argument("--smoke",  type=int)
    parser.add_argument("--tub",    type=int)
    parser.add_argument("--lung",   type=int)
    parser.add_argument("--bronc",  type=int)
    parser.add_argument("--either", type=int)
    parser.add_argument("--xray",   type=int)
    parser.add_argument("--dysp",   type=int)
    return parser.parse_args()


def make_observations(args, evaluator):
    if args.asia is not None:   evaluator.Nodes.asia.observe(args.asia)
    if args.smoke is not None:  evaluator.Nodes.smoke.observe(args.smoke)
    if args.tub is not None:    evaluator.Nodes.tub.observe(args.tub)
    if args.lung is not None:   evaluator.Nodes.lung.observe(args.lung)
    if args.bronc is not None:  evaluator.Nodes.bronc.observe(args.bronc)
    if args.either is not None: evaluator.Nodes.either.observe(args.either)
    if args.xray is not None:   evaluator.Nodes.xray.observe(args.xray)


def __main__():
    # Interpreta argumentos
    args = parse_arguments()

    # Cria rede bayesiana referente ao problema
    evaluator = BayesianNetwork()
    evaluator.create_network()

    # Faz as observações na rede baseadas nos argumentos do programa
    make_observations(args, evaluator)

    # Roda as inferencias e printa os resultados
    evaluator.run_inference()
    evaluator.show_result_as_table()


__main__()
