# metaheuristicas

O trabalho final investiga o uso da metaheurística GRASP (Greedy Randomized Adaptive Search Procedure)
para resolver o Problema da Mochila
Binária, um desafio clássico em otimização combinatória. Além do GRASP,
o trabalho também faz uso do Arrefecimento Simulado (AS) para fins de comparação
e também como mecanismo de Busca Local.

## Problema da Mochila

Na formulaçã clássica, chamada de Problema da Mochila Binária, cada item apresenta
um valor e um peso: a somatória dos pesos deve ser menor ou igual à capacidade da
mochila enquanto se maximiza o valor total dos items, mas cada item pode ser colocado
apenas uma vez. 

## Resultados

| Medida          | Apenas AS | GRASP sem AS | GRASP com AS |
|-----------------|------------|---------------|---------------|
| Melhor Valor    | 2033       | 2195          | 2195          |
| Pior Valor      | 0          | 2195          | 2192          |
| Média           | 1905       | 2195          | 2194.5        |
| Desvio Padrão   | 448,796    | 0             | 0.827         |
