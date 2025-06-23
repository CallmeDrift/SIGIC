SIGIC - Módulo de Caja Registradora (versión offline)

📦 ¿Qué contiene este paquete?
- `SIGIC.exe`: Ejecutable principal de la aplicación (doble clic y magia).
- `static/`: Archivos estáticos como imágenes, CSS y JS.
- `templates/`: Archivos HTML de la aplicación.
- `base_datos.sql`: Archivo para importar la base de datos.
- `README.txt`: Este documento que estás leyendo.
- `requirements.txt`: Dependencias por si deseas reinstalar o correr desde código.

⚙️ ¿Cómo usar la aplicación?

1. **Instala XAMPP** (o MariaDB local, si no tienes):
   - Asegúrate de que el servicio de MySQL esté activo.
   - No necesitas usar PHPMyAdmin, con consola basta.

2. **Importa la base de datos**:
   - Abre la consola de MySQL:
     ```bash
     mysql -u root -p
     ```
   - Luego ejecuta:
     ```sql
     SOURCE ruta/del/archivo/base_datos.sql;
     ```

3. **Ejecuta la app**:
   - Da doble clic sobre `SIGIC.exe`
   - Se abrirá una ventana en el navegador con la aplicación lista para usar.

📌 Recomendaciones:
- No necesitas internet para usar la app.
- Evita cerrar la consola negra mientras usas la aplicación (es el servidor corriendo).
- Para detenerla, solo cierra esa ventana de consola.

👨‍🔧 ¿Soporte?
Si algo no funciona, revisa que MySQL esté activo o que los puertos no estén bloqueados por firewall.
