import PySimpleGUI as gui
import pages.functions as func

gui.theme("DarkPurple2")
homePage = [[gui.Text("Roll20 Macro Generator")],
            [gui.Button('Gerar Ataque')],
            [gui.Button('Gerar Magia')],
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
        func.AttackPage()
    if event == "Gerar Magia":
        func.MagicPage()
    if event == "Gerar GIF":
        func.GIFPage()
window.close()
