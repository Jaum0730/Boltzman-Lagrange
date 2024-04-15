import turtle
import math
import random
from time import sleep
import winsound

geral = turtle.Turtle()
geral.penup()
geral.speed(0)

def Pontos(instrumento):
    instrumento.undo()
    instrumento.color("white")
    instrumento.penup()
    instrumento.setposition(-100, 250)
    instrumento.write(f"Pontos: {player.score}", font=("Arial", 13, "bold"))

class Arena(): # class Arena é a função onde principal onde eu coloco o personagem e os entes para o jogo
    def __init__(self):
        self.x = 0  # não tem limite de borda
        self.y = 0  # não tem limite de borda
        self.heading = 0
        self.dx = 0
        self.dy = 0
        self.shape = "square"
        self.color = "green"
        self.size = 1.0
        self.active = True

    def posicao(self):
        if self.active:
            self.x += self.dx
            self.y += self.dy

            if self.x > 400:  # estabelece o escopo de spawn e de ação dos entes e do personagem
                self.x = -400  # estabelece o escopo de spawn e de ação dos entes e do personagem
            elif self.x < -400:  # estabelece o escopo de spawn e de ação dos entes e do personagem
                self.x = 400  # estabelece o escopo de spawn e de ação dos entes e do personagem

            if self.y > 300:  # estabelece o escopo de spawn e de ação dos entes e do personagem
                self.y = -300  # estabelece o escopo de spawn e de ação dos entes e do personagem
            elif self.y < -300:  # estabelece o escopo de spawn e de ação dos entes e do personagem
                self.y = 300  # estabelece o escopo de spawn e de ação dos entes e do personagem

    def Renderizardor(self, geral): #  estanbelece o spawn dos entes e do personagem
        if self.active:
            geral.goto(self.x, self.y)
            geral.setheading(self.heading)
            geral.shape(self.shape)
            geral.shapesize(self.size, self.size, 0)
            geral.color(self.color)
            geral.stamp()

    def Contato(self, other):  # define o contato entre o personagem e os entes
        x = self.x - other.x
        y = self.y - other.y
        espacamento = ((x ** 2) + (y ** 2)) ** 0.5  # definição
        if espacamento < ((10 * self.size) + (10 * other.size)):
            return True
        else:
            return False

    def goto(self, x, y):  # atrubuição para o 'go to' do personagem e dos entres na tela
        self.x = x
        self.y = y


class Boltzman(Arena): # dentro dos parenteses chama a classe arena
    def __init__(self):
        Arena.__init__(self)
        self.shape = ('Nave-2.gif')
        self.lives = 5
        self.score = 0

    def rotate_left(self):  # movimentação de 30º ou seja, o personagem totaciona em um eixo 12 vezes
        self.heading += 30

    def rotate_right(self):  # movimentação de 30º ou seja, o personagem totaciona em um eixo 12 vezes
        self.heading -= 30

    def forward(self):  # movimentação para a frente
        ax = math.cos(math.radians(self.heading))
        ay = math.sin(math.radians(self.heading))
        self.dx += ax * 0.1
        self.dy += ay * 0.1

    def backward(self):  # movimentação para a tras
        ax = math.cos(math.radians(self.heading))
        ay = math.sin(math.radians(self.heading))
        self.dx -= ax * 0.1
        self.dy -= ay * 0.1

    def Renderizardor(self, geral):  # a partir da variavel chamada GERAL o personagem é colocado dentro de um laço onde onde é feita a contabilidade das vidas
        if self.active:
            geral.goto(self.x, self.y)
            geral.setheading(self.heading)
            geral.shape(self.shape)
            geral.shapesize(self.size / 2.0, self.size, 0)  # modifica a forma do triangulo, deixa mais achatado nos lados
            geral.color(self.color)
            geral.stamp()

class Missil(Arena):  # dentro dos parenteses chama a classe arena
    def __init__(self):
        Arena.__init__(self)
        self.shape = "missel.gif"
        self.size = 0.2
        self.active = False  # False para ser ativado somente quando chamado pelo 'space' do teclado

    def posicao(self):
        if self.active:
            self.x += self.dx
            self.y += self.dy

            if self.x > 400:
                self.active = False
            elif self.x < -400:
                self.active = False

            if self.y > 300:
                self.active = False
            elif self.y < -300:
                self.active = False

    def foguete(self):
        if not self.active:
            self.active = True
            self.x = player.x
            self.y = player.y
            self.heading = player.heading  # sai a partir da ponta do personagem
            self.dx = math.cos(math.radians(self.heading)) * 10  # estabelece a velicidade do disparo
            self.dy = math.sin(math.radians(self.heading)) * 10  # estabelece a velicidade do disparo


# ESTABELECE AS CLASSES ASTEROIDES E ALIENS, SEUS DETALHES ESTÃO MAIS A FRENTE
class Asteroide(Arena):  # dentro dos parenteses chama a classe arena
    def __init__(self):
        Arena.__init__(self)
        self.shape = ('asteroids.gif')


class Alien(Arena):  # dentro dos parenteses chama a classe arena
    def __init__(self):
        Arena.__init__(self)
        self.shape = ('alien1.gif') #



#Corpo Principal
# recolhe os entes e os personagens para o jogo em uma lista
colecao = []

#SoundTrack

winsound.PlaySound("song.wav", winsound.SND_ASYNC + winsound.SND_LOOP)

player = Boltzman()  # chama o persogagem e adiciona na lista
colecao.append(player)

missile = Missil()  # chama o missil e adiciona na lista
colecao.append(missile)

# tela do jogo
janela = turtle.Screen()
janela.bgcolor("black")
janela.title("Boltzmann Lagrange")
janela.setup(800, 600)
janela.tracer(0)

# adiciona as sprites do personagem, entes e do background
janela.bgpic('885542.gif') # janela.bgpic('background.gif')
janela.addshape('asteroids.gif')
janela.addshape('alien1.gif')
janela.addshape('coracao.gif')
janela.addshape('missel.gif')
janela.addshape('Nave-2.gif')


#Contador de pontos
contabilizador = turtle.Turtle()
contabilizador.shape('blank')




# Laço que estabelece os detalhes dos de asteroides e dos aliens
for _ in range(5):  # total de spawnam na tela
    asteroide = Asteroide()  # chama o ente
    x = random.randint(-375, 375)
    y = random.randint(-275, 275)
    asteroide.goto(x, y)
    dx = random.randint(-5, 5) / 20.0
    dy = random.randint(-5, 5) / 20.0
    asteroide.dx = dx
    asteroide.dy = dy
    size = random.randint(10, 30) / 10.0
    asteroide.size = size
    colecao.append(asteroide)  # adiciona o asteroide na lista

for _ in range(2):  # total de spawnam na tela
    alien = Alien()   # chama o ente
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    alien.goto(x, y)
    dx = random.randint(-5, 5) / 30.0
    dy = random.randint(-5, 5) / 30.0
    alien.dx = dx
    alien.dy = dy
    size = random.randint(10, 30) / 10.0
    alien.size = size
    colecao.append(alien)  # adiciona o asteroide na lista

# chamada de funções do personagem no teclado
janela.listen()
janela.onkeypress(player.rotate_left, "Left")
janela.onkeypress(player.rotate_right, "Right")
janela.onkeypress(player.forward, "Up")
janela.onkeypress(player.backward, "Down")
janela.onkeypress(missile.foguete, "space")

# mosta o titulo do jogo na tela
'''
titulo = turtle.Turtle()
titulo.color("white")
titulo.penup()
titulo.setposition(-358, 250)
titulo.write('BOLTZMAN LAGRANGE!', font=('arial', 30, 'bold'))
titulo.hideturtle()
'''
# mosta o texto 'vidas' na tela

vidas = turtle.Turtle()
vidas.color("white")
vidas.penup()
vidas.setposition(-200, 250)
vidas.write("Vidas", font=("Arial", 15, "bold"))
vidas.hideturtle()



#Laços
# laço que faz a ação do jogo
while True:
    # Atualiza a janela

    janela.update()

    geral.clear()

    # Imprime scores e vidas
    for i in range(player.lives):  # exibe o contador de vidas na tela
        geral.goto(-350 + 30 * i, 265)
        geral.shape("coracao.gif")
        geral.shapesize(0.7, 0.7, 0)
        geral.setheading(90)
        geral.stamp()


    for entes in colecao:  # tras os entes e personagens a arena
        entes.posicao()
        entes.Renderizardor(geral)

    # checador de coalizão
    for entes in colecao:
        if isinstance(entes, Asteroide):
            if player.Contato(entes):  # CHAMA O ENTE PARA QUE SEJA ESTABELECIDO O CONTATO.
                player.lives -= 1  # COMPUTA UMA VIDA A MENOS QUANDO HÁ O CONTATO
                print(f"Vidas: {player.lives}")
                player.goto(0, 0)   # ONDE O JOGADOR ESTARÁ APOS O CONTATO
                entes.goto(100, 100)  # ONDE O ENTE ESTARÁ APOS O CONTATO

            if player.lives <= 0: # checador de vidas (É MENOR / IGUAL PARA QUE TODAS OS CORAÇÕES SUMAM DA TELA)
                print("O JOGADOR ESTÁ MORTO")
                player.active = False
                gm = turtle.Turtle()
                gm.speed(0)
                gm.color("white")
                gm.penup()
                gm.write(f"GAME OVER", align="center", font=("Arial", 50, "bold"))
                gm.hideturtle()
                sleep(15)  # APOS A MORTE DO PERSONAGEM O JOGO ESPERA 15 SEGUNDOS PARA FECHAR
                exit()

            if missile.active and missile.Contato(entes):  # laço que estabelece o contato do missil com os entes
                print("UM  ASTEROIDE FOI DESTRUIDO")
                missile.active = False
                player.score += 5
                Pontos(contabilizador)
                print(f"A NAVE MARCA: {player.score} PONTOS")
                entes.goto(100, 100)

            elif (player.score == 5000):  #  laço que estabelece o objetivo do jogo
                win = turtle.Turtle()
                win.speed(0)
                win.color("white")
                win.penup()
                win.write(f"VOCÊ ANIQUILOU\n A AMEAÇA ALIENIGINA", align="center", font=("Arial", 50, "bold",))
                win.hideturtle()
                sleep(15)
                exit()
            #elif (player.score == 500):
                #player.lives += 1


    for entes in colecao:
        if isinstance(entes, Alien):
            if player.Contato(entes):
                player.lives -= 1
                print(f"Vidas: {player.lives}")
                player.goto(0, 0)
                entes.goto(100, 100)


                if player.lives <= 0:  # checador de vidas (É MENOR IGUAL PARA QUE TODAS OS CORAÇÕES SUMAM DA TELA)
                    print("O JOGADOR ESTÁ MORTO")
                    player.active = False
                    gm = turtle.Turtle()
                    gm.speed(0)
                    gm.color("white")
                    gm.penup()
                    gm.write(f"GAME OVER", align="center", font=("Arial", 50, "bold",))
                    gm.hideturtle()

                    sleep(15)
                    exit()

            if missile.active and missile.Contato(entes):
                print("UM  ALIEN FOI DESTRUIDO")
                missile.active = False
                player.score += 10
                Pontos(contabilizador)
                print(f"A NAVE MARCA: {player.score} PONTOS")
                entes.goto(-100,100)

            #elif (player.score == 1000):
                #player.lives += 1

            elif(player.score == 10000):
                win = turtle.Turtle()
                win.speed(0)
                win.color("white")
                win.penup()
                win.write(f"VOCÊ ANIQUILOU\n A AMEAÇA ALIENIGINA", align="center", font=("Arial", 50, "bold",))
                win.hideturtle()
                sleep(15)
                exit()





janela.mainloop()

