# OBSERVATIONS.md

## 1. Image Size
The nginx:alpine image is relatively small compared to other images. This is because it is based on Alpine Linux, which is a very lightweight operating system designed to keep Docker images minimal.

---

## 2. Image Layers
The image has multiple layers. Each layer represents a step in building the image, such as adding system files or installing nginx. The largest layers usually contain the base operating system and the main nginx installation.

---

## 3. Operating System and Architecture
From the docker inspect command:
- Operating System: Linux
- Architecture: amd64

This means the container runs on a Linux-based system and is built for 64-bit systems.

---

## 4. Port Mapping Explanation
The port mapping `-p 8080:80` means that port 8080 on my computer is connected to port 80 inside the container.

So when I go to `http://localhost:8080`, the request is forwarded to the nginx server running inside the container on port 80.

If I used `-p 9090:80`, then I would need to access the server using `http://localhost:9090` instead.

---

## 5. What Surprised Me
What surprised me the most is how easy it is to run a web server using Docker. With just one command, nginx was running and accessible in the browser. Also, containers are temporary and can be removed quickly, which makes testing and development much easier.