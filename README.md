# wordpress-kit (WIP)

A wordpress kit for quickly constructing a website on your server.

This kit can automatically compile, deploy and configure wordpress with a nice method.

---

## Pre-work

Install basic packages:

```zsh
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

## Configuring

Opening the file "config.json" in root folder, 

---

## Compiling

```bash
sudo apt install build-essential cmake 
```

ads

---

## Deploying

This project support localhost and docker(recommended).

```bash
sudo apt install python3 python3-pip
```

If you had already installed anaconda, you can ignore command above.

### 1. To localhost

If your host is new and pure, directly deploying project to your localhost is most easy and fast, otherwise not recommended, looking 2.

### 2. To docker

If your localhost is mess, I recommend that you deploy project to docker, otherwise the project maybe don't work or mess up your environment of localhost. even if localhost is pure and new, I still recommend using this method to deploy.

```bash
sudo apt install docker.io
```



---

## Use directly

download a release of the project, and use it.

---

## Try your website

kkk

---
