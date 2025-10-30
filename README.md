# 🏪 Tienda Online Async API

**Autor:** Sergio Zuñiga  
**Universidad:** Universidad Católica de Colombia  
**Programa:** Ingeniería de Sistemas y Computacion  
**Versión:** ProMax  
**Framework:** FastAPI + SQLAlchemy Async  
**Base de datos:** SQLite (aiosqlite)

---

## Tabla de contenidos

* [Descripción general](#descripción-general)
* [Objetivos del proyecto](#objetivos-del-proyecto)
* [Tecnologías utilizadas](#tecnologías-utilizadas)
* [Modelado de datos](#modelado-de-datos)

  * [Categoria](#categoria)
  * [Producto](#producto)
  * [Relaciones (ERD)](#relaciones-erd)
* [Instalación y ejecución](#instalación-y-ejecución)
* [Mapa de endpoints](#mapa-de-endpoints)

  * [Categorias](#categorias)
  * [Productos](#productos)
* [Reglas de negocio](#reglas-de-negocio)
* [Control de versiones (Git y GitHub)](#control-de-versiones-git-y-github)

---

## Descripción general

**Tienda Online Async API** es un backend desarrollado con **FastAPI y SQLAlchemy asincrónico**, diseñado para gestionar la información de una tienda virtual.  
Permite administrar **categorías y productos** con operaciones **CRUD completas**, validaciones de datos, filtros, manejo de errores y relaciones entre entidades.

El sistema busca simular el funcionamiento de una tienda real, como una **tienda de artículos de fútbol**, gestionando su inventario de **guayos, camisetas y balones**.

---

## Objetivos del proyecto

**Objetivo general**  
Desarrollar una API REST asíncrona que permita la administración completa de productos y categorías de una tienda online, utilizando SQLite como base de datos y validaciones robustas en Pydantic.

**Objetivos específicos**

* Implementar relaciones **1:N** entre categorías y productos.
* Incorporar operaciones **CRUD** (crear, leer, actualizar, eliminar).
* Validar datos de entrada con **Pydantic**.
* Controlar errores mediante **códigos HTTP estandarizados**.
* Garantizar la consistencia de la base de datos y la integridad referencial.

---

## Tecnologías utilizadas

| Tecnología   | Descripción                                   |
| ------------- | --------------------------------------------- |
| FastAPI       | Framework principal para la creación del backend |
| SQLAlchemy    | ORM asincrónico para la gestión de modelos y consultas |
| SQLite        | Base de datos ligera y embebida               |
| Uvicorn       | Servidor ASGI utilizado por FastAPI           |
| Pydantic      | Validación de datos y esquemas                |
| Python 3.11+  | Lenguaje de programación principal            |
| aiosqlite     | Control asincrónico para SQLite               |

---

## Modelado de datos

### Categoria

| Atributo     | Tipo   | Descripción                                         |
| ------------- | ------ | --------------------------------------------------- |
| `id`          | int    | Identificador único (PK autoincremental)           |
| `nombre`      | str    | Nombre único de la categoría                       |
| `descripcion` | str    | Detalle o propósito de la categoría                 |
| `activa`      | bool   | Indica si la categoría está activa o desactivada   |

### Producto

| Atributo       | Tipo   | Descripción                                      |
| --------------- | ------ | ------------------------------------------------ |
| `id`            | int    | Identificador único (PK autoincremental)        |
| `nombre`        | str    | Nombre del producto                             |
| `precio`        | float  | Precio del producto (nunca negativo)            |
| `stock`         | int    | Cantidad disponible en inventario (≥ 0)         |
| `descripcion`   | str    | Detalle o características del producto          |
| `activo`        | bool   | Indica si el producto está disponible           |
| `categoria_id`  | int    | FK → Categoria (relación 1:N)                   |

### Mapa de endpoints

| Método   | Ruta               | Descripción                         |
| -------- | ------------------ | ----------------------------------- |
| `POST`   | `/categorias/`     | Crear una nueva categoría           |
| `GET`    | `/categorias/`     | Listar categorías activas           |
| `GET`    | `/categorias/{id}` | Consultar categoría por ID          |
| `PUT`    | `/categorias/{id}` | Actualizar nombre o descripción     |
| `DELETE` | `/categorias/{id}` | Eliminar categoría (borrado físico) |

### Productos

| Método   | Ruta                        | Descripción                         |
| -------- | --------------------------- | ----------------------------------- |
| `POST`   | `/productos/`               | Crear un nuevo producto             |
| `GET`    | `/productos/`               | Listar productos activos            |
| `GET`    | `/productos?precio=&stock=` | Filtrar por precio máximo y stock   |
| `GET`    | `/productos/{id}`           | Obtener producto por ID             |
| `PUT`    | `/productos/{id}`           | Actualizar información del producto |
| `DELETE` | `/productos/{id}`           | Eliminar producto (borrado físico)  |

### Reglas de negocio

* Nombre de categoría único: no se permiten duplicados.
* Stock no puede ser negativo: validado en creación y actualización.
* Productos requieren categoría activa: no se pueden registrar productos en categorías inactivas.
* Relación 1:N: una categoría puede tener muchos productos.
* Validaciones Pydantic: controlan formato, longitud y límites.

## Manejo de errores estandarizado:

* 200 – OK
* 201 – Creado correctamente
* 400 – Petición inválida
* 404 – No encontrado
* 409 – Conflicto (duplicados)

### Relaciones (ERD)

```mermaid
erDiagram
    CATEGORIA {
        int id
        string nombre
        string descripcion
        bool activa
    }

    PRODUCTO {
        int id
        string nombre
        float precio
        int stock
        string descripcion
        bool activo
        int categoria_id
    }

    CATEGORIA ||--o{ PRODUCTO : contiene


