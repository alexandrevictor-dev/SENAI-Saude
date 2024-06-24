class Musica:
    nome = ""
    artista = ""
    genero = ""


m1 = Musica()
m1.nome = "After Life"
m1.artista = "Five Fingers Death Punch"
m1.genero = "Rock"

m2 = Musica()
m2.nome = "I Had Some Help"
m2.artista = "Post Malone"
m2.genero = "Country Rock"

m3 = Musica()
m3.nome = "Tu és"
m3.artista = "Fhop Music"
m3.genero  = "Gospel Worship"





print(m2) # Quando executamos dessa forma, ele mostra o código de onde
#Está alocado na memória. Para mostrar o que há de funções e atributos em forma de dicionário, utiliza-se a função "vars"

print(vars(m2))