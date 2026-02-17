# ferreteria
Link del video: [video](https://drive.google.com/file/d/1to1X_HXi7IUK9upVbrDpn9-4xe3NKEIN/view?usp=sharing)

# 🔧 Sistema de Gestión de Herramientas
Sistema de consola en Python para gestionar el préstamo de herramientas en una comunidad vecinal.

---

## ▶️ Cómo ejecutar

**1.** Entra a la carpeta del proyecto:
```bash
cd ferreteria
```

**2.** Ejecuta el programa:
```bash
python main.py
```

> ⚠️ Asegúrate de ejecutarlo **desde dentro de la carpeta `ferreteria/`**.

---

## 🔐 Inicio de sesión

El sistema pide un **ID de usuario**. El administrador por defecto es:

| Campo  | Valor                  |
|------- |------------------------|
| ID     | `01`                   |
| Nombre | Cristian Ferney Solano |
| Tipo   | Administrador          |

Para crear más usuarios, inicia como administrador y ve a **Gestionar usuarios → Agregar usuario**.

---

## 👥 Tipos de usuario

**Administrador** → Acceso completo: usuarios, herramientas, préstamos, reportes y logs.

**Residente** → Puede ver herramientas disponibles, buscarlas y hacer solicitudes de préstamo.

---

## 📁 Archivos del proyecto

| Archivo | Función |
|---------|---------|
| `main.py` | Punto de entrada, login y menús |
| `herramientas_config.py` | Gestión del inventario |
| `prestamos_config.py` | Solicitudes y préstamos |
| `reportes_config.py` | Consultas y estadísticas |
| `usuario_config.py` | Gestión de usuarios |
| `json_config.py` | Leer y guardar archivos JSON |
| `estilos.py` | Colores y formato visual |
| `logs.py` | Registro de eventos |
| `sistema_logs.txt` | Bitácora (se crea automáticamente) |

---

## ✅ Requisitos

- Python 3.x
- No requiere instalar librerías externas