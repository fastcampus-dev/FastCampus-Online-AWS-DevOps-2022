# node base image 설치
FROM node:16-slim
# 기본 디렉토리 지정
WORKDIR /usr/src/app
# 소스 복사
COPY . .
# 패키지 설치 (강의 영상 > http-server 설치로 변경, 수정하지 말 것)
RUN npm install http-server -g
# Listen 포트 정의
EXPOSE 8080
# 서버 기동 (강의 영상 > npm start에서 변경, 수정하지 말 것)
CMD ["http-server", "./dist"]