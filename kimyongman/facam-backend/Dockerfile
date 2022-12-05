FROM openjdk:11-jre-slim


# Language
ENV LC_ALL=C.UTF-8

# timezone
ENV TZ=Asia/Seoul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR app

COPY ./target/employee-management-backend-0.0.1-SNAPSHOT.jar .
CMD java -jar employee-management-backend-0.0.1-SNAPSHOT.jar
