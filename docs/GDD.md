# PINDORAMA — Documento de Design (v0.1)

## Visão
Sobrevivência online em que o jogador **é** um animal real da fauna brasileira, num Brasil sem
presença humana. Visual realista, tom de documentário de natureza. Sem mitos, folclore ou
criaturas fantásticas.

- **Primeiro mapa:** Pindorama: Pantanal.
- **Mapas futuros:** Amazônia, Cerrado, Mata Atlântica, Caatinga, Pampa.
- **Câmera:** terceira pessoa, atrás do animal.
- **Engine:** Unreal Engine 5.

## Ciclo de jogo
Nascer filhote → achar água e comida → evitar predadores → crescer → marcar território →
reproduzir → continuar como o filhote (a linhagem é o "progresso").

## Mecânicas principais

| Sistema | Como funciona |
|---|---|
| Necessidades | Fome, sede, energia (sono) e saúde. Caem com o tempo; correr gasta mais. Zerar fome ou sede drena a saúde. |
| Sentidos | Visão, audição e faro. O faro mostra rastros de presa, água e predador. À noite a visão depende da espécie. |
| Caça | Aproximação furtiva (agachado, contra o vento) → bote → mordida. Presa foge se perceber. Falhar custa energia. |
| Fuga | Presas têm fôlego, esconderijo na vegetação e refúgio na água (capivara mergulha). |
| Dia e noite | Um dia dura cerca de 40 min reais. Noite realmente escura, com lua, estrelas, vaga-lumes e som denso de sapos e insetos. |
| Comportamento | Cada espécie tem horário de atividade, dieta, medo e território próprios (ver tabela abaixo). |
| Crescimento | Filhote → jovem → adulto. Tamanho, força e velocidade aumentam com a idade. |
| Reprodução | Adulto bem alimentado encontra parceiro; nasce filhote que o jogador pode assumir ao morrer. |
| Estações | Cheia e seca do Pantanal mudam onde há água e presas (fase avançada). |

## Espécies do Pantanal (ordem de entrada)

| Espécie | Papel | Atividade | Notas de comportamento |
|---|---|---|---|
| Onça-pintada | Predador de topo, jogável | Crepuscular e noturna | Solitária, territorial, nada bem, emboscada com mordida no crânio |
| Capivara | Presa | Crepuscular | Vive em grupo perto da água, dá alarme e foge mergulhando |
| Jacaré-do-pantanal | Predador e presa | Noturno | Fica na margem, toma sol de dia, ataca na água |
| Anta | Herbívoro grande | Noturna | Solitária, usa trilhas fixas, foge para a água |
| Tamanduá-bandeira | Insetívoro | Diurno ou noturno conforme o calor | Lento, se defende em pé com as garras |
| Lobo-guará | Onívoro | Crepuscular | Solitário, come frutos (lobeira) e pequenas presas |
| Sucuri | Predador de emboscada | Diurna e noturna | Aquática, constrição |
| Outros | Ambiente | — | Tuiuiú, arara-azul, queixada, cervo-do-pantanal, ariranha |

## Flora do Pantanal
Buriti, carandá, ipê (roxo e amarelo), piúva, cambará, aguapé, vitória-régia, capim nativo,
campos alagados, corixos, baías e capões de mata.

## Multiplayer (fase posterior)
Servidor de até 8–16 amigos, cada um um animal. Modelo de rede da Unreal (servidor com
autoridade). A IA dos animais roda no servidor. Desde a Fase 2 a lógica é escrita já pensando em
replicação, para não precisar refazer tudo depois.

## Escopo do primeiro protótipo
**Dentro:**
- Um trecho pequeno de mata do Pantanal (cerca de 500 m × 500 m) com um corpo d'água.
- Onça controlável: andar, correr, agachar, beber, atacar, comer.
- Barras de fome e sede.
- Uma capivara com IA simples: pastar, perceber, fugir.
- Noite escura com lua e som ambiente.

**Fora (por enquanto):** multiplayer, crescimento, reprodução, outras espécies, estações,
menus, salvamento.

**Pronto quando:** dá para jogar 5 minutos — a onça fica com fome, encontra a capivara no
escuro, caça, come, bebe água, e as barras reagem.
