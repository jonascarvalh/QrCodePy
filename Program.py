import qrcode
import shutil

from pathlib import Path

# create "images" path
caminho = ('./images')
Path(caminho).mkdir(exist_ok=True)

# Input
link = input('Type your link: ')
nome = input('Create a name of link: ')
link = qrcode.make(link)


# Output: saving qrcode
link.save(f'{nome}.png')
source = f'./{nome}.png'

shutil.move(source,caminho)