import qrcode

def EscolhaTamanho():

    # Define um tamanho ao QR Code
    opcao = input('\n |> Deseja alterar o tamanho da imagem? \n |> Opcao: ').lower()
    if (opcao == 'sim'):
        print(' |> Indique apenas um lado em px da figura')
        tamanho = int(input(' |> Lado: '))
        qr = Tamanho(tamanho/25)
    else:
        #Padrão da Imagem: 1000x1000
        qr = Tamanho(1000/25)
    # if  

    return qr
# EscolhaTamanho

def Tamanho(tamanho):

    # Retorna os atributos definidos ao QRCode
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=tamanho,
        border=0,)
    return qr
# Tamanho