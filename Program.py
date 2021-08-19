import shutil
import Tamanho as tam
import Diretorio as Dir
from pathlib import Path

# Criação da pasta 'imagens'
caminho = ('.\imagens')
Path(caminho).mkdir(exist_ok=True)
arquivos = Dir.Arquivos(caminho)

while (1):
    # Entrada
    link = input('Seu link: ')
    nome = input('Nome do QR Code: ').lower()

    existe = Dir.Verificar(arquivos,caminho,nome)
    if (existe == 0): 
        break
    else:
        print('Indique outro nome para o arquivo!')
    # if
# while

# Setar tamanho do QR Code
qr = tam.EscolhaTamanho()

# Processamento: Criação da Imagem
qr.add_data(link)
qr.make(fit = True)
imagem = qr.make_image( fill_color = "black", back_color="white")

# Saída: Salvando QR Code e movendo para a pasta "imagens"
imagem.save(f'{nome}.png')

source = f'./{nome}.png'
shutil.move(source,caminho)

print(f'\nA imagem foi gerada em: {caminho}\{nome}.png !')