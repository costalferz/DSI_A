## micro webserver
Dockerfile build Express.js
Please check comment in the Dockefile

### 1.build an image
create a new image locally and name it as ```week03``` and tag ```1.1``` using the Dockerfile in current directory (. means current directory)
```bash
$cd demo4
$docker build -t 2023_dsi321:1.1 .
```

### 2.run container from image
start a container from the image. 
```bash
$docker run -it --rm -p 8000:5000 week03:1.1
```
* ```-it``` is interactive mode.
* ```--rm``` is remove container when process stop.
* ```-p 8000:5000``` forward host port 8000 to container port 5000

### 3. check result in browser
* go to http://localhost:8000/ you should see "Hello World"
* go to http://localhost:8000/date you should see datetime in JSON format as following
```json
{
  "day": 24,
  "month": 1,
  "weekday": 1,
  "year": 2023
}
``` 
