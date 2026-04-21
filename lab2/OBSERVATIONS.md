# OBSERVATIONS.md

## 1. Difference between docker run and kubectl run

When I used `docker run` in Lab 1, I was just starting a container directly on my machine. It was simple and everything was controlled locally by Docker.

With `kubectl run`, I am not running the container directly. Instead, I am telling Kubernetes to create a pod, and Kubernetes decides how and where to run it inside the cluster.

Even though both use the same image (in my case nginx), the difference is that Kubernetes adds a management layer. It handles scheduling, networking, and monitoring, while Docker just runs the container.

---

## 2. Role of the Scheduler in kubectl describe

In the `kubectl describe pod` output, I saw an event from the Scheduler. Its role is to decide which node should run the pod.

This corresponds to the Kubernetes control plane component called the scheduler. It checks available resources and assigns the pod to a node.

---

## 3. Components in kube-system

When I ran `kubectl get pods -n kube-system`, I saw several components. Two that I recognized are:

- kube-apiserver: This is the main component that handles communication with the cluster. All commands like kubectl go through it.
- etcd: This is the database that stores all the cluster data like configurations and state.

These are core components that keep the cluster running.

---

## 4. Nginx observation

The command `kubectl port-forward` allows me to access the pod from my local machine. It connects a local port (8080) to the pod’s port (80).

Without using port-forward, I could not open the nginx page in my browser because the pod is running inside the Kubernetes network, not directly exposed to my system.

So port-forward basically acts like a temporary bridge between my computer and the pod.

---

## 5. Task 6 reflection (Pod deletion)

After I deleted the pod using `kubectl delete pod my-pod`, Kubernetes did not restart it.

This is because I created the pod manually, and there is no controller managing it. Kubernetes only restarts pods automatically if they are part of a controller like a Deployment.

Since my pod was standalone, once it was deleted, it was gone permanently.

To make Kubernetes restart it automatically, I would need to use a Deployment, which ensures that a specified number of pods are always running.