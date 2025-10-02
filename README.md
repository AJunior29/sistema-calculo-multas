# Sistema Simples de Cálculo de Multas de Trânsito em Python

Este é um script em Python que simula o cálculo de multas de trânsito baseado na velocidade registrada, velocidade máxima permitida e fatores adicionais como reincidência e pagamento com desconto.

## Funcionalidades

* Calcula a classificação da infração (**Leve**, **Grave** ou **Gravíssima**).
* Aplica o valor base da multa e pontos na CNH.
* Determina a **suspensão** da CNH em casos de infração Gravíssima.
* **Dobra o valor** da multa em caso de **reincidência** para infrações Graves ou Gravíssimas.
* Aplica **20% de desconto** no valor final da multa caso o motorista opte por pagar.

## Como Executar

Para rodar este script, você precisará ter o Python instalado.

1.  Clone este repositório ou baixe o arquivo `sistema_multas.py`.
2.  Abra o terminal ou prompt de comando.
3.  Navegue até o diretório onde o arquivo está salvo.
4.  Execute o script com o comando:

```bash
python sistema_multas.py
