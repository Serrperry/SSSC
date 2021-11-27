
label amddlc1:


# $ delete_all_saves()
# $ persistent.deleted_saves = True

show amadeoloco at panic:
    xalign 0.5
    yalign 0.5

am "Vale, entonces ¡¿POR QUE COJONES ESTOY AQUI?! ¿No me pude haber metido en el doom?"
s "Porque el doom no me lo tira."
am "Vale, makes sense. ¿Y cómo salgo?"
s "Calmate bro, ahora mismo me voy para mi casa, aquí no tengo wifi."

hide amadeoloco with None
show amadeo serio with None:
    xalign 0.5
    yalign 0.5

am "Dolor. Ya que estoy aprovecho y me paso el jueguito."
s "No creo que te de tiempo ya que pausaré el juego."
am "Pues quiza me cago un poco en tus muertos."
s "Ya tendrás tiempo de pasartelo las veces que quieras."
am "Bueno, que si, vete a pastar."
s "Tardo un segundo que tengo que hablar con los demas."
"{i}Vemos como amadeoamadel sale corriendo de la casa del MC.{/i}"

play sound "audio/puerta.ogg"

pause 3.0

scene bgddlc2
with wipeleft_scene

pause 1.8

scene bgddlc3
with wipeleft_scene

stop music
pause 1.0
play music "<loop 4.499>audio/2) Ohayou Sayori!.ogg"
pause 1.0

sy "¡¡Heeeeeeeyyy!!"
am "{i}No recordaba este punto del juego tan molesto.{/i}"
am "{i}Sayori es una chica muy energica y simpatica, lastima de que se suicide en unos dias.{/i}"

show sayori sf16 at t11:
    zorder2

sy "Haaahhh...Haaahhh..."
sy "¡Otra vez me quedé dormida!"
sy "¡Pero esta vez te atrapé!"
am "Jo, y eso que me doy prisa para yo pillarte a ti"

show serrperrynormal with None:
    zorder3

s "Creo que ya funciona, ¿me ves? No hace falta que me digas nada."
am "Tu puta madre, lo siento Sayori no iba para ti."

hide sayori sf16 with None
show sayori sf12 at hop:
    xalign 0.5
    yalign 0.8
show filtro1
with vpunch

pause 0.8

hide serrperrynormal
with moveoutbottom
show serrperrynormal at right with moveinbottom

s "Pausemos un rato el juego, ¿Amadeo me escuchas?"

show serrperrynormal at center with moveinright

am "Alto y claro."
s "Debo de contarte la situacion del grupo. Estaís todos jugando al juego desde el mismo punto pero en diferentes guardados."
am "Vale, entonces vigila a Nestea está muy necesitado."
s "Al unico que no encuentro jugando pero si en los archivos es a [name], es como si estubiese corrupto sus archivos."
am "Joder, ya me joderia ser tan desgraciado."
s "JAJAJA, La cosa es que no puedo sacaros de aquí ya que no tengo permisos de administrador sobre el juego."
am "Eres un hijo de puta."
s "Yo no tengo na da que ver con esto."
am "Mentira, era tu plan desde el principio"

show objection with hpunch: 
    xalign 0.75
    yalign 0.17

s "Eso no es verdad, ¿Cómo iba a saber que mi portatil os tragaria de esta forma?"

hide objection with dissolve

am "Es una forma de hablar, ¿Entonces como salgo del jueguito?"
s "La unica 'Persona' que podría ayudaros sería Monika ya que tiene los permisos de la 'consola'."
am "Razonable, pero el juego no me dejará hablar con ella."
s "Por eso hablaré yo con ella ya que soy esencialmente un pequeño mod del juego."
am "Yo tambien quiero hablar con ella para un personaje que me gusta de este juego."
s "Como has dicho antes no puedes el juego no te dejará, pero lo intentaré"
am "Bueno, me vale."
s "Te dejo que te estaré viendo como juegas al juego."
am "Ok y vigila al Nestea."
s "Si ya lo hago pero por partes que soy muchos."

hide filtro1 with None

pause 0.1

hide serrperrynormal with moveoutbottom

sy "Eeeehhh!. ¿Estas bien, Amadeo?"

show serrperrynormal at right with moveinbottom

am "Si, si. Un dia raro"

hide sayori sf12 with None
show sayori sd1 at hop:
    zorder2

sy "Supongo. Tu pensabas que ya me había ido, eso es raro de ti."
sy "Ejeje~"
am "Pero no lo hiciste que es lo que me importa"
sy "Hace tiempo que no me decias algo así. Me gusta."

hide sayori sf12 with None
show sayori sd7 at s11:
    zorder2

pause 2.0

sy "Por cierto, Amadeo..."
sy "¿Ya has decidido a que club quieres unirte?"
am "Ostia, Es cierto que te prometí que me uniria a un club."
am "Mmmm... No lo había pensado, supongo que me unire al club de Tekken"

hide sayori sd7 with None
show sayori sd15 at s11:
    zorder2

sy "De Te..."
sy "De Tekken, ¿qué es 'Tekken'?"
am "Un videojuego de lucha."
sy "Ahh. Un videojuego, ¿Alguna vez me lo enseñastes?"
am "Aun no lo he jugado pero lo ví en el tele y me gustó."
sy "¡Uh-huh!"
sy "¿Solo has pensado en eso?"
am "Si te soy sincero, en realidad no he pensado nada."

hide sayori sf7 with None
show sayori sd8 at s11:
    zorder2

sy "Eso no esta bien, Amadeo."
sy "Si dices eso me harás preocuparme más por ti."
sy "Por favor, dime que intentaras buscar algún club."
am "Bueno, vale, Te lo prometo."

hide sayori sd8 with None
show sayori sf17 at hop:
    zorder2

sy "¡Yaay~!"
s "Se viene transicíonnnn!"

scene bgddlc4
with wipeleft_scene

show serrperrynormal at center with moveinbottom

am "Ah! Espera, ¿qué?"
s "Y volvemos de la transicíon. ¿Cómo se siente?"
am "Como un parpadeo muy raro y muy largo."
s "Y ahora debería entrar sayori por la puerta."

show serrperrynormal at right with moveinright

pause 0.5

show sayori sd2 at t11:
    zorder2

sy "¿Holaaaa?"
am "Hey, sayori, ¿Qué haces aquí?"
am "{i}La puta de serrperry tenia razón.{/i}"

hide sayori sd2 with None
show sayori sd1 at s11:
    zorder2

sy "Pensé que podría atraparte saliendo del aula, pero te vi sentado aquí, así que entré."
sy "Honestamente, eres peor que yo algunas veces...¡Estoy impresionada!"
am "No es nada, solo estaba pensando en las actividades."
am "Y, ¿qué haces aquí?"
sy "Yo..."

hide sayori sd1 with None
show sayori sd25 at s11:
    zorder2

sy "Queria hablarte del tema de los clubs..."
sy "Y..."
sy "Pensé que necesitabas un enpujon."
am "No se a que punto quieres llegar. Sé más especifica, por favor."

hide sayori sd25 with None
show sayori sd1 at s11:
    zorder2

sy "Bueno, ¡Que podrías venir a mi club!"
am "..."
am "Sayori... Sabes que esto es muy repentino, ¿no?"

hide sayori sd1 with None
show sayori se11 at t11:
    zorder2

sy "Si"
am ""

menu:

        "Decido ir a por Monika":
            jump amddlc1a

        "Decido ir a por Yuri":
            jump amddlc1b
return