import os

def Arquivos(caminho):

    # Atualiza a lista de caminhos para o arquivo
    lista_arquivos = []

    for diretorio,subpastas,arquivos in os.walk(caminho):
        for arquivo in arquivos:
            lista_arquivos.append(os.path.join(diretorio, arquivo))
        # for
    # for

    return lista_arquivos
# Arquivos

def Verificar(arquivos,caminho,nome):

    # Verifica se já existe um arquivo com aquele nome
    existe = 0
    for arquivo in arquivos:
        comparacao = os.path.join(caminho,f'{nome}.png')
        if comparacao == arquivo:
            existe = 1
            break
        else:
            existe = 0
        # if
    # for

    return existe
# Verificar