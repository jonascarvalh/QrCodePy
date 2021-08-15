import shutil
import Tamanho as tam

from pathlib import Path

# Criação da pasta imagens
caminho = ('./imagens')
Path(caminho).mkdir(exist_ok=True)

# Entrada
link = input('Seu link: ')
nome = input('Nome do QR Code: ')

# Setar tamanho do QR Code
qr = tam.EscolhaTamanho()

# Processamento
qr.add_data(link)
qr.make(fit = True)
link = qr.make_image( fill_color = "black", back_color="white")

# Saída: Salvando QR Code e movendo para a pasta "imagens"
link.save(f'{nome}.png')

source = f'./{nome}.png'
shutil.move(source,caminho)

print(f'\nA imagem foi gerada em: {caminho}/{nome}.png !')