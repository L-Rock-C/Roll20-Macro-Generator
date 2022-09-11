import PySimpleGUI as gui

gui.theme("DarkPurple2")
homePage = [[gui.Text("Roll20 Macro Generator")],
            [gui.Button('Gerar Ataque')],
            [gui.Button('Gerar GIF')],
            [gui.Button('Sair')]]

# Set homepage window
window = gui.Window("Roll20 Macro Generator", homePage, size=(400, 300), resizable=True, element_justification='c')

# Display window
while True:
    event, values = window.read()
    if event == gui.WINDOW_CLOSED or event == 'Sair':
        break
    if event == "Gerar Ataque":
        genAttackColl1 = [[gui.Text("Nome do ataque*")],
                          [gui.Input()],
                          [gui.Text("Modificador de acerto/dano")],
                          [gui.Combo(values=("Força", "Destreza", "Inteligência", "Sabedoria", "Carisma"),
                                     default_value="Força", size=(43, 6))],
                          [gui.Text("Proeficente")],
                          [gui.Combo(values=("Sim", "Não"), default_value="Sim", size=(43, 2))],
                          [gui.Text("Imagem/Gif")],
                          [gui.Input()]
                          ]
        genAttackColl2 = [[gui.Text("Bônus de acerto")],
                          [gui.Input(default_text=0)],
                          [gui.Text("Dano*")],
                          [gui.Input(default_text='1d6')],
                          [gui.Text("Crítico*")],
                          [gui.Input(default_text='2d6')],
                          [gui.Text("Quantidade de ataques*")],
                          [gui.Input(default_text=1)]
                          ]
        genAttack = [[gui.Text("Gerar Ataque")],
                     [gui.Col(genAttackColl1), gui.Col(genAttackColl2)],
                     [gui.Text("Macro")],
                     [gui.Output(size=(93, 5), key='MACRO')],
                     [gui.Button("Gerar Macro")],
                     [gui.Button("Voltar")]
                     ]
        # Set Attack Macro Generator window
        attkGen = gui.Window("Roll20 Macro Generator", genAttack, size=(800, 600), resizable=True, element_justification='c')
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
                bonus = values[4]
                dmg = values[5]
                crit = values[6]
                qtdAttk = int(values[7])
                # Check if there's an empty value
                if name == "" or dmg == "" or crit == "" or qtdAttk == "":
                    attkGen.Element("MACRO").update(value="*Preencha os campos obrigatórios corretamente*")
                else:
                    # Set value of 'Modificador de Acerto/Dano'
                    if mod == "Força":
                        mod = "strength_mod"
                    elif mod == "Destreza":
                        mod = "dexterity_mod"
                    elif mod == "Inteligência":
                        mod = "intelligence_mod"
                    elif mod == "Sabedoria":
                        mod = "wisdom_mod"
                    elif mod == "Carisma":
                        mod = "charisma_mod"

                    # Set value of 'Proeficiencia'
                    if pb == "Sim":
                        pb = "+@{pb}"
                    else:
                        pb = ""

                    # Set the template value of the macro
                    macro = "&{template:default}{{name=" + str(name) + "}}"

                    # Check if there's link to insert
                    if img != "":
                        macro += "{{[Missile](" + str(img) + ")}}"

                    # Check if there's more than one attack
                    if qtdAttk > 1:
                        # If there's more than one attack, a loop will add the same command as many times as needed
                        for i in range(qtdAttk):
                            macro += "{{" + str(i+1) + "° Acerto: [[1d20+@{" + str(mod) + "}" + str(pb) + "+" + str(bonus)\
                                     + "]] Vantagem: [[1d20+@{" + str(mod) + "}" + str(pb) + "+" + str(bonus) + "]]}}{{" + str(i+1) \
                                     + "° Dano: [[" + str(dmg) + "+@{" + str(mod) + "}]] Crítico: [[" + str(crit) + "+@{"\
                                     + str(mod) + "}]]}}"
                    else:
                        macro += "{{Acerto: [[1d20+@{" + str(mod) + "}" + str(pb) + "+" + str(bonus) + "]] Vantagem: [[1d20+@{"\
                                 + str(mod) + "}" + str(pb) + "+" + str(bonus) + "]]}}{{Dano: [[" + str(dmg) \
                                 + "+@{" + str(mod) + "}]] Crítico: [[" + str(crit) + "+@{" + str(mod) + "}]]}}"

                    # Display the result
                    attkGen.Element("MACRO").update(value=macro)
        attkGen.close()
    if event == "Gerar GIF":
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
        genGifPage = gui.Window("Roll20 Macro Generator", genGif, size=(800, 600), element_justification='c')
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
window.close()
