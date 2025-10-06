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


## Sal del terminal, ¿que ocurrió con el contenedor?
## ¿Cuanta memoria en el disco duro ocupaste?
## ¿Cuanta RAM ocupan los contenedores? ¿Hay algún comando docker para saber esto?.











