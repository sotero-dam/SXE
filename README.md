# Tarefa Docker 
**Desenvolvido por**: Sofía Otero  
**Asignatura**: SXE

---

## Descarga la imagen "alpine" SIN ARRANCARLA y comprueba que está en tu equipo
<img width="832" height="431" alt="image" src="https://github.com/user-attachments/assets/c2823bcf-e0b8-4187-9ba9-7bd06e2b7595" />
Comenzo descargando Alpine co comando docker pull alpine. Logo emprego docker images para ver unha lista das imaxes instaladas.


## Crea un contenedor sin ponerle nombre. ¿está arrancado? Obtén el nombre
<img width="629" height="60" alt="image" src="https://github.com/user-attachments/assets/61760d2b-f241-48f0-b1c9-e4c2e9bfe3f2" />
Creo contedor co comando docker run -d alpine sleep 10m. Que inicia un contedor en segundo plano (co -d) empregando a miña imaxe Alpine. Emprego sleep 10m, xa que o contedor precisa dun proceso principal. A súa función e agardar 10 minutos mantendo o contedor vivo e execuntándose durante ese tempo. Cando o proceso remate, docker deteno automáticamente e libera os recursos.
<img width="872" height="571" alt="image" src="https://github.com/user-attachments/assets/96225c0c-6216-4ee8-b3a5-883c97e07f41" />
Para ver o estado e nome do proceso emprego, docker ps -a. Con el amoso todos os contedores que teño creado en docker, o -a final é moi importante, xa que permite amosar TODOS os contedores non so os que se están executando. Sobre o estado do meu proceso, este estase executando dende hai 4 minutos, pódese ver no apartado STATUS. Respecto ó nome, este é asignado de forma aleatoria cando non se lle indica un.


## Crea un contenedor con el nombre 'dam_alp1'. ¿Como puedes acceder a él?
<img width="617" height="123" alt="image" src="https://github.com/user-attachments/assets/a55e7b22-83dc-48bc-ba06-01f455e99f9b" />
Agora, con docker run, creo e arranco un novo contedor a partir da imaxe. Con -d inicioo en segundo plano. As terminacións -i e -t (imput e cmd) permitiránme acceder logo no contenedor se o preciso. Finalmente, só engado o nome que quero porlle ao meu contedor.
<img width="687" height="127" alt="image" src="https://github.com/user-attachments/assets/2a5a98f1-b765-47b1-bb06-6e994fe2a105" />
Para acceder ao contedor, doulle ao terminal a instrucción de executar o comando dentro dun contedor activo con docker exec. Engado -i e -t segundo expliquei antes. Adxunto o nome do contedor e engado sh que me permite interactuar co sistema operativo do contedor Alpine.


## Comprueba que ip tiene y si puedes hacer un ping a google.com
<img width="815" height="274" alt="image" src="https://github.com/user-attachments/assets/e5d624b1-5aa7-4f7a-9ae6-4274818646ca" />
Fago un ip -a para ver a IP interna do contedor.
<img width="647" height="467" alt="image" src="https://github.com/user-attachments/assets/b26dc9d1-2ff0-45ae-8046-dcd862533cac" />
Introduzo o comando ping e indico a que dirección o quero facer, neste caso google.com, para ver se ten conectividade. É moi importante empregar CONTROL + C, para parar o ping.


## Crea un contenedor con el nombre 'dam_alp2'. ¿Puedes hacer ping entre los contenedores?
<img width="539" height="97" alt="image" src="https://github.com/user-attachments/assets/cc2b165b-f2ed-4379-a644-d1af02e39ece" />

Con exit saio do anterior contedor.
<img width="690" height="88" alt="image" src="https://github.com/user-attachments/assets/686d9eb3-75ac-4d6e-b9ac-fcbe93d33fb6" />
Creo o contedor do mesmo xeito que fixemos antes.
<img width="605" height="75" alt="image" src="https://github.com/user-attachments/assets/20364cd0-fc77-43b6-9cc7-b875ff71790d" />
Executo o contedor como se explicou anteriormente.
<img width="419" height="118" alt="image" src="https://github.com/user-attachments/assets/2099ca71-28f2-4714-854c-6ebd30728d98" />

Coma se ve, o meu comando fallou, esto é porque os contedores por defescto están na rede Bridge. Esto fai que a rede non sepa a que dirección IP corresponde ese nome, é dicir, que carece dun servizo que faga resolución DNS.
### Extra
Decidín arreglar este problema e fixen o seguinte:
<img width="367" height="52" alt="image" src="https://github.com/user-attachments/assets/bafaff88-272a-4a0b-b9e7-d9477eb2eb2d" />

Primeiro saín do contedor onde estaba e non podía facer o ping.
<img width="479" height="157" alt="image" src="https://github.com/user-attachments/assets/ee15e884-cfbd-4a0a-9c31-b650455b12aa" />

Logo parei os dous contedores que creara para despois eliminalos. Esto fíxeno para poder traballar cunha rede limpa que non me de problemas.
<img width="603" height="55" alt="image" src="https://github.com/user-attachments/assets/bfb2dd8a-603d-4bda-9b8c-75ea8b81f471" />


Creei unha nova rede sofia-rede-monisima, esto realiceino xa que Docker dota a estas redes que creamos automáticamente son equipadas cun servizo de DNS interno, que me permitirá usar os nomes dos contedores creados.
<img width="750" height="122" alt="image" src="https://github.com/user-attachments/assets/9086a0c5-e5bd-42ab-ae6a-1f43e54b2df1" />

Igual que antes creo os meus contedores, pero neste caso no final do comando engado tamén a miña nova rede.
<img width="583" height="214" alt="image" src="https://github.com/user-attachments/assets/15eeb1a4-618d-4c9f-af8a-f74525ddfe26" />

Fago o ping coma antes, pero neste caso funciona, xa que a diferencia de antes a rede pode entender ós nomes aos que me refiro.

## Sal del terminal, ¿que ocurrió con el contenedor?
<img width="917" height="175" alt="image" src="https://github.com/user-attachments/assets/3b5f2e9b-e43d-4291-975b-7e8649ba7edb" />

Saín con exit, e logo fixen ps-a para ver todos os contedores que creara. O contedor ó que fixen exit sigue funcionando xa que só pechei a sesión que me conectaba con el non o contedor en si. O meu proceso de 10min aparece pechado porque rematou o seu tempo de duracion (os 10 min).

## ¿Cuanta memoria en el disco duro ocupaste?
<img width="635" height="133" alt="image" src="https://github.com/user-attachments/assets/a8b31964-b75d-4bf9-b062-b9f367849520" />
Para ver a memoria que usei, emprego docker system df, para ver o uso do meu disco. En total, entre imaxes e contedores terei usado uns 129MB.

## ¿Cuanta RAM ocupan los contenedores? ¿Hay algún comando docker para saber esto?.
<img width="953" height="137" alt="image" src="https://github.com/user-attachments/assets/b16f600f-1b1f-4fb1-8e2d-313f5f668544" />

Si, so tiven que usar docker stats. Poiden apreciar que, dam_alp1 e dam_alp2, están practicamente inactivos e cada un só executa un PID.

















