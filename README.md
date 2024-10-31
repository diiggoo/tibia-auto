# Automação de Controle de Suprimentos e Combate

Este projeto é um bot para automação de ações em um jogo, com o propósito de gerenciar habilidades, coletar loot e monitorar vida e mana de forma automática. O código utiliza bibliotecas como `pyautogui`, `pynput`, e `threading` para simular comandos e realizar verificações visuais em tempo real, ajustando as ações com base nas condições do jogo.

## Funcionalidades

- **Rotação de Skills**: Executa ataques automaticamente com intervalos de tempo predefinidos.
- **Controle de Suprimentos**: Monitora o nível de vida e mana e ativa poções conforme necessário.
- **Coleta de Loot**: Realiza o movimento de coleta em posições definidas, simulando cliques no loot.
- **Hotkeys Configuráveis**: O script permite iniciar e parar a rotação de habilidades e coletar loot com comandos de teclado (`f` para iniciar/parar rotação de skills, `r` para loot).

## Arquivos

- **`main.py`**: Script principal que controla o fluxo do bot, incluindo a rotação de habilidades, a coleta de loot e a interação via hotkeys.
- **`vida_mana.py`**: Script de suporte para monitoramento dos níveis de vida e mana, acionando teclas para utilizar poções quando necessário.

## Bibliotecas Utilizadas

- **pyautogui**: Utilizada para simular teclas, movimentos do mouse e realizar verificações de cor em regiões específicas da tela.
- **pynput**: Usada para monitorar o teclado e capturar eventos de hotkeys.
- **threading**: Permite a execução simultânea de tarefas, como a rotação de skills e o monitoramento de vida e mana.
- **opencv-python**: Biblioteca para processamento de imagens e visão computacional, utilizada para tarefas como detecção e reconhecimento de objetos.
- **pillow**: Biblioteca de manipulação de imagens que permite abrir, modificar e salvar diferentes formatos de imagem.


## Requisitos

- Python 3.x
- Instalar dependências com:
  ```bash
  pip install pyautogui pynput


## Como Usar

1. Execute o arquivo `main.py`.
2. Utilize a tecla **`f`** para iniciar ou parar a rotação de habilidades e o controle de suprimentos.
3. Pressione **`r`** para coletar loot nas posições predefinidas.
4. Para encerrar o bot, pressione a tecla **`delete`**.

## Créditos

Este código foi inspirado no conteúdo do canal do YouTube [DevMau](https://www.youtube.com/@devmau1716). Agradecimentos ao DevMau pela contribuição com o conhecimento compartilhado.
