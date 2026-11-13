# PINDORAMA — Roadmap

Cada fase termina com algo jogável. Só passar para a próxima quando a atual estiver pronta.

| Fase | Entrega | Pronto quando |
|---|---|---|
| **1. Fundação** | Unreal instalada, projeto criado, repositório funcionando, cena noturna de teste com um animal provisório andando | Abro o projeto, aperto Play, ando pela mata à noite, e o commit está no GitHub |
| **2. Onça** | Personagem da onça com modelo e animações reais: andar, correr, agachar | A onça se move de forma convincente em terceira pessoa |
| **3. Necessidades** | Fome, sede e saúde com barras na tela; beber no rio | As barras caem com o tempo e beber recupera a sede |
| **4. Capivara e caça** | IA da capivara (pastar, perceber, fugir), ataque da onça, comer a carcaça | **Protótipo mínimo completo:** caço, como e bebo à noite |
| **5. Pantanal de verdade** | Mapa maior com World Partition, flora fiel (buriti, carandá, ipê, aguapé), água, PCG para espalhar vegetação | O cenário é reconhecível como Pantanal |
| **6. Dia e noite vivo** | Ciclo completo, lua, vaga-lumes, som por horário, horário de atividade das espécies | A noite parece filmagem de câmera noturna |
| **7. Mais espécies** | Jacaré, anta, tamanduá, lobo-guará, sucuri — IA própria e, depois, jogáveis | Ecossistema com predadores e presas interagindo |
| **8. Ciclo de vida** | Sono, crescimento, território, reprodução, salvamento | Uma vida inteira jogável, de filhote a adulto |
| **9. Multiplayer** | Replicação, servidor hospedado por um jogador, depois servidor dedicado; escolha de animal | Jogo com amigos, cada um um animal |
| **10. Novos biomas** | Amazônia, Cerrado, Mata Atlântica, Caatinga, Pampa | Um bioma novo por vez |

## Regras do projeto
- **Blueprints primeiro.** C++ só quando um sistema ficar lento ou complexo demais (provavelmente
  IA e rede, a partir da Fase 7). Isso também evita compilar C++ com 16 GB de RAM.
- **Pensar em rede desde a Fase 2:** estado importante (fome, sede, saúde) fica no personagem
  e muda só por funções que depois virarão chamadas ao servidor.
- **Um commit por sessão de trabalho**, com mensagem dizendo o que mudou.
- **Assets de terceiros não entram no Git** — a lista fica em `docs/ASSETS.md`.
