# Encapsulamento

## Conceitos Fundamentais:

- **Encapsulamento**: Ocultar os detalhes internos de uma classe e expor apenas uma interface pública para interagir com ela.
Protege o estado interno do objeto de acessos e modificações indesejadas.

- **Níveis de Acesso (Convenção em Python)**:
    - **Público**: Atributos e métodos acessíveis de qualquer lugar (padrão).
    - **Protegido**: Atributos e métodos prefixados com _ (um underscore). Convenção para indicar que são para uso interno da classe ou suas subclasses, mas ainda acessíveis.
    - **"Privado" (Name Mangling)**: Atributos e métodos prefixados com __ (dois underscores). Python renomeia esses atributos para evitar conflitos de nome em subclasses. Ainda são acessíveis, mas de forma mais "complicada", desincentivando o acesso direto.

:::conteudo.modulo_1.encapsulamento