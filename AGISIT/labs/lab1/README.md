# DIY: Do In Yourself

### **1. Start with an NGINX image**

1. Pull the official NGINX image:

   ```bash
   docker pull nginx
   ```

2. Run a container:

   ```bash
   docker run --name my-nginx -d -p 8080:80 nginx
   ```

3. Open `http://localhost:8080` in a browser → you should see the default NGINX welcome page.

---

### **2. Start with an Ubuntu image and install NGINX**

1. Run an Ubuntu container interactively:

   ```bash
   docker run -it ubuntu
   ```

2. Inside the container, update and install NGINX:

   ```bash
   apt update
   apt install -y nginx
   ```

3. Start the NGINX service:

   ```bash
   service nginx start
   ```

4. Exit the container (type `exit`).

5. Test it by mapping a port when starting the container (e.g.):

   ```bash
   docker run -it -p 8081:80 ubuntu
   ```

   Then repeat the installation steps and open `http://localhost:8081`.

---

### **3. Serve a static webpage from the host (shared volume)**

1. Create a simple `index.html` file on your host machine:

   ```html
   <!DOCTYPE html>
   <html>
   	<head>
   		<title>My Docker Site</title>
   	</head>
   	<body>
   		<h1>Hello from Docker + NGINX!</h1>
   	</body>
   </html>
   ```

2. Run NGINX with a volume mount:

   ```bash
   docker run --name my-nginx-vol -d -p 8082:80 \
     -v $(pwd)/index.html:/usr/share/nginx/html/index.html \
     nginx
   ```

   or in powershell:

   ```bash
   docker run --name my-nginx-vol -d -p 8082:80 `
     -v ${PWD}/index.html:/usr/share/nginx/html/index.html `
     nginx
   ```

3. Open `http://localhost:8082` → you should see your custom page.

---

### **4. Copy the webpage into the Docker image (build time)**

1. Create a `Dockerfile`:

   ```dockerfile
   FROM nginx
   COPY index.html /usr/share/nginx/html/index.html
   ```

2. Build the image:

   ```bash
   docker build -t my-custom-nginx .
   ```

3. Run it:

   ```bash
   docker run --name my-nginx-img -d -p 8083:80 my-custom-nginx
   ```

4. Open `http://localhost:8083` → your page is served from inside the image.

---

### **5. Networking options to explore**

- **Port mapping (used above)**: `-p hostPort:containerPort` (e.g. `-p 8080:80`)
- **Host network mode**:

  ```bash
  docker run --network host nginx
  ```

  (then NGINX listens directly on your host’s ports — works on Linux, not Docker Desktop for Mac/Windows).
