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

**INSTALACIÓN PARA EL USO DE PYTHON**

Se utiliza el subsistema Ubuntu 22.04.2 LTS a través de WSL (Windows Subsystem for Linux) para usar Python y las herramientas necesarias para su uso en estos ejercicios.

- Primero se verifica la versión de Python.
  ```sh
  melsy@bonne:~$ python3 --version
  Python 3.10.6
  ```

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

  ![Ejecución de hello.py](a)

- Se ve que se ejecutó correctamente. Para desactivar el entorno virtual, se utiliza el siguiente comando.

  ```sh
  (my_env) melsy@bonne:~/univ/pw2/lab04/my_env/src$ deactivate
  melsy@bonne:~/univ/pw2/lab04/my_env/src$
  ```

##
**I. EJERCICIOS RESUELTOS**

Se activa el entorno virtual y se crean los directorios donde trabajaremos los ejercicios resueltos.

```sh
melsy@bonne:~/univ/pw2/lab04/my_env/src$ source ../bin/activate
(my_env) melsy@bonne:~/univ/pw2/lab04/my_env/src$ mkdir resueltos
(my_env) melsy@bonne:~/univ/pw2/lab04/my_env/src$ cd resueltos/
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

  ![Ejecución de test_esEscalar.py](a)

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

  ![Ejecución de test_esUnitaria.py](a)
