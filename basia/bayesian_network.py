from bayespy.nodes import Categorical, Mixture, MultiMixture
from bayespy.inference import VB

FALSE = 0
TRUE = 1


class BayesianNetwork:

    asia = Categorical
    smoke = Categorical
    tub = Mixture
    lung = Mixture
    bronc = Mixture
    either = MultiMixture
    xray = Mixture
    dysp = MultiMixture

    def create_network(self):
        print("LOG -> Creating bayesian network ...")
        n = self

        ap1 = 0.9999999999999999
        ap0 = 0.0000000000000001

        n.asia = Categorical([0.01, 0.99])
        n.smoke = Categorical([0.5, 0.5])
        n.tub = Mixture(n.asia, Categorical, [[0.99, 0.01], [0.95, 0.05]])
        n.lung = Mixture(n.smoke, Categorical, [[0.99, 0.01], [0.9, 0.1]])
        n.bronc = Mixture(n.smoke, Categorical, [[0.7, 0.3], [0.4, 0.6]])
        n.either = MultiMixture((n.lung, n.tub), Categorical, [[[ap1, ap0], [ap0, ap1]], [[ap0, ap1], [ap0, ap1]]])
        n.xray = Mixture(n.either, Categorical, [[0.95, 0.05], [0.02, 0.98]])
        n.dysp = MultiMixture((n.bronc, n.either), Categorical, [[[0.1, 0.9], [0.3, 0.7]], [[0.2, 0.8], [0.1, 0.9]]])

        print("LOG -> Bayesian network successfully created!")

    def show_result_as_table(self):
        n = self

        precision = "%.2f"
        space = "           | "
        space_after = "          |"

        print("\n================ BAYESIAN NETWORK ================\n")
        print("    + -------------------------------------- +")
        print("    |          TABELA DE INFERÊNCIAS         |")
        print("    + -------- + -------------- + ---------- +")
        print("    | NÓ       | PROBABILIDADE  | OBSERVADO  |")
        print("    + -------- + -------------- + ---------- +")
        print("    | asia     | " + precision % n.asia.get_moments()[0][TRUE] + space + [" ", "x"][
            n.asia.observed] + space_after)
        print("    | smoke    | " + precision % n.smoke.get_moments()[0][TRUE] + space + [" ", "x"][
            n.smoke.observed] + space_after)
        print("    | tub      | " + precision % n.tub.get_moments()[0][TRUE] + space + [" ", "x"][
            n.tub.observed] + space_after)
        print("    | lung     | " + precision % n.lung.get_moments()[0][TRUE] + space + [" ", "x"][
            n.lung.observed] + space_after)
        print("    | bronc    | " + precision % n.bronc.get_moments()[0][TRUE] + space + [" ", "x"][
            n.bronc.observed] + space_after)
        print("    | either   | " + precision % n.either.get_moments()[0][TRUE] + space + [" ", "x"][
            n.either.observed] + space_after)
        print("    | xray     | " + precision % n.xray.get_moments()[0][TRUE] + space + [" ", "x"][
            n.xray.observed] + space_after)
        print("    | dysp     | " + precision % n.dysp.get_moments()[0][TRUE] + space + [" ", "x"][
            n.dysp.observed] + space_after)
        print("    + -------- + -------------- + ---------- +")
        print("\n==================================================\n")

    def run_inference(self):
        print("LOG -> Running inference ...")
        n = self

        Q = VB(
            n.dysp,
            n.xray,
            n.either,
            n.bronc,
            n.lung,
            n.tub,
            n.smoke,
            n.asia)
        Q.update(repeat=100)
