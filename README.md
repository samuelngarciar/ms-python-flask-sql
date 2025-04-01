# ms-python-flask-sql

This project is a Proof of concept that allow tech of simple way how can be organized a microservice and how to access to system table from Microsoft SQL 2019
The main idea here is show the basic structure and test the basic flow of commnication between the components of the solution even this can be use as base for other projects

Note. You can to compare this with other similar project here called "ms-python-fastapi-sql"
Technical aspects follows:

1. Distribution reponsability in layers (models, repository, service and apis)
2. Two modes of manage the mapping from the response of data base to objects, using models and without it.
3. Basic autentication
4. Method for test the health service

## Setup database container 
docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=YourPassword01-' -p 1433:1433 --name sqlserver4 -d mcr.microsoft.com/mssql/server:2019-latest
![image](https://github.com/user-attachments/assets/9061078a-889c-4add-9746-f9a157da5deb)

### Check the container is running up ok
docker ps
![image](https://github.com/user-attachments/assets/aaa00c9d-72e4-4c6d-9da2-59a5123ca3d6)

### Clone this repository and build the image docker
docker build --no-cache -t ms-python-flask-sql .
![image](https://github.com/user-attachments/assets/812aaabc-4c61-4fcc-98ad-a0bb73b1280f)


### Check if the image was generated ok
docker images
![image](https://github.com/user-attachments/assets/f61c0528-c649-4ca4-b271-9f49e5f008ad)


### Start up the microservice
docker run --net=host -p 5000:5000 --name mymicroservice ms-python-flask-sql
![image](https://github.com/user-attachments/assets/5d00cb20-71d3-49c1-b943-306cb7f432c1)

Note. that the service show the IP address of the machine local where is the db previously started
![image](https://github.com/user-attachments/assets/96e032a5-0217-4d58-bf33-deb6186c09e4)

### In other terminal session execute the follows test

## Tests
### Test case 1 - Service is up and health
curl -v "http://127.0.0.1:5000/health"
![image](https://github.com/user-attachments/assets/27837a26-e10a-4a93-b883-55d0c56012f7)

### Test case 2 - Access sysobjects table is a operation with mapping simple and time consumed
time curl -v "http://127.0.0.1:5000/sysobjects"
![image](https://github.com/user-attachments/assets/affba760-aee4-4fe4-a93f-ccf67ca9b1f0)

Time consumed
![image](https://github.com/user-attachments/assets/b38a7763-bf6b-446c-bc8e-19aecc48dfaf)

### Test case 3 - Access sysobjects table is a operation with mapping using models and time consumed
![image](https://github.com/user-attachments/assets/fa169fb5-d705-4192-8150-9fbd7d619160)

Time consumed
![image](https://github.com/user-attachments/assets/472d8e21-6fa4-4d0d-9a66-1c49e8d9afbb)

### Test case 4 - Access sysobjects table is a operation with mapping simple and pagination with limit 3 and offset 10 and time consumed
time curl -v "http://127.0.0.1:5000/sysobjects?limit=3&offset=10"
![image](https://github.com/user-attachments/assets/0edbc472-03c6-4b9c-a7d6-1128d75031a2)

### Test case 5 - Access sysobjects table is a operation with mapping using models and pagination with limit 3 and offset 10 and time consumed
time curl -v "http://127.0.0.1:5000/sysobjects?limit=3&offset=10"
![image](https://github.com/user-attachments/assets/b5139e85-68f1-48e6-b195-0fb5135bd898)


### Test case 6 - (Secure version without credentials) Access sysobjects table is a operation with mapping simple and pagination with limit 3 and offset 10 and time consumed
time curl -v "http://127.0.0.1:5000/protected/sysobjects?limit=3&offset=10"
![image](https://github.com/user-attachments/assets/f0638963-5a28-4996-8bca-b2065cafa43a)


### Test case 7 - (Secure version with credentials) Access sysobjects table is a operation with mapping simple and pagination with limit 3 and offset 10 and time consumed
time curl -v -u test:password "http://127.0.0.1:5000/protected/sysobjects?limit=3&offset=10"
![image](https://github.com/user-attachments/assets/99935985-5319-4858-8877-653c02e92284)

### Container traces
![image](https://github.com/user-attachments/assets/21866ae4-356d-4a3a-b8a9-cfd036c0bff0)










