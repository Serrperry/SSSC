define g = Character("Goo", color="cc8500")
define am = Character("Amadeo", color="001d9c")
define k = Character("Kinacha", color="971efa", image="k")
define n = Character("Nestea", color="00d0ff")
define j = Character("Jules", color="cc00be")
define s = Character("Serrperry", color="aaa300")
define gys = Character("Goo y Serrperry")
define sw = Character("Sparrow")
define x = Character("???")
define d = Character("Director")
define mc = Character("[name]" , color="696969")
define mmc = Character("Mama de [name]")
define p1 = Character("Profesor")
define e = Character("Todos")
define p = Character("El Progrmador", color="e51a4c")
define t = Character("Todos")
define m = Character("Monika", color="ea899a")
define sy = Character("Sayori", color="ea899a")
define nt = Character("Natsuki", color="ea899a")
define y = Character("Yuri", color="ea899a")

init:
    $ circlewipe = ImageDissolve("wipes/circlewipe-cw.jpg", 1.0, 8)
    $ ccirclewipe = ImageDissolve("wipes/circlewipe-ccw.jpg", 1.0, 8)
    $ bites = ImageDissolve("wipes/bites.jpg", 1.0, 8)
    $ bowtie = ImageDissolve("wipes/bowtie.png", 1.0, 8)
    $ cmet = ImageDissolve("wipes/cmet.jpg", 1.0, 8)
    $ cwside = ImageDissolve("wipes/cw-side.jpg", 1.0, 8)
    $ cwtop = ImageDissolve("wipes/cw-top.jpg", 1.0, 8)
    $ dots = ImageDissolve("wipes/dots.png", 1.0, 8)
    $ edges = ImageDissolve("wipes/edges.png", 1.0, 8)
    $ flips = ImageDissolve("wipes/flips.png", 1.0, 8)
    $ fur = ImageDissolve("wipes/fur.jpg", 1.0, 8)
    $ goslow = ImageDissolve("wipes/goslow.png", 5.0, 8)
    $ letter = ImageDissolve("wipes/letter.png", 1.0, 8)
    $ maze = ImageDissolve("wipes/maze.png", 1.0, 8)
    $ radio = ImageDissolve("wipes/radio.jpg", 1.0, 8)
    $ snake = ImageDissolve("wipes/snake.png", 1.0, 8)
    $ snake2 = ImageDissolve("wipes/snake2.png", 1.0, 8)
    $ snakes = ImageDissolve("wipes/snakes.png", 1.0, 8)
    $ sunshine = ImageDissolve("wipes/sunshine.jpg", 1.0, 8)
    $ glasswool = ImageDissolve("wipes/glasswool.jpg", 1.0, 8)
    $ wet = ImageDissolve("wipes/wet.jpg", 1.0, 8,)

    $ w1 = ImageDissolve("wipes/1.jpg", 1.0, 8)
    $ w2 = ImageDissolve("wipes/2.png", 1.0, 8)
    $ w3 = ImageDissolve("wipes/3.jpg", 1.0, 8)
    $ w4 = ImageDissolve("wipes/4.jpg", 1.0, 8)
    $ w5 = ImageDissolve("wipes/5.jpg", 1.0, 8)
    $ w6 = ImageDissolve("wipes/6.jpg", 1.0, 8)
    $ w7 = ImageDissolve("wipes/7.png", 1.0, 8)
    $ w8 = ImageDissolve("wipes/8.jpg", 1.0, 8)
    $ w9 = ImageDissolve("wipes/9.jpg", 1.0, 8)
    $ w10 = ImageDissolve("wipes/10.jpg", 1.0, 8)
    $ w11 = ImageDissolve("wipes/11.jpg", 1.0, 8)
    $ w12 = ImageDissolve("wipes/12.jpg", 1.0, 8)
    $ w13 = ImageDissolve("wipes/13.jpg", 1.0, 8)
    $ w14 = ImageDissolve("wipes/14.png", 1.0, 8)
    $ w15 = ImageDissolve("wipes/15.png", 1.0, 8)
    $ w16 = ImageDissolve("wipes/16.png", 1.0, 8)
    $ w17 = ImageDissolve("wipes/17.png", 1.0, 8)
    $ w18 = ImageDissolve("wipes/18.png", 1.0, 8)
    $ w19 = ImageDissolve("wipes/19.jpg", 1.0, 8)
    $ w20 = ImageDissolve("wipes/20.jpg", 1.0, 8)
    $ w21 = ImageDissolve("wipes/21.jpg", 1.0, 8)
    $ w22 = ImageDissolve("wipes/22.png", 1.0, 8)
    $ w23 = ImageDissolve("wipes/23.png", 1.0, 8)
    $ w24 = ImageDissolve("wipes/24.png", 1.0, 8)
    $ w25 = ImageDissolve("wipes/25.png", 1.0, 8)
    $ w26 = ImageDissolve("wipes/26.png", 1.0, 8)
    $ w27 = ImageDissolve("wipes/27.png", 1.0, 8)
    $ w28 = ImageDissolve("wipes/28.png", 1.0, 8)
    $ w29 = ImageDissolve("wipes/001.png", 1.0, 8)
    $ w30 = ImageDissolve("wipes/002.png", 1.0, 8)
    $ w31 = ImageDissolve("wipes/003.png", 1.0, 8)
    $ w32 = ImageDissolve("wipes/004.png", 1.0, 8)
    $ w33 = ImageDissolve("wipes/005.png", 1.0, 8)
    $ w34 = ImageDissolve("wipes/006.png", 1.0, 8)
    $ w35 = ImageDissolve("wipes/007.png", 1.0, 8)
    $ w36 = ImageDissolve("wipes/008.png", 1.0, 8)
    $ w37 = ImageDissolve("wipes/009.png", 1.0, 8)
    $ w38 = ImageDissolve("wipes/010.png", 1.0, 8)
    $ w39 = ImageDissolve("wipes/011.png", 1.0, 8)
    $ w40 = ImageDissolve("wipes/012.png", 1.0, 8)
    $ w41 = ImageDissolve("wipes/013.png", 1.0, 8)
    $ w42 = ImageDissolve("wipes/puta.png", 1.0, 8)


label start:



$ style.namebox
$ style.window
$ gui.text_color
$ style.say_dialogue

scene saturnfhds
with fade

"Un momento..."
"Disfruta de la demo..."

$ name = renpy.input("??Cu??l es tu nombre?")

$ name = name.strip()

"??Empecemos a jugar, [name]!"
"Te recomiendo que tengas todos los sonidos bajados m??s o menos por debajo de la mitad"

pause 1.0

scene negro
with w1

x "{cps=6}h.........o........l........a{/cps}"
x "{cps=10}??Me escuchas?{/cps}"
x "[name]"

menu:
    "Si":
        pass

pause 1.0

$ style.namebox
$ style.window
$ gui.text_color
$ style.say_dialogue

play music "<from 5>audio/musica1.mp3"

scene principio2
with fade

show serrperrynormal 
with moveinbottom

s "Bienvenido! Este es el juego de SS (Saturns Stars) Empezado en el 5/10/2020."

s "Antes de empezar con el juego te voy a explicar la idea del juego."

hide serrperrynormal
with None

show serrperryexplicando at n_cg2_zoom

s "Todo empez?? el tres de octubre se anunci?? un dlc para smash que era Steve de Minecraft. Todos est??bamos emocionados por el dlc."
s "Hasta que un d??a Goo pasa un video por el WhatsApp de SS basado en doki doki literature club, pero con goo, kinacha, Amadeo y Nestea de protagonistas."
s "Gracias a eso se me ocurri?? la idea de hacer un juego parecido. Debo de decir que fue divertido programarlo con 0 ideas de Python..."
s "Dejo que veas el video que empez?? todo..."

stop music fadeout 1.0

pause 1.0

$ renpy.movie_cutscene("video/DDLC_SS.ogv")

pause 1.0

play music "<from 5>audio/musica1.mp3"

s "Una vez visto esto creo que es un buen momento de empezar con el juego. Espero que lo disfrutes, [name]."

stop music fadeout 1.0

pause 1.0

scene dia1
with fade

play sound "audio/reloj.ogg"

pause 3.0

scene cm1
with fade

"{i}Alarma{/i}"

play music "<from 5>audio/musica1.mp3"

"{i}15 de septiembre de 2019{/i}"
mc "{i}AAAAAAAHHHHhhhh... ??Ya es hora de levantarse...?{/i}"
"{i}07:20{/i}"
mc "{i}Bueno... Menos mal que estoy cerca porque si fuese mi antiguo instituto no llegar??a.{/i}"
mc "{i}Me visto, desayuno y me preparo la merienda. Seguro que termino para las 8:00.{/i}"

show negro
with fade 

hide cm1
with None

pause 2.5

show cmc1
with fade 

hide negro
with None

mc "{i}Mientras desayuno, mi madre est?? recogiendo sus cosas para despu??s irse a trabajar...{/i}"
mmc "Una pregunta, [name]."

show cmm2 at center with dissolve
    
mc "Mama, dime."
mmc "??C??mo te encuentras por ser tu primer d??a en un instituto nuevo?"
mc "Bueno... Tenso y curioso a la vez, ya que no s?? lo que me voy a encontrar en el instituto nuevo."
mmc "Te entiendo, pero tienes que procurar pas??rtelo bien y mientras est??s aprendiendo que es lo m??s importante."
mc "Bueno si, pero no ser?? f??cil divertirme si no tengo a nadie con quien hacerlo."
mmc "No es para tanto, t?? solo haz lo que mejor se te da hacer, ser tu mismo."
"Mientras terminaban esta conversaci??n, [name] estaba a punto de irse."
mc "Muchas gracias Mama, me tengo que ir."
mmc "Yo sigo recogiendo que a??n me falta un par de cosas."
    
hide cmm2 at center with dissolve
    
"[name] est?? llegando a la puerta para irse..."
mc "????Mama, me voy ha clase!!"

play sound "audio/puerta.ogg"

mmc "!!Ten un buen d??a!!"

pause 1.9

show h102
with fade

hide cmc1
with None

"Siendo una ma??ana c??lida con uno 25 grados, no hay mucha luz y sin una nube en todo el cielo"

pause 1.0

mc "{i}A ver que hora es...{/i}"
"{i}07:57{/i}"
mc "{i}No est?? mal, perooo ummm podr??a mejorar mi tiempo. Bueno tengo que seguir el camino que como se me olvide, me pierdo. {/i}"
"{i}Mientras [name] se sent??a algo solo por ser nuevo en el instituto y ve??a a los alumnos paseando por la calle, piensa...{/i}"
mc "{i}Pufff... Creo que lo m??s dif??cil de este a??o sin mencionar las asignaturas que claramente es tener amigos.{/i}"

pause 2.0

show negro
with fade

hide h102
with None

"A los 10 minutos de andar, [name] lleg?? al instituto con todos los alumnos."

pause 1.5

show cole1
with fade

stop music 
with fade 

play music "audio/ambiente1.ogg"

mc "{i}Bueno creo que he llegado al insti sano y salvo, ya cre??a que me hab??a perdido por el camino aunque no sea raro de mi parte.{/i}"

play sound "audio/campana.ogg"

mc "{i}Creo que ya es hora de entrar... Que pocas ganas de entrar uffff."
mc "{i}Pero antes me tengo que pasar por la sala del director para que me diga mi clase de este a??o. Tendr?? que darme prisa."

stop sound

pause 1.0

"[name] entra al instituto, que le espera a nuestro h??roe en estas fabulosas aventuras"

stop music 

pause 0.3

show dis1
with wet

hide cole1

"{fast}XXXXXXXXDDDDDDD {nw}"
p "Te voy a poner en situaci??n antes de que sigamos con la historia."
p "Estamos en Madrid capital y como te habr??s dado cuenta eres nuevo en un instituto donde no tienes amigos."
p "Y que m??s ten??a que decirte..."

pause 2.0

p "A si, s??... Bueno tus padres est??n divorciados y actualmente vives con tu madre. Con esto ya es suficiente, prosigamos."

pause 0.2

show negro
with None

hide dis1
with None

pause 0.5

show dis1
with None

pause 0.1

hide dis1
with None

play music "<from 5>audio/musica1.mp3"

show p1
with fade

"Mientras [name] va andando por el pasillo se da cuenta de que los alumnos de este pasillo son m??s peque??os que ??l, m??s o menos de quinto de primaria."

pause 4.0

"[name] llega a la sala del director."

pause 0.7

play sound "audio/puerta.ogg"

pause 0.3

show sd1
with fade

hide p1
with None

mc "{i}Ayer ya estuve aqu?? a s?? que ha sido f??cil llegar.{/i}"
    
show d1 at center with dissolve  

d "Hola [name], ??C??mo estamos?"
mc "Se podr??a decir que bien, pero...{nw}"
d "Supongo que los dos tenemos prisa as?? que la clase que te toca ... Un momento que encuentra el documento."

pause 4.5

d "Aj??. Bueno tu clase es 3??A esta en la segunda planta del edificio sur y Nos vemos ha ultima que tengo historia contigo."
d "Te voy a dar un mapa del instituto para que no te pierdas"
mc "Muchas gracias, se??or. Me tengo que ir."
    
hide d1 at center with dissolve  

d "Adi??s, que pases un buen d??a. {nw}"

hide sd1
with None

play sound "audio/puerta.ogg"

show p1
with None

pause 0.4

mc "{i}Necesito ir r??pido ya que no quiero llegar tarde{/i}"
"[name] yendo a paso adelantado con el mapa en la mano para llegar a la clase tambi??n se da cuenta de que no hay nadie en los pasillos"

pause 2.0

show cpt1
with moveinright

pause 0.2

hide p1
with None

pause 4.0

show p2
with moveinleft

pause 0.2

hide cpt1
with None

pause 2.5

"{i}Creo que es esta clase, pero no hay nadie en el pasillo supongo que se encuentran dentro. {/i}"

pause 1.0

hide p2
with None

play sound "audio/puerta.ogg"

show c1
with fade

pause 0.8

play sound "<loop 4>audio/ambiente1.ogg"

mc "{i}Hay mucho jaleo en la clase casi no puedo escuchar al profesor{/i}"

show p11 at center with dissolve

pause 1.5

p1 "Ejem... Por favor, un momento"

pause 2.0

hide p11 with None

show p13 at center with None

p1 "????Un Momento!!"

stop sound

pause 0.5

p1 "Bien. Este a??o a vendio un alumno a la clase, por favor pres??ntate."

hide p13 with None

show p11 at center with None

mc "{i}Todos los alumnos me est??n mirando me hace sentir nervioso{/i}"
mc "Hola a todos, soy [name] Torres Moreno y tengo 15 a??os. Un placer conocerlos."

pause 2.0

p1 "Bueno, un placer tenerte aqu??. Te puedes sentar all?? en medio de esos dos chicos que se llaman..."

p1 "Goo"

show goonormal at right with dissolve

pause 1.5

p1 "El otro compa??ero es Kinacha"

show kinachanomal at left with dissolve

p1 "Espero que te lleves bien con ellos"

hide p11 with dissolve

mc "Muchas Gracias profesor"
mc "{i}Me siento en mi sitio de forma incomoda ya que siento que todos de la clase me est??n mirando, pero me centro en la clase{/i}"


hide kinachanomal with dissolve

pause 1.0

hide goonormal with dissolve

pause 4.0

menu:
    "Pasan las primeras 3 horas de clases y llega el recreo.":
        pass

$ style.namebox
$ style.window
$ gui.text_color
$ style.say_dialogue

pause 1.5

mc "{i}Cojo mi merienda y decido salir al pasillo. {/i}"

pause 1.0

hide c1

show p2
with fade

pause 1.0

mc "{i}Ya que no s?? d??nde est?? el patio as?? que seguir?? el grupo de la clase. {/i}"

pause 1.5

hide p2
with None

show cpt1
with fade

pause 3.0

hide cpt1
with None

show r1
with fade

pause 0.8

mc "{i}Creo que es aqu?? el patio del recreo y adem??s algo que me he dado cuenta es que este instituto es m??s grande de lo que me esperaba.{/i}"
mc "{i}creo que voy a sentarme en un lugar donde me vea el campo de futbol para ver a los ni??os jugar y que no haya mucha gente.{/i}"

pause 1.5

"Pasan los primeros 15 min de la media hora y..."

show kinachanomal at left with dissolve

k "..."

show goonormal at right with dissolve

g "..."
mc "{i}Son los chicos de antes de la clase... Me est?? mirando y no escucho lo que dicen{/i}"
k "Ey, eres el chico nuevo, ??verdad?"
mc "Si"

pause 1.0

g "..."
k "..."
mc "????????DE QUE HABLAIS??!! Tengo monos en la cara o que."
g "????????MONOS, D??NDE??!!"

#El siguiente codigo se tiene que intercambiar al script de geika

k "En tu cara"
g "??C??mo?"

play sound "audio/monosound.ogg"

show monog3 at panic:
    xalign 0.8
    yalign 0.3

show monog2 at panic:
    xalign 1.0
    yalign 0.3

pause 2.0

g "Quitamelos AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
k "No puede ser."

hide monog3 with dissolve
hide monog2 with dissolve

mc "{i}Veo a los monos de la cara de goo salir coriendo.{/i} "
mc "WTF"
#Aqui termina

# k "Otra vez el pesado de los monos, es solo una manera de hablar..."
mc "Bueno, ??Qu?? quer??is?"
g "Nada, solo quer??a presentarme."
k "Y yo, y yo tambi??n."
g "Yo, soy Goo e hijo del director, creo que ya has conocido a mi padre."
mc "Si, ha sido esta ma??ana."
k "Yo soy, Kinacha y un buen amigo de Goo."
mc "{i}SE acerca Goo y me dice en voz baja:{/i}"
g "A veces, parece mi escudero..."
mc "{i}Despu??s de decirme eso, Sonr??o un poco.{/i}"
k "Que le has dicho a [name]"
g "Yo nada, Que le voy a decir..."
k "No le hagas, caso a este cabez??n."
g "Como que cabez??n, bueno nos tenemos que ir que va a tocar el timbre."
mc "Ahora voy que tengo que tirar el zumo."

hide kinachanomal at left with dissolve

hide goonormal at right with dissolve 

pause 1.0

mc "{i}Despu??s de tirar el zumo a la basura me doy cuenta de que ya se me han adelantado. Consigo perserguirlos hasta llegar a la clase.{/i}"

hide r1
with None

show cpt1
with fade

pause 3.0

hide cpt1
with None

show p2
with fade

mc "{i}Llego a la puerta de la clase y veo entrar a estos dos. Claramente entro detr??s de ellos.{/i}"

show c1
with fade

menu:
    "Pasan las tres ??ltimas horas de clase.":
        pass

pause 0.8

show d1 at left with dissolve

d "Ya hemos terminado por hoy, debo de darle la bienvenida a [name]. Espero que tengas un buen a??o."
mc "{i}Todos me miran como si esperasen algo de m??. Me siento bastante inc??modo.{/i}"
mc "Muchas gracias, director."
d "De nada. Pod??is recoger ya."
mc "{i}Me pongo a recoger todas mis cosas.{/i}"

pause 1.0

mc "{i}Antes de salir por la puerta el director dice...{/i}"
d "Goo y [name] pod??is venir un momento."
mc "Si director."
g "Claro."

pause 0.4

show goonormal at right with dissolve  

d "Goo te tienes que ir al club, ??no?"
g "Claro que si y no quiero llegar tarde porque soy el presidente."
d "Podr??as ense??arle a [name] la zona de club y le explicas un poco como van los clubs."
g "Claro, sin problema."
d "Perfecto, os veo ma??ana."
mc "Adi??s."

hide goonormal with dissolve

hide d1 with dissolve

hide c1
with None

show p2
with fade

mc "{i}Cuando salimos nos encontramos a Kinacha{/i}"

show kinachanomal at center with dissolve
hide kinachanomal with None
show kinachasorprendido with None

pause 0.7

hide kinachasorprendido with None
show kinachanomal with None

mc "{i}Goo y Kinacha se quedan 5 min hablando, pero no me entero porque no estoy cerca solo les veo desde lejos.{/i}"
g "No quiero llegar muy tarde y a??n tengo que ense??arte como van los clubs y los que hay"

hide kinachanomal with None
hide goonormal with None

pause 1.5

hide p2
with None

show cpt1
with fade

pause 3.0

hide cpt1
with None

show p1
with fade

show goonormal at right with dissolve
show kinachanomal at left with fade 

mc "{i}Sin hablar mucho por el camino llegamos al mismo edificio que al despacho del director, pero en la segunda planta.{/i}"
k "Bueno, chicos me tengo que ir a mi club, hasta luego."
mc "Hasta ma??ana, Kinacha."
g "Hasta luego."

hide kinachanomal with None
play sound "audio/puerta.ogg"

mc "{i}Veo a kinacha meterse en una clase y al lado de la puerta hay un cartel donde pone: SS Club. Presidente: Goo{/i}"
mc "Despu??s de leer esto digo:"
mc "Y ese club que se ha metido kinacha pone que eres tu el presidente..."
g "Tiene que haber un presidente en cada club y como mi padre es el presidente del instituto me dejo crear un grupo para mi y mis amigos"
mc "??Y qu?? hac??is en el club?"
g "Solemos pasar el rato jugando, charlando y otras cosas. Nada importante comparado a lo que hacen otros clubs otros clubs"
g "Pero principalmente jugamos competitivo a un juego que se llama Super Smash bros. Ultimate"
mc "Es estra??o que os dejen jugar a juegos en el instituto aunque todo se arregla con que tu padre es el presidente."
g "Bueno si... Pero por lo menos es divertido."
mc "??Y cuantos clubs hay?"
g "Hay muchos y ni siquiera me se todos. Suele haber clubs por asignatura como clubs de Matematicas o M??sica."
g "Tambi??n suelen surgir clubs nuevos todos los a??os y este a??o se ha creado el club de literatura."
mc "??Qu?? suelen hacer en los clubs?"
g "Suelen hacer cosas que tenga que ver con ese club. Una vez al a??o hay una exposici??n cada club, suele haber votaciones y el que tenga m??s votos ser?? elegida como mejor club del a??o."
mc "Es muy interesante todo el tema de los clubs, me interesa ver que clubs hay."
g "Te tengo que dejar [name], Me voy a mi club. Te puedes pasar a mirar los clubs que hay o te puedes ir ya para tu casa. Lo que tu veas, hasta ma??ana."
mc "Muchas gracias por todo, hasta ma??ana"

hide goonormal with None
menu:

        "Mirar los clubs":
            jump eleccion1_1

        "Ir a casa":
            jump eleccion1_done

label eleccion1_1:

            $ menu_flag = True

            $ P1

            mc "{i}Me paso por toda los clubs que hay, pero todos tienen algo que ver con asignaturas y lo ??ltimo que quiero es estudiar o hablar de algo que tenga que ver con alg??n tema de la clase.{/i}"
            mc "{i}Mejor hablo ma??ana con Goo para ver que club interesante hay{/i}"
            
            jump eleccion1_done

label eleccion1_done:

$ style.namebox
$ style.window
$ gui.text_color
$ style.say_dialogue

mc "{i}Estoy cansado y creo que ser?? mejor si me voy a casa ha sido un d??a extra??o{/i}"
    
scene dia2 with fade

pause 3.0

show cm1_1 with fade
play sound "audio/reloj.ogg"

mc "AAAAAAAHHHHhhhh, Segund..."

stop music

show goodrogado with moveinbottom

g "Buenos d??as, [name] es hora de levantarse..."
mc "Pero... pero GOO QUE HACES EN MI CAMA."

hide dia2 
hide p1 

g "Tu madre me dejo entrar y por cierto que maja tu madre."
mc "Vete de cama, GOOO."

hide goodrogado with vpunch
show cm1 with fade

mc "Aahh..."
mc "{i}Espera ...era un sue??o... un sue??o lucido... Menos mal.{/i}"
hide cm1_1 with None
play sound "audio/reloj.ogg"

pause 1.0

mc "{i}??Qu?? hora es?{/i}"

pause 0.5

stop sound

"{i}7:30{/i}"
mc "{i}Un poco m??s tarde que ayer, que creo que eran sobre las 7:20... Bueno da igual, me tengo que dar prisa.{/i}"

hide cm1 with fade
show negro with fade

"{i}Despu??s de un rato, [name] va a la cocina para desayunar y irse por segundo d??a en el instituto nuevo.{/i}"

hide cm1 
show cmc1 with fade

mc "{i}Igual que ayer mi madre esta apunto de irse.{/i}"
mc "{i}Me siento y empiezo ha desayunar que mi madre ya me tiene preparado el desayuno.{/i}"

hide negro with fade
pause 2.5
    
"{i}Mientras que [name] desayuna, la madre se hacerca.{/i}"
mmc "Como ha sido tu primer d??a, [name]."

show cmm1 at center with moveinright

mc "Ha sido muy extra??o al no estar en el anterior instituto."
mmc "Eso me lo imaginaba, pero... Que es lo que te a gustado y lo que no."
mc "Pues no se... emm... Creo que lo que mas destacaria es lo grande que es y por eso me siento perdido, pero con ganas de ver todo el instituto."
mmc "Bueno eso normalmente lo sabras con el tiempo. ??Algo m??s?."
mc "Bueno... Ah si, hay unos clubs o clases extraescolares que aun tengo que ver a cual me apunto..."
"{i}Le explica ha su madre como son los clubs{/i}."
mc "Pues aunque tenga muchas elecciones aun no estoy seguro a cual me unir??."
mmc "Esta muy interesante, pero seguro que encuentras algo."
mmc "Me tengo que ir que hoy tengo prisa."
mc "Adios Mama, espero que tengas un buen d??a."

pause 1.0
play sound "audio/puerta.ogg"

"{i}Despu??s de desayunar y terminar de recoger las cosas para el instituto, sale para ir el instituto{/i}"

pause 0.8

play music "<from 5>audio/musica1.mp3"

pause 0.8

show h102
with fade

pause 1.0

hide cmm1
with None

pause 0.1

show cole1
with fade

pause 1.0

hide h102
with None

pause 0.1

show dis1 
with None

pause 0.5

p "Otra vez no..."

pause 0.4

p "Supongo que tengo que esplicarte un par de cosas m??s sobre tu personaje."
p "No es una persona de jugar ha muchos videojuegos, pero siempre tuvo alguna consola de nintendo como la nintendo switch"
p "Lo que m??s le interesa es leer libros, ver peliculas o series."
p "??!Estas feilz???"
p "..."
p "Adios"

hide cole1 
with None

hide dis1 
with None

show p1 with fade

pause 1.0

show c1 with fade

"{i}Corriendo por los pasillos ya que llega muy justo a la clase.{/i}"
"{i}Entra en la clase siendo de los ultimos.{/i}"
mc "{i}Cuando entro a la clase me encuentro con un silencio. Me voy a mi sitio en silencio como si no hubiera llegado tarde.{/i}"
mc "{i}Llego ha mi sitio y escucho ha goo y kinacha hablando entre ellos{/i}"
g "..."
k "..."
mc "{i}Aunque no me entero de nada, en un momento veo al profesor mirando a kinacha y a goo.{/i}"
g "..."
k "!TE PUEDES CALLAR UN RATO E IRTE A TU SITIO??"
p1 "Podemos seguir con la clase."
g "Si"
k "Si"

menu:
    "Pasan las primeras 3 horas":
        pass

$ style.namebox
$ style.window
$ gui.text_color
$ style.say_dialogue

mc "{i}Una vez que tengo un mapa mental del instituto, decido salir por mi cuenta y sin seguir al grupo{/i}"

pause 1.0

hide c1

show p2
with fade

pause 1.0

pause 1.5

hide p2
with None

show cpt1
with fade

pause 3.0

hide cpt1
with None

show r1
with fade

pause 0.8

mc "{i}Una vez que llegamos al recreo como ayer me siento en una esquina y me como la merienda.{/i}"
"{i}Despu??s de un rato, goo y kinacha se acercan hacia [name], pero goo parece estar m??s serio de lo habilidades{/i}"

show goopensando at right with moveinright

g "Tengo que hablar con vosotros de una cosa"

show kinachanomal at left with moveinleft

k "Por lo que veo es algo serio o que."
mc "Espera, ??Qu???"
g "Me ha dicho mi padre que si no metemos a nadie que no sea amigo mio, lo va ha cerrar."
k "Tiene que ser broma. ??Qu?? has hecho ya goo?"
g "Yo, nada."
mc "Y, ??por qu?? quereis hablar conmigo?"
g "Te queria proponer una cosa, ??Quieres venir a mi club?"
k "Pero sin lo hemos habaldo en el club."
g "Ya lo se, pero tiene que ser r??pido y se tiene que quedar en el club."
k "Pero, pero."
g "Ya hablaremos con ellos esta tarde sobre el tema."
k "No me gusta esta decisi??n que has tomado sin nosotros."
g "Lo siento pero ahora tengo que hablar con [name]"
k "Vale, Vale Pesado, pero ahora nos vemos, no?"

hide kinachanomal with dissolve

g "Si"
mc "{i}Veo irse a kincacha, pero se queda con un grupo de personas que no logro ver bien.{/i}"
g "Entonces, ??qu?? te pareze la oferta?"
mc "No es mala, pero no soy alguien que juega mucho a videojuegos."
g "Solo pido que nos des una oportunidad. Si no te gusta, puedes salirte."
mc "Bueno, le doy una oportunidad."
g "Gracias, muchas gracias."
g "Me tengo que ir, hasta luego."
mc "Adios."

hide goopensando with dissolve 

play sound "audio/campana.ogg"

"Mientras vemos como goo se va con el mismo grupo que con el que se fue kinacha y pasa la media hora del recreo"

stop sound

pause 1.5

hide r1 with None

menu:
    "Pasan las tres ultimas horas de clases.":
        pass

$ style.namebox
$ style.window
$ gui.text_color
$ style.say_dialogue

show p1 with bites

mc "{i}Estoy llegando al club siguiendo a goo, pero ahora que me fijo en el veo que esta inquieto y cada cierto tiempo saca una risa corta que no entiendo.{/i}"
mc "{i}Creo que esta nervioso por ver como reacciona los del club a mi llegada pero lo de las risas no las entiendo del todo bien.{/i}"
mc "{i}Llegamos a la puerta y cuando empezamos a abrila tomamos los dos aire a la vez y goo entra con una sonrisa picarona y con mucha energia{/i}"

play sound "audio/puerta.ogg"

pause 1.5

show ss2
with fade

show goonormal with dissolve:
    xalign 0.02
    yalign 1.00

g "Que pasaaaaaaaaaaaaa gente"
mc "{i}Yo antes de que se cierre la paro con una mano y con sigilo entro sin que nadie se de cuenta ya que estancentrados en goo.{/i}"
mc "{i}Despu??s de esto, me quedo detras de goo esperando a que me presente con todos.{/i}"
mc "{i}En la habitaci??n que por lo que veo es diferente a la de clase{/i}"
g "??C??mo estamos chaveles?"
x "Como siempre llegando tarde" #Jules

play music "<from 5>audio/musica1.mp3"
hide p1 with None

show jules with dissolve:
    xalign 1.00
    yalign 1.00

x "Si fuese por mi algun d??a de estos le pegaba una paliza"# Amadeo

show amadeoserio with dissolve:
    xalign 0.90
    yalign 1.00

x "Dejadlo que tendra que hacer sus cosas"# Nestea
k "Pero goo cabez??n, donde esta el nuevo"

show kinachanomal with dissolve:
    xalign 0.72
    yalign 1.00

x "!!!COMO QUE NUEVO, GOO??????" #Jules
g "Os presento a nuestro nuevo integrante, [name]"

"{i}Y de repente entra alguien en la habitaci??n{/i}"
x "??Holaaaaaa?! Chicos, ??c??mo estamos hoy?"# serrperry

show serrperrynormal with dissolve:
    xalign 0.60
    yalign 1.00

mc "{i}Me giro para saber quien ha entrado en la habitaci??n.{/i}"
x "WTF!! Alguien me puede esplicar que co??o esta pasando"#serrperry
mc "{i}Mientras pasa todo esto mes siento en la silla m??s cercana y espero a que termine{/i}"
x "Dejadmelo a mi"#amadeo
k "Si es que te lo dige, mamon."
"{i}Vemos como uno de los mas peque??os de estatura, pero con mejor musculatura de toda la sala agarra del cuello a goo exigiendole una explicaci??n {/i}"
x "Si no quieres que te rebiente dime quien es ese." #amadeo
g "Calma todo el mundo, ese chico es el nuevo de mi clase y he dicido meterlo po..."
x "Eres un cabr??n, podr??as habermenos dicho y ver si entra en le club." #Jules 
g "Ya, pero creo que es la unica opci??n que tenemos para seguir con el club."
x "Vamos ha calmarnos y hablarlo tranquilo. por favor ((((*???_???)_" #Nestea

hide p1 with None

hide dis1 
with None

show nesteanormal with dissolve:
    xalign 0.46
    yalign 1.00

x "Pero con una condici??n, necesito que el `invitado?? no escuche nada ya que no quiero montar otro espectaculo." # Jules
x "La verdad es que si" #amadeo
"{i}Lo dice mientras que deja en paz ha goo. Se hacerca el que acaba de entrar a [name] y le dice...{/i}"
x "Mejor hacerles caso si no quieres que se monte otro espectaculo." #serrperry
mc "Si, ahora voy."
mc "{i}Cogo la silla y me siento en la parte m??s alegada de la habitaci??n.{/i}"

hide goonormal with dissolve

hide nesteanormal with dissolve

hide serrperrynormal with dissolve

hide jules with dissolve

hide amadeoserio with dissolve

hide kinachanomal with dissolve

menu:
    "Pasan 10 min.":
        pass

show goonormal with dissolve:
    xalign 0.02
    yalign 1.00

show jules with dissolve:
    xalign 1.00
    yalign 1.00

show amadeoserio with dissolve:
    xalign 0.90
    yalign 1.00

show kinachanomal with dissolve:
    xalign 0.72
    yalign 1.00

show serrperrynormal with dissolve:
    xalign 0.60
    yalign 1.00

show nesteanormal with dissolve:
    xalign 0.40
    yalign 1.00

"{i}Mientras que estaban hablando algunos del grupo sobresaltan o elevaban la voz."
mc "..."
mc "{i}Se me hacerca todos del grupo y...{/i}"
x "Perd??n por el jaleo que hemos montado aunque es comun entre nosotros.(*^-^*)q" #nestea

k "Entonces vamos ha lo que vamos."
mc "Entonces, jugais solo a smash o haceis otras movidas"
g "La verdad es que hacemos lo que nos da la gana, pero principalmente se podr??a decir que es jugar al smash."
x "Aunque solemos jugar a otros juegos como splatoon 2, mario kart 8 deluxe, pokemon y m??s juegos de nintendo." #Serrerry
mc "Bueno, los videojuegos no son por decirlo de alguna forma mi pasi??n, pero siempre me gusta jugar unas partiditas diarias a lo que sea."
x "Basta de charla, vamos ha jugar que os voy ha rebentar chavales." #Amadeo
x "Que dice de rebentar, el que te rebienta soy yo." #Jules
k "Pregunt??."

hide nesteanormal with dissolve

pause 1.0

hide serrperrynormal with dissolve

pause 1.0

hide kinachanomal with dissolve

pause 1.0

hide amadeoserio with dissolve

pause 1.0

hide jules with dissolve

mc "{i}Veo al grupo de SSSC todos con la mochila puesta y en la puerta como si fueran a salir.{/i}"
mc "{i}Me voy a acercar al grupo...{/i}"
g "Un momento, [name] "
mc "Si?"
g "Seria de mal presidente no presentar a todos los miembros del club de SSSC."
g "Pero lo quiero hacer de una forma diferente es decir que te digo el nombre y una frase que represente a esa persona."
mc "Podr??as hacerlo de una forma mas sencilla."
g "Nah, bueno vamos a empezar con {cps=2}...{/cps} Amadeo."
g "Una frase que represente {cps=2}...{/cps} como dijo su abuela: Sudor, arena y aceite."
mc "Y como identifico yo a sea persona con esa frase."
g "Lo llamo y asi te enteras de quien es."
g "??AMADEEEEEEEEEO!"
am "??DIIIIIMEE!"
g "??LEVANTA LA MAAAAANO!"
am "??VAAAAAAAALEEEEE!"

show amadeoserio at center with dissolve

#Ahora sale amadeo en pantalla
g "??Ahora sabes quien es o no?"
mc "Ahora si."
#se va amadeo

hide amadeoserio with dissolve 

g "Bueno, vamos a hacerlo m??s r??pido que no tenemos todo el d??a."
g "De jules seria: por el orto no hay aborto."

show jules at center with dissolve

pause 1.2

hide jules with dissolve

g "De Nestea seria: Hola! Soy Nestea!Main Mewtwo((*o_o??)(*^-^*)q Main? Y si se puede saber edad?"

show nesteanormal at center with dissolve

pause 1.2

hide nesteanormal with dissolve

g "De Serrperry ser??a: El tiempo sin ti es empo."

show serrperrynormal at center with dissolve

pause 1.2

hide serrperrynormal with dissolve

g "Yo creo que ya son todos los integrantes."
mc "Bueno, messirve."
mc "Y otra pregunta, ??que hacen todos en la puerta y con la mochila preparada?"
g "Perd??n no te lo he dicho, no jugamos en el insitituto ya que a mi padre no le gusta."
mc "Entonces, ??D??nde jug??is?"
g "No te adelantes peque??o saltamontes."
n "Goo, vamos que perdemos todo el d??a.(>_<)"
g "Va, va. Vamonos, despu??s te cuento m??s de lo que solemos hacer."
mc "Primero las mujeres."

hide goonormal with fade

play sound "audio/puerta.ogg"

show negro 
with fade

mc "{i}Salimos a la puerta del instituto{/i}"

pause 2.0

hide ss2
with None

hide negro
with None

hide p1 
with None

show cole1
with None

g "??Chicos, necesito que me escucheis!"

pause 1.5
    
show goonormal with moveinbottom

k "Y despu??s de eso me foll?? a tu madre."
g "??CALLA!"
k "??VALE!"

pause 1.5

g "Como siempre tendremos que dividir el grupo en dos para no jugar todos en la misma consola."
g "Hoy toca el primer grupo que va ha estar compuesto de Kinacha, Serrperry y yo y, el segundo grupo ser?? Nestea, Jules y Amadeo."
g "Entonces, ??Qu?? grupo eliges?"

menu:

        "Primer grupo":
            jump eleccion2_1

        "Segundo grupo":
            jump eleccion2_2

label eleccion2_1:

            $ menu_flag = True
            #esta elecci??n le toca al mc wolf
            mc "Creo que eligir?? el primer grupo."

            pause 1.8

            $ eleccion1 = 1

            g "Vale, ya que estamos todos divididos en grupos deberiamos irnos ya para no perder m??s tiempo."

            jump eleccion2_done

label eleccion2_2:

            $ menu_flag = True
            #esta elecci??n le toca al mc king dedede
            mc "Creo que eligir?? el segundo grupo."

            pause 1.8

            $ eleccion1 = 2

            g "Vale, ya que estamos todos divididos en grupos deberiamos irnos ya para no perder m??s tiempo."
            
            jump eleccion2_done

label eleccion2_done:

$ style.namebox
$ style.window
$ gui.text_color
$ style.say_dialogue

mc "??Entonces d??nde vamos ahora?"
g "Una vez que estamos divididos, nos vamos cada uno a una casa y como no, jugamos un par de horas."
j "Lo raro es que salga todo bien."
s "Por lo menos lo mandos no sufren."
k "Basta de charla mamones, vamos que si no perdemos todo el d??a."
# Pasamos de la calle a las habitaciones de cada uno 
# Seg??n el grupo que eliga el mc ser?? un habitaci??n o otra.
# var elecci??n 1 = 1
# var elecci??n 1 = 2

if eleccion1 == 1:

    $ style.namebox
    $ style.window
    $ gui.text_color
    $ style.say_dialogue

    play music "<from 5>audio/musica1.mp3"
    
    g "Sigueme [name] que nos tenemos que nos separamos ya."
    am "Como ma??ana me entere de que no se lo ha pasado bien, la tenemos."
    g "Claro que lo va a hacer, ha elegido el mejor grupo de los dos."
    am "No"
    s "Si"
    am "No"
    s "Si"
    am "Pesado"
    s "Tu"
    k "Callense y vamos."
    
    hide goonormal with None
    
    show negro
    with fade
    
    mc "{i}Veo a al otro grupo irse por otra calle diferente a la nuestra.{/i}"
    
    show calle1_1
    with fade
    
    g "Claramente solemos ir a mi casa ya que soy el admin."
    
    hide negro
    with None
    # modo admin
    mc "Bueno suponia que era eso."
    
    menu:
        "Pasan 20 minutos andando hasta que llegamos a la casa.":
            pass

    pause 1.0

    show cgf1
    with moveinleft
    
    g "Bienvenido a mi hogar."
    
    hide calle2_1
    with None
    
    k "Mi casa es mas grande y mejor."
    g "Claro porqu?? tu eres rico y yo no lo soy."
    k "Que va solo tengo dos trabajadoras del hogar."
    mc "*Trabajadoras del hogar*?"
    k "Si"
    g "Las llama asi para no llamarlas esclavas pinche capitalista opresor."
    k "No, payaso que ere un payaso."
    g "Bueno yo creo debemos entrar ya."

    show negro
    with fade

    mc "{i}Entramos en la casa de Goo y subimos a su cuarto.{/i}"

    play sound "audio/puerta.ogg"

    pause 2.0

    show cg1
    with fade

    g "Aqu?? estamos, vamos a prepararnos para jugar."

    show goonormal at center with moveinright

    k "Alg??n d??a llegaremos y nos encontraremos a un mono fumando."

    show kinachanomal at right with moveinright

    g "Fumando, por?"
    k "La verdad, es lo primero que se me vino a la cabeza."
    s "Dejaros de tonterias y vamos ha darle."

    show serrperrynormal at left with moveinleft

    mc "Una pregunta Goo"
    g "Dime"
    mc "??Qu?? hago yo?"
    g "Que vas a hacer jugar, no?"
    mc "Seguro que lo mejor para empezar es que me ponga con vosotros ha jugar"
    s "La verdad es que yo tampoco lo veo eso de que empieze ha jugar de golpe"
    g "Un momento..."

    pause 1.0

    mc "{i}Nos quedamos todos observando a Goo pensando unos momentos.{/i}"

    pause 1.0

    g "Ah si, es verdad."
    g "Kinacha te has traido tu nintendo switch hoy con todo."
    k "Si, por?"
    g "[name] va ha jugar en el salon con uno de nosotros que el eliga."
    s "Entonces, ??cu??l eliges [name]?"
    mc "Pues no lo se..."

    #*llamada a serrperry*
    play sound "audio/ringphone.ogg"

    s "Un momento..."
    s "Me esta llamando mi madre."
    
    #*Parar llamada*
    stop sound

    s "Hola, mama {cps=6}....{/cps} si {cps=6}.....{/cps} vale {cps=6}....{/cps} ahora voy."
    s "Chicos que me tengo que ir."
    k "??Por?"
    s "Que tengo que llevar a mi hermana a mi casa."
    mc "??Cu??nto tardas?"
    s "Unos 10 minutos m??s o menos. Ser?? mejor que eligas a goo o kinacha por si acaso."
    mc "Que quieres decir con *por si acaso*"
    s "Nada, nada tu hazme caso y elige a los otros mamertos"
    mc "Va"
    s "Bueno y eso me voy. Adios"

    hide serrperrynormal with dissolve

    mc "{i}Vemos como sale corriendo por la puerta del cuerto{/i}"

    hide goonormal with dissolve

    hide kinachanomal with dissolve
    
    k "Entonces a cual eliges."
    mc "No se a quien elegir, dejadme 2 minutos para pensarlo."
    
    menu:

        "Goo":
            jump g1

        "Kinacha":
            jump k1

else:

    $ style.namebox
    $ style.window
    $ gui.text_color
    $ style.say_dialogue

    play music "<from 5 to 15.5>audio/musica1.mp3"

    j "El manco que se venga con nosotros."
    g "Por favor, no la lieis mucho que es nuevo."
    n "Nosotros nunca, que va((*o_o)."
    g "Claro, claro. Lo que tu digas, bueno nos vemos ma??ana."
    g "Un momento [name], toma esta bolsa"
    mc "{i}Goo saca de su mochila una bolsita y me la da.{/i}"


    hide goonormal with None
    
    show negro
    with fade
    
    mc "{i}Veo a al otro grupo irse por otra calle diferente a la nuestra.{/i}"
    
    show calle2_1
    with fade
    
    mc "Al go que que aun no me habeis dicho es donde estaremos jugando."
    
    hide negro
    with None
    
    j "Solemos ir a mi casa ya que yo fui uno de los primeros en unirme al club."
    mc "Me creia que eran todos ya amigos de antes."
    j "No todos aunque la mayoria no estaba cuando creo el club."
    mc "??Cuales son los que entraron despu??s?"
    j "Kinacha, Amadeo y por ulitmo Serrperry."
    mc "Ah... Vale"
    
    menu:
        "Pasan 15 minutos andando hasta que llegamos a la casa.":
            pass

    $ style.namebox
    $ style.window
    $ gui.text_color
    $ style.say_dialogue

    pause 1.0
    
    show cjf1
    with fade
    
    j "Buenos ??BIENVENIDO A MI HOGAR!"
    
    hide calle2_1
    with None
    
    n "Tan bonito como siempre UwU!!!"
    am "Ke Gey."
    j "Dejar las tonterias que hay cosas que hacer."
    am "Ke Gey!!"
    mc "Vamos a darle."

    show negro
    with fade

    mc "{i}Entramos en la casa de Jules y subimos a su cuarto{/i}"
    play sound "audio/puerta.ogg"

    pause 2.0

    show cj1
    with fade

    j "Y este es mi cuarto."

    hide negro
    with None

    hide cjf1
    with None

    show jules at center with moveinleft

    n "Esta como siempre.(*^-^*)q"

    show nesteanormal at left with moveinleft

    mc "Bonito cuarto."
    j "Gracias."
    am "Dejad de ser gays y vamos ha jugar."

    show amadeoserio at right with moveinright

    #*mensaje de movil*
    play sound "audio/notphone.ogg"
    
    am "Goo me ha dicho que lo mejor seria que solo le ense??e uno ha jugar."
    j "Pero no tenemos dos consolas."
    
    #*mensaje de movil*
    play sound "audio/notphone.ogg"

    am "Me ha vuelto ha decir que en la bolsa hay una consola para que pueda aprender aparte."
    n "Increible Goo tenia todo pensado.(*^-^*)q"
    mc "Yo creo que la cara que tenia cuando me lo ha dicho en el recreo."
    n "??C??mo? (>_<)"
    mc "Hoy cuando me ha dicho que necesitaba que entrase para que no quiten el club, tenia una cara mala cara que no pod??a con ella."
    n "Entonces, ??c??mo lo hacemos?(*^-^*)q"
    am "Jules, No hay nadie en tu casa, ??no?"
    j "No hay nadie em casa, ??por?"
    am "Estaba pensando en que [name] jugase con el que quiera y en el salon para que no se le moleste."
    j "Tambien podr??amos jugar todos en la misma habitaci??n, pero que juege con el modo portatil."
    mc "Creo que prefiero jugar en la television."
    n "Ser?? lo mejor para ti.((*o_o)"

    hide amadeoserio with dissolve
    
    hide jules with dissolve
    
    hide nesteanormal with dissolve
    
    mc "No se a quien elegir, dejadme 2 minutos para pensarlo."

    menu:

        "Amadeo":
            jump am1

        "Jules":
            jump j1

        "Nestea":
            jump n1

    pass

$ style.namebox
$ style.window
$ gui.text_color
$ style.say_dialogue

label am1:

mc "Creo que elegir?? a Amadeo"

$ patata = 1

# Explica el movimiento
jump eleccion3_done

label j1:

mc "Creo que elegir?? a Jules"

$ patata = 2

# Explica a recuperarse
jump eleccion3_done

label n1:

mc "Creo que elegir?? a Nestea"

$ patata = 3

# Explica a utilizar a el escudo
jump eleccion3_done

label g1:

mc "Creo que elegir?? a Goo"

$ patata = 4

# Explica el spacing
jump eleccion3_done

label k1:

mc "Creo que elegir?? a Kinacha"

$ patata = 5

# Explica los combos basicos
jump eleccion3_done

label eleccion3_done:

if patata == 1:

    $ style.namebox
    $ style.window
    $ gui.text_color
    $ style.say_dialogue

    play music "<from 5 to 15.5>audio/musica1.mp3"

    am "Es hora de reventar mariconessssss."

    show amadeoserio at center with moveinleft

    mc "??Qu???"
    am "Nada."
    mc "Vamos bajando, no?"
    am "Sisi, Jules nos bajamos."
    j "No me rompais nada mientras que poneis la nintendo."
    am "Que siiiiii, tengo cuidado."

    hide amadeoserio with dissolve

    show negro
    with fade

    play sound "audio/puerta.ogg"

    pause 1.5

    mc "{i}Bajamos al salon y rapidamente Amadeo empieza a poner la nintendo switch en la tele{/i}"

    pause 1.0

    show cjs1
    with fade

    am "Tienes ganas de aprender ha jugar."

    show amadeoserio at center with moveinleft

    hide negro
    with None

    hide cj1
    with None

    mc "No estoy super emocionado, pero tengos ganas igualmente."
    am "Como no tenemos mucho tiempo, te ense??are una de las bases del competitivo."
    mc "Solo espero que no sea muy complejo o dif??cil"
    am "No es dificil, pero sera mejor que masterizes"
    mc "Tiene sentido"
    mc "{i}Pasa unos 2 minutos{/i}"
    am "Nice, ya est?? todo preparando para jugar"
    mc "{i}Veo en la television como empieza el juego{/i}"
    mc "Entonces que me quieres ense??ar"
    am "Antes de nada, deberias elegir un personaje que te guste"
    mc "{i}Siendo la primera vez que juego a este juego, me pierdo en el menu del juego{/i}"
    am "Lamentable."
    mc "Lo siento, es la primera vez en este menu."
    am "No pasa nada, yo te ayudo."

    hide amadeoserio with None

    show amadeoexplicando at center with None

    mc "{i}Me agarra el mando y entra al plantel de personajes{/i}"
    am "Vale, te explico un poco."
    am "Pero tu ya has jugado antes a un smash, no?"
    mc "Si"
    am "Mejor, Menos cosas que explicar."
    am "Primero, estamos en el modo entrenamiento y en un mapa simple como el campo de batalla, siendo uno de los que se juega en el competi."
    am "Segundo, Elige el personaje que mas ganas tengas y te ense??are a moverte con el."
    mc "{i}Veo un buen plantel de personajes{/i}"
    mc "Pues eligo a Wolf, lo jugue un poco en el smash de la wii y me gust??"
    am "En serio no quieres jugar otro."
    mc "No, ??por qu?? lo dices?"
    am "No por nada"
    am "Que te puedo decir de wolf..."
    am "Wolf es un personaje con no muy buena movilidad en el aire, pero buena en el suelo"
    am "Ser?? mejor que te lo cuente mientras jugamos"
    mc "Si va a ser mejor"

    pause 2.0

    menu:
        "Pasa 1 hora":
            pass

    mc "{i}Escucho venir a Jules y Nestea del cuarto de Jules{/i}"

    show jules at right with moveinright

    show nesteanormal at left with moveinright

    j "Ni??os dejad el fortnait que ya ha pasado la hora."
    
    hide amadeoexplicando with None

    show amadeoserio at center with None

    mc "??C??mo lo habeis pasado hoy?"
    j "Rebentando a Nestea como siempre."
    n "Claro si empez?? hace poco ha jugar y tu ya llevas m??s de mil horas."
    j "Eso no quita mi punto."
    n "Vale... Tu ganas."
    n "Y vosotros, ??Qu?? tal?(*^-^*)q"
    am "Le estado ense??ando un par de cosas intentando tener paciencia."
    mc "Pero no tienes mucha."
    am "????Calla!! Lo estoy intentando, ??VALE!"
    mc "Supongo..."
    j "Basta de tonterias."
    mc "Bueno creo que me voy a mi casa."
    n "Nosotros tambien nos iremos a nuestra casa.((*o_o)"
    mc "Yo me voy ya que mi madre no sabe que estoy aqu??"
    n "Nos vemos ma??ana, no?(*^-^*)q"
    mc "Claro."
    mc "Adi??s a todos."
    t "Adi??s."
    
    hide jules with dissolve

    hide amadeoserio with dissolve
    
    hide nesteanormal with dissolve

    show negro
    with fade

    pause 1.5

    mc "{i}Cuando llego a mi casa hago mis deberes, ceno, me ducho y me voy ha dormir {/i}"

    pause 1.5

    hide cjs1
    with None

elif patata == 2:
    
    $ style.namebox
    $ style.window
    $ gui.text_color
    $ style.say_dialogue

    play music "<from 5 to 15.5>audio/musica1.mp3"

    hide amadeoserio with dissolve

    hide nesteanormal with dissolve

    j "Vamos a ver que podemos hacer contigo, sigueme."
    mc "Vale."
    j "Amadeo dame eso, despu??s nos vemos."
    mc "{i}Veo como Jules le quita la bolsa a Amadeo y sale de la habitiaci??n{/i}"
    am "Hasta luego"

    hide jules with dissolve

    show negro
    with fade

    play sound "audio/puerta.ogg"

    pause 1.5

    mc "{i}Bajamos al salon y rapidamente Jules empieza a poner la nintendo switch en la tele{/i}"
    
    pause 1.0

    show cjs1
    with fade

    j "Vamos a ver que podemos hacer contigo."

    show jules at center with moveinleft

    hide negro
    with None

    hide cj1
    with None

    mc "{i}Veo como termina de conectar la consola y empieza a abrir el juego.{/i}"
    j "??Has jugado a alg??n smash antes?"
    mc "Si, he jugado al smash de la wii aunque no de forma competitiva."
    j "No eres tan tan manco como pensaba, esto me ayudar?? a que sea m??s sencillo ense??arte algo basico."
    mc "{i}Veo como me da el mando con energia{/i}"
    j "Metet?? en el entrenamiento que va a ser lo mejor para ti como primera vez."
    mc "{i}Siendo la primera vez que juego a este juego literalmente me pierdo en el menu del juego.{/i}"
    j "Si hay que ser manco para no saber moverte en el menu."
    mc "Ya sabes que es mi primera vez. por favor no pidas mucho."
    j "ufff"
    j "Vale, lo intentar??."
    mc "{i}Me agarra el mando y entra al plantel de personajes{/i}"
    j "Que personaje vas a elegir como tu primer d??a."
    mc "{i}Veo un buen plantel de personajes{/i}"

    pause 1.0

    mc "Pues eligo a Wolf, lo jugue un poco en el smash de la WII y me gust??."
    j "Un personaje complicado para lo que quiero hacer que aprendas, pero podr??a ser peor."
    j "Bueno, el mapa que he elgido es uno competitivo y basico como el destino final."
    mc "??Y que me vas a ense??ar?"
    j "Te voy a ense??ar a recuperarte con ese personaje aunque tenga una recuperaci??n de mierda"
    j "Y si nos da tiempo tambien te ense??are a hacerlo con otros personajes"
    mc "??Le doy?"
    j "Claro"

    pause 1.0

    menu:
        "Pasa 1 hora":
            pass

    mc "{i}Escucho venir a Jules y Nestea del cuarto de Jules{/i}"

    show amadeoserio at right with moveinright

    show nesteanormal at left with moveinright

    am "Los maricones del fondo, dejad de jugar que ya hemos terminado."
    j "??Cuantas veces ha muerto nestea hoy?"
    am "Las suficientes para no poder contarlas."
    j "JAAJAJAJAJAJ"
    n "Sois muy malos conmigo."
    am "Bueno estas mejorando no estan f??cil como la semana pasada"
    mc "Bueno creo que me voy a mi casa."
    n "Nosotros tambien nos iremos a nuestra casa.(*^-^*)q"
    mc "Yo me voy ya que mi madre no sabe que estoy aqu??"
    n "Nos vemos ma??ana, no?(>_<)"
    mc "Claro."
    mc "Adi??s a todos."
    t "Adi??s."

    hide jules with dissolve

    hide amadeoserio with dissolve

    hide nesteanormal with dissolve

    scene negro
    with fade

    pause 1.5

    mc "{i}Cuando llego a mi casa hago mis deberes, ceno, me ducho y me voy ha dormir {/i}"

    pause 1.5

    hide cjs1
    with None

elif patata == 3:
    
    $ style.namebox
    $ style.window
    $ gui.text_color
    $ style.say_dialogue

    play music "<from 5 to 15.5>audio/musica1.mp3"

    hide amadeoserio with dissolve

    hide amadeoserio with dissolve

    show nesteanormal at center with moveinleft

    n "No, no creo que sea la mejor idea.((*o_o)"
    am "O si, tienes las bases del juego aprendiendo, puede que sea interesante que jugueis juntos."
    n "O tambien que sea tan malo que no pueda ense??ar nada.(*^-^*)q"
    am "Yo confio en ti."
    n "Voy bajando ya que hay que poner la switch.(>_<)"

    hide nesteanormal with dissolve

    show negro
    with fade

    play sound "audio/puerta.ogg"

    pause 1.5

    mc "{i}Bajamos al salon y Nestea empieza a poner la nintendo switch en la tele.{/i}"
    
    pause 1.0

    show cjs1
    with fade

    n "No me acuerdo como ponerlo dame 5 minutos.(>_<)"

    hide negro
    with None

    hide cj1
    with None

    mc "{i}Veo a Nestea un poco confundido poniendo la switch en la televisi??n.{/i}"
    
    pause 2.0

    mc "{i}Pasan 5 min{/i}"

    pause 1.0

    n "??Por fin! Pens?? que nunca acabaria.(*^-^*)q"

    hide nesteanormal with None

    show nesteapensando at center with None

    mc "{i}Veo como termina de conectar la consola y empieza a abrir el juego.{/i}"
    n "Si te digo la verdad no se que te puedo ense??ar...((*o_o)"
    n "Lo que podemos hacer es jugar unas partidas de chill para pasar el rato.(>_<)"
    mc "Me parece bien, mientras lo pasemos bien."
    n "Eligete el personaje que quieras y yo ir?? con random para que sea m??s o menos igualado.(*^-^*)q"
    mc "{i}Veo como entra al panel de personajes siendo bastante grande comparado con el de wii.{/i}"

    pause 1.0

    mc "Pues eligo a Wolf, lo jugue un poco en el smash de la WII y me gust??."
    n "Perfecto. Le voy dando al juegecito.(>_<)"

    menu:
        "Pasa 1 hora":
            pass

    am "Los maricones del fondo, dejad de jugar que ya hemos terminado."

    show amadeoserio at right with moveinright

    show jules at left with moveinright

    mc "Supongo que han estado re??idas los combates."
    am "Si, como siempre."
    j "??C??mo se lo han pasado los mancos?"
    n "Eh(>_<)"
    mc "Eh"
    n "Jugando unas partidas de chill sin nada en especial.(*^-^*)q"
    mc "Ha sido divertido."
    mc "Yo me voy ya que mi madre no sabe que estoy aqu??"
    n "Nos vemos ma??ana, no?((*o_o)"
    mc "Claro."
    mc "Adi??s a todos."
    t "Adi??s."

    hide jules with dissolve

    hide amadeoserio with dissolve

    hide nesteanormal with dissolve

    scene negro
    with fade

    pause 1.5

    mc "{i}Cuando llego a mi casa hago mis deberes, ceno, me ducho y me voy ha dormir {/i}"

    pause 1.5

    hide cjs1
    with None

elif patata == 4:
    
    play music "<from 5 to 15.5>audio/musica1.mp3"

    g "Let??s go"
    g "Te quedas solito un rato kinacha"
    k "Pero no te pregunte"
    g "Vamos a bajarnos al salon, [name]"

    hide kinachanomal with dissolve

    mc "Te sigo detras tuya."

    hide goonormal with dissolve

    hide cg1
    with dissolve

    play sound "audio/puerta.ogg"

    pause 1.5

    mc "{i}Bajamos al salon y Goo empieza a poner la nintendo switch en la tele{/i}"
    
    pause 1.0

    show cgs1
    with fade

    show goopensando at center with moveinright

    g "Un momento que tengo que poner la consola"
    mc "{i}Veo a Goo terminando poniendo la switch en la televisi??n{/i}"

    pause 1.0

    mc "Que piensas ense??arme el primer d??a Goo"
    mc "{i}Digo eso mientras me siento en sof??{/i}"
    g "Ya lo tenia pensado."
    g "Te voy ha ense??a a saber moverte y ganar la plataforma principal contra cualquier enemigo"

    play sound "audio/puerta.ogg"

    pause 2.0

    s "????HOLAAAAAA?!"

    show serrperrynormal at right with moveinright

    g "Ya has vuelto, te veo cansado."
    s "He venido corriendo para no perder mucho tiempo."
    s "??C??mo lo llevais?"
    g "Ense??andole como va el juego."
    s "Nice. Me subo que no quiero que kinacha est?? m??s tiempo solo."
    s "Hasta luego"
    mc "Adi??s"
    mc "{i}Veo como Serrperry va a la habitaci??n de Goo{/i}"

    hide serrperrynormal with dissolve

    pause 2.0

    g "??Seguimos?"
    mc "Claro"
    g "Entonces, ??qu?? personaje vas ha elegir?"

    mc "{i}Veo como entra al panel de personajes siendo bastante grande comparado con el de wii{/i}"

    pause 1.0

    mc "Pues eligo a Wolf, lo jugue un poco en el smash de la WII y me gust??."
    g "Perfecto."
    g "Wolf no es un mal personaje para el spacing"
    mc "??Y que es el spacing?"
    g "Lo que he dicho anteriormente"
    mc "Ah vale"
    g "Wolf tiene proyectiles y su velocidad es media por decirlo de alguna manera"
    mc "Interesante"
    g "Te lo ense??o mejor jugando, ??vale?"
    mc "Sip"

    menu:
        "Pasa 1 hora":
            pass

    show kinachanomal at right with moveinright

    show serrperrynormal at left with moveinright

    mc "{i}Escucho los pasos de Serrperry y Kinacha detras mia{/i}"
    g "Hey chicos, ??Que tal las partidas de hoy?"
    k "Algunos rest y down smashs."
    g "Vamos lo de siempre."
    s "Sip"
    mc "Yo me voy ya que mi madre no sabe que estoy aqu??"
    s "Nos vemos ma??ana, no?"
    mc "Claro."
    mc "Adi??s a todos."
    t "Adi??s."

    hide kinachanomal with dissolve

    hide serrperrynormal with dissolve

    hide goonormal with dissolve

    scene negro
    with fade

    pause 1.5

    mc "{i}Cuando llego a mi casa hago mis deberes, ceno, me ducho y me voy ha dormir {/i}"

    pause 1.5

    hide cgs1
    with None

else:
        
    play music "<from 5 to 15.5>audio/musica1.mp3"

    k "Pero, pregunt???"

    hide goonormal with dissolve
    
    show kinachanomal at center with moveinleft

    mc "??Qu?? dices?"
    k "Nada, Nada. ??Vamos al salon?"
    mc "Claro"

    hide goonormal with dissolve

    mc "Te sigo detras tuya."

    hide kinachanomal with dissolve

    scene negro
    with fade

    play sound "audio/puerta.ogg"

    pause 1.5

    mc "{i}Bajamos al salon y kinacha empieza a poner la nintendo switch en la tele{/i}"
    
    pause 1.0

    show cgs1
    with fade

    k "Esperate 2 min que no se como funciona esta televisi??n"

    show kinachanomal at center with moveinleft
    
    mc "{i}Pasan 2 min y veo como entra al juego{/i}"
    k "Que le ense??o a este manco en su primer d??a."
    mc "Ey."
    k "Era broma."
    k "......"
    k "Dejame pensar un rato."

    pause 1.8

    hide kinachanomal with None

    show kinachaexplicando at center with None

    k "Te ense??are los combos basicos del personaje que eligas."
    k "Dime, ??Has jugado antes a otro smash o eres nuevo?"
    mc "Ya hab??a jugado al smash de WII."
    k "Dios, bien. Mejor para mi para no gastar saliba."
    mc "XD"
    k "??Qu?? personaje piensas usar?"
    mc "{i}Cuando dice esto veo el plante mucho m??s grande que el de la WII.{/i}"

    play sound "audio/puerta.ogg"

    pause 2.0

    s "????HOLAAAAAA?!"

    show serrperrynormal at right with moveinright

    s "Hola kinacha, me subo con Goo."
    k "Pregunt???"
    s "Calla."
    k "XD"
    s "Os dejo y pasarlo bien."
    mc "Adi??s"
    mc "{i}Veo a Serrperry ir al cuarto de Goo rapidamente{/i}"

    hide serrperrynormal with dissolve

    k "Por donde ??bamos..."
    mc "{i}Nos quedamos un rato pensando por donde ??bamos{/i}"

    pause 2.0

    k "Cual es el personaje que vas a elegir."
    mc "Pues eligo a Wolf, lo jugue un poco en el smash de la WII y me gust??."
    k "Ummm... Wolf no me s?? muchos combos basicos, pero te ense??are todos los que sepa y puedas hacer."
    k "Jugaremos en el entrenamiento que ser?? m??s comodo."
    mc "Bien, ??vamos?"
    k "Claro"

    menu:
        "Pasa 1 hora":
            pass
    $ style.namebox
    $ style.window
    $ gui.text_color
    $ style.say_dialogue
    show goonormal at right with moveinright

    show serrperrynormal at left with moveinright

    hide kinachaexplicando with None

    show kinachanomal at center with None

    mc "{i}Escucho los pasos de Serrperry y Kinacha detras mia{/i}"
    g "Hey chicos, ??Que tal las partidas de hoy?"
    k "Ense??ando un par de combos, nada muy interesante"
    g "Perfecto"
    k "??Qu?? tal vosotros?"
    s "Nada en especial, lo de siempre"
    mc "Yo me voy ya que mi madre no sabe que estoy aqu??"
    s "Nos vemos ma??ana, no?"
    mc "Claro."
    mc "Adi??s a todos."
    t "Adi??s."

    hide kinachanomal with dissolve

    hide serrperrynormal with dissolve

    hide goonormal with dissolve

    scene negro
    with fade

    pause 1.5

    mc "{i}Cuando llego a mi casa hago mis deberes, ceno, me ducho y me voy ha dormir {/i}"

    pause 1.5

    hide cgs1
    with None

pass

scene dia3
with bites

hide negro
with None

pause 3.0

show p1
with fade

play music "<from 5 to 15.5>audio/musica1.mp3"

mc "{i}Estoy llegando a la sala del club.{/i}"
mc "{i}Siendo una ma??ana tranquila encuentro con ganas de entrar al club.{/i}"
mc "{i}Entro en la sala...{/i}"

pause 1.2

play sound "audio/puerta.ogg"

pause 2.1

show ss2
with fade

mc "Pos ya he llegado, ??c??mo estamos?"
t "De puta Madre."
mc "{i}Veo a todos en grupo hablando y al lado hay un portatil blanco.{/i}"
mc "??Y de quien es este portatil?"
n "Es de Serrperry y ha salido un momento al departamento de informatica."
mc "Le estais esperando, no???"
n "Si."

pause 1.5

mc "Estamos esperando a Serrperry para irnos, pero derrepente...{nw}"
mc "El portatil de Serrperry empieza a iluminarse y nos...{nw}"

scene negro
with bites

s "Des..."
s "Despierta..."

if patata == 1:

    am "??Pe-pero d??nde estoy?"
    s "Creo que estas en el juego de doki doki literature club"
    am "Y, ??d??nde co??o estas? ??D??nde co??o esta el resto?"
    s "Pues..."

    jump flass

elif patata == 2:

    j "??D??nde estoy?"
    s "no ...{nw}"
    j "Y, ??D??nde estas?"
    s "Pues..."

    jump flass

elif patata == 3:

    n "??D??nde estoy?((*o_o)"
    s "no ...{nw}"
    n "Y, ??D??nde estas?(>_<)"
    s "Pues..."

    jump flass

elif patata == 4:

    g "??D??nde estoy?"
    s "no ...{nw}"
    g "Y, ??D??nde estas?"
    s "Pues..."

    jump flass

else:

    k "??D??nde estoy?"
    s "no ...{nw}"
    k "Y, ??D??nde estas?"
    s "Pues..."
    
    jump flass

pass

label flass:

$ style.namebox
$ style.window
$ gui.text_color
$ style.say_dialogue

show ss2
with goslow

play sound "audio/puerta.ogg"

pause 2.1

s "????????Holaaaaaa??!!"

show serrperrynormal at center with moveinleft

s "No hay nadie."
"Serrperry se hacerca al portatil."
s "??Por qu?? esta el doki doki abierto?"
s "Y que hacen todo SS en el doki doki."

pause 1.0

hide serrperrynormal with None

show serrperrysorprendido at center with None

s "No puede ser... Estan dentro del juego, pero ??c??mo?"
s "??C??mo es posible?"
s "..."
s "??Qu?? hago yo ahora?"

pause 1.0

s "Tengo..."
s "Tengo que..."
s "Tengo que ayudarles con la poca habilidad en programacion que tengo."

hide serrperrysorprendido with dissolve

show bgddlc1 with goslow

$ style.namebox
$ style.window
$ gui.text_color
$ style.say_dialogue

if patata == 1:

    jump amddlc1

elif patata == 2:

    jump jddlc1

elif patata == 3:

    jump nddlc1

elif patata == 4:

    jump gddlc1

else:

    jump kddlc1

pass


show fin3
with fade

pause 5.0

hide bgddlc1
with None

hide ss2
with None

hide fin3
with dissolve

return

