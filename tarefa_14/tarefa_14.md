## Exercicio 1
```sql
CREATE TABLE EmpresasFCT (
    idEmpresa SERIAL PRIMARY KEY,
    nombre VARCHAR(40),
    quiereAlumnos BOOLEAN,
    numAlumnos INTEGER,
    fechaContacto DATE
);

```
<img width="995" height="530" alt="image" src="https://github.com/user-attachments/assets/d063883e-d0a4-45d4-937c-7b8ee06f7760" />

## Exercicio 2

Tiven que usar este método para introducir contactos que busquei en internet xa que me era imposible introducilos de xeito normal, sen pedir o id. Parece ser que algunhas partes da demo non se cargaran a pesar de clicar en ese recadro ao crear a base.

```sql
INSERT INTO res_partner (name, is_company, city) VALUES
('Tucha', TRUE, 'Arcade')
RETURNING id;
```

<img width="1239" height="552" alt="image" src="https://github.com/user-attachments/assets/0a240395-df33-4831-819d-1143d0e7653e" />

```sql
INSERT INTO res_partner (name, is_company, city, parent_id) VALUES
('Tucha', FALSE, 'Arcade', 16);
```

<img width="1217" height="577" alt="image" src="https://github.com/user-attachments/assets/c969975e-65af-4651-8e8a-75ac9079ab66" />

## Exercicio 3

```sql
SELECT
    *
FROM
    empresasfct
ORDER BY
    fechacontacto DESC;
```

<img width="1173" height="665" alt="image" src="https://github.com/user-attachments/assets/d6c01d77-e3b0-444b-bee1-ea04f8354883" />

## Exercicio 4

```sql
SELECT
    p.name AS "Nombre del Contacto",
    p.city AS "Ciudad",
    e.name AS "Nombre Comercial de la Empresa"
FROM
    res_partner p
LEFT JOIN
    res_partner e ON p.parent_id = e.id
WHERE
    p.is_company IS FALSE
    AND p.city <> 'Tracy'
ORDER BY
    e.name ASC;
```

<img width="1535" height="840" alt="image" src="https://github.com/user-attachments/assets/84537dbd-b2fc-44ff-9d13-bbf5fbdb1004" />

## Exercicio 5

Aquí tamén introducin manualmente os datos, guíandome por internet, porque non existía ningún rexistro.

```sql
INSERT INTO account_move (
    move_type, 
    partner_id, 
    name, 
    state, 
    invoice_date, 
    amount_untaxed, 
    date,
    journal_id,      
    currency_id,
    auto_post)       
VALUES
    ('in_invoice', 9, 'BILL/2025/0001', 'posted', '2025-11-01', 500.00, '2025-11-01', 2, 1, FALSE);

INSERT INTO account_move (
    move_type, 
    partner_id, 
    name, 
    state, 
    invoice_date, 
    amount_untaxed, 
    date,
    journal_id,      
    currency_id,
    auto_post)       
VALUES
    ('in_refund', 9, 'RFN/2025/0001', 'posted', '2025-11-25', 50.00, '2025-11-25', 2, 1, FALSE);
```

<img width="821" height="486" alt="image" src="https://github.com/user-attachments/assets/2288c83e-bd5c-4760-bd35-6879a848327c" />

```sql
SELECT
    rp.name AS "Nombre de la Empresa",
    am.name AS "Número de Factura",
    am.invoice_date AS "Fecha de la Factura",
    am.amount_untaxed AS "Total Factura SIN Impuestos"
FROM
    account_move am
INNER JOIN
    res_partner rp ON am.partner_id = rp.id
WHERE
    am.move_type = 'in_refund'
ORDER BY
    am.invoice_date DESC;
```

<img width="832" height="470" alt="image" src="https://github.com/user-attachments/assets/a66de274-5507-4264-b1a1-7977af6f7d62" />

## Exercicio 6

<img width="828" height="412" alt="image" src="https://github.com/user-attachments/assets/20624b50-4de7-4e25-84a7-b0ae247f7ceb" />

<img width="814" height="449" alt="image" src="https://github.com/user-attachments/assets/122373db-6c4b-4aaf-94fe-890c9e2a2864" />

```sql
SELECT
    rp.name AS "Nombre de la Empresa Cliente",
    COUNT(am.id) AS "Número de Facturas",
    SUM(am.amount_untaxed) AS "Total Facturado SIN IMPUESTOS"
FROM
    account_move am
INNER JOIN
    res_partner rp ON am.partner_id = rp.id
WHERE
    am.move_type = 'out_invoice'
    AND am.state = 'posted'
GROUP BY
    rp.id, rp.name
HAVING
    COUNT(am.id) > 2
ORDER BY
    rp.name;
```

<img width="821" height="446" alt="image" src="https://github.com/user-attachments/assets/39a86a7d-f57a-4880-b1c7-17cf1c07a0f7" />

## Exercicio 7

Creii contactos con email, para este caso, xa que os que creara antes non tiñan. Tamén tiven que facer un update previamente dos correos.

```sql
SELECT
    id,
    name,
    email
FROM
    res_partner
WHERE
    email LIKE '%@bilbao.bizkaia.eus';
```

<img width="1533" height="703" alt="image" src="https://github.com/user-attachments/assets/7897a47e-4689-40e2-bb6b-afc97b35afd8" />












