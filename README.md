# RaidBot

**Información General**

RaidBot es un bot de Discord desarrollado en **Python** utilizando la librería [discord.py](https://github.com/Rapptz/discord.py).  
Su objetivo es automatizar tareas de administración y pruebas en servidores de Discord, ofreciendo comandos que permiten desde gestión básica (latencia, roles, canales) hasta funciones avanzadas como limpieza, reinicio de canales y envío de mensajes masivos.

Este proyecto está pensado con fines **educativos y experimentales**, mostrando cómo se pueden construir comandos personalizados, manejar permisos y trabajar con eventos en Discord.

---

⚙️ **Requisitos**

- Python 3.9 o superior
- Windows

Instálalas con:
```PowerShell
pip install -U discord.py
pip install aiohttp
```
## Explicación de los comandos de RaidBot

RaidBot incluye una serie de comandos diseñados para interactuar con servidores de Discord. Cada uno cumple una función específica:

- **`$hlp`**  
  Muestra un panel de ayuda con la lista completa de comandos disponibles y sus descripciones.

- **`$ping`**  
  Devuelve la latencia del bot en milisegundos, útil para comprobar si está respondiendo correctamente.

- **`$spam`**  
  Envía un número elevado de mensajes repetidos en todos los canales de texto del servidor.

- **`$raid`**  
  Crea múltiples canales de texto con un nombre base. La cantidad se puede personalizar.

- **`$nuke`**  
  Elimina todos los canales del servidor de manera inmediata.

- **`$cn`**  
  Cambia el nombre del servidor por uno nuevo definido en el código.

- **`$cr (cantidad)`**  
  Crea una cantidad determinada de roles en el servidor, con nombres secuenciales.

- **`$ci`**  
  Cambia el ícono del servidor por una imagen que tengas en la misma carpeta del bot.

- **`$ret`**  
  Borra todos los canales existentes y luego crea nuevos canales con spam masivo en cada uno.

- **`$bn`**  
  Banea a todos los miembros del servidor, excepto al autor del comando, al dueño y al propio bot.

- **`$dr`**  
  Elimina todos los roles del servidor, excepto los protegidos (como el rol por defecto, el dueño y el bot).

- **`$ks (ID de servidor)`**  
  Programa la ejecución automática de varios comandos cuando el bot se une a un servidor específico.

- **`$vs (ID de servidor)`**  
  Ejecuta un conjunto de comandos de raid en un servidor remoto, solo si el bot está dentro.

- **`$da (ID de usuario) (ID de servidor)`**  
  Crea un rol con permisos de administrador y lo asigna a un usuario específico en el servidor indicado.

- **`$md`**  
  Envía mensajes directos (DM) a todos los miembros del servidor con un embed predefinido.

- **`$cleanbot (ID de bot)`**  
  Borra mensajes enviados por un bot específico en todos los canales de texto del servidor.

- **`$cleanraid (prefijo)`**  
  Elimina todos los canales cuyo nombre comience con un prefijo determinado, útil para limpiar canales creados en raids.

- **`$resetcanal`**  
  Elimina el canal actual y lo recrea vacío, conservando el mismo nombre y categoría.

- **`$clear`**  
  Borra todos los mensajes del canal actual.

---

RaidBot no solo reúne comandos clásicos de administración y raid.  
Gracias a funciones como `$ks` y `$vs`, el bot puede **Activar automáticamente varios comandos al entrar en un servidor** o **ejecutarlos de forma remota** sin necesidad de intervención directa.  

Esto demuestra cómo un bot puede coordinar múltiples acciones simultáneamente y aprovechar la concurrencia de Python (`asyncio`) para ejecutar cientos de tareas al mismo tiempo sin bloquearse.

---

**Nota importante**:  
Estos comandos son potentes y modifican directamente la estructura del servidor. Se recomienda usarlos únicamente en entornos de prueba o con fines educativos, ya que pueden alterar de forma drástica un servidor real.

Discord Server : https://discord.gg/3NwMRyScs4

