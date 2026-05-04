# LinkedIn Post

Today I completed a real-time polling application using FastAPI and WebSockets as part of my backend development journey.

The project allows multiple users to vote in polls and see updates instantly across different browser tabs without refreshing the page. To achieve real-time communication, I implemented WebSocket connections instead of relying only on traditional REST APIs.

One challenge I faced was handling poll data while testing with Docker containers. Since the data was stored in memory, restarting the container removed all existing polls. I solved this by improving how the frontend handles poll IDs and testing the application directly inside the running container environment.

The project also includes:
- REST API endpoints
- Real-time vote broadcasting
- Docker containerization
- Multi-client WebSocket support

This project helped me better understand the difference between request-response communication and persistent real-time connections.

GitHub Project:
https://lnkd.in/dGjUxgRB

#FastAPI #WebSockets #BackendDevelopment #Python #100DaysOfCode

# Public URL

(https://www.linkedin.com/posts/mouncif-belrhrib-0901683b3_fastapi-websockets-backenddevelopment-share-7457077641339260928-q193?utm_source=share&utm_medium=member_desktop&rcm=ACoAAGTv2GwBY1nq47OTX3jlohJnCyc7EUM8NSU)