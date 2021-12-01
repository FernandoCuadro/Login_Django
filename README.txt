Login con Docker funcionando

################################################################################################

											MODO: FULL INTERESADO

	Paso 0: sudo chown -R $USER:$USER .
	Paso 1: sudo yum -y install python3-devel mysql-devel
	Paso 2: sudo docker-compose build
	Paso 3: docker run -d -p 33060:3306 --name mysql-db -e MYSQL_ROOT_PASSWORD=secret mysql
	Paso 4: docker exec -it mysql-db mysql -p # Cuando pida la contraseña colocamos "secret"
	Paso 5: create database loginDB; # Creamos la base de datos
	Paso 6: exit # Salimos de MySQL
	Paso 7: docker-compose up -d
	Paso 8: docker-compose up # Esperamos y dejamos que finalice el proceso
	Paso 9: Ctrl+C # Detenemos los contenedores
	Paso 10: docker-compose run web python manage.py migrate
	Paso 11: docker-compose up -d
	Paso 12: docker-compose up
	Paso 13: Ingresamos desde un navegador a la maquina que esta corriendo docker
			 y colocamos el puerto 8000                
								  
################################################################################################	
