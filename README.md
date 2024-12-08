#primer paso
ejecutar docker desktop

#ejecutar los siguientes comandos estando desde la carpeta backend
docker build -f microservices/nlp_service/Dockerfile -t nlp_service .
docker build -f microservices/cover_letter_service/Dockerfile -t cover_letter_service .
docker build -f microservices/matching_service/Dockerfile -t matching_service .

#ejecutar el siguiente comando
docker images

#ejecutar comandos para inicializar contenedores
docker run -d -p 8001:8001 --name nlp_service nlp_service
docker run -d -p 8002:8002 --name cover_letter_service cover_letter_service
docker run -d -p 8003:8003 --name matching_service matching_service

#opcionales (para inicializar contenedores)
docker run -d -p 8001:8001 nlp_service
docker run -d -p 8002:8002 cover_letter_service
docker run -d -p 8003:8003 matching_service

#verificar si los contenedores estan funcionando
docker ps

#detenedor contenedores
docker stop nlp_service
docker stop cover_letter_service
docker stop matching_service

#eliminar contenedores
docker rm nlp_service
docker rm cover_letter_service
docker rm matching_service
