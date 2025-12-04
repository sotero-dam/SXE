# Módulo en Odoo que asigne la bebida adecuada según el sueño de cada usuario.
**Desenvolvido por**: Sofía Otero  
**Asignatura**: SXE

<img width="526" height="598" alt="image" src="https://github.com/user-attachments/assets/5d5f6784-9374-4de7-84bb-744ce396d2c5" />


Comecei creando a capreta adddons_locales no meu ordenador, para gardar o código. Anteriormente creara o modulo_cafetero nun contenedor docker pero esto non e adecuado, xa que o pecharse o contedor pérdese o código (tiña que engadir un novo volume no ym para vincularl). Por iso, usei docker_cp para copiar o modulo a miña carpeta local. Con isto tiña unha copia do móculo cos archivos para poder traballar.

<img width="880" height="626" alt="image" src="https://github.com/user-attachments/assets/1ddbc2ca-997e-40da-9728-89ead07bbfc0" />

No manifest defino o modulo. Esto serve para identificar o módulo co seu nome, resumo de función e categoría. Tamén lisra todos os ficheitos importantes que Odoo ten que cargar.

<img width="833" height="519" alt="image" src="https://github.com/user-attachments/assets/6036532e-d3b5-4c4d-93ca-297b61dfa1a2" />


Definin o modelo CafeteraSono para rexistrar os datos, tamen os campos nivel_sueno e un if else para ver a bebida que toca.


<img width="942" height="669" alt="image" src="https://github.com/user-attachments/assets/1b23c2dc-f6f4-4b70-9ea2-cc9501932a85" />

No view díxenlle a Odoo como quería que se visen os meus campos, tipo de vista formulario. E establecín un menu principal, Cafeteria.

<img width="957" height="904" alt="image" src="https://github.com/user-attachments/assets/50cde23f-56aa-4aa4-ba36-420846bcf18c" />

Tamén configurei alguns detalles no acess para poder acceder correctamente.

<img width="992" height="113" alt="image" src="https://github.com/user-attachments/assets/a241d63f-2027-489e-831b-f5046c02492e" />


Unha vez fixen todos os cambios fixen un docker compose up. Logo descarguei o módulo e actualiceino. Despois, seleccionenino no menú e probeino.


<img width="1888" height="406" alt="image" src="https://github.com/user-attachments/assets/903f3865-61a7-4657-9e66-0f34fb8ffb7e" />

<img width="1371" height="467" alt="image" src="https://github.com/user-attachments/assets/9eec29d2-45ec-41e0-96b4-9105037996a2" />

<img width="1438" height="277" alt="image" src="https://github.com/user-attachments/assets/1955ac6a-a3ce-4878-82b6-ed42df7532ab" />

<img width="1393" height="348" alt="image" src="https://github.com/user-attachments/assets/69c26c80-f3b5-4419-a45b-82818255050c" />

<img width="1919" height="288" alt="image" src="https://github.com/user-attachments/assets/7316c6c1-adea-404d-8fb2-1afa40ad0406" />



