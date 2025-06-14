# Polimorfismo e Abstração

## Conceitos Fundamentais:
- **Polimorfismo**: "Muitas formas". Capacidade de objetos de diferentes classes de responder ao mesmo método de maneira diferente, mas de uma forma que é consistente com a sua própria classe. Em Python, é largamente suportado por Duck Typing ("Se anda como um pato e quacks como um pato, então é um pato").
- **Abstração**: Focar no essencial e ignorar os detalhes irrelevantes. Em POO, envolve criar classes que representam conceitos gerais, definindo uma interface comum sem se preocupar com as implementações específicas.
- **Classes Abstratas**: Classes que não podem ser instanciadas diretamente e que contêm um ou mais métodos abstratos (métodos sem implementação). Forçam subclasses a fornecerem a implementação.
- **Interfaces (Protocolos em Python)**: Um contrato que define um conjunto de métodos que uma classe deve implementar. Em Python, geralmente são implícitas via Duck Typing ou explícitas via typing.Protocol ou abc.ABC.

:::conteudo.modulo_5.polimorfismo_abstracao