<div align="center">
  <table width="1000px">
    <theader>
      <tr>
        <td><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:50%; height:auto"/></td>
        <th>
          <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AGUSTIN</span><br />
          <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
          <span style="font-weight:bold;">DEPARTAMENTO ACADÉMICO DE INGENIERÍA DE SISTEMAS E INFORMÁTICA</span><br />
          <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
        </th>
        <td><img src="https://github.com/rescobedoq/pw2/blob/main/abet.png?raw=true" alt="ABET" style="width:50%; height:auto"/></td>
      </tr>
    </theader>
    <tbody>
      <tr><td colspan="3"><span style="font-weight:bold;">Formato</span>: Guía de Práctica de Laboratorio</td></tr>
      <tr><td><span style="font-weight:bold;">Aprobación</span>:  2022/03/01</td><td><span style="font-weight:bold;">Código</span>: GUIA-PRLD-001</td><td><span style="font-weight:bold;">Página</span>: 1</td></tr>
    </tbody>
  </table>
</div>

<div align="center">
    <span style="font-weight:bold;">INFORME DE LABORATORIO</span><br />
</div>

<div align="center">
  <table width="1000px">
    <theader>
      <tr><th colspan="6">INFORMACIÓN BÁSICA</th></tr>
    </theader>
    <tbody>
      <tr><td>ASIGNATURA:</td><td colspan="5">Programación Web 02</td></tr>
      <tr><td>TÍTULO DE LA PRÁCTICA:</td><td colspan="5">Python</td></tr>
      <tr><td>NÚMERO DE PRÁCTICA:</td><td>04</td><td>AÑO LECTIVO:</td><td>2023 A</td><td>NRO. SEMESTRE:</td><td width="60px">  III  </td></tr>
      <tr><td>FECHA DE PRESENTACIÓN:</td><td>05/06/2023</td><td>HORA DE PRESENTACIÓN:</td><td colspan="3">23:59</td></tr>
      <tr>
        <td colspan="4">NOMBRE:
          <ul>
            <li>Melsy Melany Huamaní Vargas</li>
          </ul>
        </td>
        <td>NOTA:</td><td></td>
      </tr>
      <tr>
        <td colspan="6" width="1000px">DOCENTES:
          <ul>
            <li>Carlo Jose Luis Corrales Delgado (Teoría)</li>
            <li>Anibal Sardon Paniagua (Laboratorio)</li>
          </ul>
        </td>
      </tr>
    </tbody>
  </table>
</div>


##
## SOLUCIÓN Y RESULTADOS

<br/>

**ENLACE GITHUB Y GIT**

Este trabajo se está presentando en el Github: https://github.com/mhuamanivar/PW2-HuamaniV-Lab04 y el .git es: https://github.com/mhuamanivar/PW2-HuamaniV-Lab04.git.

<br/>

**INSTALACIÓN PARA EL USO DE PYTHON**

Se utiliza el subsistema Ubuntu 22.04.2 LTS a través de WSL (Windows Subsystem for Linux) para usar Python y las herramientas necesarias para su uso en estos ejercicios.<br/><br/>

- Primero se verifica la versión de Python.
  ```shell
  melsy@bonne:~$ python3 --version
  Python 3.10.6
  ```
  <br/>

- Luego actualizamos los paquetes del sistema de Linux.
  ```sh
  melsy@bonne:~$ sudo apt-get update
  [sudo] password for melsy:
  Get:1 http://security.ubuntu.vom.ubuntu jammy-security InRelease [110 kB]
  Hit:2 http://archive.ubuntu.vom.ubuntu jammy InRelease
  Get:3 http://archive.ubuntu.vom.ubuntu jammy-updates InRelease [119 kB]
  Get:4 http://security.ubuntu.vom.ubuntu jammy-security/main amd64 Packages [442 kB]
  (...)
  ```

- Después se instala pip, una herramienta que (también) instala y administra los paquetes de programación que queramos usar en nuestros proyectos de desarrollo.
  ```sh
  melsy@bonne:~$ sudo apt-get install -y python3-pip
  Reading package lists... Done
  Building dependency tree... Done
  Reading state information... Done
  (...)
  ```

- Se instalan paquetes y herramientas de desarrollo que garantizan una configuración sólida para nuestro entorno de programación.
  ```sh
  melsy@bonne:~$ sudo apt-get install build-essential libssl-dev libffi-dev python3-dev
  Reading package lists... Done
  Building dependency tree... Done
  Reading state information... Done
  build-essential is already the newest version (12.9ubuntu3).
  (...)
  ```

- Después, se configura un entorno virtual, los cuales permiten tener un espacio aislado en los proyectos Python y garantizan que puedan tener su propio conjunto de dependencias, como diferentes versiones de los paquetes o varios entornos de programación. En este caso, se usa el módulo venv, que es parte de la biblioteca estándar de Python y se instala de la siguiente forma.
  ```sh
  melsy@bonne:~$ sudo apt install -y python3-venv
  Reading package lists... Done
  Building dependency tree... Done
  Reading state information... Done
  (...)
  ```

- Luego se crea el directorio en donde queremos crear el entorno virtual y se ingresa con "cd".
  ```sh
  melsy@bonne:~$ mkdir -p ~/univ/pw2/lab04/my_env
  melsy@bonne:~$ cd ~/univ/pw2/lab04/my_env
  ```

- En el directorio se crea un entorno virtual ejecutando el siguiente comando.

  ```sh
  melsy@bonne:~/univ/pw2/lab04/my_env$ virtualenv -p python3 .
  created virtual environment CPython3.10.6.final.0-64 in 137ms
    creator CPython3Posix(dest=/home/melsy/univ/pw2/lab04/my_env, clear=False, no_vcs_ignore=False, global=False)
    seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/melsy/.local/share/virtualenv)
      added seed packages: pip==22.0.2, setuptools==59.6.0, wheel==0.37.1
    activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
  melsy@bonne:~/univ/pw2/lab04/my_env$ mkdir -p ~/univ/pw2/lab04/my_env/src
  melsy@bonne:~/univ/pw2/lab04/my_env$ cd ~/univ/pw2/lab04/my_env/src
  ```

- Como no se tiene instalado tree y se quiere ver todos los directorios creados, entonces se instala tree desde el directorio principal del usuario.

  ```sh
  melsy@bonne:~/univ/pw2/lab04/my_env/src$ cd
  melsy@bonne:~$ sudo apt install tree
  Reading package lists... Done
  Building dependency tree... Done
  Reading state information... Done
  The following NEW packages will be installed:
    tree
  0 upgraded, 1 newly installed, 0 to remove and 27 not upgraded.
  ```

- Ahora se puede visualizar qué es lo que sucedió en cada directorio.

  ```sh
  melsy@bonne:~$ cd ~/univ/pw2/lab04/my_env/src
  melsy@bonne:~/univ/pw2/lab04/my_env/src$ tree -L 2 ../
  ../
  ├── bin
  │   ├── activate
  │   ├── activate.csh
  │   ├── activate.fish
  │   ├── activate.nu
  │   ├── activate.ps1
  │   ├── activate_this.py
  │   ├── deactivate.nu
  │   ├── pip
  │   ├── pip3
  │   ├── pip-3.10
  │   ├── pip3
  │   ├── pip3.10
  │   ├── python -> /usr/bin/python3
  │   ├── python3 -> python
  │   ├── python3.10 -> python
  │   ├── wheel
  │   ├── wheel-3.10
  │   ├── wheel3
  │   └── wheel3.10
  ├── lib
  │   └── python3.9
  ├── pyvenv.cfg
  └── src
  
  4 directories, 19 files
  ```

- Ahora se activa el entorno virtual.

  ```sh
  melsy@bonne:~/univ/pw2/lab04/my_env/src$ source ../bin/activate
  (my_env) melsy@bonne:~/univ/pw2/lab04/my_env/src$
  ```

- Se crea un archivo "hello.py" para probar la ejecución de un archivo Python.

  ```sh
  (my_env) melsy@bonne:~/univ/pw2/lab04/my_env/src$ vim hello.py
  ```

- Se edita el archivo "hello.py", colocando lo siguiente.

  ```python
  print("Hello, World!")
  ```

- Se sale de vim con "Esc", luego se escribe ":wq" para guardar y salir del archivo. Luego se ejecuta el archivo Python.

  <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab04/main/imagenes/hello.png" style="width:100%"/><br/><br/>

- Se ve que se ejecutó correctamente. Para desactivar el entorno virtual, se utiliza el siguiente comando.

  ```sh
  (my_env) melsy@bonne:~/univ/pw2/lab04/my_env/src$ deactivate
  melsy@bonne:~/univ/pw2/lab04/my_env/src$
  ```
  <br/><br/>

##
**I. EJERCICIOS RESUELTOS**

Se activa el entorno virtual y se crean los directorios donde trabajaremos los ejercicios resueltos.

```sh
melsy@bonne:~/univ/pw2/lab04/my_env/src$ source ../bin/activate
(my_env) melsy@bonne:~/univ/pw2/lab04/my_env/src$ mkdir resueltos
(my_env) melsy@bonne:~/univ/pw2/lab04/my_env/src$ cd resueltos/
(my_env) melsy@bonne:~/univ/pw2/lab04/my_env/src/resueltos$
```

1. **Determinar si una matriz de tamaño N x N es escalar.**

    - Se crea el archivo "esEscalar.py".

      ```python
      def esEscalar(m):
        d = m[0][0]
        for i in range(len(m)):
            for j in range(len(m)):
                if i != j:
                    if m[i][j] != 0:
                        print(m[i][j])
                        return False
                elif m[i][j] != d:
                    print(m[i][j])
                    return False
        return True
      ```

    - Se crea el archivo "test_esEscalar.py", en el cual importamos el archivo anterior como función.

      ```python
      import esEscalar as fu

      def prueba(M):
          if fu.esEscalar(M):
              print("Si es escalar")
          else:
              print("No es escalar")

      #Z = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
      #Z = [[1, 2, 3], [4, 1, 6], [7, 8, 1]]
      Z = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

      prueba(Z)
      ```

    - Se ejecuta el archivo "test_esEscalar.py" con la matriz de prueba que no está comentada.

      <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab04/main/imagenes/r_escalar.png" style="width:100%"/><br/><br/>

2. **Determinar si una matriz de tamaño N x N es unitaria.**

    - Se crea el archivo "esUnitaria.py".

      ```python
      import esEscalar as fu

      def esUnitaria(m):
          return m[0][0] == 1 and fu.esEscalar(m)
      ```

    - Se crea el archivo "test_esUnitaria.py", en el cual importamos el archivo anterior como función.

      ```python
      import esUnitaria as fu
      
      def prueba(M):
          if fu.esUnitaria(M):
              print("Si es unitaria")
          else:
              print("No es unitaria")
              
      #Z = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
      #Z = [[1, 2, 3], [4, 1, 6], [7, 8, 1]]
      Z = [[2, 0, 0], [0, 2, 0], [0, 0, 2]]
      #Z = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
      
      prueba(Z)
      ```

    - Se ejecuta el archivo "test_esUnitaria.py" con la matriz de prueba que no está comentada.

      <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab04/main/imagenes/r_unitaria.png" style="width:100%"/><br/><br/><br/>

##
**II. EJERCICIOS PROPUESTOS**

En este caso como se estaba trabajando en WSL, no está permitido el uso de gráficos como "pygame", por lo que se trabajó en el sistema principal Windows. Por lo que se crea un nuevo ambiente y lo activamos.

```sh
C:\Users\melsy\Lab04>python -m venv my_env
C:\Users\melsy\Lab04>my_env\Scripts\activate
```
<br/>

Ahora se actualiza el pip de python en Windows.
```sh
(my_env) C:\Users\melsy\Lab04>python.exe -m pip install --upgrade pip
Requirement already satisfied: pip in c:\users\melsy\lab04\my_env\lib\site-packages (22.3.1)
Collecting pip
  Downloading pip-23.1.2-py3-none-any.whl (2.1 MB)
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 848.2 kB/s eta 0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 22.3.1
    Uninstalling pip-22.3.1:
      Successfully uninstalled pip-22.3.1
Successfully installed pip-23.1.2
```
<br/>

Posteriormente se instala pygame para mostrar los gráficos.
```sh
(my_env) C:\Users\melsy\Lab04>pip3 install pygame
Collecting pygame
  Downloading pygame-2.4.0-cp311-cp311-win_amd64.whl (10.6 MB)
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.6/10.6 MB 531.0 kB/s eta 0:00:00
Installing collected packages: pygame
Successfully installed pygame-2.4.0
```
<br/>

Luego se ingresa a una carpeta ya creada llamada "propuestos", donde (como dice el nombre) se guardarán todos los ejercicios propuestos.
```sh
(my_env) C:\Users\melsy\Lab04>cd my_env\Scripts\propuestos
(my_env) C:\Users\melsy\Lab04\my_env\Scripts\propuestos>
```
<br/>

1. **Implementar los métodos de la clase Picture.**
  <br/><br/>
  Una vez guardados los archivos dados por el profesor se deben realizar pruebas para realizar los métodos que son dados en este primer ejercicio propuesto.
    ```sh
    (my_env) C:\Users\melsy\Lab04\my_env\Scripts\propuestos>python
    Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from chessPictures import *
    >>> from interpreter import draw
    pygame 2.4.0 (SDL 2.26.4, Python 3.11.1)
    Hello from the pygame community. https://www.pygame.org/contribute.html
    ```
    Ahora se realizan los métodos a continuación:<br/><br/>
    - **verticalMirror:** Devuelve el espejo vertical de la imagen
    
      Se crea un arreglo vacío "vertical" en donde se colcoa poco a poco cada valor del arreglo de la imagen dada, de manera que cada string parte de ese arreglo se invierta utilizando ``[::-1]``, de esta manera como cada elemento se está inviertando se obtiene un resultado en forma de reflejo vertical de la imagen. 
      ```python
      def verticalMirror(self):
          vertical = []
          for value in self.img:
              vertical.append(value[::-1])
          return Picture(vertical)
      ```
        - Para probar utilizamos el siguiente comando
          ```sh
          >>> draw(knight)
          ```
          <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab04/main/imagenes/p_vertical1.png" style="width:50%"/><br/><br/>
        - Luego comparamos al utilizar el siguiente comando, para ver que funcionó correctamente
          ```sh
          >>> draw(knight.verticalMirror())
          ```
          <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab04/main/imagenes/p_vertical2.png" style="width:50%"/><br/><br/>

      <br/>
    - **horizontalMirror:** Devuelve el espejo horizontal de la imagen
      
      Se crea un arreglo vacío "horizontal" en el cual se almacena el arreglo invertido del atributo ``img`` del picture, se esta manera se obtiene un espejo horizontal de la figura, de la misma forma que el anterior para invertir el arreglo se utiliza ``[::-1]``.
      ```python
      def horizontalMirror(self):
          horizontal = self.img[::-1]
          return Picture(horizontal)
      ```
        - Para probar utilizamos el siguiente comando
          ```sh
          >>> draw(rock)
          ```
          <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab04/main/imagenes/p_horizontal1.png" style="width:50%"/><br/><br/>
        - Luego comparamos al utilizar el siguiente comando, para ver que funcionó correctamente
          ```sh
          >>> draw(rock.horizontalMirror())
          ```
          <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab04/main/imagenes/p_horizontal2.png" style="width:50%"/><br/><br/>

      <br/>
    - **negative:** Devuelve un negativo de la imagen

      Se crea un nuevo arreglo "negative", el cual por cada valor del arreglo del atributo ``img`` del picture, se invertira los colores (un caracter por otro caracter) al utilizar el método ``_invColor()``, luego se unen utilizando el método ``join()`` a un solo string y se devuelve como un nuevo elemento del nuevo arreglo creado.
      ```python
      def negative(self):
          negative = []
          for value in self.img:
              invertedColor = "".join([self._invColor(c) for c in value])
              negative.append(invertedColor)
          return Picture(negative)
      ```
        - Para probar utilizamos el siguiente comando
          ```sh
          >>> draw(queen)
          ```
          <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab04/main/imagenes/p_negative1.png" style="width:50%"/><br/><br/>
        - Luego comparamos al utilizar el siguiente comando, para ver que funcionó correctamente
          ```sh
          >>> draw(queen.negative())
          ```
          <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab04/main/imagenes/p_negative2.png" style="width:50%"/><br/><br/>

      <br/>
    - **join:** Devuelve una nueva figura poniendo la figura del argumento al lado derecho de la figura actual

      Se crea un nuevo arreglo "joined" el cual for cada elemento del arreglo del atributo ``img`` del picture actual se agrega el elemento con el mismo índice del arreglo del atributo ``img`` del picture "p", de esta manera forman un nuevo arreglo que será almacenado en "joined".
      ```python
      def join(self, p):
          joined = []
          for i in range(len(self.img)):
              joined.append(self.img[i]+p.img[i])
          return Picture(joined)
      ```
        - Para probar utilizamos el siguiente comando
          ```sh
          >>> draw(king)
          ```
          <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab04/main/imagenes/p_join1.png" style="width:50%"/><br/><br/>
        - Luego comparamos al utilizar el siguiente comando, para ver que funcionó correctamente
          ```sh
          >>> draw(king.join(queen))
          ```
          <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab04/main/imagenes/p_join2.png" style="width:50%"/><br/><br/>

      <br/>
    - **up:** Devuelve una nueva figura poniendo la figura recibida como argumento, encima de la figura actual

      Se crea un nuevo arreglo "newFigure" que almacena el arreglo del atributo ``img`` del picture que es recibido como argumento "p", luego se le va añadiendo cada elemento del arreglo ``img`` del picture actual, para que en "newFigure", el picture "p" se muestre encima del picture actual.
      ```python
      def up(self, p):
          newFigure = p.img[:]
          for value in self.img:
              newFigure.append(value)
          return Picture(newFigure)
      ```
        - Para probar utilizamos el siguiente comando
          ```sh
          >>> draw(bishop)
          ```
          <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab04/main/imagenes/p_up1.png" style="width:50%"/><br/><br/>
        - Luego comparamos al utilizar el siguiente comando, para ver que funcionó correctamente
          ```sh
          >>> draw(bishop.up(pawn))
          ```
          <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab04/main/imagenes/p_up2.png" style="width:50%"/><br/><br/>

      <br/>
    - **under:** Devuelve una nueva figura poniendo la figura recibida como argumento, sobre la figura actual

      Se crean las variables "filas" y "columnas" que almacena el valor de ellas usando el método ``range()`` que depende del arreglo. Luego se crea un nuevo arreglo "newFigure", el cual recorrerá por las filas y columnas, de esta manera cuando el caracter colocado del picture actual sea diferente al caracter colocado del picture "p", y cuando en el picture "p" no sea vacío, entonces se priorizará colocar el caracter del picture "p", de lo contrario se colocará el caracter del picture actual.
      ```python
      def under(self, p):
        filas = range(len(self.img))
        columnas = range(len(self.img[0]))

        newFigure = []
        for i in filas:
            string = ""
            for j in columnas:
                if (self.img[i][j] != p.img[i][j] and p.img[i][j] != " "):
                    string += p.img[i][j]
                else:
                    string += self.img[i][j]
            newFigure.append(string)
        return Picture(newFigure)
      ```
        - Para probar utilizamos el siguiente comando
          ```sh
          >>> draw(square)
          ```
          <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab04/main/imagenes/p_under1.png" style="width:50%"/><br/><br/>
        - Luego comparamos al utilizar el siguiente comando, para ver que funcionó correctamente
          ```sh
          >>> draw(square.under(knight))
          ```
          <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab04/main/imagenes/p_under2.png" style="width:50%"/><br/><br/>

      <br/>
    - **horizontalRepeat:** Devuelve una nueva figura repitiendo la figura actual al costado la cantidad de veces que indique el valor de "n"

      Se crea un nuevo arreglo, el cual va almacenando los elementos del arreglo del atributo ``img`` del pciture, y los va multiplicando la cantidad "n" introducida, de tal manera que al final se vea de manera repetida horizontalmente la misma figura.
      ```python
      def horizontalRepeat(self, n):
          newFigure = []
          for value in self.img:
              newFigure.append(value*n)
          return Picture(newFigure)
      ```
        - Para probar utilizamos el siguiente comando
          ```sh
          >>> draw(rock)
          ```
          <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab04/main/imagenes/p_horizontalr1.png" style="width:50%"/><br/><br/>
        - Luego comparamos al utilizar el siguiente comando, para ver que funcionó correctamente
          ```sh
          >>> draw(rock.horizontalRepeat(5))
          ```
          <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab04/main/imagenes/p_horizontalr2.png" style="width:50%"/><br/><br/>

      <br/>
    - **verticalRepeat:** Devuelve una nueva figura repitiendo la figura actual debajo, la cantidad de veces que indique el valor de "n"

      Se crea un nuevo arreglo donde multiplica todo el arreglo del atributo ``img`` del picture, es por ello que en el resultado se ve de manera repetida verticalmente.
      ```python
      def verticalRepeat(self, n):
          newFigure = self.img[:] * n
          return Picture(newFigure)
      ```
        - Para probar utilizamos el siguiente comando
          ```sh
          >>> draw(king)
          ```
          <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab04/main/imagenes/p_verticalr1.png" style="width:50%"/><br/><br/>
        - Luego comparamos al utilizar el siguiente comando, para ver que funcionó correctamente
          ```sh
          >>> draw(king.verticalRepeat(2))
          ```
          <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab04/main/imagenes/p_verticalr2.png" style="width:50%"/><br/><br/>

      <br/>
    - **rotate (Extra):** Devuelve una figura rotada en 90 grados

      De la misma forma que en la función ``under()`` se obtienen las filas y columnas. Luego se crea un nuevo arreglo "newFigure", en el cual se irá almacenando el valor correspondiente de las columnas, pero para que vaya rotando entonces colocamos el índice de las filas de manera "-i", para obtener el orden inverso solamente de la fila.
      ```python
      def rotate(self):
          """Devuelve una figura rotada en 90 grados """
          filas = range(len(self.img))
          columnas = range(len(self.img[0]))

          newFigure = []
          for i in filas:
              string = ""
              for j in columnas:
                  string += self.img[j][-i]
              newFigure.append(string)
          return Picture(newFigure)
      ```
        - Para probar utilizamos el siguiente comando
          ```sh
          >>> draw(knight)
          ```
          <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab04/main/imagenes/p_rotate1.png" style="width:50%"/><br/><br/>
        - Luego comparamos al utilizar el siguiente comando, para ver que funcionó correctamente
          ```sh
          >>> draw(knight.rotate())
          ```
          <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab04/main/imagenes/p_rotate2.png" style="width:50%"/><br/><br/>

      <br/>

2. **Usando únicamente los métodos de los objetos de la clase Picture dibujar las siguientes figuras.**
  <br/><br/>
  Se sale de "python" con ``exit()``, pero continuamos en el entorno virtual para probar los ejercicios y demostrar que cumplen de acuerdo a las imágenes pedidas.
  <br/><br/>
    - **Se crea el archivo "Ejercicio2a.py"**

      Utilizando las funciones creadas anteriormente, se contruye de acuerdo a la imagen dada en el laboratorio.
      ```python
      # Melsy Melany Huamaní Vargas
      # Pw2 - Laboratorio 04

      from interpreter import draw
      from chessPictures import *

      wKnight = knight
      bKnight = knight.negative()

      firstKnights = wKnight.join(bKnight)
      secondKnights = bKnight.join(wKnight)

      draw(secondKnights.up(firstKnights))
      ```
        - Se ejecuta de la siguiente manera.
          ```sh
          (my_env) C:\Users\melsy\Lab04\my_env\Scripts\propuestos>python Ejercicio2a.py
          pygame 2.4.0 (SDL 2.26.4, Python 3.11.1)
          Hello from the pygame community. https://www.pygame.org/contribute.html
          ```
          <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab04/main/imagenes/p_ej2a.png" style="width:50%"/><br/><br/>

      <br/>
    - **Se crea el archivo "Ejercicio2b.py"**

      Utilizando las funciones creadas anteriormente, se contruye de acuerdo a la imagen dada en el laboratorio.
      ```python
      # Melsy Melany Huamaní Vargas
      # Pw2 - Laboratorio 04

      from interpreter import draw
      from chessPictures import *

      wKnight = knight
      bKnight = knight.negative()

      firstKnights = wKnight.join(bKnight)
      secondKnights = firstKnights.verticalMirror()

      draw(secondKnights.up(firstKnights))
      ```
        - Se ejecuta de la siguiente manera.
          ```sh
          (my_env) C:\Users\melsy\Lab04\my_env\Scripts\propuestos>python Ejercicio2b.py
          pygame 2.4.0 (SDL 2.26.4, Python 3.11.1)
          Hello from the pygame community. https://www.pygame.org/contribute.html
          ```
          <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab04/main/imagenes/p_ej2b.png" style="width:50%"/><br/><br/>

      <br/>
    - **Se crea el archivo "Ejercicio2c.py"**

      Utilizando las funciones creadas anteriormente, se contruye de acuerdo a la imagen dada en el laboratorio.
      ```python
      # Melsy Melany Huamaní Vargas
      # Pw2 - Laboratorio 04

      from interpreter import draw
      from chessPictures import *

      draw(queen.horizontalRepeat(4))
      ```
        - Se ejecuta de la siguiente manera.
          ```sh
          (my_env) C:\Users\melsy\Lab04\my_env\Scripts\propuestos>python Ejercicio2c.py
          pygame 2.4.0 (SDL 2.26.4, Python 3.11.1)
          Hello from the pygame community. https://www.pygame.org/contribute.html
          ```
          <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab04/main/imagenes/p_ej2c.png" style="width:50%"/><br/><br/>

      <br/>
    - **Se crea el archivo "Ejercicio2d.py"**

      Utilizando las funciones creadas anteriormente, se contruye de acuerdo a la imagen dada en el laboratorio.
      ```python
      # Melsy Melany Huamaní Vargas
      # Pw2 - Laboratorio 04

      from interpreter import draw
      from chessPictures import *

      squares = square.join(square.negative())

      draw(squares.horizontalRepeat(4))
      ```
        - Se ejecuta de la siguiente manera.
          ```sh
          (my_env) C:\Users\melsy\Lab04\my_env\Scripts\propuestos>python Ejercicio2d.py
          pygame 2.4.0 (SDL 2.26.4, Python 3.11.1)
          Hello from the pygame community. https://www.pygame.org/contribute.html
          ```
          <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab04/main/imagenes/p_ej2d.png" style="width:50%"/><br/><br/>

      <br/>
    - **Se crea el archivo "Ejercicio2e.py"**

      Utilizando las funciones creadas anteriormente, se contruye de acuerdo a la imagen dada en el laboratorio.
      ```python
      # Melsy Melany Huamaní Vargas
      # Pw2 - Laboratorio 04

      from interpreter import draw
      from chessPictures import *

      squares = square.negative().join(square)

      draw(squares.horizontalRepeat(4))
      ```
        - Se ejecuta de la siguiente manera.
          ```sh
          (my_env) C:\Users\melsy\Lab04\my_env\Scripts\propuestos>python Ejercicio2e.py
          pygame 2.4.0 (SDL 2.26.4, Python 3.11.1)
          Hello from the pygame community. https://www.pygame.org/contribute.html
          ```
          <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab04/main/imagenes/p_ej2e.png" style="width:50%"/><br/><br/>

      <br/>
    - **Se crea el archivo "Ejercicio2f.py".**

      Utilizando las funciones creadas anteriormente, se contruye de acuerdo a la imagen dada en el laboratorio.
      ```python
      # Melsy Melany Huamaní Vargas
      # Pw2 - Laboratorio 04

      from interpreter import draw
      from chessPictures import *

      squares1 = square.negative().up(square)
      squares2 = square.up(square.negative())

      finalSquares = squares1.join(squares2)

      draw(finalSquares.verticalRepeat(2).horizontalRepeat(4))
      ```
        - Se ejecuta de la siguiente manera.
          ```sh
          (my_env) C:\Users\melsy\Lab04\my_env\Scripts\propuestos>python Ejercicio2f.py
          pygame 2.4.0 (SDL 2.26.4, Python 3.11.1)
          Hello from the pygame community. https://www.pygame.org/contribute.html
          ```
          <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab04/main/imagenes/p_ej2f.png" style="width:50%"/><br/><br/>

      <br/>
    - **Se crea el archivo "Ejercicio2g.py"**

      Utilizando las funciones creadas anteriormente, se contruye de acuerdo a la imagen dada en el laboratorio.
      ```python
      # Melsy Melany Huamaní Vargas
      # Pw2 - Laboratorio 04

      from interpreter import draw
      from chessPictures import *

      wSquare = square
      bSquare = square.negative()

      wPawns = wSquare.under(pawn).join(bSquare.under(pawn)).horizontalRepeat(4)
      bPawns = wPawns.negative()

      wPieces = bSquare.under(rock).join(wSquare.under(knight)).join(bSquare.under(bishop)).join(wSquare.under(queen)).join(bSquare.under(king)).join(wSquare.under(bishop)).join(bSquare.under(knight)).join(wSquare.under(rock))
      bPieces = wPieces.negative()

      squares1 = bSquare.up(wSquare)
      squares2 = wSquare.up(bSquare)

      finalSquares = squares1.join(squares2).verticalRepeat(2).horizontalRepeat(4)

      draw(wPieces.up(wPawns.up(finalSquares.up(bPawns.up(bPieces)))))
      ```
        - Se ejecuta de la siguiente manera.
          ```sh
          (my_env) C:\Users\melsy\Lab04\my_env\Scripts\propuestos>python Ejercicio2g.py
          pygame 2.4.0 (SDL 2.26.4, Python 3.11.1)
          Hello from the pygame community. https://www.pygame.org/contribute.html
          ```
          <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab04/main/imagenes/p_ej2g.png" style="width:50%"/><br/><br/>

    - **Se crea el archivo "PruebaRotate.py"**

      Este es una figura extra que se creo en base a "Ejercicio2g.py", pero que se muestra el tablero de manera que ha rotado 90 grados.
      ```python
      # Melsy Melany Huamaní Vargas
      # Pw2 - Laboratorio 04

      from interpreter import draw
      from chessPictures import *

      wSquare = square
      bSquare = square.negative()

      wPawns = wSquare.under(pawn).join(bSquare.under(pawn)).horizontalRepeat(4)
      bPawns = wPawns.negative()

      wPieces = bSquare.under(rock).join(wSquare.under(knight)).join(bSquare.under(bishop)).join(wSquare.under(queen)).join(bSquare.under(king)).join(wSquare.under(bishop)).join(bSquare.under(knight)).join(wSquare.under(rock))
      bPieces = wPieces.negative()

      squares1 = bSquare.up(wSquare)
      squares2 = wSquare.up(bSquare)

      finalSquares = squares1.join(squares2).verticalRepeat(2).horizontalRepeat(4)

      tabla = wPieces.up(wPawns.up(finalSquares.up(bPawns.up(bPieces))))

      draw(tabla.rotate())
      ```
        - Se ejecuta de la siguiente manera.
          ```sh
          (my_env) C:\Users\melsy\Lab04\my_env\Scripts\propuestos>python PruebaRotate.py
          pygame 2.4.0 (SDL 2.26.4, Python 3.11.1)
          Hello from the pygame community. https://www.pygame.org/contribute.html
          ```
          <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab04/main/imagenes/p_ej2extra.png" style="width:50%"/><br/><br/>


##
## COMMITS MÁS IMPORTANTES

<br/>

<img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab04/main/imagenes/commits.png" style="width:70%"/><br/><br/>

##
## CUESTIONARIO

- **¿Qué son los archivos ``.pyc``?**

  Son los archivos compilados de Python, es una versión de un módulo que ya ha sido compilado en bytes con éxito. Sin embargo, si la compilación falla, entonces el archivo ``.pyc`` sera reconocido como inválido. En los archivos ``.pyc`` se deben tener en cuenta ciertas características:
  
    - Cuando el intérprete de Python es invocado con flag ``-o``, entonces los archivos que son compilados son optimizados y eliminan datos no importantes, por lo que ya no son ``.pyc``, sino que son ``.pyo``.
    - El programa no compila más rápido si es que ejecutar los ``.pyc``, lo único en lo que son rápidos es la velocidad con la que se cargan.
    - Es posible que existan archivos ``.pyc``, sin la necesidad de haber modulos con el nombre que tiene el ``.pyc``, esto puede usarse para distribuir una librería de Python.
    - El módulo ``compile all`` puede crear archivos ``.pyc`` para todos los módulos de un directorio.
    - Python verifica la fecha de modificación del código con la versión compilada para ver si está desactualizada y necesita ser recompilado, ya que en los archivos ``.pyc`` se puede visualizar la versión con la que ha sido compilado el módulo.

  <br/>
- **¿Para qué sirve el directorio pycache?**

  El directorio ``__pycache__`` sirve para acelerar la carga de módulos, puesto que Python almacena en caché la versión compilada de cada módulo bajo el nombre de ``nombre_de_modulo.version.pyc``, donde se muestra la versión del formato con el que se ha compilado el archivo, el cual generalmente es el número de versíon de Python. No se recomienda borrar a menudo estos archivos ni suprimir la creación de estos ya que como han sido compilados, se estaría restando a su función principal que es acelerar el proceso de la carga de módulos.

  <br/>
- **¿Cuáles son los usos y lo que representa el subguión en Python?**

  El subguión tiene una gran variedad de usos en Python, además de una representación cuando se habla de atributos o métodos de una clase. Entre ellos tenemos:

    - Para omitir valores: Es decir, podemos usarlo como una variable ``_`` la cual solo la utilizaremos una vez, por ejemplo, en las iteraciones del ``for``. Por otro lado, cuando tenemos muchos valores y queremos seleccionar solo unos cuantos e ignorar un rango de ellos, entonces podemos utilizar ``*_``.
    - Como placeholder: Esto quiere decir que cuando nos encontremos en el intérprete de Python podemos guardar la anterior respuesta para utilizarla en una siguiente operación.
    - Como namespace: Cuando queremos utilizar un nombre para una variable, pero esta ya es una palabra reservada para Python, entonces podemos utilzar ``_`` al final del nombre de la palabra.
    - Para números: Podemos utilizar ``_`` para expresar números muy grandes, y queremos separar cada tres cifrar para un mejor entendimiento.
    - Representación en clases: Cuando utilizamos ``_`` dos veces antes y después del nombre de un atributo, de manera ``__nombre_de_atributo__``, entonces esto representa un atributo privado de la clase. Por otro lado, para los métodos, al utilizar de la siguiente manera ``__nombre_del_metodo__`` quiere decir que estos son métodos que se pueden sobreescribir facilmente en las clases que heredan, siendo esta usada en la clase padre.

  <br/>

<br/>

##
## REFERENCIAS

- https://www.w3schools.com/python/python_reference.asp
- https://docs.python.org/3/tutorial/
- https://docs.python.org/release/1.5.1p1/tut/node43.html
- https://docs.python.org/3/tutorial/modules.html
- https://pywombat.com/articles/guion-bajo-python
