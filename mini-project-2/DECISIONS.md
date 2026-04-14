# Part B — Docker Decisions

## 1. Why does DATABASE_URL use "mongo" instead of "localhost"?

In Docker, each service runs in its own container. If I use "localhost", the app container will try to connect to itself instead of the MongoDB container, which causes a connection error. 

Using "mongo" works because it is the service name defined in docker-compose, and Docker automatically allows containers to communicate using these names.


## 2. What does depends_on do? Does it guarantee MongoDB is ready?

The depends_on option ensures that the MongoDB container starts before the FastAPI app. However, it does not guarantee that MongoDB is fully ready to accept connections.

In my testing, I noticed that sometimes the app starts before MongoDB is fully initialized, which can cause connection issues. A proper solution would be to add a wait mechanism or retry logic.


## 3. What is the purpose of the volume in MongoDB?

The volume is used to store MongoDB data outside of the container. This means that even if the container is stopped or removed, the data is not lost.

When I tested using docker compose down and then starting again, my data was still there because of the volume. Without it, all data would be deleted when the container is removed.


## 4. Why install requirements before copying the app code?

In the Dockerfile, requirements.txt is copied and installed first to take advantage of Docker caching. 

If the requirements do not change, Docker will reuse the cached layer and not reinstall everything again, which makes the build faster. If we copy the whole app first, even small code changes would force all dependencies to reinstall.