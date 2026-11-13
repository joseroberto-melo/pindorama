"""Cria (ou recria) o mapa /Game/Pindorama/Mapas/Teste_Noite.

Rodar no console do editor (caixa "Cmd" na barra de baixo):
  py "C:/Users/user/Desktop/PINDORAMA/Pindorama/Scripts/criar_teste_noite.py"
Ou com o editor fechado:
  UnrealEditor.exe Pindorama.uproject -ExecutePythonScript=Scripts/criar_teste_noite.py
O resultado fica em Saved/criar_teste_noite.log.
"""
import os
import random
import traceback

import unreal

MAPA = "/Game/Pindorama/Mapas/Teste_Noite"
LOG = os.path.join(unreal.Paths.project_saved_dir(), "criar_teste_noite.log")
linhas = []


def log(msg):
    linhas.append(str(msg))
    unreal.log("[Pindorama] " + str(msg))


def tentar(descricao, fn):
    """Ajustes opcionais: se um nome de propriedade mudou na engine, registra e segue."""
    try:
        fn()
    except Exception as e:  # noqa: BLE001
        log("AVISO: %s falhou: %s" % (descricao, e))


def criar():
    les = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
    eas = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)

    if unreal.EditorAssetLibrary.does_asset_exist(MAPA):
        log("Mapa ja existe: recriando o conteudo.")
        if not les.load_level(MAPA):
            raise RuntimeError("nao consegui abrir " + MAPA)
        # Atores internos do World Partition nao podem ser apagados: o editor trava ao salvar.
        internos = ("WorldDataLayers", "WorldPartition", "WorldSettings", "LevelInstance")
        for a in eas.get_all_level_actors():
            if any(n in a.get_class().get_name() for n in internos):
                continue
            eas.destroy_actor(a)
    else:
        if not les.new_level(MAPA):
            raise RuntimeError("nao consegui criar " + MAPA)

    def spawn(cls, x=0.0, y=0.0, z=0.0, pitch=0.0, yaw=0.0, nome=None, pasta=None):
        a = eas.spawn_actor_from_class(
            cls, unreal.Vector(x, y, z), unreal.Rotator(roll=0.0, pitch=pitch, yaw=yaw)
        )
        if a is None:
            raise RuntimeError("falha ao criar " + str(cls))
        if nome:
            a.set_actor_label(nome)
        if pasta:
            a.set_folder_path(pasta)
        return a

    def malha(caminho, nome, x, y, z, sx, sy, sz, material=None, pasta="Cenario"):
        a = spawn(unreal.StaticMeshActor, x, y, z, nome=nome, pasta=pasta)
        comp = a.static_mesh_component
        comp.set_static_mesh(unreal.load_asset(caminho))
        a.set_actor_scale3d(unreal.Vector(sx, sy, sz))
        if material:
            m = unreal.load_asset(material)
            if m:
                comp.set_material(0, m)
        return a

    # --- Chao: 500 m x 500 m, topo em z = 0 ---
    malha("/Engine/BasicShapes/Cube", "Chao", 0, 0, -50, 500, 500, 1,
          "/Game/LevelPrototyping/Materials/MI_PrototypeGrid_Gray")

    # --- Troncos provisorios (so para ter sombra e escala ate chegarem as arvores) ---
    rnd = random.Random(1500)
    for i in range(60):
        x = rnd.uniform(-6000, 6000)
        y = rnd.uniform(-6000, 6000)
        if abs(x) < 400 and abs(y) < 400:
            continue
        altura = rnd.uniform(6, 14)
        raio = rnd.uniform(0.4, 0.9)
        malha("/Engine/BasicShapes/Cylinder", "Tronco_%02d" % i,
              x, y, altura * 50, raio, raio, altura, pasta="Cenario/Troncos")

    spawn(unreal.PlayerStart, 0, 0, 120, nome="Inicio_Jogador")

    # --- Lua: luz direcional fraca e azulada ---
    lua = spawn(unreal.DirectionalLight, 0, 0, 1000, pitch=-40.0, yaw=35.0,
                nome="Lua", pasta="Iluminacao")
    lc = lua.get_component_by_class(unreal.DirectionalLightComponent)
    lc.set_mobility(unreal.ComponentMobility.MOVABLE)
    lc.set_intensity(0.5)
    lc.set_light_color(unreal.LinearColor(0.6, 0.75, 1.0, 1.0))
    tentar("lua como luz da atmosfera",
           lambda: lc.set_editor_property("atmosphere_sun_light", True))

    # --- Ceu ---
    spawn(unreal.SkyAtmosphere, nome="Atmosfera", pasta="Iluminacao")
    spawn(unreal.VolumetricCloud, nome="Nuvens", pasta="Iluminacao")

    ceu = spawn(unreal.SkyLight, 0, 0, 1000, nome="Luz_do_Ceu", pasta="Iluminacao")
    sc = ceu.get_component_by_class(unreal.SkyLightComponent)
    sc.set_mobility(unreal.ComponentMobility.MOVABLE)
    tentar("captura em tempo real do ceu",
           lambda: sc.set_editor_property("real_time_capture", True))

    nevoa = spawn(unreal.ExponentialHeightFog, 0, 0, 0, nome="Nevoa", pasta="Iluminacao")
    fc = nevoa.get_component_by_class(unreal.ExponentialHeightFogComponent)
    tentar("densidade da nevoa", lambda: fc.set_editor_property("fog_density", 0.04))
    tentar("nevoa volumetrica", lambda: fc.set_editor_property("enable_volumetric_fog", True))

    # --- Exposicao travada: sem isso a camera clareia a noite sozinha ---
    ppv = spawn(unreal.PostProcessVolume, nome="Exposicao_Noite", pasta="Iluminacao")
    ppv.set_editor_property("unbound", True)
    s = ppv.get_editor_property("settings")
    for chave, valor in (
        ("override_auto_exposure_min_brightness", True),
        ("auto_exposure_min_brightness", 1.0),
        ("override_auto_exposure_max_brightness", True),
        ("auto_exposure_max_brightness", 1.0),
    ):
        s.set_editor_property(chave, valor)
    ppv.set_editor_property("settings", s)

    if not les.save_current_level():
        raise RuntimeError("nao consegui salvar o mapa")
    log("Atores no mapa: %d" % len(eas.get_all_level_actors()))
    log("OK")


try:
    criar()
except Exception:  # noqa: BLE001
    log("ERRO\n" + traceback.format_exc())

with open(LOG, "w", encoding="utf-8") as f:
    f.write("\n".join(linhas) + "\n")

# So fecha o editor quando foi aberto apenas para rodar este script.
if "ExecutePythonScript" in unreal.SystemLibrary.get_command_line():
    unreal.SystemLibrary.quit_editor()
