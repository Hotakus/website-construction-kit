# wordpress-kit

A wordpress kit for quikly constructing a website on your server.

---

### Pre-work

Install basic packages:

```bash
sudo apt install bison re2c pkg-config libxml2-dev libssl-dev \ 
 libsqlite3-dev  libcurl4-openssl-dev libpng-dev libwebp-dev libjpeg-dev \
 libfreetype-dev libonig-dev libzip-dev
```

And pull this repo. Use SSH to pull repo is recommended.

```bash
git clone --recurse-submodules \
 ssh://git@ssh.github.com:443/Hotakus/wordpress-kit.git
```

If the submodules folder is empty, you can run:

```bash
git submodule update --init --recursive --depth 1
```

---

### Configuring

Opening the file "config.json" in root folder, 

---

### Compiling

ads

---

### Deploying

This project support localhost and docker(recommended).

#### 1. Deploying to localhost

If your host is new and pure, derectly deploying project to your localhost is most easy and fast, otherwise not recommended, looking 2.



#### 2. Deploying to docker

If your localhost is mess, I recommend that you deploy project to docker, otherwise the project maybe don't work or mess up your env of localhost. even if localhost is pure and new, I still recommend using this method to deploy.



---

### Try you website

---
