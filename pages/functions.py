import PySimpleGUI as gui
import pyperclip as pc


def AttackPage():
    macro = ""
    genAttackColl1 = [[gui.Text("Nome do ataque*")],
                      [gui.Input()],
                      [gui.Text("Modificador de acerto/dano")],
                      [gui.Combo(values=("", "Força", "Destreza", "Inteligência", "Sabedoria", "Carisma"),
                                 default_value="", readonly=True, size=(43, 6))],
                      [gui.Text("Proficente")],
                      [gui.Combo(values=("Sim", "Não"), default_value="Sim", readonly=True, size=(43, 2))],
                      [gui.Text("Imagem/Gif")],
                      [gui.Input()],
                      [gui.Text("Efeito do ataque")],
                      [gui.Combo(values=("", "Feixe", "Bomba", "Sopro", "Borbulho", "Queima", "Explosão", "Brilho",
                                         "Míssil", "Supernova", "Espirro"),
                                 default_value="", readonly=True, size=(43, 6))],
                      [gui.Text("Tipo do efeito")],
                      [gui.Combo(values=("", "Ácido", "Sangue", "Charme", "Morte", "Fogo", "Gelo", "Sagrado",
                                         "Mágico", "Gosma", "Fumaça", "Água"), default_value="", readonly=True,
                                 size=(43, 6))]
                      ]
    genAttackColl2 = [[gui.Text("Dano*")],
                      [gui.Input(default_text='1d6')],
                      [gui.Text("Crítico*")],
                      [gui.Input(default_text='2d6')],
                      [gui.Text("Quantidade de ataques*")],
                      [gui.Input(default_text=1)],
                      [gui.Text("Modificador global de acerto?")],
                      [gui.Combo(values=("Sim", "Não"), default_value="Sim", readonly=True, size=(43, 2))],
                      [gui.Text("Modificador global de dano?")],
                      [gui.Combo(values=("Sim", "Não"), default_value="Sim", readonly=True, size=(43, 2))],
                      ]
    genAttack = [[gui.Text("Gerar Ataque")],
                 [gui.Col(genAttackColl1), gui.Col(genAttackColl2)],
                 [gui.Text("Macro")],
                 [gui.Output(size=(93, 5), key='MACRO')],
                 [gui.Button("Gerar Macro")],
                 [gui.Button("Copiar")],
                 [gui.Button("Voltar")]
                 ]
    # Set Attack Macro Generator window
    attkGen = gui.Window("Roll20 Macro Generator", genAttack,
                         icon=r'C:\Users\lucas\OneDrive\Área de Trabalho\Arquivos\Roll20 Macro '
                              r'Generator\image\logoicon.ico',
                         size=(800, 600), resizable=True,
                         element_justification='c')
    # Open Attack window
    while True:
        event, values = attkGen.read()
        if event == gui.WINDOW_CLOSED or event == "Voltar":
            break
        if event == "Gerar Macro":
            # Get values from inputs
            name = values[0]
            mod = values[1]
            pb = values[2]
            img = values[3]
            effectType = values[4]
            effectColor = values[5]
            dmg = values[6]
            crit = values[7]
            qtdAttk = int(values[8])
            modAttack = values[9]
            modDmg = values[10]

            # Check if there's an empty value
            if name == "" or dmg == "" or crit == "" or qtdAttk == "":
                attkGen.Element("MACRO").update(value="*Preencha os campos obrigatórios corretamente*")
            else:
                # Set value of 'Modificador de Acerto/Dano'
                if mod == "":
                    mod = ""
                elif mod == "Força":
                    mod = "+@{strength_mod}"
                elif mod == "Destreza":
                    mod = "+@{dexterity_mod}"
                elif mod == "Inteligência":
                    mod = "+@{intelligence_mod}"
                elif mod == "Sabedoria":
                    mod = "+@{wisdom_mod}"
                elif mod == "Carisma":
                    mod = "+@{charisma_mod}"

                # Set value of 'Proficiência'
                if pb == "Sim":
                    pb = "+@{pb}"
                else:
                    pb = ""

                if modAttack == "Sim":
                    modAttack = "+@{global_attack_mod}"
                else:
                    modAttack = ""

                if modDmg == "Sim":
                    modDmg = "+@{global_damage_mod_roll}"
                else:
                    modDmg = ""

                # Set the template value of the macro
                macro = "&{template:default}{{name=" + str(name) + "}}"

                # Check if there's link to insert
                if img != "":
                    macro += "{{[Missile](" + str(img) + ")}}"

                # Check if there's more than one attack
                if qtdAttk > 1:
                    # If there's more than one attack the loop will add the same command as many times as needed
                    for i in range(qtdAttk):
                        macro += "{{" + str(i + 1) + "° Acerto: [[1d20" + str(mod) + str(pb)\
                                 + str(modAttack) + "]] Vantagem: [[1d20" + str(mod) + str(pb) \
                                 + str(modAttack) + "]]}}{{" + str(i + 1) \
                                 + "° Dano: [[" + str(dmg) + str(mod) + str(modDmg) + "]] Crítico: [[" \
                                 + str(crit) + str(mod) + str(modDmg) + "]]}}"
                else:
                    macro += "{{Acerto: [[1d20" + str(mod) + str(pb) + str(modAttack) \
                             + "]] Vantagem: [[1d20" + str(mod) + str(pb) + str(modAttack) \
                             + "]]}}{{Dano: [[" + str(dmg) + str(mod) + str(modDmg) + "]] Crítico: [[" \
                             + str(crit) + str(mod) + str(modDmg) + "]]}}"

                # Check if there's an attack effect
                if effectType != "":
                    if effectColor != "":
                        if effectType == "Feixe":
                            effectType = "\n/fx beam-"
                        elif effectType == "Bomba":
                            effectType = "\n/fx bomb-"
                        elif effectType == "Sopro":
                            effectType = "\n/fx breath-"
                        elif effectType == "Borbulho":
                            effectType = "\n/fx bubbling-"
                        elif effectType == "Queima":
                            effectType = "\n/fx burn-"
                        elif effectType == "Explosão":
                            effectType = "\n/fx explode-"
                        elif effectType == "Brilho":
                            effectType = "\n/fx glow-"
                        elif effectType == "Míssel":
                            effectType = "\n/fx missile-"
                        elif effectType == "Supernova":
                            effectType = "\n/fx nova-"
                        elif effectType == "Espirro":
                            effectType = "\n/fx splatter-"

                        if effectColor == "Ácido":
                            effectColor = "acid @{target|Origem|token_id} @{target|Alvo|token_id}"
                        elif effectColor == "Sangue":
                            effectColor = "blood @{target|Origem|token_id} @{target|Alvo|token_id}"
                        elif effectColor == "Charme":
                            effectColor = "charm @{target|Origem|token_id} @{target|Alvo|token_id}"
                        elif effectColor == "Morte":
                            effectColor = "death @{target|Origem|token_id} @{target|Alvo|token_id}"
                        elif effectColor == "Fogo":
                            effectColor = "fire @{target|Origem|token_id} @{target|Alvo|token_id}"
                        elif effectColor == "Gelo":
                            effectColor = "frost @{target|Origem|token_id} @{target|Alvo|token_id}"
                        elif effectColor == "Sagrado":
                            effectColor = "holy @{target|Origem|token_id} @{target|Alvo|token_id}"
                        elif effectColor == "Mágico":
                            effectColor = "magic @{target|Origem|token_id} @{target|Alvo|token_id}"
                        elif effectColor == "Gosma":
                            effectColor = "slime @{target|Origem|token_id} @{target|Alvo|token_id}"
                        elif effectColor == "Fumaça":
                            effectColor = "smoke @{target|Origem|token_id} @{target|Alvo|token_id}"
                        elif effectColor == "Água":
                            effectColor = "water @{target|Origem|token_id} @{target|Alvo|token_id}"
                    else:
                        effectType = ""
                        effectColor = ""
                        attkGen.Element("MACRO").update(value="Insira o tipo de efeito no ataque")

                    macro += effectType+effectColor

                # Display the result
                attkGen.Element("MACRO").update(value=macro)
        if event == "Copiar":
            if macro != "":
                pc.copy(macro)
                gui.popup("Macro adicionado a área de transferência", auto_close_duration=2, auto_close=True,
                          no_titlebar=True, button_type=5)
    attkGen.close()


def MagicPage():
    genMagicColl1 = [[gui.Text("Nome da magia")],
                     [gui.Input()],
                     [gui.Text("Nome do primeiro valor:")],
                     [gui.Input(default_text="Cura: ")],
                     [gui.Text("")]
                     ]
    genMagicContent = [[gui.Text("Gerar Magia")],
                       [gui.Col(genMagicColl1)],
                       [gui.Output(size=(93, 5))],
                       [gui.Button("Gerar Macro")],
                       [gui.Button("Voltar")]
                       ]

    magicGen = gui.Window("Roll20 Macro Generator", genMagicContent,
                          icon=r'C:\Users\lucas\OneDrive\Área de Trabalho\Arquivos\Roll20 Macro '
                               r'Generator\image\logoicon.ico',
                          size=(800, 600), element_justification='c')
    while True:
        event, values = magicGen.read()
        if event == gui.WINDOW_CLOSED or event == 'Voltar':
            break
    magicGen.close()


def GIFPage():
    genGifContent = [[gui.Text("Nome*")],
                     [gui.Input()],
                     [gui.Text("Link*")],
                     [gui.Multiline(size=(93, 5))],
                     [gui.Output(size=(93, 5), key='GIF')]
                     ]
    genGif = [[gui.Text("Gerar GIF", )],
              [gui.Col(genGifContent)],
              [gui.Button("Gerar Macro")],
              [gui.Button("Voltar")]
              ]
    # Set GIF Macro Generator
    genGifPage = gui.Window("Roll20 Macro Generator", genGif,
                            icon=r'C:\Users\lucas\OneDrive\Área de Trabalho\Arquivos\Roll20 Macro '
                                 r'Generator\image\logoicon.ico',
                            size=(800, 600), element_justification='c')
    # Display the window
    while True:
        event, values = genGifPage.read()
        if event == gui.WINDOW_CLOSED or event == 'Voltar':
            break
        if event == "Gerar Macro":
            # Get the values of inputs
            name = values[0]
            img = values[1]
            # Check if there's an empty value
            if img == "" or name == "":
                genGifPage.Element("GIF").update("*Preencha os campos obrigatórios*")
            else:
                macro = "&{template:default}{{name=" + str(name) + "}}{{[Missile](" + str(img) + ")}}"
                # Display the result
                genGifPage.Element("GIF").update(value=macro)
    genGifPage.close()
