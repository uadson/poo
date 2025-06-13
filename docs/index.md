# Módulo 1: Introdução à Programação Orientada a Objetos (POO)

## Conceitos Fundamentais:
- O que é POO? Paradigma de programação que organiza o software em torno de "objetos" em vez de "funções e lógica". Foca nos dados e em como as funções operam nesses dados.
- Por que POO? Vantagens: Modularidade, Reutilização de Código, Facilidade de Manutenção, Flexibilidade, Escalabilidade, Melhor Organização do Código.
- Principais Pilares da POO: Abstração, Encapsulamento, Herança, Polimorfismo. (Introdução breve, aprofundados posteriormente).
  
# Módulo 2: Classes e Objetos

## Conceitos Fundamentais:
- **Classe**: Um blueprint ou molde para criar objetos. Define as características (atributos) e os comportamentos (métodos) que os objetos terão.
- **Objeto (ou Instância)**: Uma ocorrência concreta de uma classe. Cada objeto é único, mas segue a estrutura da classe.
- **Atributo**: Uma variável associada a uma classe ou objeto, que armazena dados.
    - **Atributo de Instância**: Pertence a uma instância específica do objeto.
    - **Atributo de Classe**: Pertence à classe e é compartilhado por todas as instâncias.
- **Método**: Uma função associada a uma classe ou objeto, que define um comportamento.
    - **Método de Instância**: Opera sobre os dados da instância.
    - **Método de Classe (@classmethod)**: Opera sobre a classe e seus atributos de classe.
    - **Método Estático (@staticmethod)**: Não opera sobre a instância nem sobre a classe; é uma função utilitária dentro do escopo da classe.

# Módulo 3: Encapsulamento

## Conceitos Fundamentais:

- **Encapsulamento**: Ocultar os detalhes internos de uma classe e expor apenas uma interface pública para interagir com ela.
Protege o estado interno do objeto de acessos e modificações indesejadas.

- **Níveis de Acesso (Convenção em Python)**:
    - **Público**: Atributos e métodos acessíveis de qualquer lugar (padrão).
    - **Protegido**: Atributos e métodos prefixados com _ (um underscore). Convenção para indicar que são para uso interno da classe ou suas subclasses, mas ainda acessíveis.
    - **"Privado" (Name Mangling)**: Atributos e métodos prefixados com __ (dois underscores). Python renomeia esses atributos para evitar conflitos de nome em subclasses. Ainda são acessíveis, mas de forma mais "complicada", desincentivando o acesso direto.

# Módulo 4: Herança

## Conceitos Fundamentais:
- **Herança**: Permite que uma classe (subclasse ou classe filha) herde atributos e métodos de outra classe (superclasse ou classe pai). Modela a relação "é um tipo de".
- **Sobrescrita de Métodos (Method Overriding)**: Uma subclasse pode fornecer sua própria implementação de um método já definido na superclasse.
- **super()**: Função usada para chamar métodos da superclasse a partir da subclasse.
- **Herança Múltipla**: Uma classe pode herdar de múltiplas superclasses.
- **MRO (Method Resolution Order)**: A ordem em que o Python procura métodos em uma hierarquia de herança múltipla.

# Módulo 5: Polimorfismo e Abstração

## Conceitos Fundamentais:
- **Polimorfismo**: "Muitas formas". Capacidade de objetos de diferentes classes de responder ao mesmo método de maneira diferente, mas de uma forma que é consistente com a sua própria classe. Em Python, é largamente suportado por Duck Typing ("Se anda como um pato e quacks como um pato, então é um pato").
- **Abstração**: Focar no essencial e ignorar os detalhes irrelevantes. Em POO, envolve criar classes que representam conceitos gerais, definindo uma interface comum sem se preocupar com as implementações específicas.
- **Classes Abstratas**: Classes que não podem ser instanciadas diretamente e que contêm um ou mais métodos abstratos (métodos sem implementação). Forçam subclasses a fornecerem a implementação.
- **Interfaces (Protocolos em Python)**: Um contrato que define um conjunto de métodos que uma classe deve implementar. Em Python, geralmente são implícitas via Duck Typing ou explícitas via typing.Protocol ou abc.ABC.

# Módulo 6: Composição e Relações entre Objetos

## Conceitos Fundamentais:
- **Composição**: Uma classe contém instâncias de outras classes como seus atributos. Modela a relação "tem um".
- **Agregação**: Um tipo mais fraco de composição, onde os objetos componentes podem existir independentemente do objeto que os contém.
- **Vantagens da Composição sobre Herança**:
    - **Maior flexibilidade**: permite mudanças na composição em tempo de execução.
    - **Menor acoplamento**: as classes não estão tão rigidamente ligadas.
    - **Maior reutilização de código**: um componente pode ser reutilizado em várias classes.
    - **Evita o "problema do diamante" da herança múltipla.**

# Módulo 7: Princípios SOLID

## Conceitos Fundamentais:

Conjunto de cinco princípios de design de software orientados a objetos, introduzidos por Robert C. Martin (Uncle Bob). Visam tornar os designs mais compreensíveis, flexíveis e manuteníveis.
- S (Single Responsibility Principle - SRP): Uma classe deve ter apenas uma razão para mudar. (Uma classe = uma responsabilidade).
- O (Open/Closed Principle - OCP): Entidades de software (classes, módulos, funções, etc.) devem ser abertas para extensão, mas fechadas para modificação.
- L (Liskov Substitution Principle - LSP): Subtipos devem ser substituíveis por seus tipos base sem alterar a corretude do programa. (Objetos de uma superclasse devem poder ser substituídos por objetos de suas subclasses sem quebrar o código).
- I (Interface Segregation Principle - ISP): Clientes não devem ser forçados a depender de interfaces que não utilizam. (Interfaces grandes e monolíticas devem ser divididas em interfaces menores e mais específicas).
- D (Dependency Inversion Principle - DIP): Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações. Abstrações não devem depender de detalhes. Detalhes devem depender de abstrações.