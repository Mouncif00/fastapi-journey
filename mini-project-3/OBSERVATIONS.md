# Observations — Mini Project 3

## 1. Pod vs Deployment


a pod is used to run the application and it is a single instance of a container in kubernetes 
a deployment is like a manager for pods it can create them restart or make more of them 
i used deployment because i had to scale up the number of replicas to 3 and a pod alone cant do that 

## 2. ConfigMap usage

the config map is used to store stuff like the url of mongodb connection 

instead of putting the url of the database inside the application or the deployment file , it is stored seperatly , this makes it easy to modify 

the web application reads the url from the configmap

## 3. Scaling behavior

when i scaled the web app from 1 to 3 kubernetes didnt replace the original pod 
instead it created 2 addditional pods 

## 4. MongoDB failure scenario

if the mongodb pod craches it will be automatically restarted by kubernetes because its managed by a deployment , this means  the app will recover after a possible downtime 


## 5. Personal reflection
everything went smoothly , other that the github stuff 