# Fase 1 — Fundação (passo a passo)

Meta: abrir o projeto, apertar Play, andar com um animal provisório numa mata à noite, e ter
isso salvo no GitHub.

## 1. Preparar o Windows (16 GB de RAM)
1. **Arquivo de paginação:** Configurações → Sistema → Sobre → Configurações avançadas do
   sistema → Desempenho → Avançado → Memória virtual. Desmarque o automático e ponha
   tamanho inicial **16000 MB** e máximo **32000 MB**, num SSD. Reinicie.
2. Tenha pelo menos **150 GB livres em SSD** (engine ≈ 60 GB, mais projeto e cache).
3. Atualize o driver da NVIDIA.
4. Ao usar a Unreal, feche Chrome, Discord e launchers de jogos.

## 2. Instalar
1. **Epic Games Launcher** → aba Unreal Engine → Library → instale a **versão 5.x estável mais
   recente**. Nas opções de instalação, desmarque plataformas que não vai usar (Android, iOS,
   Linux) e os "Editor symbols for debugging" — economiza dezenas de GB.
2. **Git** e **Git LFS**: já estão instalados neste PC.
3. **Visual Studio não é necessário agora** (projeto só em Blueprints).

## 3. Criar o projeto
No Unreal Project Browser:
- Categoria **Games** → modelo **Third Person**
- **Blueprint** (não C++)
- Target Platform: **Desktop** · Quality Preset: **Maximum**
- Starter Content: **desmarcado**
- Raytracing: **desmarcado**
- Local: `C:\Users\user\Desktop\PINDORAMA` · Nome: **Pindorama**

O projeto fica em `PINDORAMA\Pindorama\`, ao lado da pasta `docs\`.

## 4. Configurar o editor para não travar
**Edit → Editor Preferences**
- *Loading & Saving* → Auto Save: mantenha ligado, a cada 10 min.
- *Performance* → marque **Use Less CPU when in Background**.
- *Performance* → desmarque **Show Frame Rate and Memory** só se incomodar; é útil deixar.

**Barra do viewport → Settings (engrenagem) → Engine Scalability Settings:** ponha em **High**
(não Epic) enquanto edita. Suba para Epic só para tirar screenshots.

**Edit → Project Settings**
- *Rendering* → Global Illumination e Reflections: **Lumen** (software, sem hardware ray tracing).
- *Rendering* → Shadow Map Method: **Virtual Shadow Maps**.
- *Rendering* → **Enable virtual texture support**: ligado.
- *Platforms → Windows* → Default RHI: **DirectX 12**.

**Edit → Plugins:** desligue o que não usa (por exemplo os de VR/XR, Android, iOS e
Chaos Cloth) e reinicie o editor.

**Hábitos**
- Texturas em **2K no máximo** ao baixar da Fab (8 GB de VRAM enchem rápido com 4K/8K).
- Um nível aberto por vez; feche abas de assets que não está editando.
- A primeira abertura compila shaders e demora — é normal, deixe terminar.
- Se o editor reclamar de "texture streaming pool over budget", abra o console (tecla `'`)
  e digite `r.Streaming.PoolSize 3000`.

## 5. Assets (preferindo gratuitos)
Tudo pela **Fab** (fab.com, mesma conta da Epic), usando o filtro **Price: Free**.

| Para quê | O que procurar | Observação |
|---|---|---|
| Animal provisório | **Animal Variety Pack** (Epic, gratuito) | Não tem onça: use qualquer quadrúpede só para testar movimento |
| Vegetação | Megascans: "tropical", "palm", "fern", "grass", "swamp" | Parte do Megascans hoje é paga; pegue só o que aparecer no filtro Free |
| Solo | Megascans surfaces: "mud", "forest floor", "wet soil" | 2K |
| Céu e noite | Nenhum download: Sky Atmosphere, Directional Light, Sky Light, Volumetric Cloud e Exponential Height Fog já vêm na engine | — |

**Aviso honesto:** não há onça-pintada nem capivara realistas gratuitas confiáveis. A onça de
verdade (com animações) será uma **compra na Fab na Fase 2** — procure "jaguar" e escolha um
pacote com esqueleto, animações de andar/correr/atacar e boa avaliação. Espere promoções da Fab.
Buriti e carandá específicos provavelmente também serão pagos ou feitos sob medida (Fase 5).

Ao adicionar um pacote, mande-o para a pasta `Content/Fab/` e anote em `docs/ASSETS.md`
(nome, link, versão). Essas pastas **não vão para o Git**.

## 6. Cena noturna de teste
1. File → New Level → **Basic** → salve como `Content/Pindorama/Mapas/Teste_Noite`.
2. Window → **Env. Light Mixer** → crie Sky Light, Atmospheric Light, Sky Atmosphere,
   Volumetric Cloud e Height Fog.
3. Gire o Directional Light para abaixo do horizonte (Pitch por volta de +10) → fica noite.
4. Adicione um segundo Directional Light como **lua**: Intensity 0.1–0.3 lux, cor azulada,
   Pitch −40. Em Atmosphere Sun Light Index ponha 1.
5. Sky Light → marque **Real Time Capture**.
6. Adicione um **Post Process Volume** com Infinite Extent ligado; em Exposure use
   Metering Mode **Manual** ou limite Min/Max EV para a noite não clarear sozinha.
7. Espalhe algumas árvores e capim com o **Foliage Mode** (Shift+3).
8. Project Settings → Maps & Modes → defina `Teste_Noite` como Editor Startup Map e
   Game Default Map.
9. Aperte **Play**.

## 7. Repositório
A pasta `PINDORAMA` já é um repositório Git próprio, com `.gitignore`, `.gitattributes` (LFS) e
o remoto `origin` apontando para `github.com/joseroberto-melo/pindorama`.

Depois de criar o projeto Unreal, em cada sessão de trabalho (com o editor fechado):

```bash
git add .
git commit -m "Fase 1: projeto Unreal e cena noturna de teste"
git push -u origin main
```

Antes do primeiro push, confira com `git lfs ls-files` que os `.uasset` e `.umap` aparecem na
lista. O Git LFS do GitHub tem cota gratuita limitada (veja em Settings → Billing): por isso os
pacotes de terceiros ficam fora do repositório.

## Checklist da Fase 1
- [ ] Paginação ajustada e Unreal instalada
- [ ] Projeto `Pindorama` criado (Third Person, Blueprint)
- [ ] Editor configurado (High, Lumen, DX12, plugins desligados)
- [ ] Animal provisório e vegetação baixados
- [ ] Mapa `Teste_Noite` com noite escura e lua
- [ ] Commit e push feitos, LFS conferido
