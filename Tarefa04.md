
## 1. Descarga la imagen 'httpd' y comprueba que está en tu equipo.
<img width="1032" height="339" alt="image" src="https://github.com/user-attachments/assets/d463c056-b8b1-4655-aef5-eed8ef009c74" />

Comenzo descargando httpd co comando docker pull httpd:2.4. Logo emprego docker images para ver unha lista das imaxes instaladas.
<img width="1025" height="281" alt="image" src="https://github.com/user-attachments/assets/b342739d-9a56-45d7-938a-c2bc060cdec1" />

## 2. Crea un contedor con el nombre 'dam_web1'.
<img width="1029" height="108" alt="image" src="https://github.com/user-attachments/assets/ce7c1afa-ce5f-45d6-ada5-4dba7038fa77" />
<img width="1106" height="51" alt="image" src="https://github.com/user-attachments/assets/601dd7a5-92dc-49a5-aea9-f42a7d277bbf" />
Creo o contedor co comando da imaxe e o nomeo como dam_web1_tarefa4. Tras isto comprobo se se creou mirando a lista de contedores. 


## 3. Si quieres poder acceder desde el navegador de tu equipo, ¿que debes hacer?
<img width="1031" height="85" alt="image" src="https://github.com/user-attachments/assets/0315c672-d0be-4bed-86d6-a19d057f16cf" />
Emprego o comando da imaxe para conectar o contedor ao porto 8000 do ordenador
<img width="681" height="463" alt="image" src="https://github.com/user-attachments/assets/65c70785-8e7a-4eb1-ab55-4e540dc7caec" />
ao tratar de conectalo aparéceme unha mensaxe de seguridade de windows. Permito o acceso as redes privadas
<img width="681" height="452" alt="image" src="https://github.com/user-attachments/assets/4dc1edbd-17a1-4104-97d0-70bf4b262e4c" />
Nesta imaxe podemos ver que funciona.

## 4. Utiliza bind mount para que el directorio del apache2 'htdocs' esté montado un directorio que tu elijas.
<img width="834" height="266" alt="image" src="https://github.com/user-attachments/assets/6c3ff275-cb6d-451b-81b1-1e4f9cde8b15" />
Primeiro creo un directorio no que se almacenará o docker. Tras isto paro o contendor e o reinicio
# Tarefa Docker 04 
**Desenvolvido por**: Sofía Otero  
**Asignatura**: SXE

---

<img width="1127" height="53" alt="image" src="https://github.com/user-attachments/assets/4424e61f-ea6d-4b66-b343-1503466f906d" />
Aquí creo o contendor con mapeo de puertos y bind mount
<img width="1030" height="96" alt="image" src="https://github.com/user-attachments/assets/64a58de1-61de-4537-9cdd-111218dfe435" />
Emprego este comando para comprobar que o contendor creouse correctamente

## 5. Realiza un 'hola mundo' en html y comprueba que accedes desde el navegador.

<img width="1032" height="34" alt="image" src="https://github.com/user-attachments/assets/1f6b9a1a-0283-4049-9f56-80e4e067a2b0" />
<img width="1042" height="211" alt="image" src="https://github.com/user-attachments/assets/5e7ba2c6-0b70-4f00-a7e3-d9fa06437d9e" />

Aquí edito o contendor para que diga hola mundo e o fago a través do porto 8000 do ordenador. Tras isto entro no navegador e comprobo que, efectivamente, funciona correctamente

## 6. Crea otro contenedor 'dam_web2' con el mismo bind mount y a otro puerto, por ejemplo 9080.
<img width="969" height="46" alt="image" src="https://github.com/user-attachments/assets/53762fec-ce34-44e9-9e5c-7f981c8dc539" />
Aquí creo outro contendor que chamei dam_web2 asociado ao mismo bind mount pero a outro porto, o 9080
## 7.Comprueba que los dos servidores 'sirven' la misma página, es decir, cuando consultamos en el navegador:
<img width="1033" height="355" alt="image" src="https://github.com/user-attachments/assets/5156002d-ae56-4195-8a74-30a841a4aac1" />
Aquí mirei como se mostra a mesma páxima

## 8. Realiza modificaciones de la página y comprueba que los dos servidores 'sirven' la misma página.

<img width="1051" height="349" alt="image" src="https://github.com/user-attachments/assets/4d97746d-8a84-4af7-a5be-e7b74cfd49dc" />
<img width="1029" height="373" alt="image" src="https://github.com/user-attachments/assets/35ada958-ef6e-40d0-808c-5924dbd87fee" />
Modifiquei a mensaxe empregando este comando: 
echo "< html>< body>< h1> 
Modificación: Los dos servidores comparten ESTA página. < /h1>< /body>< /html>" > C:\Sofia\web\index.html.
ao estar no mesmo bind mount os dous contedores modificáronse
