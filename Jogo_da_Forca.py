# Trabalho Prático I: Implementar o jogo da forca
# Completar a seguinte informação:
# Nome: Juliana
# Matrícula: <Matrícula>
# jogoforca.py

# tomadas de https://duvidas.dicio.com.br/as-15-palavras-mais-engracadas-da-lingua-portuguesa/
# você pode incluir mais palavras na lista.

BONECO = ['''

    +---+
    |   /
        /
        /
        /
        /
===========''', '''

    +---+
    |   /
    O   /
        /
        /
        /
===========''', '''

    +---+
    |   /
    O   /
    |   /
        /
        /
===========''', '''

    +---+
    /   /
    O   /
    |\  /
        /
        /
===========''', '''

    +---+
    |   /
    O   /
   /|\  /
        /
        /
===========''', '''

    +---+
    |   /
    O   /
   /|\  /
   /    /
        /
===========''', '''

    +---+
    |   /
    O   /
   /|\  /
   / \  /
        /
===========''']


LISTA_PALAVRAS = ('Mequetrefe', 'Salamaleque', 'Piripaque', 'Serelepe',
                  'Siricutico', 'Bugiganga', 'Borogodo', 'Birimbau', 'Quinquilharia',
                  'Beleleu', 'Balacobaco', 'Faniquito', 'Quiproquo', 'Pebolim',
                  'Ziquizira', 'Zunzunzum', 'Ziguezague', 'Ferreiro', 'Filomena')

# Número máximo de tentativas.
MAX_TENTATIVAS = 6

tentativa = 0

def obter_palavra():
    '''
    Retorna uma palavra aleatória da lista de palavras LISTA_PALAVRAS.
    '''
    # Eliminar esta linha uma vez que a função esteja implementada.
    raise NotImplementedError('Função obter_palavra() não implementada!')

    # seu código deve retornar um elemento de LISTA_PALAVRAS
    # palavra_secreta = ...
    # return palavra_secreta


def palavra_adivinhada(palavra_secreta, letras_usuario):
    '''
    Retorna True se os caracteres presentes na lista letras_usuario são
    suficentes para adivinhar a palavra palavra_secreta. Retorna False em outro caso.
    Parâmetros:
    * palavra_secreta: palavra a ser adivinhada.
    * letras_usuario: lista das letras que o usuário entrou até agora.
    '''
    raise NotImplementedError('Função palavra_adivinhada() não implementada!')

def tentativas_erradas(palavra_secreta, letras_usuario):
    '''
    Retorna a quantidade de letras em letras_usuario que não aparecem em
    palavra_secreta.
    Parâmetros:
    * palavra_secreta: palavra a ser adivinhada.
    * letras_usuario: lista das letras que o usuário entrou até agora.
    '''
    raise NotImplementedError('Função tentativas_erradas() não implementada!')


def mostra_adivinhadas(palavra_secreta, letras_usuario):
    '''
    Mostra que letras de palavra_secreta tem sido adivinhadas até agora e
    todas as letras entradas pelo usuário.
    Por exemplo, a saída para a palavra secreta "batatinha" e as entradas do
    usuário b, c e t deve ser do tipo:
    Palavra secreta: B _ T _ T _ _ _ _
    Letras tentadas até agora: B, C, T
    Parâmetros:
    * palavra_secreta: palavra a ser adivinhada.
    * letras_usuario: lista das letras que o usuário entrou até agora.
    '''

    raise NotImplementedError('Função mostra_adivinhadas() não implementada!')



def entra_tentativa(palavra_secreta, letras_usuario):
    '''
    Permite ao usuário entrar com uma letra. Deve garantir que a entrada não seja
    um caracter inválido (números, varias letras, signos de pontuação, etc.)
    Deve validar se a letra informada existe ou não existe na palavra secreta. Deve informar se o usuário acertou/errou a letra.
    Deve validar se a letra já foi informada pelo usuário.

    '''

    raise NotImplementedError('Função entra_tentativa() não implementada!')

    # Perguntar ao usuário por uma letra e, se a entrada não é correta, insistir.
    # letra = ...
    # return letra

def displayBoard(BONECO, tentativa):
    ''' Permitir que o boneco da forca seja apresentado para o usuário em cada uma de suas tentativas. O boneco deve
     ser apresentado de acordo com o erro/acerto do usuário.'''

    raise NotImplementedError('Função displayBoard() não implementada!')


def jogo_da_forca():
    '''
    Função principal do jogo.
    '''

    print('Bem vindo ao jogo da forca.')
    tentativa = 0

    while True:
        palavra_secreta = obter_palavra()

        letras_usuario = []

        displayBoard(BONECO, tentativa)

        while not palavra_adivinhada(palavra_secreta, letras_usuario) and \
              tentativas_erradas(palavra_secreta, letras_usuario) < MAX_TENTATIVAS:

              mostra_adivinhadas(palavra_secreta, letras_usuario)

              restantes = MAX_TENTATIVAS - tentativas_erradas(palavra_secreta, letras_usuario)
              print('Tentativas restantes:', restantes)
              letra = entra_tentativa(palavra_secreta, letras_usuario)
              letras_usuario.append(letra)

              #Informar aqui o ajuste necessário no programa, a fim de que o boneco seja apresentado.
              # Use a variável tentativa já declarada.

        mostra_adivinhadas(palavra_secreta, letras_usuario)


        if palavra_adivinhada(palavra_secreta, letras_usuario):
            print('Parabéns, você adivinhou a palavra!')
        else:
            print('¯\\_(ツ)_/¯ você perdeu.')
            print("A palavra da forca era: ", palavra_secreta)

        cont = input('Entre C se deseja continuar jogando.')
        if not (cont == 'C' or cont =='c'):
            break
        else:
           jogo_da_forca()

    print('Game over.')


# chamada a função principal para executar o jogo.
jogo_da_forca()
