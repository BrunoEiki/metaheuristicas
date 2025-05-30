from random import choice, sample
from primeiro_trabalho.modelagem import custo_total, tamanho_matriz, custo


class SolucaoGulosa:
    def __init__(self):
        self.tamanho = tamanho_matriz()
        self.solution = sample(range(9), 9)
        self.total_cost = custo_total(self.solution)

    def algoritmo(self, iteracoes):
        print(f"Solução Inicial: {self.total_cost}")
        print("Empresas alocadas para cada Projeto")
        for idx, i in enumerate(self.solution):
            print(f"Projeto {idx + 1} = Empresa {i + 1}")

        for _ in range(iteracoes):
            self.abordagem_gulosa()

        print(f"\nSolução após Função de Vizinhança: {self.total_cost}")
        print("Empresas alocadas para cada Projeto")
        for idx, i in enumerate(self.solution):
            print(f"Projeto {idx + 1} = Empresa {i+1}")
        return self.total_cost


    def abordagem_gulosa(self):
        empresas = [i for i in range(0, 9)]
        projetos = [i for i in range(0, 9)]
        total_cost = 0
        solution = self.solution.copy()

        for _ in range(self.tamanho):
            best_value = 100
            best_empresa = -1
            projeto_aleatorio = choice(projetos)

            for empresa in empresas:
                if (best_value > custo(empresa, projeto_aleatorio)):
                    best_value = custo(empresa, projeto_aleatorio)
                    best_empresa = empresa

            solution[projeto_aleatorio] = best_empresa
            empresas.remove(best_empresa)
            projetos.remove(projeto_aleatorio)
            total_cost += best_value

        if (self.total_cost > total_cost):
            self.solution = solution
            self.total_cost = total_cost


if __name__ == "__main__":
    heuristica = SolucaoGulosa()
    total_cost = heuristica.algoritmo(2000)
