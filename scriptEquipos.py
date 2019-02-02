import django
from JuEq.models import Equipo, Jugador
Equipo.objects.all()

nombre_equipo = ['Alaves', 'At.Madrid', 'Ath.Bilbao', 'Barcelona', 'Celta de Vigo', 'Deportivo', 'Eibar', 'Espanyol', 'Granada', 'Leganes', 'Real Betis', 'Real Madrid', 'Real Sociedad', 'Sevilla', 'Sporting', 'UD Las Palmas', 'Valencia', 'Villareal']

for i in nombre_equipo:
    print i
    equipo = Equipo.objects.create(nombre_equipo="Barcelona", ciudad_equipo="Barcelona", anio_creacion="", historia_equipo="blabla", entrenador_equipo="Luis Enrique")
	jugador = Jugador.objects.create(nombre_jugador="Andres Iniesta", ciudad_natal="Fuente Alvilla", edad_jugador="23", fecha_nacimiento="2-23-1987", posicion_jugador="Centrocampista", ="adsfqwer", equipo_jugador="Barcelona", )

    equipo.save()
    jugador.save()

    print q.id
exit()

$ ./manage.py shell
...
>>> execfile('myscript.py')

#jugador = Jugador.objects.create(nombre_jugador="Andres Iniesta", posicion_jugador="Centrocampista",ciudad_natal="Fuente Alvilla", edad_jugador="23", fecha_nacimiento="2/23/1987", ="adsfqwer", equipo_jugador="Barcelona", )
#equipo = Equipo.objects.create(nombre_equipo="Barcelona", ciudad_equipo="Barcelona", anio_creacion="2/20/1842", historia_equipo="asdcre", entrenador_equipo="Luis Enrique")

equipo = Equipo.objects.create(nombre_equipo="Malaga CF", ciudad_equipo="Malaga", entrenador_equipo="Juande Ramos")
equipo2 = Equipo.objects.create(nombre_equipo="Deportivo Alaves", ciudad_equipo="Alaves",  entrenador_equipo="Mauricio Pellegrino")
equipo3 = Equipo.objects.create(nombre_equipo="Real Club Celta de Vigo", ciudad_equipo="Vigo", entrenador_equipo="Eduardo Berizzo")
equipo4 = Equipo.objects.create(nombre_equipo="Real Betis Balompie", ciudad_equipo="Sevilla",  entrenador_equipo="Victor Sánchez del Amo")
equipo5 = Equipo.objects.create(nombre_equipo="Real Club Deportivo de la Corunia", ciudad_equipo="Corunia", entrenador_equipo="Gaizka Garitano")
equipo6 = Equipo.objects.create(nombre_equipo="Club Deportivo Leganés", ciudad_equipo="Leganés",  entrenador_equipo="Asier Garitano")
equipo7 = Equipo.objects.create(nombre_equipo="Valencia CF", ciudad_equipo="Valencia",  entrenador_equipo="Cesare Prandelli")
equipo8 = Equipo.objects.create(nombre_equipo="Real Sporting de Gijon",  entrenador_equipo="Abelardo Fernandez")
equipo9 = Equipo.objects.create(nombre_equipo="Granada CF", ciudad_equipo="Granada",  entrenador_equipo="Lucas Alcazar")
equipo10 = Equipo.objects.create(nombre_equipo="Club Atlético Osasuna", ciudad_equipo="Pamplona",  entrenador_equipo="Joaquin Caparros")

	equipo11 = Equipo.objects.create(nombre_equipo="Real Madrid CF", ciudad_equipo="Madrid",  entrenador_equipo="Zinedine Zidane")
	equipo12 = Equipo.objects.create(nombre_equipo="FC Barcelona", ciudad_equipo="Barcelona",  entrenador_equipo="Luis Enrique Martinez Garcia")
	equipo13 = Equipo.objects.create(nombre_equipo="Sevilla FC", ciudad_equipo="Sevilla",  entrenador_equipo="Jorge Sampaoli")
	equipo14 = Equipo.objects.create(nombre_equipo="Villareal CF", ciudad_equipo="Villareal",  entrenador_equipo="Fran Escriba")
	equipo15 = Equipo.objects.create(nombre_equipo="Real Sociedad de Futbol", ciudad_equipo="San Sebastian", entrenador_equipo="Eusebio Sacristan")
	equipo16 = Equipo.objects.create(nombre_equipo="Club Atletico de Madrid", ciudad_equipo="Madrid",  entrenador_equipo="Diego Pablo Simeone")
	equipo17 = Equipo.objects.create(nombre_equipo="Athletic Club", ciudad_equipo="Bilbao",  entrenador_equipo="Ernesto Valverde")
	equipo18 = Equipo.objects.create(nombre_equipo="Sociedad Deportiva Eibar", ciudad_equipo="Eibar", entrenador_equipo="Jose Luis Mendilibar")
	equipo19 = Equipo.objects.create(nombre_equipo="Real Club Deportivo Espaniol", ciudad_equipo="Barcelona",  entrenador_equipo="Quique Sanchez Flores")
	equipo20 = Equipo.objects.create(nombre_equipo="Union Deportiva Las Palmas", ciudad_equipo="Las Palmas",  entrenador_equipo="Quique Setien")

equipo_id=Equipo.objects.get(id=16)
jugador = Jugador.objects.create(nombre_jugador="Andres Iniesta",ciudad_natal="Fuente Alvilla",edad_jugador="32",fecha_nacimiento="1984-05-11", posicion="Centrocampista",  equipo_jugador=equipo_id, puntos_jugador="0", valor_jugador="120000" )
jugador2 = Jugador.objects.create(nombre_jugador="Marc-Andre ter Stegen",ciudad_natal="Monchengladbach",edad_jugador="24",fecha_nacimiento="1992-04-30", posicion="Portero",  equipo_jugador=equipo_id, puntos_jugador="0", valor_jugador="120000")
jugador3 = Jugador.objects.create(nombre_jugador="Gerard Pique",ciudad_natal="Barcelona",edad_jugador="29",fecha_nacimiento="1987-02-02", posicion="Defensa",  equipo_jugador=equipo_id, puntos_jugador="0", valor_jugador="120000")
jugador4 = Jugador.objects.create(nombre_jugador="Javier Mascherano",ciudad_natal="Argentina",edad_jugador="32",fecha_nacimiento="1984-06-08", posicion="Defensa",  equipo_jugador=equipo_id, puntos_jugador="0", valor_jugador="120000")
jugador5 = Jugador.objects.create(nombre_jugador="Jeremy Mathieu",ciudad_natal="Francia",edad_jugador="33",fecha_nacimiento="1983-10-29", posicion="Defensa",  equipo_jugador=equipo_id, puntos_jugador="0", valor_jugador="120000")
jugador6 = Jugador.objects.create(nombre_jugador="Jordi Alba",ciudad_natal="Hospitalet de Llobregat",edad_jugador="27",fecha_nacimiento="1989-03-21", posicion="Defensa",  equipo_jugador=equipo_id, puntos_jugador="0", valor_jugador="120000")
jugador7 = Jugador.objects.create(nombre_jugador="Sergio Busquets",ciudad_natal="Sabadell",edad_jugador="28",fecha_nacimiento="1988-07-16", posicion="Centrocampista",  equipo_jugador=equipo_id, puntos_jugador="0", valor_jugador="120000")
jugador8 = Jugador.objects.create(nombre_jugador="Ivan Rakitic",ciudad_natal="Mohlin",edad_jugador="28",fecha_nacimiento="1988-03-10",  posicion="Centrocampista",  equipo_jugador=equipo_id, puntos_jugador="0", valor_jugador="120000")
jugador9 = Jugador.objects.create(nombre_jugador="Neymar",ciudad_natal="Brasil",edad_jugador="24",fecha_nacimiento="1992-02-05",  posicion="Delantero",  equipo_jugador=equipo_id, puntos_jugador="0", valor_jugador="120000")
jugador10 = Jugador.objects.create(nombre_jugador="Luis Suarez",ciudad_natal="Uruguay",edad_jugador="29",fecha_nacimiento="1987-01-24",  posicion="Delantero",  equipo_jugador=equipo_id, puntos_jugador="0", valor_jugador="120000")
jugador11 = Jugador.objects.create(nombre_jugador="Lionel Messi",ciudad_natal="Argentina",edad_jugador="29",fecha_nacimiento="1987-06-24", posicion="Delantero",  equipo_jugador=equipo_id, puntos_jugador="0", valor_jugador="120000")






