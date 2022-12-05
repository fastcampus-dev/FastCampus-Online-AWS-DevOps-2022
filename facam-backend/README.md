# backend

### JDK Version
- jDK 11 이상

### Modify with your MySQL info 
`path` : src/main/resources/config/application.properties
```
spring.datasource.url=jdbc:mysql://YOUR_MYSQL_URL/employee?serverTimezone=UTC&useSSL=false&allowPublicKeyRetrieval=true
spring.datasource.username=
spring.datasource.password=
spring.jpa.hibernate.ddl-auto=update
```

### docker mysql insatll
```
docker pull mysql:8.0.22 --platform linux/amd64
docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=12345 --name mysql-db mysql:8.0.22

docker exec -it mysql-db bash

## (optional) 
# apt-get update 
# apt-get install -y vim
# vi /etc/mysql/my.cnf
```
### MySQL DB
- Create DB Name : employee
- (생성할 필요 없음) Create Table : employee
- (생성할 필요 없음) Columns : id, email_address, first_name, last_name

```
create database employee;
show databases;
GRANT ALL PRIVILEGES ON employee.* TO root@localhost;
flush privileges;
```

### maven build
```
mvn clean
mvn package
```

### java 
```
java -jar employee-management-backend-0.0.1-SNAPSHOT.jar
```

### docker build and running

```
docker build -t backend .

## Mac m1 에서는 이렇게 실행
docker buildx build --platform linux/amd64 -t bakcend .

docker run --net="host" -p 8080:8080 app:0.1 
## 이 도커안에는 mysql이 없으니까 host network를 사용하도록 설정
## 도커끼리 통신할 수 있도록 하고 DB url설정 변경필요
``` 
