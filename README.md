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

## Crea un contenedor con el nombre 'dam_alp1'. ¿Como puedes acceder a él?
## Comprueba que ip tiene y si puedes hacer un ping a google.com
## Crea un contenedor con el nombre 'dam_alp2'. ¿Puedes hacer ping entre los contenedores?
## Sal del terminal, ¿que ocurrió con el contenedor?
## ¿Cuanta memoria en el disco duro ocupaste?
## ¿Cuanta RAM ocupan los contenedores? ¿Hay algún comando docker para saber esto?.



