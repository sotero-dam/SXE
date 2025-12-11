# Tarea 16: Extendiendo el modelo
## Completa la funcionalidad del módulo indicado en la guía (Zodiaco) y añade la gestión de Fidelización de Clientes:

<img width="600" height="778" alt="image" src="https://github.com/user-attachments/assets/c745696b-d37c-4315-bba6-1287b10c4a8b" />

<img width="1327" height="822" alt="image" src="https://github.com/user-attachments/assets/4b9c518e-bbb9-4bbc-ac28-7c6da6492aac" />

### Campo Nuevo: Un campo de texto para el Código de Socio (ej. "VIP-1234").

Engadín o campo partner_code = fields.Char(...) ao modelo Python.

<img width="441" height="47" alt="image" src="https://github.com/user-attachments/assets/5c8d93ca-3280-4f44-9d24-e36e4aed952c" />


### Campo Calculado: Un campo llamado Nivel de Fidelidad que se calcule automáticamente:

  Si el contacto tiene Código de Socio: Nivel "Premium".
  
  Si el campo está vacío: Nivel "Estándar".
  
  Si el código empieza por "G": Nivel "Gold".

Definín a lóxica de cálculo (Gold/Premium/Estándar) no método _compute_fidelity_level do código Python.

<img width="551" height="270" alt="image" src="https://github.com/user-attachments/assets/b144c310-5e85-4dc4-8c3c-82d4dedb6f55" />


## Modificaciones en Vistas:

### Formulario: Crear una pestaña "Membresía" con estos campos.

<img width="1429" height="692" alt="image" src="https://github.com/user-attachments/assets/9a30f695-c2eb-4276-ad95-21d5c60ddb98" />

### Lista: Mostrar el Nivel de Fidelidad en color azul si es Premium/Gold (pista: decoration-info).

Empreguei decoration-primary en vez do proposto, xa que como non había rosa, polo menos polo morado.

<img width="1916" height="295" alt="image" src="https://github.com/user-attachments/assets/cb455dd1-2053-45f0-8c3b-9699640940fd" />

### Kanban: Mostrar el Código de Socio en negrita debajo del nombre.

<img width="1395" height="426" alt="image" src="https://github.com/user-attachments/assets/e1806d8c-276c-450a-977d-4dd27fdd8bdc" />





