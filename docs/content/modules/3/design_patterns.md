# O que são Design Patterns (Padrões de Projeto)?

Design Patterns (Padrões de Projeto) são soluções reutilizáveis e testadas para problemas
comuns de design de software. Eles não são blocos de código prontos, mas modelos para resolver
problemas recorrentes, melhorando a organização, flexibilidade e manutenção do código.
    Pense neles como boas práticas universais para estruturar seu código de forma
    elegante e eficaz.

## Por que usar Design Patterns?

- Evitam reinvenção da roda
- Tornam o código mais legível, manutenível e testável
- Facilitam a comunicação entre desenvolvedores (padrões são um vocabulário comum)
- Melhoram a separação de responsabilidades (SRP/SOLID)
- Auxiliam na escalabilidade de sistemas
  

## Classificação dos Design Patterns

### Os padrões são normalmente divididos em 3 grandes grupos:

| **Tipo**        | **O que resolve**                           | **Exemplos principais**            |
| --------------- | ------------------------------------------- | ---------------------------------- |
| Criacionais     | Instanciação de objetos                     | Singleton, Factory Method, Builder |
| Estruturais     | Como organizar objetos em si                | Adapter, Composite, Decorator      |
| Comportamentais | Como os objetos se interagem e se comportam | Strategy, Observer, Command        |
                                                                     

## Design Patterns com Python

### Python é uma linguagem dinâminca, então:
- Alguns padrões são naturais (ex: Singleton via módulo)
- O uso de funções de ordem superior, decoradores e duck typing simplificam alguns padrões
- Padrões podem ser implementados com menos boilerplate

**boilerplate** : "... _boilerplate refere-se a seções de código que devem ser incluídas em muitos lugares com pouca ou nenhuma alteração. É frequentemente usado quando se refere a linguagens consideradas verborrágicas, ou seja, o programador deve escrever muito código para fazer trabalhos mínimos._"

Fonte: [FreeCodeCamp](https://www.freecodecamp.org/portuguese/news/o-que-e-um-boilerplate-e-por-que-o-usamos-a-necessidade-de-um-guia-de-estilo-de-codigo/)
