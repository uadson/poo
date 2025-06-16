# Princípios SOLID

## Conceitos Fundamentais:

Conjunto de cinco princípios de design de software orientados a objetos, introduzidos por Robert C. Martin (Uncle Bob). Visam tornar os designs mais compreensíveis, flexíveis e manuteníveis.

- S (Single Responsibility Principle - SRP): Uma classe deve ter apenas uma razão para mudar. (Uma classe = uma responsabilidade).
- O (Open/Closed Principle - OCP): Entidades de software (classes, módulos, funções, etc.) devem ser abertas para extensão, mas fechadas para modificação.
- L (Liskov Substitution Principle - LSP): Subtipos devem ser substituíveis por seus tipos base sem alterar a corretude do programa. (Objetos de uma superclasse devem poder ser substituídos por objetos de suas subclasses sem quebrar o código).
- I (Interface Segregation Principle - ISP): Clientes não devem ser forçados a depender de interfaces que não utilizam. (Interfaces grandes e monolíticas devem ser divididas em interfaces menores e mais específicas).
- D (Dependency Inversion Principle - DIP): Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações. Abstrações não devem depender de detalhes. Detalhes devem depender de abstrações.

:::conteudo.modulo_2.solid