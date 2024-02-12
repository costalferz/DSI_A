## micro webserver
Docker Compose build Express.js and Redis

### 1.build an image
create a new image locally and name it as ```week04``` and tag ```1.1``` using the Dockerfile in current directory (. means current directory)
```bash
$docker-compose build -t week04:1.1 .
```

### 2.run container from image
start a container from the image. 
```bash
$docker-compose up -d run
```

### 3. check result in browser
* go to http://localhost:81/ you should see "Hello World"
* go to http://localhost:81/redis you should see `Hello World! I have been seen count times.`
