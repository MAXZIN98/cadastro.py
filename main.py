from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(40,1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(40,1))],
    [sg.Checkbox('Salvar o login')],
    [sg.Button('Entrar')],
]
# Janela
janela = sg.Window('Tela de Login', layout)
# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'max' and valores['senha'] == 'max1908':
            print('Bem-vindo a MaxLab!')
