# DECISIONS

## 1. Connection Management

I used a ConnectionManager class to manage active WebSocket clients. The connections are stored in a dictionary where the poll ID is the key and the value is a list of connected clients for that poll. When a client connects, it is added to the list, and when it disconnects, it is removed. This prevents the server from crashing if a user closes the browser or loses connection during voting.

## 2. State Storage

I decided to store polls and vote counts in memory using Python dictionaries because it was simpler and faster for this mini project. This approach works well for demonstrating real-time communication with WebSockets. The downside is that all polls and votes are lost if the server restarts because nothing is saved permanently. To make the application production-ready, I would use a database such as PostgreSQL or MongoDB to persist poll data.

## 3. Concurrency

If two users vote at almost the same time, FastAPI processes the requests asynchronously, so both votes are usually handled correctly. However, since the application stores data only in memory and does not use locks or transactions, there is still a small risk of race conditions in high-traffic situations. In a larger production system, I would use database transactions or synchronization mechanisms to guarantee consistency.

## 4. REST vs WebSocket

The REST endpoint works using the normal request-response model. A client sends a vote request and receives a single response back from the server. The WebSocket connection works differently because it stays open continuously, allowing the server to instantly broadcast updated vote counts to all connected clients in real time. REST is useful for simple API interactions, while WebSockets are better for live features where users need immediate updates without refreshing the page.