Amazon Q can now help you write, modify, and maintain code by combining the power of natural language understanding with the ability to take actions on your behalf such as directly making code changes, modifying files, and running commands.

---

<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 200px 0 20px 0;">

<div style="font-size: 24px; margin-bottom: 12px;"><strong>Amazon Q</strong></div>
<div style="background: rgba(128, 128, 128, 0.15); border: 1px solid rgba(128, 128, 128, 0.25); border-radius: 8px; padding: 8px; margin: 4px 0; text-align: center;">
<div style="font-size: 14px; margin-bottom: 4px;"><strong>Did you know?</strong></div>
<div>Pinned context is always included in future chat messages</div>
</div>

Select code & ask me to explain, debug or optimize it, or type `/` for quick actions

</div>

---

azureuser@Remindbot:~/Remind_Bot/Remind_Bot$ ./deploy-azure.sh
-bash: ./deploy-azure.sh: Permission denied

why permission is denied

---


The permission denied error occurs because the `deploy-azure.sh` script doesn't have execute permissions. You need to make it executable first.

Run this command to fix it:

---

Adding execute permissions to the deploy-azure.sh script so it can be run

---

shell

---

You stopped your current work and asked me to work on the following task instead.

---

chandu@chandu:~/Remind_Bot/Remind_Bot$ ssh -i ~/Downloads/remindbot-new-key.pem azureuser@104.214.168.248
Welcome to Ubuntu 22.04.5 LTS (GNU/Linux 6.8.0-1031-azure x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Wed Sep 10 07:47:35 UTC 2025

  System load:  0.01              Processes:             109
  Usage of /:   6.5% of 28.89GB   Users logged in:       0
  Memory usage: 33%               IPv4 address for eth0: 172.16.0.4
  Swap usage:   0%

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

Expanded Security Maintenance for Applications is not enabled.

0 updates can be applied immediately.

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status

New release &#39;24.04.3 LTS&#39; available.
Run &#39;do-release-upgrade&#39; to upgrade to it.


Last login: Wed Sep 10 07:44:19 2025 from 210.212.210.87
azureuser@Remindbot:~$ cd ~/Remind_Bot/Remind_Bot
azureuser@Remindbot:~/Remind_Bot/Remind_Bot$ ./deploy-azure.sh
-bash: ./deploy-azure.sh: Permission denied
azureuser@Remindbot:~/Remind_Bot/Remind_Bot$ chmod +x deploy-azure.sh
azureuser@Remindbot:~/Remind_Bot/Remind_Bot$ ./deploy-azure.sh
🚀 Starting Azure deployment for Rasa chatbot...
✅ Environment variables loaded
🔨 Building Docker images...
./deploy-azure.sh: line 25: docker-compose: command not found
🚀 Starting services...
./deploy-azure.sh: line 28: docker-compose: command not found
✅ Deployment complete!

📊 Service Status:
./deploy-azure.sh: line 33: docker-compose: command not found

🌐 Your services are running on:
- Rasa Server: http://your-azure-vm-ip:80
- Action Server: http://your-azure-vm-ip:5055
- Telegram Bridge: http://your-azure-vm-ip:5006

📝 To check logs: docker-compose -f azure-compose.yml logs -f
🛑 To stop services: docker-compose -f azure-compose.yml down

---


The issue is that `docker-compose` is not installed on your Azure VM. You need to install Docker Compose first. Here's how to fix it:

---

Installing Docker Compose on the Azure VM

---

shell

---


Great! Docker Compose is now installed. Now you can run your deployment script again:

---

Running the deployment script now that Docker Compose is installed

---

shell

---

You stopped your current work and asked me to work on the following task instead.

---

azureuser@Remindbot:~$ sudo systemctl start docker
Failed to start docker.service: Unit docker.service not found.
azureuser@Remindbot:~$

---


Docker is not installed on your Azure VM. You need to install Docker first. Here's how to install it:

---

Installing Docker on the Azure VM

---

shell

---

You stopped your current work and asked me to work on the following task instead.

---

azureuser@Remindbot:~$ ssh -i ~/Downloads/remindbot-new-key.pem azureuser@104.214.168.248
Warning: Identity file /home/azureuser/Downloads/remindbot-new-key.pem not accessible: No such file or directory.
The authenticity of host &#39;104.214.168.248 (104.214.168.248)&#39; can&#39;t be established.
ED25519 key fingerprint is SHA256:O3UWUg47CBxiGtn6SzUNmhH0LY68RYQGVRaoGtfKoCw.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added &#39;104.214.168.248&#39; (ED25519) to the list of known hosts.
azureuser@104.214.168.248&#39;s password: 
Permission denied, please try again.
azureuser@104.214.168.248&#39;s password: 
Permission denied, please try again.
azureuser@104.214.168.248&#39;s password: 
azureuser@104.214.168.248: Permission denied (publickey,password

---


The SSH key file is not found in the expected location. You're trying to SSH from within the Azure VM itself, but the key file is on your local machine. 

Since you're already logged into the Azure VM (as shown by the prompt `azureuser@Remindbot:~$`), you can install Docker directly:

```bash
# Update package index
sudo apt update

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add your user to the docker group
sudo usermod -aG docker $USER

# Start Docker service
sudo systemctl start docker
sudo systemctl enable docker

# Verify installation
docker --version
```

After running these commands, you'll need to log out and log back in (or run `newgrp docker`) for the group changes to take effect, then you can run your deployment script.

---

azureuser@Remindbot:~$ curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
# Executing docker install script, commit: 5c8855edd778525564500337f5ac4ad65a0c168e
+ sh -c apt-get -qq update &gt;/dev/null
+ sh -c DEBIAN_FRONTEND=noninteractive apt-get -y -qq install ca-certificates curl &gt;/dev/null
+ sh -c install -m 0755 -d /etc/apt/keyrings
+ sh -c curl -fsSL &quot;https://download.docker.com/linux/ubuntu/gpg&quot; -o /etc/apt/keyrings/docker.asc
+ sh -c chmod a+r /etc/apt/keyrings/docker.asc
+ sh -c echo &quot;deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu jammy stable&quot; &gt; /etc/apt/sources.list.d/docker.list
+ sh -c apt-get -qq update &gt;/dev/null
+ sh -c DEBIAN_FRONTEND=noninteractive apt-get -y -qq install docker-ce docker-ce-cli containerd.io docker-compose-plugin docker-ce-rootless-extras docker-buildx-plugin docker-model-plugin &gt;/dev/null
+ sh -c docker version
Client: Docker Engine - Community
 Version:           28.4.0
 API version:       1.51
 Go version:        go1.24.7
 Git commit:        d8eb465
 Built:             Wed Sep  3 20:57:05 2025
 OS/Arch:           linux/amd64
 Context:           default

Server: Docker Engine - Community
 Engine:
  Version:          28.4.0
  API version:      1.51 (minimum version 1.24)
  Go version:       go1.24.7
  Git commit:       249d679
  Built:            Wed Sep  3 20:57:05 2025
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.7.27
  GitCommit:        05044ec0a9a75232cad458027ca83437aae3f4da
 runc:
  Version:          1.2.5
  GitCommit:        v1.2.5-0-g59923ef
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0

================================================================================

To run Docker as a non-privileged user, consider setting up the
Docker daemon in rootless mode for your user:

    dockerd-rootless-setuptool.sh install

Visit https://docs.docker.com/go/rootless/ to learn about rootless mode.


To run the Docker daemon as a fully privileged service, but granting non-root
users access, refer to https://docs.docker.com/go/daemon-access/

WARNING: Access to the remote API on a privileged Docker daemon is equivalent
         to root access on the host. Refer to the &#39;Docker daemon attack surface&#39;
         documentation for details: https://docs.docker.com/go/attack-surface/

================================================================================

azureuser@Remindbot:~$ docker group
sudo usermod -aG docker $USER
docker: unknown command: docker group

Run &#39;docker --help&#39; for more information

---


You typed the commands incorrectly. Run them separately:

```bash
# Add user to docker group
sudo usermod -aG docker $USER

# Start and enable Docker service
sudo systemctl start docker
sudo systemctl enable docker

# Apply group changes (or logout/login)
newgrp docker

# Verify Docker works
docker --version
```

After running these commands, you should be able to run your deployment script successfully.

---

i got the version guuide me next steps

---


Now run your deployment script:

```bash
cd ~/Remind_Bot/Remind_Bot
./deploy-azure.sh
```

This should now work since Docker and Docker Compose are both installed and running.

---

Created wheel for tornado: filename=tornado-6.1-cp310-cp310-linux_x86_64.whl size=421985 sha256=f28715597123cee8dafff5153161b0a219beaf510fda9b23f809991e391e6963
18.83   Stored in directory: /tmp/pip-ephem-wheel-cache-5ggl8br5/wheels/34/83/69/b89863a68e62add6e149dbaadcc049886105ce2405c1979bf2
18.83 Successfully built tornado
19.18 Installing collected packages: uritemplate, tzdata, tornado, requests, pydantic, psycopg2-binary, proto-plus, httplib2, googleapis-common-protos, cachetools, apscheduler, python-telegram-bot, pandas, google-auth-httplib2, google-api-core, gspread, google-api-python-client
19.18 ERROR: Could not install packages due to an OSError: [Errno 13] Permission denied: &#39;/opt/venv/lib/python3.10/site-packages/uritemplate&#39;
19.18 Check the permissions.
19.18 
20.05 
20.05 [notice] A new release of pip available: 22.3.1 -&gt; 25.2
20.05 [notice] To update, run: pip install --upgrade pip
------
failed to solve: process &quot;/bin/bash -o pipefail -c pip install --no-cache-dir -r requirements.txt&quot; did not complete successfully: exit code: 1
✅ Deployment complete!

📊 Service Status:
NAME      IMAGE     COMMAND   SERVICE   CREATED   STATUS    PORTS

🌐 Your services are running on:
- Rasa Server: http://your-azure-vm-ip:80
- Action Server: http://your-azure-vm-ip:5055
- Telegram Bridge: http://your-azure-vm-ip:5006

---

The Docker build failed due to permission issues in the Dockerfile. You need to fix the Dockerfile to run pip as root or use the correct user. Let's check and fix the Dockerfile:

---

The issue is in the Dockerfile.actions. The error shows it's trying to install to `/opt/venv/` which suggests there's a virtual environment issue. Let's fix it:

---

Fixing the Dockerfile.actions to properly handle pip installation permissions

---

Actually, let's use a simpler approach - run as root:

---

Simplifying the Dockerfile.actions to run pip as root

---


Now rebuild and run:

```bash
# Clean up previous failed builds
docker system prune -f

# Run the deployment script again
./deploy-azure.sh
```

---

but latest pip is not compatiblw with rasa

---

You're right. Let's fix the Dockerfile to use a compatible pip version for Rasa:

---

Using a Rasa-compatible pip version in the Dockerfile

---


Now rebuild:

```bash
docker system prune -f
./deploy-azure.sh
```

---

Installing collected packages: uritemplate, tzdata, tornado, requests, pydantic, psycopg2-binary, proto-plus, httplib2, googleapis-common-protos, cachetools, apscheduler, python-telegram-bot, pandas, google-auth-httplib2, google-api-core, gspread, google-api-python-client
18.86 ERROR: Could not install packages due to an OSError: [Errno 13] Permission denied: &#39;/opt/venv/lib/python3.10/site-packages/uritemplate&#39;
18.86 Check the permissions.

---

The issue is that the base Python image has a virtual environment that's causing permission problems. Let's use a different approach:

---

Fixing the virtual environment permission issue by using --break-system-packages flag

---


Now rebuild:

```bash
docker system prune -f
./deploy-azure.sh
```

---

it getting same error

---

Let's try a different approach by switching to a non-slim Python image and running as root explicitly:

---

Using regular Python image and running as root to avoid permission issues

---


Now rebuild:

```bash
docker system prune -f
./deploy-azure.sh
```

---

13.66 Installing collected packages: uritemplate, tzdata, tornado, requests, pydantic, psycopg2-binary, proto-plus, httplib2, googleapis-common-protos, cachetools, apscheduler, python-telegram-bot, pandas, google-auth-httplib2, google-api-core, gspread, google-api-python-client
13.66 ERROR: Could not install packages due to an OSError: [Errno 13] Permission denied: &#39;/opt/venv/lib/python3.10/site-packages/uritemplate&#39;
13.66 Check the permissions.
13.66 
14.53 
14.53 [notice] A new release of pip available: 22.3.1 -&gt; 25.2
14.53 [notice] To update, run: pip install --upgrade pip
------
failed to solve: process &quot;/bin/bash -o pipefail -c pip install --no-cache-dir -r requirements.txt&quot; did not complete successfully: exit code: 1
✅ Deployment complete!

📊 Service Status:
NAME      IMAGE     COMMAND   SERVICE   CREATED   STATUS    PORTS

🌐 Your services are running on:
- Rasa Server: http://your-azure-vm-ip:80
- Action Server: http://your-azure-vm-ip:5055
- Telegram Bridge: http://your-azure-vm-ip:5006

📝 To check logs: docker-compose -f azure-compose.yml logs -f
🛑 To stop services: docker-compose -f azure-compose.yml down

the erro is not rectifying once check all code in all the files

---

I see the issue. The Python 3.10.11 image has a pre-configured virtual environment at `/opt/venv/` that's causing permission issues. Let's fix this by deactivating the virtual environment:

---

Deactivating the virtual environment and installing packages globally to fix permission issues

---

Now let's also check the other Dockerfiles to ensure consistency:

---

The Rasa Dockerfile might have the same issue. Let's fix it too:

---

Fixing the Rasa Dockerfile to avoid virtual environment permission issues

---


Now rebuild:

```bash
docker system prune -f
./deploy-azure.sh
```

---

error is not solved and one more thing im using ubuntu os

---

Let's try a completely different approach using Ubuntu base image since you're on Ubuntu:

---

Using Ubuntu base image and installing Python manually to avoid virtual environment issues

---

Also update the CMD to use python3:

---

Updating CMD to use python3 instead of python

---


Now rebuild:

```bash
docker system prune -f
./deploy-azure.sh
```

---

same error 
zureuser@Remindbot:~/Remind_Bot/Remind_Bot$ ./deploy-azure.sh
🚀 Starting Azure deployment for Rasa chatbot...
✅ Environment variables loaded
🔨 Building Docker images...
[+] Building 127.2s (19/22)                                                                                                                               docker:default
 =&gt; [action-server internal] load build definition from Dockerfile.actions                                                                                          0.1s
 =&gt; =&gt; transferring dockerfile: 297B                                                                                                                                0.0s
 =&gt; [action-server internal] load metadata for docker.io/library/python:3.9-slim                                                                                    1.6s
 =&gt; [action-server internal] load .dockerignore                                                                                                                     0.1s
 =&gt; =&gt; transferring context: 154B                                                                                                                                   0.0s
 =&gt; [action-server 1/6] FROM docker.io/library/python:3.9-slim@sha256:71b97a8eed69cddd132431327ff7c204fd6ea3d38e0c5d11d52f9661482bc8a3                              0.0s
 =&gt; [action-server internal] load build context                                                                                                                     0.1s
 =&gt; =&gt; transferring context: 48.36kB                                                                                                                                0.0s
 =&gt; CACHED [action-server 2/6] WORKDIR /app                                                                                                                         0.0s
 =&gt; CACHED [action-server 3/6] COPY requirements.txt .                                                                                                              0.0s
 =&gt; CACHED [action-server 4/6] RUN pip install --no-cache-dir -r requirements.txt                                                                                   0.0s
 =&gt; CACHED [action-server 5/6] COPY actions/ ./actions/                                                                                                             0.0s
 =&gt; CACHED [action-server 6/6] COPY config.json .                                                                                                                   0.0s
 =&gt; [action-server] exporting to image                                                                                                                              0.1s
 =&gt; =&gt; exporting layers                                                                                                                                             0.0s
 =&gt; =&gt; writing image sha256:9896e6478bdf06a813f6e48dc8f7c8d5d16d21535f5b2847276e17af48f2b6ab                                                                        0.0s
 =&gt; =&gt; naming to docker.io/library/remind_bot-action-server                                                                                                         0.0s
 =&gt; [rasa-server internal] load build definition from Dockerfile.rasa                                                                                               0.0s
 =&gt; =&gt; transferring dockerfile: 344B                                                                                                                                0.0s
 =&gt; [rasa-server internal] load metadata for docker.io/rasa/rasa:3.6.21                                                                                             2.3s
 =&gt; [rasa-server internal] load .dockerignore                                                                                                                       0.0s
 =&gt; =&gt; transferring context: 154B                                                                                                                                   0.0s
 =&gt; [rasa-server 1/7] FROM docker.io/rasa/rasa:3.6.21@sha256:7c0204065d4859e1b7a691c972ca3d26f5d39ad23fbd992b654084721226d813                                     105.9s
 =&gt; =&gt; resolve docker.io/rasa/rasa:3.6.21@sha256:7c0204065d4859e1b7a691c972ca3d26f5d39ad23fbd992b654084721226d813                                                   0.0s
 =&gt; =&gt; sha256:7c0204065d4859e1b7a691c972ca3d26f5d39ad23fbd992b654084721226d813 1.61kB / 1.61kB                                                                      0.0s
 =&gt; =&gt; sha256:e4ea2b9d9dc38044ee4038855f5593313ecfcb0a3c652cf686c3f85b9b93ec63 6.96kB / 6.96kB                                                                      0.0s
 =&gt; =&gt; sha256:0e5aa551ea881f1b6fcfab87032007ac64da8563632b87173b618b086a7a0cf0 1.82kB / 1.82kB                                                                      0.0s
 =&gt; =&gt; sha256:445a6a12be2be54b4da18d7c77d4a41bc4746bc422f1f4325a60ff4fc7ea2e5d 29.54MB / 29.54MB                                                                    0.9s
 =&gt; =&gt; sha256:50532f3355eccaa7f184475b4da83a263ac11f86cc1c6618d28b6567c3fe7675 284.83MB / 284.83MB                                                                  9.4s
 =&gt; =&gt; sha256:24e4804a1dbf7990aa9d9ec6e01b2a56aadfdfb721f7c1c1f9207adfe2943052 1.46MB / 1.46MB                                                                      0.9s
 =&gt; =&gt; sha256:5c0e8d16e4048876e4b65942adc6035d36abd48d50643659e6e8b25d12c641c9 1.09kB / 1.09kB                                                                      1.3s
 =&gt; =&gt; sha256:01639847809681d4e0ac6dad6d2efcfe1fc34aa0b0d46dfc5bd9d41483e01c7b 4.22kB / 4.22kB                                                                      2.6s
 =&gt; =&gt; extracting sha256:445a6a12be2be54b4da18d7c77d4a41bc4746bc422f1f4325a60ff4fc7ea2e5d                                                                          21.3s
 =&gt; =&gt; sha256:01029823f2260f38ea9d97d01059d16f7184edee64e335ce1811fa611380484d 807.93MB / 807.93MB                                                                 22.2s
 =&gt; =&gt; sha256:4f4fb700ef54461cfa02571ae0db9a0dc1e0cdb5577484a6d75e68dc38e8acc1 32B / 32B                                                                            6.5s
 =&gt; =&gt; sha256:903b9bd8420885647ab87a8d4beb3496b9d79835baf6ba9086470c0caa4cb631 2.30kB / 2.30kB                                                                     11.2s
 =&gt; =&gt; extracting sha256:50532f3355eccaa7f184475b4da83a263ac11f86cc1c6618d28b6567c3fe7675                                                                          20.5s
 =&gt; =&gt; extracting sha256:24e4804a1dbf7990aa9d9ec6e01b2a56aadfdfb721f7c1c1f9207adfe2943052                                                                           0.2s
 =&gt; =&gt; extracting sha256:5c0e8d16e4048876e4b65942adc6035d36abd48d50643659e6e8b25d12c641c9                                                                           0.0s
 =&gt; =&gt; extracting sha256:01639847809681d4e0ac6dad6d2efcfe1fc34aa0b0d46dfc5bd9d41483e01c7b                                                                           0.0s
 =&gt; =&gt; extracting sha256:01029823f2260f38ea9d97d01059d16f7184edee64e335ce1811fa611380484d                                                                          60.9s
 =&gt; =&gt; extracting sha256:4f4fb700ef54461cfa02571ae0db9a0dc1e0cdb5577484a6d75e68dc38e8acc1                                                                           0.0s
 =&gt; =&gt; extracting sha256:903b9bd8420885647ab87a8d4beb3496b9d79835baf6ba9086470c0caa4cb631                                                                           0.0s
 =&gt; [rasa-server internal] load build context                                                                                                                       0.1s
 =&gt; =&gt; transferring context: 81.65kB                                                                                                                                0.0s
 =&gt; [rasa-server 2/7] WORKDIR /app                                                                                                                                  0.1s
 =&gt; [rasa-server 3/7] COPY requirements.txt .                                                                                                                       0.1s
 =&gt; ERROR [rasa-server 4/7] RUN pip install --no-cache-dir -r requirements.txt                                                                                     15.5s
------
 &gt; [rasa-server 4/7] RUN pip install --no-cache-dir -r requirements.txt:
2.227 Requirement already satisfied: rasa==3.6.21 in /opt/venv/lib/python3.10/site-packages (from -r requirements.txt (line 2)) (3.6.21)
2.230 Requirement already satisfied: rasa-sdk==3.6.2 in /opt/venv/lib/python3.10/site-packages (from -r requirements.txt (line 3)) (3.6.2)
2.583 Collecting gspread==6.2.1
2.841   Downloading gspread-6.2.1-py3-none-any.whl (59 kB)
2.896      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 60.0/60.0 kB 1.0 MB/s eta 0:00:00
3.194 Collecting google-api-python-client==2.178.0
3.236   Downloading google_api_python_client-2.178.0-py3-none-any.whl (13.8 MB)
3.507      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 13.8/13.8 MB 103.8 MB/s eta 0:00:00
3.580 Requirement already satisfied: google-auth-oauthlib==1.0.0 in /opt/venv/lib/python3.10/site-packages (from -r requirements.txt (line 8)) (1.0.0)
3.701 Collecting python-telegram-bot==13.15
3.742   Downloading python_telegram_bot-13.15-py3-none-any.whl (519 kB)
3.747      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 519.2/519.2 kB 219.2 MB/s eta 0:00:00
4.240 Collecting pandas==2.3.1
4.279   Downloading pandas-2.3.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (12.3 MB)
4.393      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.3/12.3 MB 126.5 MB/s eta 0:00:00
4.572 Collecting requests==2.32.4
4.611   Downloading requests-2.32.4-py3-none-any.whl (64 kB)
4.615      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 64.8/64.8 kB 202.3 MB/s eta 0:00:00
4.902 Collecting psycopg2-binary==2.9.10
4.942   Downloading psycopg2_binary-2.9.10-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.0 MB)
4.964      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.0/3.0 MB 169.1 MB/s eta 0:00:00
5.169 Requirement already satisfied: typing-extensions&lt;5.0.0,&gt;=4.1.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.7.1)
5.171 Requirement already satisfied: portalocker&lt;3.0.0,&gt;=2.7.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.7.0)
5.172 Requirement already satisfied: sanic&lt;21.13,&gt;=21.12 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (21.12.2)
5.175 Requirement already satisfied: scipy&lt;1.11.0,&gt;=1.10.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.10.1)
5.177 Requirement already satisfied: structlog-sentry&lt;3.0.0,&gt;=2.0.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.0.3)
5.178 Requirement already satisfied: pydot&lt;1.5,&gt;=1.4 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.4.2)
5.180 Requirement already satisfied: sentry-sdk&lt;1.15.0,&gt;=0.17.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.14.0)
5.181 Requirement already satisfied: pytz&lt;2023.0,&gt;=2019.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2022.7.1)
5.183 Requirement already satisfied: sanic-jwt&lt;2.0.0,&gt;=1.6.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.8.0)
5.185 Requirement already satisfied: prompt-toolkit&lt;3.0.29,&gt;=3.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.0.28)
5.188 Requirement already satisfied: python-socketio&lt;6,&gt;=4.4 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (5.8.0)
5.198 Requirement already satisfied: tensorflow-text==2.12.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.12.0)
5.201 Requirement already satisfied: scikit-learn&lt;1.2,&gt;=0.22 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.1.3)
5.202 Requirement already satisfied: tensorflow_hub&lt;0.14.0,&gt;=0.13.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.13.0)
5.205 Requirement already satisfied: sanic-cors&lt;2.1.0,&gt;=2.0.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.0.1)
5.207 Requirement already satisfied: aio-pika&lt;8.2.4,&gt;=6.7.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (8.2.3)
5.212 Requirement already satisfied: jsonschema&lt;4.18,&gt;=3.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.17.3)
5.212 Requirement already satisfied: websockets&lt;11.0,&gt;=10.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (10.4)
5.212 Requirement already satisfied: coloredlogs&lt;16,&gt;=10 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (15.0.1)
5.213 Requirement already satisfied: certifi&gt;=2023.7.22 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2023.7.22)
5.215 Requirement already satisfied: pyyaml&gt;=6.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (6.0.1)
5.216 Requirement already satisfied: regex&lt;2022.11,&gt;=2020.6 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2022.10.31)
5.218 Requirement already satisfied: cryptography&gt;=41.0.7 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (41.0.7)
5.219 Requirement already satisfied: matplotlib&lt;3.6,&gt;=3.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.5.3)
5.221 Requirement already satisfied: tqdm&lt;5.0,&gt;=4.31 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.65.0)
5.223 Requirement already satisfied: ujson&lt;6.0,&gt;=1.35 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (5.8.0)
5.224 Requirement already satisfied: apscheduler&lt;3.10,&gt;=3.6 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.9.1.post1)
5.226 Requirement already satisfied: packaging&lt;21.0,&gt;=20.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (20.9)
5.228 Requirement already satisfied: webexteamssdk&lt;1.7.0,&gt;=1.1.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.6.1)
5.230 Requirement already satisfied: sklearn-crfsuite&lt;0.4,&gt;=0.3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.3.6)
5.231 Requirement already satisfied: pluggy&lt;2.0.0,&gt;=1.0.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.2.0)
5.716 Collecting pydantic&lt;1.10.10
5.758   Downloading pydantic-1.10.9-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.1 MB)
5.783      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.1/3.1 MB 141.3 MB/s eta 0:00:00
5.803 Requirement already satisfied: safetensors&lt;0.5.0,&gt;=0.4.5 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.4.5)
5.805 Requirement already satisfied: pykwalify&lt;1.9,&gt;=1.7 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.8.0)
5.814 Requirement already satisfied: skops==0.9.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.9.0)
5.816 Requirement already satisfied: slack-sdk&lt;4.0.0,&gt;=3.19.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.21.3)
5.819 Requirement already satisfied: python-engineio!=5.0.0,&lt;6,&gt;=4 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.5.1)
5.822 Requirement already satisfied: structlog&lt;24.0.0,&gt;=23.1.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (23.1.0)
5.823 Requirement already satisfied: questionary&lt;1.11.0,&gt;=1.5.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.10.0)
5.824 Requirement already satisfied: ruamel.yaml&lt;0.17.22,&gt;=0.16.5 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.17.21)
5.826 Requirement already satisfied: terminaltables&lt;3.2.0,&gt;=3.1.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.1.10)
5.828 Requirement already satisfied: fbmessenger&lt;6.1.0,&gt;=6.0.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (6.0.0)
5.829 Requirement already satisfied: tarsafe&lt;0.0.5,&gt;=0.0.3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.0.4)
5.831 Requirement already satisfied: typing-utils&lt;0.2.0,&gt;=0.1.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.1.0)
5.833 Requirement already satisfied: SQLAlchemy&lt;1.5.0,&gt;=1.4.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.4.49)
5.834 Requirement already satisfied: google-auth&lt;3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.21.0)
5.836 Requirement already satisfied: absl-py&lt;1.5,&gt;=0.9 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.4.0)
5.837 Requirement already satisfied: colorhash&lt;1.3.0,&gt;=1.0.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.2.1)
5.839 Requirement already satisfied: boto3&lt;2.0.0,&gt;=1.26.136 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.27.1)
5.842 Requirement already satisfied: numpy&lt;1.25.0,&gt;=1.19.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.23.5)
5.843 Requirement already satisfied: randomname&lt;0.2.0,&gt;=0.1.5 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.1.5)
5.845 Requirement already satisfied: dnspython==2.3.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.3.0)
5.846 Requirement already satisfied: setuptools&lt;70.4.0,&gt;=70.3.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (70.3.0)
5.850 Requirement already satisfied: aiogram&lt;2.26 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.15)
5.853 Requirement already satisfied: twilio&lt;8.3,&gt;=6.26 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (8.2.2)
5.853 Requirement already satisfied: sanic-routing&lt;0.8.0,&gt;=0.7.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.7.2)
5.855 Requirement already satisfied: python-dateutil&lt;2.9,&gt;=2.8 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.8.2)
5.856 Requirement already satisfied: confluent-kafka&lt;3.0.0,&gt;=1.9.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.1.1)
5.858 Requirement already satisfied: mattermostwrapper&lt;2.3,&gt;=2.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.2)
5.874 Requirement already satisfied: jsonpickle&lt;3.1,&gt;=1.3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.0.4)
5.875 Requirement already satisfied: colorclass&lt;2.3,&gt;=2.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.2.2)
5.878 Requirement already satisfied: pymongo[srv,tls]&lt;4.4,&gt;=3.8 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.3.3)
5.879 Requirement already satisfied: tensorflow==2.12.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.12.0)
5.881 Requirement already satisfied: redis&lt;5.0,&gt;=4.5.3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.6.0)
5.885 Requirement already satisfied: rocketchat_API&lt;1.31.0,&gt;=0.6.31 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.30.0)
5.886 Requirement already satisfied: attrs&lt;22.2,&gt;=19.3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (22.1.0)
5.888 Requirement already satisfied: PyJWT[crypto]&lt;3.0.0,&gt;=2.0.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.7.0)
5.891 Requirement already satisfied: aiohttp&lt;3.10,&gt;=3.9.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.9.3)
5.893 Requirement already satisfied: networkx&lt;2.7,&gt;=2.4 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.6.3)
5.894 Requirement already satisfied: wheel&gt;=0.38.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.40.0)
5.897 Requirement already satisfied: dask==2022.10.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2022.10.2)
5.901 Requirement already satisfied: CacheControl&lt;0.13.0,&gt;=0.12.9 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.12.14)
5.904 Requirement already satisfied: tensorflow-io-gcs-filesystem==0.32 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.32.0)
5.906 Requirement already satisfied: protobuf&lt;4.23.4,&gt;=4.23.3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.23.3)
6.019 Collecting uritemplate&lt;5,&gt;=3.0.1
6.055   Downloading uritemplate-4.2.0-py3-none-any.whl (11 kB)
6.117 Collecting google-auth-httplib2&lt;1.0.0,&gt;=0.2.0
6.154   Downloading google_auth_httplib2-0.2.0-py2.py3-none-any.whl (9.3 kB)
6.339 Collecting google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,&lt;3.0.0,&gt;=1.31.5
6.377   Downloading google_api_core-2.25.1-py3-none-any.whl (160 kB)
6.382      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 160.8/160.8 kB 232.9 MB/s eta 0:00:00
6.465 Collecting httplib2&lt;1.0.0,&gt;=0.19.0
6.501   Downloading httplib2-0.30.0-py3-none-any.whl (91 kB)
6.504      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 91.1/91.1 kB 136.6 MB/s eta 0:00:00
6.519 Requirement already satisfied: requests-oauthlib&gt;=0.7.0 in /opt/venv/lib/python3.10/site-packages (from google-auth-oauthlib==1.0.0-&gt;-r requirements.txt (line 8)) (1.3.1)
6.664 Collecting tornado==6.1
6.704   Downloading tornado-6.1.tar.gz (497 kB)
6.714      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 497.4/497.4 kB 76.8 MB/s eta 0:00:00
6.862   Preparing metadata (setup.py): started
7.700   Preparing metadata (setup.py): finished with status &#39;done&#39;
7.797 Collecting apscheduler&lt;3.10,&gt;=3.6
7.834   Downloading APScheduler-3.6.3-py2.py3-none-any.whl (58 kB)
7.839      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 58.9/58.9 kB 184.5 MB/s eta 0:00:00
7.915 Collecting cachetools==4.2.2
7.952   Downloading cachetools-4.2.2-py3-none-any.whl (11 kB)
8.147 Collecting tzdata&gt;=2022.7
8.185   Downloading tzdata-2025.2-py2.py3-none-any.whl (347 kB)
8.190      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 347.8/347.8 kB 230.9 MB/s eta 0:00:00
8.209 Requirement already satisfied: charset_normalizer&lt;4,&gt;=2 in /opt/venv/lib/python3.10/site-packages (from requests==2.32.4-&gt;-r requirements.txt (line 15)) (3.1.0)
8.211 Requirement already satisfied: idna&lt;4,&gt;=2.5 in /opt/venv/lib/python3.10/site-packages (from requests==2.32.4-&gt;-r requirements.txt (line 15)) (3.4)
8.213 Requirement already satisfied: urllib3&lt;3,&gt;=1.21.1 in /opt/venv/lib/python3.10/site-packages (from requests==2.32.4-&gt;-r requirements.txt (line 15)) (1.26.16)
8.286 Requirement already satisfied: tzlocal&gt;=1.2 in /opt/venv/lib/python3.10/site-packages (from apscheduler&lt;3.10,&gt;=3.6-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (5.0.1)
8.288 Requirement already satisfied: six&gt;=1.4.0 in /opt/venv/lib/python3.10/site-packages (from apscheduler&lt;3.10,&gt;=3.6-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.16.0)
8.319 Requirement already satisfied: click&gt;=7.0 in /opt/venv/lib/python3.10/site-packages (from dask==2022.10.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (8.1.3)
8.321 Requirement already satisfied: toolz&gt;=0.8.2 in /opt/venv/lib/python3.10/site-packages (from dask==2022.10.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.12.0)
8.322 Requirement already satisfied: partd&gt;=0.3.10 in /opt/venv/lib/python3.10/site-packages (from dask==2022.10.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.4.0)
8.324 Requirement already satisfied: cloudpickle&gt;=1.1.1 in /opt/venv/lib/python3.10/site-packages (from dask==2022.10.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.2.1)
8.326 Requirement already satisfied: fsspec&gt;=0.6.0 in /opt/venv/lib/python3.10/site-packages (from dask==2022.10.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2023.6.0)
8.387 Requirement already satisfied: tabulate&gt;=0.8.8 in /opt/venv/lib/python3.10/site-packages (from skops==0.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.9.0)
8.389 Requirement already satisfied: huggingface-hub&gt;=0.17.0 in /opt/venv/lib/python3.10/site-packages (from skops==0.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.27.0)
8.423 Requirement already satisfied: libclang&gt;=13.0.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (16.0.0)
8.425 Requirement already satisfied: grpcio&lt;2.0,&gt;=1.24.3 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.56.0)
8.426 Requirement already satisfied: termcolor&gt;=1.1.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.3.0)
8.428 Requirement already satisfied: gast&lt;=0.4.0,&gt;=0.2.1 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.4.0)
8.430 Requirement already satisfied: tensorboard&lt;2.13,&gt;=2.12 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.12.3)
8.431 Requirement already satisfied: tensorflow-estimator&lt;2.13,&gt;=2.12.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.12.0)
8.433 Requirement already satisfied: flatbuffers&gt;=2.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (23.5.26)
8.435 Requirement already satisfied: keras&lt;2.13,&gt;=2.12.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.12.0)
8.438 Requirement already satisfied: google-pasta&gt;=0.1.1 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.2.0)
8.440 Requirement already satisfied: jax&gt;=0.3.15 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.4.13)
8.442 Requirement already satisfied: wrapt&lt;1.15,&gt;=1.11.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.14.1)
8.444 Requirement already satisfied: h5py&gt;=2.9.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.9.0)
8.445 Requirement already satisfied: astunparse&gt;=1.6.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.6.3)
8.448 Requirement already satisfied: opt-einsum&gt;=2.3.2 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.3.0)
8.512 Requirement already satisfied: yarl in /opt/venv/lib/python3.10/site-packages (from aio-pika&lt;8.2.4,&gt;=6.7.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.9.2)
8.514 Requirement already satisfied: aiormq~=6.4.0 in /opt/venv/lib/python3.10/site-packages (from aio-pika&lt;8.2.4,&gt;=6.7.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (6.4.2)
8.528 Requirement already satisfied: Babel&gt;=2.8.0 in /opt/venv/lib/python3.10/site-packages (from aiogram&lt;2.26-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.9.1)
8.552 Requirement already satisfied: aiosignal&gt;=1.1.2 in /opt/venv/lib/python3.10/site-packages (from aiohttp&lt;3.10,&gt;=3.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.3.1)
8.554 Requirement already satisfied: multidict&lt;7.0,&gt;=4.5 in /opt/venv/lib/python3.10/site-packages (from aiohttp&lt;3.10,&gt;=3.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (5.2.0)
8.557 Requirement already satisfied: async-timeout&lt;5.0,&gt;=4.0 in /opt/venv/lib/python3.10/site-packages (from aiohttp&lt;3.10,&gt;=3.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.0.2)
8.558 Requirement already satisfied: frozenlist&gt;=1.1.1 in /opt/venv/lib/python3.10/site-packages (from aiohttp&lt;3.10,&gt;=3.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.3.3)
8.610 Requirement already satisfied: jmespath&lt;2.0.0,&gt;=0.7.1 in /opt/venv/lib/python3.10/site-packages (from boto3&lt;2.0.0,&gt;=1.26.136-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.0.1)
8.613 Requirement already satisfied: botocore&lt;1.31.0,&gt;=1.30.1 in /opt/venv/lib/python3.10/site-packages (from boto3&lt;2.0.0,&gt;=1.26.136-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.30.1)
8.613 Requirement already satisfied: s3transfer&lt;0.7.0,&gt;=0.6.0 in /opt/venv/lib/python3.10/site-packages (from boto3&lt;2.0.0,&gt;=1.26.136-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.6.1)
8.624 Requirement already satisfied: msgpack&gt;=0.5.2 in /opt/venv/lib/python3.10/site-packages (from CacheControl&lt;0.13.0,&gt;=0.12.9-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.0.5)
8.648 Requirement already satisfied: humanfriendly&gt;=9.1 in /opt/venv/lib/python3.10/site-packages (from coloredlogs&lt;16,&gt;=10-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (10.0)
8.737 Requirement already satisfied: cffi&gt;=1.12 in /opt/venv/lib/python3.10/site-packages (from cryptography&gt;=41.0.7-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.15.1)
8.871 Collecting googleapis-common-protos&lt;2.0.0,&gt;=1.56.2
8.910   Downloading googleapis_common_protos-1.70.0-py3-none-any.whl (294 kB)
8.917      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 294.5/294.5 kB 200.0 MB/s eta 0:00:00
9.007 Collecting proto-plus&lt;2.0.0,&gt;=1.22.3
9.043   Downloading proto_plus-1.26.1-py3-none-any.whl (50 kB)
9.047      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 50.2/50.2 kB 170.7 MB/s eta 0:00:00
9.098 Requirement already satisfied: pyasn1-modules&gt;=0.2.1 in /opt/venv/lib/python3.10/site-packages (from google-auth&lt;3-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.3.0)
9.100 Requirement already satisfied: rsa&lt;5,&gt;=3.1.4 in /opt/venv/lib/python3.10/site-packages (from google-auth&lt;3-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.9)
9.118 Requirement already satisfied: pyparsing&lt;4,&gt;=3.0.4 in /opt/venv/lib/python3.10/site-packages (from httplib2&lt;1.0.0,&gt;=0.19.0-&gt;google-api-python-client==2.178.0-&gt;-r requirements.txt (line 7)) (3.1.0)
9.193 Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,&gt;=0.14.0 in /opt/venv/lib/python3.10/site-packages (from jsonschema&lt;4.18,&gt;=3.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.19.3)
9.211 Requirement already satisfied: pillow&gt;=6.2.0 in /opt/venv/lib/python3.10/site-packages (from matplotlib&lt;3.6,&gt;=3.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (10.0.1)
9.213 Requirement already satisfied: cycler&gt;=0.10 in /opt/venv/lib/python3.10/site-packages (from matplotlib&lt;3.6,&gt;=3.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.11.0)
9.215 Requirement already satisfied: fonttools&gt;=4.22.0 in /opt/venv/lib/python3.10/site-packages (from matplotlib&lt;3.6,&gt;=3.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.40.0)
9.216 Requirement already satisfied: kiwisolver&gt;=1.0.1 in /opt/venv/lib/python3.10/site-packages (from matplotlib&lt;3.6,&gt;=3.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.4.4)
9.307 Requirement already satisfied: wcwidth in /opt/venv/lib/python3.10/site-packages (from prompt-toolkit&lt;3.0.29,&gt;=3.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.2.6)
9.385 Requirement already satisfied: docopt&gt;=0.6.2 in /opt/venv/lib/python3.10/site-packages (from pykwalify&lt;1.9,&gt;=1.7-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.6.2)
9.459 Requirement already satisfied: bidict&gt;=0.21.0 in /opt/venv/lib/python3.10/site-packages (from python-socketio&lt;6,&gt;=4.4-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.22.1)
9.505 Requirement already satisfied: fire in /opt/venv/lib/python3.10/site-packages (from randomname&lt;0.2.0,&gt;=0.1.5-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.5.0)
9.547 Requirement already satisfied: oauthlib&gt;=3.0.0 in /opt/venv/lib/python3.10/site-packages (from requests-oauthlib&gt;=0.7.0-&gt;google-auth-oauthlib==1.0.0-&gt;-r requirements.txt (line 8)) (3.2.2)
9.578 Requirement already satisfied: ruamel.yaml.clib&gt;=0.2.6 in /opt/venv/lib/python3.10/site-packages (from ruamel.yaml&lt;0.17.22,&gt;=0.16.5-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.2.7)
9.751 Requirement already satisfied: httptools&gt;=0.0.10 in /opt/venv/lib/python3.10/site-packages (from sanic&lt;21.13,&gt;=21.12-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.5.0)
9.755 Requirement already satisfied: aiofiles&gt;=0.6.0 in /opt/venv/lib/python3.10/site-packages (from sanic&lt;21.13,&gt;=21.12-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (23.1.0)
9.760 Requirement already satisfied: uvloop&gt;=0.5.3 in /opt/venv/lib/python3.10/site-packages (from sanic&lt;21.13,&gt;=21.12-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.17.0)
9.879 Requirement already satisfied: threadpoolctl&gt;=2.0.0 in /opt/venv/lib/python3.10/site-packages (from scikit-learn&lt;1.2,&gt;=0.22-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.1.0)
9.882 Requirement already satisfied: joblib&gt;=1.0.0 in /opt/venv/lib/python3.10/site-packages (from scikit-learn&lt;1.2,&gt;=0.22-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.4.2)
9.993 Requirement already satisfied: python-crfsuite&gt;=0.8.3 in /opt/venv/lib/python3.10/site-packages (from sklearn-crfsuite&lt;0.4,&gt;=0.3-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.9.9)
10.14 Requirement already satisfied: greenlet!=0.4.17 in /opt/venv/lib/python3.10/site-packages (from SQLAlchemy&lt;1.5.0,&gt;=1.4.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.0.2)
10.27 Requirement already satisfied: aiohttp-retry&gt;=2.8.3 in /opt/venv/lib/python3.10/site-packages (from twilio&lt;8.3,&gt;=6.26-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.8.3)
10.41 Requirement already satisfied: future in /opt/venv/lib/python3.10/site-packages (from webexteamssdk&lt;1.7.0,&gt;=1.1.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.18.3)
10.41 Requirement already satisfied: requests-toolbelt in /opt/venv/lib/python3.10/site-packages (from webexteamssdk&lt;1.7.0,&gt;=1.1.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.0.0)
10.49 Requirement already satisfied: pamqp==3.2.1 in /opt/venv/lib/python3.10/site-packages (from aiormq~=6.4.0-&gt;aio-pika&lt;8.2.4,&gt;=6.7.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.2.1)
10.67 Requirement already satisfied: pycparser in /opt/venv/lib/python3.10/site-packages (from cffi&gt;=1.12-&gt;cryptography&gt;=41.0.7-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.21)
11.16 Requirement already satisfied: filelock in /opt/venv/lib/python3.10/site-packages (from huggingface-hub&gt;=0.17.0-&gt;skops==0.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.12.2)
11.24 Requirement already satisfied: ml_dtypes&gt;=0.1.0 in /opt/venv/lib/python3.10/site-packages (from jax&gt;=0.3.15-&gt;tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.2.0)
11.42 Requirement already satisfied: locket in /opt/venv/lib/python3.10/site-packages (from partd&gt;=0.3.10-&gt;dask==2022.10.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.0.0)
11.50 Requirement already satisfied: pyasn1&lt;0.6.0,&gt;=0.4.6 in /opt/venv/lib/python3.10/site-packages (from pyasn1-modules&gt;=0.2.1-&gt;google-auth&lt;3-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.5.0)
11.69 Requirement already satisfied: tensorboard-data-server&lt;0.8.0,&gt;=0.7.0 in /opt/venv/lib/python3.10/site-packages (from tensorboard&lt;2.13,&gt;=2.12-&gt;tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.7.1)
11.69 Requirement already satisfied: markdown&gt;=2.6.8 in /opt/venv/lib/python3.10/site-packages (from tensorboard&lt;2.13,&gt;=2.12-&gt;tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.4.3)
11.70 Requirement already satisfied: werkzeug&gt;=1.0.1 in /opt/venv/lib/python3.10/site-packages (from tensorboard&lt;2.13,&gt;=2.12-&gt;tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.3.6)
12.18 Requirement already satisfied: MarkupSafe&gt;=2.1.1 in /opt/venv/lib/python3.10/site-packages (from werkzeug&gt;=1.0.1-&gt;tensorboard&lt;2.13,&gt;=2.12-&gt;tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.1.3)
12.35 Building wheels for collected packages: tornado
12.35   Building wheel for tornado (setup.py): started
14.07   Building wheel for tornado (setup.py): finished with status &#39;done&#39;
14.07   Created wheel for tornado: filename=tornado-6.1-cp310-cp310-linux_x86_64.whl size=421981 sha256=44cea9f20300eeea983c7d0783bcf355ca22d054498365219dd424abd2433fdf
14.07   Stored in directory: /tmp/pip-ephem-wheel-cache-mne7np1i/wheels/34/83/69/b89863a68e62add6e149dbaadcc049886105ce2405c1979bf2
14.08 Successfully built tornado
14.38 Installing collected packages: uritemplate, tzdata, tornado, requests, pydantic, psycopg2-binary, proto-plus, httplib2, googleapis-common-protos, cachetools, apscheduler, python-telegram-bot, pandas, google-auth-httplib2, google-api-core, gspread, google-api-python-client
14.39 ERROR: Could not install packages due to an OSError: [Errno 13] Permission denied: &#39;/opt/venv/lib/python3.10/site-packages/uritemplate&#39;
14.39 Check the permissions.
14.39 
14.96 
14.96 [notice] A new release of pip available: 22.3.1 -&gt; 25.2
14.96 [notice] To update, run: pip install --upgrade pip
------
failed to solve: process &quot;/bin/bash -o pipefail -c pip install --no-cache-dir -r requirements.txt&quot; did not complete successfully: exit code: 1
🚀 Starting services...
[+] Building 22.4s (8/11)                                                                                                                                 docker:default
 =&gt; [rasa-server internal] load build definition from Dockerfile.rasa                                                                                               0.0s
 =&gt; =&gt; transferring dockerfile: 344B                                                                                                                                0.0s
 =&gt; [rasa-server internal] load metadata for docker.io/rasa/rasa:3.6.21                                                                                             0.8s
 =&gt; [rasa-server internal] load .dockerignore                                                                                                                       0.0s
 =&gt; =&gt; transferring context: 154B                                                                                                                                   0.0s
 =&gt; [rasa-server 1/7] FROM docker.io/rasa/rasa:3.6.21@sha256:7c0204065d4859e1b7a691c972ca3d26f5d39ad23fbd992b654084721226d813                                       0.0s
 =&gt; [rasa-server internal] load build context                                                                                                                       0.0s
 =&gt; =&gt; transferring context: 1.41kB                                                                                                                                 0.0s
 =&gt; CACHED [rasa-server 2/7] WORKDIR /app                                                                                                                           0.0s
 =&gt; CACHED [rasa-server 3/7] COPY requirements.txt .                                                                                                                0.0s
 =&gt; ERROR [rasa-server 4/7] RUN pip install --no-cache-dir -r requirements.txt                                                                                     20.4s
------
 &gt; [rasa-server 4/7] RUN pip install --no-cache-dir -r requirements.txt:
2.953 Requirement already satisfied: rasa==3.6.21 in /opt/venv/lib/python3.10/site-packages (from -r requirements.txt (line 2)) (3.6.21)
2.955 Requirement already satisfied: rasa-sdk==3.6.2 in /opt/venv/lib/python3.10/site-packages (from -r requirements.txt (line 3)) (3.6.2)
3.497 Collecting gspread==6.2.1
3.886   Downloading gspread-6.2.1-py3-none-any.whl (59 kB)
3.971      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 60.0/60.0 kB 743.4 kB/s eta 0:00:00
4.439 Collecting google-api-python-client==2.178.0
4.484   Downloading google_api_python_client-2.178.0-py3-none-any.whl (13.8 MB)
4.857      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 13.8/13.8 MB 57.0 MB/s eta 0:00:00
4.962 Requirement already satisfied: google-auth-oauthlib==1.0.0 in /opt/venv/lib/python3.10/site-packages (from -r requirements.txt (line 8)) (1.0.0)
5.164 Collecting python-telegram-bot==13.15
5.203   Downloading python_telegram_bot-13.15-py3-none-any.whl (519 kB)
5.216      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 519.2/519.2 kB 93.7 MB/s eta 0:00:00
6.099 Collecting pandas==2.3.1
6.144   Downloading pandas-2.3.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (12.3 MB)
6.322      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.3/12.3 MB 76.8 MB/s eta 0:00:00
6.664 Collecting requests==2.32.4
6.689   Downloading requests-2.32.4-py3-none-any.whl (64 kB)
6.695      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 64.8/64.8 kB 83.0 MB/s eta 0:00:00
7.168 Collecting psycopg2-binary==2.9.10
7.211   Downloading psycopg2_binary-2.9.10-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.0 MB)
7.260      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.0/3.0 MB 82.1 MB/s eta 0:00:00
7.644 Requirement already satisfied: coloredlogs&lt;16,&gt;=10 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (15.0.1)
7.644 Requirement already satisfied: scikit-learn&lt;1.2,&gt;=0.22 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.1.3)
7.663 Requirement already satisfied: python-engineio!=5.0.0,&lt;6,&gt;=4 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.5.1)
7.663 Requirement already satisfied: twilio&lt;8.3,&gt;=6.26 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (8.2.2)
7.663 Requirement already satisfied: skops==0.9.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.9.0)
7.663 Requirement already satisfied: fbmessenger&lt;6.1.0,&gt;=6.0.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (6.0.0)
7.663 Requirement already satisfied: ujson&lt;6.0,&gt;=1.35 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (5.8.0)
7.673 Requirement already satisfied: sanic-cors&lt;2.1.0,&gt;=2.0.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.0.1)
7.673 Requirement already satisfied: sanic-jwt&lt;2.0.0,&gt;=1.6.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.8.0)
7.673 Requirement already satisfied: pymongo[srv,tls]&lt;4.4,&gt;=3.8 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.3.3)
7.673 Requirement already satisfied: redis&lt;5.0,&gt;=4.5.3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.6.0)
7.673 Requirement already satisfied: webexteamssdk&lt;1.7.0,&gt;=1.1.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.6.1)
7.673 Requirement already satisfied: google-auth&lt;3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.21.0)
7.710 Requirement already satisfied: confluent-kafka&lt;3.0.0,&gt;=1.9.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.1.1)
7.710 Requirement already satisfied: regex&lt;2022.11,&gt;=2020.6 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2022.10.31)
7.710 Requirement already satisfied: questionary&lt;1.11.0,&gt;=1.5.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.10.0)
7.716 Requirement already satisfied: portalocker&lt;3.0.0,&gt;=2.7.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.7.0)
7.716 Requirement already satisfied: dnspython==2.3.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.3.0)
7.721 Requirement already satisfied: aio-pika&lt;8.2.4,&gt;=6.7.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (8.2.3)
7.721 Requirement already satisfied: pluggy&lt;2.0.0,&gt;=1.0.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.2.0)
7.721 Requirement already satisfied: structlog&lt;24.0.0,&gt;=23.1.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (23.1.0)
8.686 Collecting pydantic&lt;1.10.10
8.686   Downloading pydantic-1.10.9-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.1 MB)
8.828      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.1/3.1 MB 23.3 MB/s eta 0:00:00
8.857 Requirement already satisfied: protobuf&lt;4.23.4,&gt;=4.23.3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.23.3)
8.857 Requirement already satisfied: scipy&lt;1.11.0,&gt;=1.10.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.10.1)
8.861 Requirement already satisfied: sanic&lt;21.13,&gt;=21.12 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (21.12.2)
8.866 Requirement already satisfied: sentry-sdk&lt;1.15.0,&gt;=0.17.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.14.0)
8.866 Requirement already satisfied: sanic-routing&lt;0.8.0,&gt;=0.7.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.7.2)
8.866 Requirement already satisfied: apscheduler&lt;3.10,&gt;=3.6 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.9.1.post1)
8.882 Requirement already satisfied: pytz&lt;2023.0,&gt;=2019.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2022.7.1)
8.882 Requirement already satisfied: jsonschema&lt;4.18,&gt;=3.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.17.3)
8.882 Requirement already satisfied: cryptography&gt;=41.0.7 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (41.0.7)
8.882 Requirement already satisfied: mattermostwrapper&lt;2.3,&gt;=2.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.2)
8.882 Requirement already satisfied: attrs&lt;22.2,&gt;=19.3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (22.1.0)
8.882 Requirement already satisfied: aiohttp&lt;3.10,&gt;=3.9.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.9.3)
8.904 Requirement already satisfied: jsonpickle&lt;3.1,&gt;=1.3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.0.4)
8.904 Requirement already satisfied: certifi&gt;=2023.7.22 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2023.7.22)
8.904 Requirement already satisfied: colorhash&lt;1.3.0,&gt;=1.0.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.2.1)
8.904 Requirement already satisfied: tensorflow-io-gcs-filesystem==0.32 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.32.0)
8.904 Requirement already satisfied: python-dateutil&lt;2.9,&gt;=2.8 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.8.2)
8.904 Requirement already satisfied: setuptools&lt;70.4.0,&gt;=70.3.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (70.3.0)
8.904 Requirement already satisfied: prompt-toolkit&lt;3.0.29,&gt;=3.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.0.28)
8.904 Requirement already satisfied: pydot&lt;1.5,&gt;=1.4 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.4.2)
8.904 Requirement already satisfied: aiogram&lt;2.26 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.15)
8.909 Requirement already satisfied: networkx&lt;2.7,&gt;=2.4 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.6.3)
8.909 Requirement already satisfied: randomname&lt;0.2.0,&gt;=0.1.5 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.1.5)
8.909 Requirement already satisfied: tarsafe&lt;0.0.5,&gt;=0.0.3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.0.4)
8.925 Requirement already satisfied: tensorflow==2.12.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.12.0)
8.925 Requirement already satisfied: pykwalify&lt;1.9,&gt;=1.7 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.8.0)
8.925 Requirement already satisfied: dask==2022.10.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2022.10.2)
8.925 Requirement already satisfied: rocketchat_API&lt;1.31.0,&gt;=0.6.31 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.30.0)
8.925 Requirement already satisfied: typing-extensions&lt;5.0.0,&gt;=4.1.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.7.1)
8.925 Requirement already satisfied: safetensors&lt;0.5.0,&gt;=0.4.5 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.4.5)
8.934 Requirement already satisfied: colorclass&lt;2.3,&gt;=2.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.2.2)
8.934 Requirement already satisfied: terminaltables&lt;3.2.0,&gt;=3.1.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.1.10)
8.934 Requirement already satisfied: typing-utils&lt;0.2.0,&gt;=0.1.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.1.0)
8.937 Requirement already satisfied: matplotlib&lt;3.6,&gt;=3.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.5.3)
8.937 Requirement already satisfied: ruamel.yaml&lt;0.17.22,&gt;=0.16.5 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.17.21)
8.940 Requirement already satisfied: PyJWT[crypto]&lt;3.0.0,&gt;=2.0.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.7.0)
8.953 Requirement already satisfied: sklearn-crfsuite&lt;0.4,&gt;=0.3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.3.6)
8.953 Requirement already satisfied: CacheControl&lt;0.13.0,&gt;=0.12.9 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.12.14)
8.953 Requirement already satisfied: tensorflow_hub&lt;0.14.0,&gt;=0.13.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.13.0)
8.953 Requirement already satisfied: wheel&gt;=0.38.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.40.0)
8.953 Requirement already satisfied: absl-py&lt;1.5,&gt;=0.9 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.4.0)
8.953 Requirement already satisfied: python-socketio&lt;6,&gt;=4.4 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (5.8.0)
8.966 Requirement already satisfied: SQLAlchemy&lt;1.5.0,&gt;=1.4.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.4.49)
8.966 Requirement already satisfied: structlog-sentry&lt;3.0.0,&gt;=2.0.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.0.3)
8.966 Requirement already satisfied: packaging&lt;21.0,&gt;=20.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (20.9)
8.966 Requirement already satisfied: boto3&lt;2.0.0,&gt;=1.26.136 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.27.1)
8.967 Requirement already satisfied: pyyaml&gt;=6.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (6.0.1)
8.971 Requirement already satisfied: numpy&lt;1.25.0,&gt;=1.19.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.23.5)
8.977 Requirement already satisfied: tensorflow-text==2.12.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.12.0)
8.981 Requirement already satisfied: slack-sdk&lt;4.0.0,&gt;=3.19.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.21.3)
8.981 Requirement already satisfied: tqdm&lt;5.0,&gt;=4.31 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.65.0)
8.983 Requirement already satisfied: websockets&lt;11.0,&gt;=10.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (10.4)
9.125 Collecting httplib2&lt;1.0.0,&gt;=0.19.0
9.170   Downloading httplib2-0.30.0-py3-none-any.whl (91 kB)
9.176      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 91.1/91.1 kB 207.8 MB/s eta 0:00:00
9.475 Collecting google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,&lt;3.0.0,&gt;=1.31.5
9.521   Downloading google_api_core-2.25.1-py3-none-any.whl (160 kB)
9.531      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 160.8/160.8 kB 187.9 MB/s eta 0:00:00
9.601 Collecting uritemplate&lt;5,&gt;=3.0.1
9.647   Downloading uritemplate-4.2.0-py3-none-any.whl (11 kB)
9.715 Collecting google-auth-httplib2&lt;1.0.0,&gt;=0.2.0
9.754   Downloading google_auth_httplib2-0.2.0-py2.py3-none-any.whl (9.3 kB)
9.782 Requirement already satisfied: requests-oauthlib&gt;=0.7.0 in /opt/venv/lib/python3.10/site-packages (from google-auth-oauthlib==1.0.0-&gt;-r requirements.txt (line 8)) (1.3.1)
9.913 Collecting apscheduler&lt;3.10,&gt;=3.6
9.962   Downloading APScheduler-3.6.3-py2.py3-none-any.whl (58 kB)
9.996      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 58.9/58.9 kB 105.2 MB/s eta 0:00:00
10.25 Collecting tornado==6.1
10.29   Downloading tornado-6.1.tar.gz (497 kB)
10.30      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 497.4/497.4 kB 153.1 MB/s eta 0:00:00
10.53   Preparing metadata (setup.py): started
12.01   Preparing metadata (setup.py): finished with status &#39;done&#39;
12.13 Collecting cachetools==4.2.2
12.18   Downloading cachetools-4.2.2-py3-none-any.whl (11 kB)
12.51 Collecting tzdata&gt;=2022.7
12.57   Downloading tzdata-2025.2-py2.py3-none-any.whl (347 kB)
12.57      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 347.8/347.8 kB 121.5 MB/s eta 0:00:00
12.63 Requirement already satisfied: urllib3&lt;3,&gt;=1.21.1 in /opt/venv/lib/python3.10/site-packages (from requests==2.32.4-&gt;-r requirements.txt (line 15)) (1.26.16)
12.70 Requirement already satisfied: idna&lt;4,&gt;=2.5 in /opt/venv/lib/python3.10/site-packages (from requests==2.32.4-&gt;-r requirements.txt (line 15)) (3.4)
12.70 Requirement already satisfied: charset_normalizer&lt;4,&gt;=2 in /opt/venv/lib/python3.10/site-packages (from requests==2.32.4-&gt;-r requirements.txt (line 15)) (3.1.0)
12.81 Requirement already satisfied: six&gt;=1.4.0 in /opt/venv/lib/python3.10/site-packages (from apscheduler&lt;3.10,&gt;=3.6-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.16.0)
12.81 Requirement already satisfied: tzlocal&gt;=1.2 in /opt/venv/lib/python3.10/site-packages (from apscheduler&lt;3.10,&gt;=3.6-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (5.0.1)
12.89 Requirement already satisfied: partd&gt;=0.3.10 in /opt/venv/lib/python3.10/site-packages (from dask==2022.10.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.4.0)
12.89 Requirement already satisfied: toolz&gt;=0.8.2 in /opt/venv/lib/python3.10/site-packages (from dask==2022.10.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.12.0)
12.89 Requirement already satisfied: cloudpickle&gt;=1.1.1 in /opt/venv/lib/python3.10/site-packages (from dask==2022.10.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.2.1)
12.89 Requirement already satisfied: click&gt;=7.0 in /opt/venv/lib/python3.10/site-packages (from dask==2022.10.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (8.1.3)
12.89 Requirement already satisfied: fsspec&gt;=0.6.0 in /opt/venv/lib/python3.10/site-packages (from dask==2022.10.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2023.6.0)
13.04 Requirement already satisfied: tabulate&gt;=0.8.8 in /opt/venv/lib/python3.10/site-packages (from skops==0.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.9.0)
13.05 Requirement already satisfied: huggingface-hub&gt;=0.17.0 in /opt/venv/lib/python3.10/site-packages (from skops==0.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.27.0)
13.14 Requirement already satisfied: flatbuffers&gt;=2.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (23.5.26)
13.15 Requirement already satisfied: jax&gt;=0.3.15 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.4.13)
13.16 Requirement already satisfied: termcolor&gt;=1.1.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.3.0)
13.16 Requirement already satisfied: tensorflow-estimator&lt;2.13,&gt;=2.12.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.12.0)
13.16 Requirement already satisfied: tensorboard&lt;2.13,&gt;=2.12 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.12.3)
13.16 Requirement already satisfied: astunparse&gt;=1.6.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.6.3)
13.21 Requirement already satisfied: wrapt&lt;1.15,&gt;=1.11.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.14.1)
13.21 Requirement already satisfied: keras&lt;2.13,&gt;=2.12.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.12.0)
13.21 Requirement already satisfied: google-pasta&gt;=0.1.1 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.2.0)
13.21 Requirement already satisfied: h5py&gt;=2.9.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.9.0)
13.21 Requirement already satisfied: grpcio&lt;2.0,&gt;=1.24.3 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.56.0)
13.21 Requirement already satisfied: libclang&gt;=13.0.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (16.0.0)
13.21 Requirement already satisfied: gast&lt;=0.4.0,&gt;=0.2.1 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.4.0)
13.21 Requirement already satisfied: opt-einsum&gt;=2.3.2 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.3.0)
13.28 Requirement already satisfied: aiormq~=6.4.0 in /opt/venv/lib/python3.10/site-packages (from aio-pika&lt;8.2.4,&gt;=6.7.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (6.4.2)
13.28 Requirement already satisfied: yarl in /opt/venv/lib/python3.10/site-packages (from aio-pika&lt;8.2.4,&gt;=6.7.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.9.2)
13.28 Requirement already satisfied: Babel&gt;=2.8.0 in /opt/venv/lib/python3.10/site-packages (from aiogram&lt;2.26-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.9.1)
13.31 Requirement already satisfied: multidict&lt;7.0,&gt;=4.5 in /opt/venv/lib/python3.10/site-packages (from aiohttp&lt;3.10,&gt;=3.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (5.2.0)
13.31 Requirement already satisfied: aiosignal&gt;=1.1.2 in /opt/venv/lib/python3.10/site-packages (from aiohttp&lt;3.10,&gt;=3.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.3.1)
13.31 Requirement already satisfied: frozenlist&gt;=1.1.1 in /opt/venv/lib/python3.10/site-packages (from aiohttp&lt;3.10,&gt;=3.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.3.3)
13.31 Requirement already satisfied: async-timeout&lt;5.0,&gt;=4.0 in /opt/venv/lib/python3.10/site-packages (from aiohttp&lt;3.10,&gt;=3.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.0.2)
13.37 Requirement already satisfied: jmespath&lt;2.0.0,&gt;=0.7.1 in /opt/venv/lib/python3.10/site-packages (from boto3&lt;2.0.0,&gt;=1.26.136-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.0.1)
13.37 Requirement already satisfied: botocore&lt;1.31.0,&gt;=1.30.1 in /opt/venv/lib/python3.10/site-packages (from boto3&lt;2.0.0,&gt;=1.26.136-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.30.1)
13.37 Requirement already satisfied: s3transfer&lt;0.7.0,&gt;=0.6.0 in /opt/venv/lib/python3.10/site-packages (from boto3&lt;2.0.0,&gt;=1.26.136-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.6.1)
13.38 Requirement already satisfied: msgpack&gt;=0.5.2 in /opt/venv/lib/python3.10/site-packages (from CacheControl&lt;0.13.0,&gt;=0.12.9-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.0.5)
13.41 Requirement already satisfied: humanfriendly&gt;=9.1 in /opt/venv/lib/python3.10/site-packages (from coloredlogs&lt;16,&gt;=10-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (10.0)
13.50 Requirement already satisfied: cffi&gt;=1.12 in /opt/venv/lib/python3.10/site-packages (from cryptography&gt;=41.0.7-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.15.1)
13.62 Collecting googleapis-common-protos&lt;2.0.0,&gt;=1.56.2
13.66   Downloading googleapis_common_protos-1.70.0-py3-none-any.whl (294 kB)
13.67      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 294.5/294.5 kB 213.9 MB/s eta 0:00:00
13.76 Collecting proto-plus&lt;2.0.0,&gt;=1.22.3
13.80   Downloading proto_plus-1.26.1-py3-none-any.whl (50 kB)
13.80      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 50.2/50.2 kB 146.8 MB/s eta 0:00:00
13.83 Requirement already satisfied: pyasn1-modules&gt;=0.2.1 in /opt/venv/lib/python3.10/site-packages (from google-auth&lt;3-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.3.0)
13.83 Requirement already satisfied: rsa&lt;5,&gt;=3.1.4 in /opt/venv/lib/python3.10/site-packages (from google-auth&lt;3-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.9)
13.86 Requirement already satisfied: pyparsing&lt;4,&gt;=3.0.4 in /opt/venv/lib/python3.10/site-packages (from httplib2&lt;1.0.0,&gt;=0.19.0-&gt;google-api-python-client==2.178.0-&gt;-r requirements.txt (line 7)) (3.1.0)
13.95 Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,&gt;=0.14.0 in /opt/venv/lib/python3.10/site-packages (from jsonschema&lt;4.18,&gt;=3.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.19.3)
13.97 Requirement already satisfied: cycler&gt;=0.10 in /opt/venv/lib/python3.10/site-packages (from matplotlib&lt;3.6,&gt;=3.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.11.0)
13.97 Requirement already satisfied: pillow&gt;=6.2.0 in /opt/venv/lib/python3.10/site-packages (from matplotlib&lt;3.6,&gt;=3.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (10.0.1)
13.98 Requirement already satisfied: kiwisolver&gt;=1.0.1 in /opt/venv/lib/python3.10/site-packages (from matplotlib&lt;3.6,&gt;=3.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.4.4)
13.98 Requirement already satisfied: fonttools&gt;=4.22.0 in /opt/venv/lib/python3.10/site-packages (from matplotlib&lt;3.6,&gt;=3.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.40.0)
14.06 Requirement already satisfied: wcwidth in /opt/venv/lib/python3.10/site-packages (from prompt-toolkit&lt;3.0.29,&gt;=3.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.2.6)
14.13 Requirement already satisfied: docopt&gt;=0.6.2 in /opt/venv/lib/python3.10/site-packages (from pykwalify&lt;1.9,&gt;=1.7-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.6.2)
14.20 Requirement already satisfied: bidict&gt;=0.21.0 in /opt/venv/lib/python3.10/site-packages (from python-socketio&lt;6,&gt;=4.4-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.22.1)
14.25 Requirement already satisfied: fire in /opt/venv/lib/python3.10/site-packages (from randomname&lt;0.2.0,&gt;=0.1.5-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.5.0)
14.29 Requirement already satisfied: oauthlib&gt;=3.0.0 in /opt/venv/lib/python3.10/site-packages (from requests-oauthlib&gt;=0.7.0-&gt;google-auth-oauthlib==1.0.0-&gt;-r requirements.txt (line 8)) (3.2.2)
14.33 Requirement already satisfied: ruamel.yaml.clib&gt;=0.2.6 in /opt/venv/lib/python3.10/site-packages (from ruamel.yaml&lt;0.17.22,&gt;=0.16.5-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.2.7)
14.48 Requirement already satisfied: uvloop&gt;=0.5.3 in /opt/venv/lib/python3.10/site-packages (from sanic&lt;21.13,&gt;=21.12-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.17.0)
14.48 Requirement already satisfied: httptools&gt;=0.0.10 in /opt/venv/lib/python3.10/site-packages (from sanic&lt;21.13,&gt;=21.12-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.5.0)
14.48 Requirement already satisfied: aiofiles&gt;=0.6.0 in /opt/venv/lib/python3.10/site-packages (from sanic&lt;21.13,&gt;=21.12-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (23.1.0)
14.57 Requirement already satisfied: threadpoolctl&gt;=2.0.0 in /opt/venv/lib/python3.10/site-packages (from scikit-learn&lt;1.2,&gt;=0.22-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.1.0)
14.58 Requirement already satisfied: joblib&gt;=1.0.0 in /opt/venv/lib/python3.10/site-packages (from scikit-learn&lt;1.2,&gt;=0.22-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.4.2)
14.68 Requirement already satisfied: python-crfsuite&gt;=0.8.3 in /opt/venv/lib/python3.10/site-packages (from sklearn-crfsuite&lt;0.4,&gt;=0.3-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.9.9)
14.81 Requirement already satisfied: greenlet!=0.4.17 in /opt/venv/lib/python3.10/site-packages (from SQLAlchemy&lt;1.5.0,&gt;=1.4.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.0.2)
14.93 Requirement already satisfied: aiohttp-retry&gt;=2.8.3 in /opt/venv/lib/python3.10/site-packages (from twilio&lt;8.3,&gt;=6.26-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.8.3)
15.12 Requirement already satisfied: future in /opt/venv/lib/python3.10/site-packages (from webexteamssdk&lt;1.7.0,&gt;=1.1.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.18.3)
15.13 Requirement already satisfied: requests-toolbelt in /opt/venv/lib/python3.10/site-packages (from webexteamssdk&lt;1.7.0,&gt;=1.1.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.0.0)
15.21 Requirement already satisfied: pamqp==3.2.1 in /opt/venv/lib/python3.10/site-packages (from aiormq~=6.4.0-&gt;aio-pika&lt;8.2.4,&gt;=6.7.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.2.1)
15.34 Requirement already satisfied: pycparser in /opt/venv/lib/python3.10/site-packages (from cffi&gt;=1.12-&gt;cryptography&gt;=41.0.7-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.21)
15.76 Requirement already satisfied: filelock in /opt/venv/lib/python3.10/site-packages (from huggingface-hub&gt;=0.17.0-&gt;skops==0.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.12.2)
15.83 Requirement already satisfied: ml_dtypes&gt;=0.1.0 in /opt/venv/lib/python3.10/site-packages (from jax&gt;=0.3.15-&gt;tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.2.0)
16.01 Requirement already satisfied: locket in /opt/venv/lib/python3.10/site-packages (from partd&gt;=0.3.10-&gt;dask==2022.10.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.0.0)
16.08 Requirement already satisfied: pyasn1&lt;0.6.0,&gt;=0.4.6 in /opt/venv/lib/python3.10/site-packages (from pyasn1-modules&gt;=0.2.1-&gt;google-auth&lt;3-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.5.0)
16.25 Requirement already satisfied: markdown&gt;=2.6.8 in /opt/venv/lib/python3.10/site-packages (from tensorboard&lt;2.13,&gt;=2.12-&gt;tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.4.3)
16.26 Requirement already satisfied: werkzeug&gt;=1.0.1 in /opt/venv/lib/python3.10/site-packages (from tensorboard&lt;2.13,&gt;=2.12-&gt;tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.3.6)
16.27 Requirement already satisfied: tensorboard-data-server&lt;0.8.0,&gt;=0.7.0 in /opt/venv/lib/python3.10/site-packages (from tensorboard&lt;2.13,&gt;=2.12-&gt;tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.7.1)
16.65 Requirement already satisfied: MarkupSafe&gt;=2.1.1 in /opt/venv/lib/python3.10/site-packages (from werkzeug&gt;=1.0.1-&gt;tensorboard&lt;2.13,&gt;=2.12-&gt;tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.1.3)
16.82 Building wheels for collected packages: tornado
16.82   Building wheel for tornado (setup.py): started
18.65   Building wheel for tornado (setup.py): finished with status &#39;done&#39;
18.65   Created wheel for tornado: filename=tornado-6.1-cp310-cp310-linux_x86_64.whl size=421980 sha256=deac15aa8f5bcd31fe5eaa3b332f80a0099e953e46561e2826385869c5105a1f
18.65   Stored in directory: /tmp/pip-ephem-wheel-cache-3blf1ho9/wheels/34/83/69/b89863a68e62add6e149dbaadcc049886105ce2405c1979bf2
18.66 Successfully built tornado
18.99 Installing collected packages: uritemplate, tzdata, tornado, requests, pydantic, psycopg2-binary, proto-plus, httplib2, googleapis-common-protos, cachetools, apscheduler, python-telegram-bot, pandas, google-auth-httplib2, google-api-core, gspread, google-api-python-client
18.99 ERROR: Could not install packages due to an OSError: [Errno 13] Permission denied: &#39;/opt/venv/lib/python3.10/site-packages/uritemplate&#39;
18.99 Check the permissions.
18.99 
19.89 
19.89 [notice] A new release of pip available: 22.3.1 -&gt; 25.2
19.89 [notice] To update, run: pip install --upgrade pip
------
failed to solve: process &quot;/bin/bash -o pipefail -c pip install --no-cache-dir -r requirements.txt&quot; did not complete successfully: exit code: 1
✅ Deployment complete!

📊 Service Status:
NAME      IMAGE     COMMAND   SERVICE   CREATED   STATUS    PORTS

🌐 Your services are running on:
- Rasa Server: http://your-azure-vm-ip:80
- Action Server: http://your-azure-vm-ip:5055
- Telegram Bridge: http://your-azure-vm-ip:5006

📝 To check logs: docker-compose -f azure-compose.yml logs -f
🛑 To stop services: docker-compose -f azure-compose.yml down

---

The issue is that the Rasa base image has a pre-configured virtual environment that's causing permission conflicts. Let's create a simple solution by using a different approach - install packages as root and then switch user:

---

Fixing the Rasa Dockerfile by installing as root and then switching to the rasa user

---

Also fix the actions Dockerfile:

---

Reverting actions Dockerfile to use python:3.9-slim and install as root

---

Fix the CMD back to use rasa:

---

Fixing CMD to use rasa command directly

---


Now rebuild:

```bash
docker system prune -f
./deploy-azure.sh
```

---

same error i tried many ways

---

Let's try a completely different approach. The issue is with the virtual environment permissions. Let's create a simple requirements file with only essential packages and skip the problematic ones:

---

The requirements.txt file has encoding issues. Let's create a clean one:

---

Creating a clean requirements.txt file without encoding issues

---

Now let's try a different approach - use the official Rasa image but install packages in the system Python instead of the virtual environment:

---

Installing packages in system Python to avoid virtual environment permission issues

---


Now rebuild:

```bash
docker system prune -f
./deploy-azure.sh
```

---

in my files why so many .sh files are preesent

---

Let me check what .sh files are in your project:

---


You have several .sh files for different deployment and setup purposes:

1. **azure-student-deploy.sh** - Deployment script for Azure Student accounts
2. **build.sh** - Build script for the project
3. **complete-setup.sh** - Complete setup automation script
4. **deploy-azure.sh** - Main Azure deployment script (the one you're using)
5. **run-local.sh** - Script to run the project locally

These are automation scripts to make deployment and setup easier. You only need to use the relevant one for your purpose. For Azure deployment, you're using `deploy-azure.sh` which is correct.

You can remove the unused ones if you want:

```bash
# Keep only the ones you need
rm azure-student-deploy.sh build.sh complete-setup.sh run-local.sh
```

But they're not causing any issues - they're just there for convenience.

---

16.70 Requirement already satisfied: ml_dtypes&gt;=0.1.0 in /opt/venv/lib/python3.10/site-packages (from jax&gt;=0.3.15-&gt;tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.2.0)
16.88 Requirement already satisfied: locket in /opt/venv/lib/python3.10/site-packages (from partd&gt;=0.3.10-&gt;dask==2022.10.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.0.0)
16.97 Requirement already satisfied: pyasn1&lt;0.6.0,&gt;=0.4.6 in /opt/venv/lib/python3.10/site-packages (from pyasn1-modules&gt;=0.2.1-&gt;google-auth&lt;3-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.5.0)
17.15 Requirement already satisfied: tensorboard-data-server&lt;0.8.0,&gt;=0.7.0 in /opt/venv/lib/python3.10/site-packages (from tensorboard&lt;2.13,&gt;=2.12-&gt;tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.7.1)
17.15 Requirement already satisfied: markdown&gt;=2.6.8 in /opt/venv/lib/python3.10/site-packages (from tensorboard&lt;2.13,&gt;=2.12-&gt;tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.4.3)
17.15 Requirement already satisfied: werkzeug&gt;=1.0.1 in /opt/venv/lib/python3.10/site-packages (from tensorboard&lt;2.13,&gt;=2.12-&gt;tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.3.6)
17.57 Requirement already satisfied: MarkupSafe&gt;=2.1.1 in /opt/venv/lib/python3.10/site-packages (from werkzeug&gt;=1.0.1-&gt;tensorboard&lt;2.13,&gt;=2.12-&gt;tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.1.3)
17.74 Building wheels for collected packages: tornado
17.74   Building wheel for tornado (setup.py): started
19.25   Building wheel for tornado (setup.py): finished with status &#39;done&#39;
19.25   Created wheel for tornado: filename=tornado-6.1-cp310-cp310-linux_x86_64.whl size=421980 sha256=1f7e010ea49bfb85e28b70aabf79b671ed18daf09dd991f068b114d4b2f6194d
19.25   Stored in directory: /tmp/pip-ephem-wheel-cache-e_pdiy3t/wheels/34/83/69/b89863a68e62add6e149dbaadcc049886105ce2405c1979bf2
19.26 Successfully built tornado
19.57 Installing collected packages: uritemplate, tzdata, tornado, requests, pydantic, psycopg2-binary, proto-plus, httplib2, googleapis-common-protos, cachetools, apscheduler, python-telegram-bot, pandas, google-auth-httplib2, google-api-core, gspread, google-api-python-client
19.57 ERROR: Could not install packages due to an OSError: [Errno 13] Permission denied: &#39;/opt/venv/lib/python3.10/site-packages/uritemplate&#39;
19.57 Check the permissions.
19.57 
20.46 
20.46 [notice] A new release of pip available: 22.3.1 -&gt; 25.2
20.46 [notice] To update, run: pip install --upgrade pip
------
failed to solve: process &quot;/bin/bash -o pipefail -c pip install --no-cache-dir -r requirements.txt&quot; did not complete successfully: exit code: 1
✅ Deployment complete!

📊 Service Status:
NAME      IMAGE     COMMAND   SERVICE   CREATED   STATUS    PORTS

🌐 Your services are running on:
- Rasa Server: http://your-azure-vm-ip:80
- Action Server: http://your-azure-vm-ip:5055
- Telegram Bridge: http://your-azure-vm-ip:5006

📝 To check logs: docker-compose -f azure-compose.yml logs -f
🛑 To stop services: docker-compose -f azure-compose.yml down

---

The issue persists. Let's try a final approach - change the ownership of the virtual environment directory before installing:

---

Changing ownership of the virtual environment directory to fix permission issues

---

Now rebuild:

```bash
docker system prune -f
./deploy-azure.sh
```

If this still fails, let's create a minimal requirements.txt with only essential packages:

---

Creating a minimal requirements file with only essential packages

---


If the current approach fails, change the Dockerfile to use the minimal requirements:

```dockerfile
COPY requirements-minimal.txt requirements.txt
```

---

8.54 Installing collected packages: uritemplate, tzdata, tornado, requests, pydantic, psycopg2-binary, proto-plus, httplib2, googleapis-common-protos, cachetools, apscheduler, python-telegram-bot, pandas, google-auth-httplib2, google-api-core, gspread, google-api-python-client
18.55 ERROR: Could not install packages due to an OSError: [Errno 13] Permission denied: &#39;/opt/venv/lib/python3.10/site-packages/uritemplate&#39;
18.55 Check the permissions.
18.55 

again same error

---

Let's try a completely different approach - use a base Python image instead of the Rasa image and install Rasa manually:

---

Using base Python image instead of Rasa image to avoid virtual environment issues

---


Now rebuild:

```bash
docker system prune -f
./deploy-azure.sh
```

This should work since we're using a clean Python image without any pre-configured virtual environments.

---

12.73 ERROR: Could not install packages due to an OSError: [Errno 13] Permission denied: &#39;/opt/venv/lib/python3.10/site-packages/uritemplate&#39;


in vm creation i use ubuntu 22 version

---

The issue is that even the base Python image has a virtual environment. Let's use Ubuntu 22.04 base image since that's what your VM uses:

---

Using Ubuntu 22.04 base image to match your VM and avoid virtual environment issues

---

Also update the CMD to use python3:

---

Updating CMD to use python3 and rasa module

---


Now rebuild:

```bash
docker system prune -f
./deploy-azure.sh
```

---

azureuser@Remindbot:~/Remind_Bot/Remind_Bot$ docker system prune -f
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Head &quot;http://%2Fvar%2Frun%2Fdocker.sock/_ping&quot;: dial unix /var/run/docker.sock: connect: permission denied

---


You need to add your user to the docker group and restart the session. Run these commands:

```bash
# Add user to docker group
sudo usermod -aG docker $USER

# Apply group changes
newgrp docker

# Or logout and login again
exit
# Then SSH back in

# Then try the commands
docker system prune -f
./deploy-azure.sh
```

Alternatively, you can run with sudo:

```bash
sudo docker system prune -f
sudo ./deploy-azure.sh
```

---

nothing changes same error do you name need any info about the vm i created in azure if you want guide me to get the details

---

getaddrinfo EAI_AGAIN codewhisperer.us-east-1.amazonaws.com

---

nothing changes same error do you name need any info about the vm i created in azure if you want guide me to get the details

---


Let's check your Docker setup and get VM details. Run these commands to diagnose:

```bash
# Check Docker service status
sudo systemctl status docker

# Check if Docker daemon is running
sudo docker ps

# Check your user groups
groups

# Check Docker socket permissions
ls -la /var/run/docker.sock

# Get VM details
uname -a
cat /etc/os-release
```

Also, let's get your Azure VM configuration:

```bash
# Check VM metadata
curl -H Metadata:true "http://169.254.169.254/metadata/instance?api-version=2021-02-01" | jq '.'
```

If jq is not installed:
```bash
curl -H Metadata:true "http://169.254.169.254/metadata/instance?api-version=2021-02-01"
```

This will help me understand your VM setup and fix the Docker permission issue.

---

azureuser@Remindbot:~/Remind_Bot/Remind_Bot$ sudo systemctl status docker
● docker.service - Docker Application Container Engine
     Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
     Active: active (running) since Wed 2025-09-10 08:02:33 UTC; 1h 13min ago
TriggeredBy: ● docker.socket
       Docs: https://docs.docker.com
   Main PID: 16364 (dockerd)
      Tasks: 11
     Memory: 274.6M
        CPU: 11min 1.822s
     CGroup: /system.slice/docker.service
             └─16364 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock

---


Docker is running fine. The issue is user permissions. Let's fix it:

```bash
# Check current groups
groups

# Check docker socket permissions
ls -la /var/run/docker.sock

# Add user to docker group (if not already done)
sudo usermod -aG docker azureuser

# Change socket permissions temporarily
sudo chmod 666 /var/run/docker.sock

# Test docker without sudo
docker ps

# If that works, run your deployment
./deploy-azure.sh
```

The `chmod 666` command will temporarily fix the socket permissions. After this works, you should logout and login again to make the group membership permanent.

---

azureuser@Remindbot:~/Remind_Bot/Remind_Bot$ sudo docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
azureuser@Remindbot:~/Remind_Bot/Remind_Bot$ ^C

groups:
docker azureuser

srw-rw---- 1 root docker 0 Sep 10 08:02 /var/run/docker.sock

azureuser@Remindbot:~/Remind_Bot/Remind_Bot$ uname -a
cat /etc/os-release
Linux Remindbot 6.8.0-1031-azure #36~22.04.1-Ubuntu SMP Tue Jul  1 03:54:01 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux
PRETTY_NAME=&quot;Ubuntu 22.04.5 LTS&quot;
NAME=&quot;Ubuntu&quot;
VERSION_ID=&quot;22.04&quot;
VERSION=&quot;22.04.5 LTS (Jammy Jellyfish)&quot;
VERSION_CODENAME=jammy
ID=ubuntu
ID_LIKE=debian
HOME_URL=&quot;https://www.ubuntu.com/&quot;
SUPPORT_URL=&quot;https://help.ubuntu.com/&quot;
BUG_REPORT_URL=&quot;https://bugs.launchpad.net/ubuntu/&quot;
PRIVACY_POLICY_URL=&quot;https://www.ubuntu.com/legal/terms-and-policies/privacy-policy&quot;
UBUNTU_CODENAME=jammy

---

getaddrinfo EAI_AGAIN codewhisperer.us-east-1.amazonaws.com

---

azureuser@Remindbot:/Remind_Bot/Remind_Bot$ sudo docker ps
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
azureuser@Remindbot:/Remind_Bot/Remind_Bot$ ^C

groups:
docker azureuser

srw-rw---- 1 root docker 0 Sep 10 08:02 /var/run/docker.sock

azureuser@Remindbot:/Remind_Bot/Remind_Bot$ uname -a
cat /etc/os-release
Linux Remindbot 6.8.0-1031-azure #3622.04.1-Ubuntu SMP Tue Jul 1 03:54:01 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux
PRETTY_NAME=&quot;Ubuntu 22.04.5 LTS&quot;
NAME=&quot;Ubuntu&quot;
VERSION_ID=&quot;22.04&quot;
VERSION=&quot;22.04.5 LTS (Jammy Jellyfish)&quot;
VERSION_CODENAME=jammy
ID=ubuntu
ID_LIKE=debian
HOME_URL=&quot;https://www.ubuntu.com/&quot;
SUPPORT_URL=&quot;https://help.ubuntu.com/&quot;
BUG_REPORT_URL=&quot;https://bugs.launchpad.net/ubuntu/&quot;
PRIVACY_POLICY_URL=&quot;https://www.ubuntu.com/legal/terms-and-policies/privacy-policy&quot;
UBUNTU_CODENAME=jammy

---


Good! You're already in the docker group and Docker is running. The socket permissions look correct. Let's try running Docker commands without sudo:

```bash
# Test docker access
docker ps

# If that works, navigate to your project directory
cd ~/Remind_Bot/Remind_Bot

# Clean up and deploy
docker system prune -f
./deploy-azure.sh
```

If you still get permission denied, try:

```bash
# Restart Docker service
sudo systemctl restart docker

# Then try again
docker ps
./deploy-azure.sh
```

The issue might be that your current shell session doesn't recognize the group membership. If it still doesn't work, logout and SSH back in to refresh your session.

---

docker ps

after ruuning this can you show me example output

---


When you run `docker ps`, you should see output like this:

**If no containers are running:**
```
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

**If containers are running:**
```
CONTAINER ID   IMAGE                    COMMAND                  CREATED          STATUS          PORTS                    NAMES
abc123def456   nginx:latest            "/docker-entrypoint.…"   2 minutes ago    Up 2 minutes    0.0.0.0:80->80/tcp      web-server
def789ghi012   postgres:13             "docker-entrypoint.s…"   5 minutes ago    Up 5 minutes    0.0.0.0:5432->5432/tcp  database
```

**If you get permission denied:**
```
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/containers/json": dial unix /var/run/docker.sock: connect: permission denied
```

Run `docker ps` now and tell me what output you get. This will help determine if Docker access is working properly.

---

zureuser@Remindbot:~/Remind_Bot/Remind_Bot$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
azureuser@Remindbot:~/Remind_Bot/Remind_Bot$ ^C


no data is shown under the labels

---


Perfect! That's the correct output - it shows no containers are currently running, which is expected. Docker is working properly.

Now let's run your deployment:

```bash
# Clean up any previous failed builds
docker system prune -f

# Run the deployment script
./deploy-azure.sh
```

This should now work since Docker permissions are correct and we've fixed the Dockerfile to use Ubuntu 22.04 base image.

---

zureuser@Remindbot:~/Remind_Bot/Remind_Bot$ ./deploy-azure.sh
🚀 Starting Azure deployment for Rasa chatbot...
✅ Environment variables loaded
🔨 Building Docker images...
[+] Building 128.8s (19/22)                                                                                                                docker:default
 =&gt; [action-server internal] load build definition from Dockerfile.actions                                                                           0.1s
 =&gt; =&gt; transferring dockerfile: 297B                                                                                                                 0.0s
 =&gt; [action-server internal] load metadata for docker.io/library/python:3.9-slim                                                                     1.9s
 =&gt; [action-server internal] load .dockerignore                                                                                                      0.1s
 =&gt; =&gt; transferring context: 154B                                                                                                                    0.0s
 =&gt; [action-server 1/6] FROM docker.io/library/python:3.9-slim@sha256:71b97a8eed69cddd132431327ff7c204fd6ea3d38e0c5d11d52f9661482bc8a3               0.0s
 =&gt; [action-server internal] load build context                                                                                                      0.1s
 =&gt; =&gt; transferring context: 48.36kB                                                                                                                 0.0s
 =&gt; CACHED [action-server 2/6] WORKDIR /app                                                                                                          0.0s
 =&gt; CACHED [action-server 3/6] COPY requirements.txt .                                                                                               0.0s
 =&gt; CACHED [action-server 4/6] RUN pip install --no-cache-dir -r requirements.txt                                                                    0.0s
 =&gt; CACHED [action-server 5/6] COPY actions/ ./actions/                                                                                              0.0s
 =&gt; CACHED [action-server 6/6] COPY config.json .                                                                                                    0.0s
 =&gt; [action-server] exporting to image                                                                                                               0.1s
 =&gt; =&gt; exporting layers                                                                                                                              0.0s
 =&gt; =&gt; writing image sha256:3e08a80b14c893d646808f174d20118a5fc8f536130d6fd773d6b9e7095abd25                                                         0.0s
 =&gt; =&gt; naming to docker.io/library/remind_bot-action-server                                                                                          0.0s
 =&gt; [rasa-server internal] load build definition from Dockerfile.rasa                                                                                0.0s
 =&gt; =&gt; transferring dockerfile: 344B                                                                                                                 0.0s
 =&gt; [rasa-server internal] load metadata for docker.io/rasa/rasa:3.6.21                                                                              2.4s
 =&gt; [rasa-server internal] load .dockerignore                                                                                                        0.0s
 =&gt; =&gt; transferring context: 154B                                                                                                                    0.0s
 =&gt; [rasa-server 1/7] FROM docker.io/rasa/rasa:3.6.21@sha256:7c0204065d4859e1b7a691c972ca3d26f5d39ad23fbd992b654084721226d813                      107.0s
 =&gt; =&gt; resolve docker.io/rasa/rasa:3.6.21@sha256:7c0204065d4859e1b7a691c972ca3d26f5d39ad23fbd992b654084721226d813                                    0.1s
 =&gt; =&gt; sha256:7c0204065d4859e1b7a691c972ca3d26f5d39ad23fbd992b654084721226d813 1.61kB / 1.61kB                                                       0.0s
 =&gt; =&gt; sha256:445a6a12be2be54b4da18d7c77d4a41bc4746bc422f1f4325a60ff4fc7ea2e5d 29.54MB / 29.54MB                                                     1.0s
 =&gt; =&gt; sha256:0e5aa551ea881f1b6fcfab87032007ac64da8563632b87173b618b086a7a0cf0 1.82kB / 1.82kB                                                       0.0s
 =&gt; =&gt; sha256:e4ea2b9d9dc38044ee4038855f5593313ecfcb0a3c652cf686c3f85b9b93ec63 6.96kB / 6.96kB                                                       0.0s
 =&gt; =&gt; sha256:50532f3355eccaa7f184475b4da83a263ac11f86cc1c6618d28b6567c3fe7675 284.83MB / 284.83MB                                                  10.1s
 =&gt; =&gt; sha256:24e4804a1dbf7990aa9d9ec6e01b2a56aadfdfb721f7c1c1f9207adfe2943052 1.46MB / 1.46MB                                                       1.0s
 =&gt; =&gt; extracting sha256:445a6a12be2be54b4da18d7c77d4a41bc4746bc422f1f4325a60ff4fc7ea2e5d                                                           21.6s
 =&gt; =&gt; sha256:5c0e8d16e4048876e4b65942adc6035d36abd48d50643659e6e8b25d12c641c9 1.09kB / 1.09kB                                                       1.5s
 =&gt; =&gt; sha256:01639847809681d4e0ac6dad6d2efcfe1fc34aa0b0d46dfc5bd9d41483e01c7b 4.22kB / 4.22kB                                                       1.4s
 =&gt; =&gt; sha256:01029823f2260f38ea9d97d01059d16f7184edee64e335ce1811fa611380484d 807.93MB / 807.93MB                                                  22.4s
 =&gt; =&gt; sha256:4f4fb700ef54461cfa02571ae0db9a0dc1e0cdb5577484a6d75e68dc38e8acc1 32B / 32B                                                             2.3s
 =&gt; =&gt; sha256:903b9bd8420885647ab87a8d4beb3496b9d79835baf6ba9086470c0caa4cb631 2.30kB / 2.30kB                                                       2.8s
 =&gt; =&gt; extracting sha256:50532f3355eccaa7f184475b4da83a263ac11f86cc1c6618d28b6567c3fe7675                                                           20.7s
 =&gt; =&gt; extracting sha256:24e4804a1dbf7990aa9d9ec6e01b2a56aadfdfb721f7c1c1f9207adfe2943052                                                            0.2s
 =&gt; =&gt; extracting sha256:5c0e8d16e4048876e4b65942adc6035d36abd48d50643659e6e8b25d12c641c9                                                            0.0s
 =&gt; =&gt; extracting sha256:01639847809681d4e0ac6dad6d2efcfe1fc34aa0b0d46dfc5bd9d41483e01c7b                                                            0.0s
 =&gt; =&gt; extracting sha256:01029823f2260f38ea9d97d01059d16f7184edee64e335ce1811fa611380484d                                                           60.7s
 =&gt; =&gt; extracting sha256:4f4fb700ef54461cfa02571ae0db9a0dc1e0cdb5577484a6d75e68dc38e8acc1                                                            0.0s
 =&gt; =&gt; extracting sha256:903b9bd8420885647ab87a8d4beb3496b9d79835baf6ba9086470c0caa4cb631                                                            0.0s
 =&gt; [rasa-server internal] load build context                                                                                                        0.1s
 =&gt; =&gt; transferring context: 81.65kB                                                                                                                 0.0s
 =&gt; [rasa-server 2/7] WORKDIR /app                                                                                                                   0.2s
 =&gt; [rasa-server 3/7] COPY requirements.txt .                                                                                                        0.1s
 =&gt; ERROR [rasa-server 4/7] RUN pip install --no-cache-dir -r requirements.txt                                                                      15.9s
------
 &gt; [rasa-server 4/7] RUN pip install --no-cache-dir -r requirements.txt:
2.261 Requirement already satisfied: rasa==3.6.21 in /opt/venv/lib/python3.10/site-packages (from -r requirements.txt (line 2)) (3.6.21)
2.268 Requirement already satisfied: rasa-sdk==3.6.2 in /opt/venv/lib/python3.10/site-packages (from -r requirements.txt (line 3)) (3.6.2)
2.899 Collecting gspread==6.2.1
3.247   Downloading gspread-6.2.1-py3-none-any.whl (59 kB)
3.347      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 60.0/60.0 kB 554.3 kB/s eta 0:00:00
3.609 Collecting google-api-python-client==2.178.0
3.689   Downloading google_api_python_client-2.178.0-py3-none-any.whl (13.8 MB)
4.316      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 13.8/13.8 MB 43.9 MB/s eta 0:00:00
4.379 Requirement already satisfied: google-auth-oauthlib==1.0.0 in /opt/venv/lib/python3.10/site-packages (from -r requirements.txt (line 8)) (1.0.0)
4.498 Collecting python-telegram-bot==13.15
4.582   Downloading python_telegram_bot-13.15-py3-none-any.whl (519 kB)
4.588      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 519.2/519.2 kB 188.0 MB/s eta 0:00:00
5.036 Collecting pandas==2.3.1
5.076   Downloading pandas-2.3.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (12.3 MB)
5.203      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.3/12.3 MB 96.0 MB/s eta 0:00:00
5.366 Collecting requests==2.32.4
5.405   Downloading requests-2.32.4-py3-none-any.whl (64 kB)
5.409      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 64.8/64.8 kB 170.6 MB/s eta 0:00:00
5.673 Collecting psycopg2-binary==2.9.10
5.715   Downloading psycopg2_binary-2.9.10-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.0 MB)
5.742      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.0/3.0 MB 133.8 MB/s eta 0:00:00
5.941 Requirement already satisfied: fbmessenger&lt;6.1.0,&gt;=6.0.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (6.0.0)
5.945 Requirement already satisfied: jsonpickle&lt;3.1,&gt;=1.3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.0.4)
5.946 Requirement already satisfied: packaging&lt;21.0,&gt;=20.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (20.9)
5.947 Requirement already satisfied: rocketchat_API&lt;1.31.0,&gt;=0.6.31 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.30.0)
5.950 Requirement already satisfied: pymongo[srv,tls]&lt;4.4,&gt;=3.8 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.3.3)
5.950 Requirement already satisfied: sentry-sdk&lt;1.15.0,&gt;=0.17.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.14.0)
5.952 Requirement already satisfied: python-dateutil&lt;2.9,&gt;=2.8 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.8.2)
5.953 Requirement already satisfied: portalocker&lt;3.0.0,&gt;=2.7.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.7.0)
5.956 Requirement already satisfied: python-socketio&lt;6,&gt;=4.4 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (5.8.0)
5.956 Requirement already satisfied: ruamel.yaml&lt;0.17.22,&gt;=0.16.5 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.17.21)
5.958 Requirement already satisfied: webexteamssdk&lt;1.7.0,&gt;=1.1.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.6.1)
5.960 Requirement already satisfied: PyJWT[crypto]&lt;3.0.0,&gt;=2.0.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.7.0)
5.961 Requirement already satisfied: coloredlogs&lt;16,&gt;=10 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (15.0.1)
5.963 Requirement already satisfied: sanic-jwt&lt;2.0.0,&gt;=1.6.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.8.0)
5.964 Requirement already satisfied: typing-extensions&lt;5.0.0,&gt;=4.1.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.7.1)
5.965 Requirement already satisfied: pydot&lt;1.5,&gt;=1.4 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.4.2)
5.967 Requirement already satisfied: google-auth&lt;3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.21.0)
5.970 Requirement already satisfied: dask==2022.10.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2022.10.2)
5.971 Requirement already satisfied: tensorflow_hub&lt;0.14.0,&gt;=0.13.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.13.0)
5.973 Requirement already satisfied: safetensors&lt;0.5.0,&gt;=0.4.5 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.4.5)
5.974 Requirement already satisfied: sanic-cors&lt;2.1.0,&gt;=2.0.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.0.1)
5.975 Requirement already satisfied: pyyaml&gt;=6.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (6.0.1)
6.452 Collecting pydantic&lt;1.10.10
6.492   Downloading pydantic-1.10.9-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.1 MB)
6.512      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.1/3.1 MB 190.2 MB/s eta 0:00:00
6.528 Requirement already satisfied: apscheduler&lt;3.10,&gt;=3.6 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.9.1.post1)
6.529 Requirement already satisfied: tarsafe&lt;0.0.5,&gt;=0.0.3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.0.4)
6.531 Requirement already satisfied: structlog-sentry&lt;3.0.0,&gt;=2.0.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.0.3)
6.532 Requirement already satisfied: networkx&lt;2.7,&gt;=2.4 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.6.3)
6.533 Requirement already satisfied: confluent-kafka&lt;3.0.0,&gt;=1.9.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.1.1)
6.534 Requirement already satisfied: twilio&lt;8.3,&gt;=6.26 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (8.2.2)
6.539 Requirement already satisfied: pytz&lt;2023.0,&gt;=2019.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2022.7.1)
6.540 Requirement already satisfied: sklearn-crfsuite&lt;0.4,&gt;=0.3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.3.6)
6.542 Requirement already satisfied: terminaltables&lt;3.2.0,&gt;=3.1.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.1.10)
6.543 Requirement already satisfied: sanic&lt;21.13,&gt;=21.12 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (21.12.2)
6.545 Requirement already satisfied: ujson&lt;6.0,&gt;=1.35 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (5.8.0)
6.546 Requirement already satisfied: SQLAlchemy&lt;1.5.0,&gt;=1.4.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.4.49)
6.550 Requirement already satisfied: tensorflow-io-gcs-filesystem==0.32 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.32.0)
6.550 Requirement already satisfied: aiogram&lt;2.26 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.15)
6.551 Requirement already satisfied: pykwalify&lt;1.9,&gt;=1.7 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.8.0)
6.556 Requirement already satisfied: tensorflow-text==2.12.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.12.0)
6.558 Requirement already satisfied: tqdm&lt;5.0,&gt;=4.31 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.65.0)
6.560 Requirement already satisfied: redis&lt;5.0,&gt;=4.5.3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.6.0)
6.561 Requirement already satisfied: typing-utils&lt;0.2.0,&gt;=0.1.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.1.0)
6.579 Requirement already satisfied: absl-py&lt;1.5,&gt;=0.9 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.4.0)
6.580 Requirement already satisfied: CacheControl&lt;0.13.0,&gt;=0.12.9 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.12.14)
6.583 Requirement already satisfied: numpy&lt;1.25.0,&gt;=1.19.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.23.5)
6.585 Requirement already satisfied: wheel&gt;=0.38.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.40.0)
6.587 Requirement already satisfied: dnspython==2.3.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.3.0)
6.589 Requirement already satisfied: skops==0.9.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.9.0)
6.589 Requirement already satisfied: randomname&lt;0.2.0,&gt;=0.1.5 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.1.5)
6.591 Requirement already satisfied: scikit-learn&lt;1.2,&gt;=0.22 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.1.3)
6.593 Requirement already satisfied: sanic-routing&lt;0.8.0,&gt;=0.7.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.7.2)
6.595 Requirement already satisfied: tensorflow==2.12.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.12.0)
6.597 Requirement already satisfied: matplotlib&lt;3.6,&gt;=3.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.5.3)
6.598 Requirement already satisfied: prompt-toolkit&lt;3.0.29,&gt;=3.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.0.28)
6.600 Requirement already satisfied: colorclass&lt;2.3,&gt;=2.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.2.2)
6.601 Requirement already satisfied: protobuf&lt;4.23.4,&gt;=4.23.3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.23.3)
6.603 Requirement already satisfied: slack-sdk&lt;4.0.0,&gt;=3.19.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.21.3)
6.606 Requirement already satisfied: boto3&lt;2.0.0,&gt;=1.26.136 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.27.1)
6.608 Requirement already satisfied: python-engineio!=5.0.0,&lt;6,&gt;=4 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.5.1)
6.609 Requirement already satisfied: structlog&lt;24.0.0,&gt;=23.1.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (23.1.0)
6.611 Requirement already satisfied: websockets&lt;11.0,&gt;=10.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (10.4)
6.612 Requirement already satisfied: pluggy&lt;2.0.0,&gt;=1.0.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.2.0)
6.613 Requirement already satisfied: mattermostwrapper&lt;2.3,&gt;=2.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.2)
6.615 Requirement already satisfied: cryptography&gt;=41.0.7 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (41.0.7)
6.616 Requirement already satisfied: questionary&lt;1.11.0,&gt;=1.5.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.10.0)
6.618 Requirement already satisfied: setuptools&lt;70.4.0,&gt;=70.3.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (70.3.0)
6.621 Requirement already satisfied: aiohttp&lt;3.10,&gt;=3.9.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.9.3)
6.621 Requirement already satisfied: colorhash&lt;1.3.0,&gt;=1.0.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.2.1)
6.622 Requirement already satisfied: jsonschema&lt;4.18,&gt;=3.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.17.3)
6.624 Requirement already satisfied: aio-pika&lt;8.2.4,&gt;=6.7.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (8.2.3)
6.626 Requirement already satisfied: scipy&lt;1.11.0,&gt;=1.10.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.10.1)
6.628 Requirement already satisfied: regex&lt;2022.11,&gt;=2020.6 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2022.10.31)
6.629 Requirement already satisfied: certifi&gt;=2023.7.22 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2023.7.22)
6.630 Requirement already satisfied: attrs&lt;22.2,&gt;=19.3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (22.1.0)
6.845 Collecting google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,&lt;3.0.0,&gt;=1.31.5
6.886   Downloading google_api_core-2.25.1-py3-none-any.whl (160 kB)
6.890      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 160.8/160.8 kB 173.8 MB/s eta 0:00:00
6.945 Collecting uritemplate&lt;5,&gt;=3.0.1
6.984   Downloading uritemplate-4.2.0-py3-none-any.whl (11 kB)
7.048 Collecting httplib2&lt;1.0.0,&gt;=0.19.0
7.087   Downloading httplib2-0.30.0-py3-none-any.whl (91 kB)
7.092      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 91.1/91.1 kB 206.1 MB/s eta 0:00:00
7.148 Collecting google-auth-httplib2&lt;1.0.0,&gt;=0.2.0
7.186   Downloading google_auth_httplib2-0.2.0-py2.py3-none-any.whl (9.3 kB)
7.197 Requirement already satisfied: requests-oauthlib&gt;=0.7.0 in /opt/venv/lib/python3.10/site-packages (from google-auth-oauthlib==1.0.0-&gt;-r requirements.txt (line 8)) (1.3.1)
7.289 Collecting apscheduler&lt;3.10,&gt;=3.6
7.331   Downloading APScheduler-3.6.3-py2.py3-none-any.whl (58 kB)
7.336      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 58.9/58.9 kB 168.6 MB/s eta 0:00:00
7.481 Collecting tornado==6.1
7.522   Downloading tornado-6.1.tar.gz (497 kB)
7.529      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 497.4/497.4 kB 222.3 MB/s eta 0:00:00
7.654   Preparing metadata (setup.py): started
8.659   Preparing metadata (setup.py): finished with status &#39;done&#39;
8.733 Collecting cachetools==4.2.2
8.773   Downloading cachetools-4.2.2-py3-none-any.whl (11 kB)
8.973 Collecting tzdata&gt;=2022.7
9.011   Downloading tzdata-2025.2-py2.py3-none-any.whl (347 kB)
9.017      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 347.8/347.8 kB 230.0 MB/s eta 0:00:00
9.094 Requirement already satisfied: idna&lt;4,&gt;=2.5 in /opt/venv/lib/python3.10/site-packages (from requests==2.32.4-&gt;-r requirements.txt (line 15)) (3.4)
9.096 Requirement already satisfied: urllib3&lt;3,&gt;=1.21.1 in /opt/venv/lib/python3.10/site-packages (from requests==2.32.4-&gt;-r requirements.txt (line 15)) (1.26.16)
9.097 Requirement already satisfied: charset_normalizer&lt;4,&gt;=2 in /opt/venv/lib/python3.10/site-packages (from requests==2.32.4-&gt;-r requirements.txt (line 15)) (3.1.0)
9.139 Requirement already satisfied: six&gt;=1.4.0 in /opt/venv/lib/python3.10/site-packages (from apscheduler&lt;3.10,&gt;=3.6-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.16.0)
9.142 Requirement already satisfied: tzlocal&gt;=1.2 in /opt/venv/lib/python3.10/site-packages (from apscheduler&lt;3.10,&gt;=3.6-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (5.0.1)
9.176 Requirement already satisfied: cloudpickle&gt;=1.1.1 in /opt/venv/lib/python3.10/site-packages (from dask==2022.10.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.2.1)
9.178 Requirement already satisfied: toolz&gt;=0.8.2 in /opt/venv/lib/python3.10/site-packages (from dask==2022.10.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.12.0)
9.179 Requirement already satisfied: fsspec&gt;=0.6.0 in /opt/venv/lib/python3.10/site-packages (from dask==2022.10.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2023.6.0)
9.181 Requirement already satisfied: click&gt;=7.0 in /opt/venv/lib/python3.10/site-packages (from dask==2022.10.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (8.1.3)
9.182 Requirement already satisfied: partd&gt;=0.3.10 in /opt/venv/lib/python3.10/site-packages (from dask==2022.10.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.4.0)
9.239 Requirement already satisfied: huggingface-hub&gt;=0.17.0 in /opt/venv/lib/python3.10/site-packages (from skops==0.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.27.0)
9.241 Requirement already satisfied: tabulate&gt;=0.8.8 in /opt/venv/lib/python3.10/site-packages (from skops==0.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.9.0)
9.283 Requirement already satisfied: gast&lt;=0.4.0,&gt;=0.2.1 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.4.0)
9.284 Requirement already satisfied: termcolor&gt;=1.1.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.3.0)
9.285 Requirement already satisfied: keras&lt;2.13,&gt;=2.12.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.12.0)
9.287 Requirement already satisfied: tensorflow-estimator&lt;2.13,&gt;=2.12.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.12.0)
9.289 Requirement already satisfied: wrapt&lt;1.15,&gt;=1.11.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.14.1)
9.290 Requirement already satisfied: tensorboard&lt;2.13,&gt;=2.12 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.12.3)
9.292 Requirement already satisfied: libclang&gt;=13.0.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (16.0.0)
9.294 Requirement already satisfied: google-pasta&gt;=0.1.1 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.2.0)
9.295 Requirement already satisfied: flatbuffers&gt;=2.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (23.5.26)
9.297 Requirement already satisfied: h5py&gt;=2.9.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.9.0)
9.299 Requirement already satisfied: grpcio&lt;2.0,&gt;=1.24.3 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.56.0)
9.301 Requirement already satisfied: astunparse&gt;=1.6.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.6.3)
9.302 Requirement already satisfied: jax&gt;=0.3.15 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.4.13)
9.304 Requirement already satisfied: opt-einsum&gt;=2.3.2 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.3.0)
9.360 Requirement already satisfied: aiormq~=6.4.0 in /opt/venv/lib/python3.10/site-packages (from aio-pika&lt;8.2.4,&gt;=6.7.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (6.4.2)
9.362 Requirement already satisfied: yarl in /opt/venv/lib/python3.10/site-packages (from aio-pika&lt;8.2.4,&gt;=6.7.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.9.2)
9.374 Requirement already satisfied: Babel&gt;=2.8.0 in /opt/venv/lib/python3.10/site-packages (from aiogram&lt;2.26-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.9.1)
9.397 Requirement already satisfied: aiosignal&gt;=1.1.2 in /opt/venv/lib/python3.10/site-packages (from aiohttp&lt;3.10,&gt;=3.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.3.1)
9.399 Requirement already satisfied: multidict&lt;7.0,&gt;=4.5 in /opt/venv/lib/python3.10/site-packages (from aiohttp&lt;3.10,&gt;=3.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (5.2.0)
9.402 Requirement already satisfied: async-timeout&lt;5.0,&gt;=4.0 in /opt/venv/lib/python3.10/site-packages (from aiohttp&lt;3.10,&gt;=3.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.0.2)
9.403 Requirement already satisfied: frozenlist&gt;=1.1.1 in /opt/venv/lib/python3.10/site-packages (from aiohttp&lt;3.10,&gt;=3.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.3.3)
9.459 Requirement already satisfied: jmespath&lt;2.0.0,&gt;=0.7.1 in /opt/venv/lib/python3.10/site-packages (from boto3&lt;2.0.0,&gt;=1.26.136-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.0.1)
9.461 Requirement already satisfied: s3transfer&lt;0.7.0,&gt;=0.6.0 in /opt/venv/lib/python3.10/site-packages (from boto3&lt;2.0.0,&gt;=1.26.136-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.6.1)
9.463 Requirement already satisfied: botocore&lt;1.31.0,&gt;=1.30.1 in /opt/venv/lib/python3.10/site-packages (from boto3&lt;2.0.0,&gt;=1.26.136-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.30.1)
9.475 Requirement already satisfied: msgpack&gt;=0.5.2 in /opt/venv/lib/python3.10/site-packages (from CacheControl&lt;0.13.0,&gt;=0.12.9-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.0.5)
9.502 Requirement already satisfied: humanfriendly&gt;=9.1 in /opt/venv/lib/python3.10/site-packages (from coloredlogs&lt;16,&gt;=10-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (10.0)
9.582 Requirement already satisfied: cffi&gt;=1.12 in /opt/venv/lib/python3.10/site-packages (from cryptography&gt;=41.0.7-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.15.1)
9.733 Collecting proto-plus&lt;2.0.0,&gt;=1.22.3
9.774   Downloading proto_plus-1.26.1-py3-none-any.whl (50 kB)
9.779      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 50.2/50.2 kB 164.4 MB/s eta 0:00:00
9.867 Collecting googleapis-common-protos&lt;2.0.0,&gt;=1.56.2
9.907   Downloading googleapis_common_protos-1.70.0-py3-none-any.whl (294 kB)
9.913      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 294.5/294.5 kB 192.8 MB/s eta 0:00:00
9.944 Requirement already satisfied: rsa&lt;5,&gt;=3.1.4 in /opt/venv/lib/python3.10/site-packages (from google-auth&lt;3-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.9)
9.946 Requirement already satisfied: pyasn1-modules&gt;=0.2.1 in /opt/venv/lib/python3.10/site-packages (from google-auth&lt;3-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.3.0)
9.968 Requirement already satisfied: pyparsing&lt;4,&gt;=3.0.4 in /opt/venv/lib/python3.10/site-packages (from httplib2&lt;1.0.0,&gt;=0.19.0-&gt;google-api-python-client==2.178.0-&gt;-r requirements.txt (line 7)) (3.1.0)
10.04 Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,&gt;=0.14.0 in /opt/venv/lib/python3.10/site-packages (from jsonschema&lt;4.18,&gt;=3.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.19.3)
10.06 Requirement already satisfied: cycler&gt;=0.10 in /opt/venv/lib/python3.10/site-packages (from matplotlib&lt;3.6,&gt;=3.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.11.0)
10.06 Requirement already satisfied: fonttools&gt;=4.22.0 in /opt/venv/lib/python3.10/site-packages (from matplotlib&lt;3.6,&gt;=3.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.40.0)
10.07 Requirement already satisfied: pillow&gt;=6.2.0 in /opt/venv/lib/python3.10/site-packages (from matplotlib&lt;3.6,&gt;=3.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (10.0.1)
10.07 Requirement already satisfied: kiwisolver&gt;=1.0.1 in /opt/venv/lib/python3.10/site-packages (from matplotlib&lt;3.6,&gt;=3.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.4.4)
10.16 Requirement already satisfied: wcwidth in /opt/venv/lib/python3.10/site-packages (from prompt-toolkit&lt;3.0.29,&gt;=3.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.2.6)
10.24 Requirement already satisfied: docopt&gt;=0.6.2 in /opt/venv/lib/python3.10/site-packages (from pykwalify&lt;1.9,&gt;=1.7-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.6.2)
10.30 Requirement already satisfied: bidict&gt;=0.21.0 in /opt/venv/lib/python3.10/site-packages (from python-socketio&lt;6,&gt;=4.4-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.22.1)
10.34 Requirement already satisfied: fire in /opt/venv/lib/python3.10/site-packages (from randomname&lt;0.2.0,&gt;=0.1.5-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.5.0)
10.38 Requirement already satisfied: oauthlib&gt;=3.0.0 in /opt/venv/lib/python3.10/site-packages (from requests-oauthlib&gt;=0.7.0-&gt;google-auth-oauthlib==1.0.0-&gt;-r requirements.txt (line 8)) (3.2.2)
10.42 Requirement already satisfied: ruamel.yaml.clib&gt;=0.2.6 in /opt/venv/lib/python3.10/site-packages (from ruamel.yaml&lt;0.17.22,&gt;=0.16.5-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.2.7)
10.58 Requirement already satisfied: uvloop&gt;=0.5.3 in /opt/venv/lib/python3.10/site-packages (from sanic&lt;21.13,&gt;=21.12-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.17.0)
10.58 Requirement already satisfied: aiofiles&gt;=0.6.0 in /opt/venv/lib/python3.10/site-packages (from sanic&lt;21.13,&gt;=21.12-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (23.1.0)
10.59 Requirement already satisfied: httptools&gt;=0.0.10 in /opt/venv/lib/python3.10/site-packages (from sanic&lt;21.13,&gt;=21.12-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.5.0)
10.67 Requirement already satisfied: threadpoolctl&gt;=2.0.0 in /opt/venv/lib/python3.10/site-packages (from scikit-learn&lt;1.2,&gt;=0.22-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.1.0)
10.68 Requirement already satisfied: joblib&gt;=1.0.0 in /opt/venv/lib/python3.10/site-packages (from scikit-learn&lt;1.2,&gt;=0.22-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.4.2)
10.79 Requirement already satisfied: python-crfsuite&gt;=0.8.3 in /opt/venv/lib/python3.10/site-packages (from sklearn-crfsuite&lt;0.4,&gt;=0.3-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.9.9)
10.93 Requirement already satisfied: greenlet!=0.4.17 in /opt/venv/lib/python3.10/site-packages (from SQLAlchemy&lt;1.5.0,&gt;=1.4.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.0.2)
11.05 Requirement already satisfied: aiohttp-retry&gt;=2.8.3 in /opt/venv/lib/python3.10/site-packages (from twilio&lt;8.3,&gt;=6.26-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.8.3)
11.15 Requirement already satisfied: requests-toolbelt in /opt/venv/lib/python3.10/site-packages (from webexteamssdk&lt;1.7.0,&gt;=1.1.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.0.0)
11.18 Requirement already satisfied: future in /opt/venv/lib/python3.10/site-packages (from webexteamssdk&lt;1.7.0,&gt;=1.1.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.18.3)
11.26 Requirement already satisfied: pamqp==3.2.1 in /opt/venv/lib/python3.10/site-packages (from aiormq~=6.4.0-&gt;aio-pika&lt;8.2.4,&gt;=6.7.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.2.1)
11.45 Requirement already satisfied: pycparser in /opt/venv/lib/python3.10/site-packages (from cffi&gt;=1.12-&gt;cryptography&gt;=41.0.7-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.21)
11.92 Requirement already satisfied: filelock in /opt/venv/lib/python3.10/site-packages (from huggingface-hub&gt;=0.17.0-&gt;skops==0.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.12.2)
11.99 Requirement already satisfied: ml_dtypes&gt;=0.1.0 in /opt/venv/lib/python3.10/site-packages (from jax&gt;=0.3.15-&gt;tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.2.0)
12.16 Requirement already satisfied: locket in /opt/venv/lib/python3.10/site-packages (from partd&gt;=0.3.10-&gt;dask==2022.10.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.0.0)
12.28 Requirement already satisfied: pyasn1&lt;0.6.0,&gt;=0.4.6 in /opt/venv/lib/python3.10/site-packages (from pyasn1-modules&gt;=0.2.1-&gt;google-auth&lt;3-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.5.0)
12.45 Requirement already satisfied: werkzeug&gt;=1.0.1 in /opt/venv/lib/python3.10/site-packages (from tensorboard&lt;2.13,&gt;=2.12-&gt;tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.3.6)
12.48 Requirement already satisfied: markdown&gt;=2.6.8 in /opt/venv/lib/python3.10/site-packages (from tensorboard&lt;2.13,&gt;=2.12-&gt;tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.4.3)
12.49 Requirement already satisfied: tensorboard-data-server&lt;0.8.0,&gt;=0.7.0 in /opt/venv/lib/python3.10/site-packages (from tensorboard&lt;2.13,&gt;=2.12-&gt;tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.7.1)
12.91 Requirement already satisfied: MarkupSafe&gt;=2.1.1 in /opt/venv/lib/python3.10/site-packages (from werkzeug&gt;=1.0.1-&gt;tensorboard&lt;2.13,&gt;=2.12-&gt;tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.1.3)
13.09 Building wheels for collected packages: tornado
13.09   Building wheel for tornado (setup.py): started
14.65   Building wheel for tornado (setup.py): finished with status &#39;done&#39;
14.65   Created wheel for tornado: filename=tornado-6.1-cp310-cp310-linux_x86_64.whl size=421979 sha256=ce22d73a28bb4f477c6c567e1988ca6d82cde41449c3a8039d9e365b84ac7b67
14.65   Stored in directory: /tmp/pip-ephem-wheel-cache-kf9kp66i/wheels/34/83/69/b89863a68e62add6e149dbaadcc049886105ce2405c1979bf2
14.66 Successfully built tornado
14.96 Installing collected packages: uritemplate, tzdata, tornado, requests, pydantic, psycopg2-binary, proto-plus, httplib2, googleapis-common-protos, cachetools, apscheduler, python-telegram-bot, pandas, google-auth-httplib2, google-api-core, gspread, google-api-python-client
14.97 ERROR: Could not install packages due to an OSError: [Errno 13] Permission denied: &#39;/opt/venv/lib/python3.10/site-packages/uritemplate&#39;
14.97 Check the permissions.
14.97 
15.56 
15.56 [notice] A new release of pip available: 22.3.1 -&gt; 25.2
15.56 [notice] To update, run: pip install --upgrade pip
------
failed to solve: process &quot;/bin/bash -o pipefail -c pip install --no-cache-dir -r requirements.txt&quot; did not complete successfully: exit code: 1
🚀 Starting services...
[+] Building 22.2s (8/11)                                                                                                                  docker:default
 =&gt; [rasa-server internal] load build definition from Dockerfile.rasa                                                                                0.2s
 =&gt; =&gt; transferring dockerfile: 344B                                                                                                                 0.1s
 =&gt; [rasa-server internal] load metadata for docker.io/rasa/rasa:3.6.21                                                                              0.9s
 =&gt; [rasa-server internal] load .dockerignore                                                                                                        0.0s
 =&gt; =&gt; transferring context: 154B                                                                                                                    0.0s
 =&gt; [rasa-server 1/7] FROM docker.io/rasa/rasa:3.6.21@sha256:7c0204065d4859e1b7a691c972ca3d26f5d39ad23fbd992b654084721226d813                        0.0s
 =&gt; [rasa-server internal] load build context                                                                                                        0.0s
 =&gt; =&gt; transferring context: 1.41kB                                                                                                                  0.0s
 =&gt; CACHED [rasa-server 2/7] WORKDIR /app                                                                                                            0.0s
 =&gt; CACHED [rasa-server 3/7] COPY requirements.txt .                                                                                                 0.0s
 =&gt; ERROR [rasa-server 4/7] RUN pip install --no-cache-dir -r requirements.txt                                                                      19.8s
------
 &gt; [rasa-server 4/7] RUN pip install --no-cache-dir -r requirements.txt:
3.150 Requirement already satisfied: rasa==3.6.21 in /opt/venv/lib/python3.10/site-packages (from -r requirements.txt (line 2)) (3.6.21)
3.150 Requirement already satisfied: rasa-sdk==3.6.2 in /opt/venv/lib/python3.10/site-packages (from -r requirements.txt (line 3)) (3.6.2)
3.619 Collecting gspread==6.2.1
4.030   Downloading gspread-6.2.1-py3-none-any.whl (59 kB)
4.110      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 60.0/60.0 kB 623.2 kB/s eta 0:00:00
4.577 Collecting google-api-python-client==2.178.0
4.598   Downloading google_api_python_client-2.178.0-py3-none-any.whl (13.8 MB)
5.041      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 13.8/13.8 MB 40.1 MB/s eta 0:00:00
5.148 Requirement already satisfied: google-auth-oauthlib==1.0.0 in /opt/venv/lib/python3.10/site-packages (from -r requirements.txt (line 8)) (1.0.0)
5.332 Collecting python-telegram-bot==13.15
5.393   Downloading python_telegram_bot-13.15-py3-none-any.whl (519 kB)
5.403      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 519.2/519.2 kB 81.5 MB/s eta 0:00:00
6.335 Collecting pandas==2.3.1
6.370   Downloading pandas-2.3.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (12.3 MB)
6.540      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.3/12.3 MB 81.0 MB/s eta 0:00:00
6.812 Collecting requests==2.32.4
6.854   Downloading requests-2.32.4-py3-none-any.whl (64 kB)
6.857      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 64.8/64.8 kB 166.7 MB/s eta 0:00:00
7.353 Collecting psycopg2-binary==2.9.10
7.408   Downloading psycopg2_binary-2.9.10-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.0 MB)
7.448      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.0/3.0 MB 82.5 MB/s eta 0:00:00
7.887 Requirement already satisfied: sklearn-crfsuite&lt;0.4,&gt;=0.3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.3.6)
7.887 Requirement already satisfied: websockets&lt;11.0,&gt;=10.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (10.4)
7.900 Requirement already satisfied: python-engineio!=5.0.0,&lt;6,&gt;=4 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.5.1)
7.900 Requirement already satisfied: scipy&lt;1.11.0,&gt;=1.10.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.10.1)
7.900 Requirement already satisfied: tensorflow_hub&lt;0.14.0,&gt;=0.13.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.13.0)
7.900 Requirement already satisfied: pluggy&lt;2.0.0,&gt;=1.0.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.2.0)
8.880 Collecting pydantic&lt;1.10.10
8.880   Downloading pydantic-1.10.9-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.1 MB)
8.948      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.1/3.1 MB 53.8 MB/s eta 0:00:00
9.003 Requirement already satisfied: jsonpickle&lt;3.1,&gt;=1.3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.0.4)
9.003 Requirement already satisfied: packaging&lt;21.0,&gt;=20.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (20.9)
9.003 Requirement already satisfied: terminaltables&lt;3.2.0,&gt;=3.1.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.1.10)
9.003 Requirement already satisfied: safetensors&lt;0.5.0,&gt;=0.4.5 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.4.5)
9.003 Requirement already satisfied: setuptools&lt;70.4.0,&gt;=70.3.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (70.3.0)
9.003 Requirement already satisfied: tensorflow-text==2.12.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.12.0)
9.003 Requirement already satisfied: skops==0.9.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.9.0)
9.018 Requirement already satisfied: certifi&gt;=2023.7.22 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2023.7.22)
9.018 Requirement already satisfied: tarsafe&lt;0.0.5,&gt;=0.0.3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.0.4)
9.018 Requirement already satisfied: coloredlogs&lt;16,&gt;=10 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (15.0.1)
9.018 Requirement already satisfied: sanic-routing&lt;0.8.0,&gt;=0.7.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.7.2)
9.029 Requirement already satisfied: aio-pika&lt;8.2.4,&gt;=6.7.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (8.2.3)
9.029 Requirement already satisfied: ruamel.yaml&lt;0.17.22,&gt;=0.16.5 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.17.21)
9.029 Requirement already satisfied: mattermostwrapper&lt;2.3,&gt;=2.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.2)
9.029 Requirement already satisfied: typing-extensions&lt;5.0.0,&gt;=4.1.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.7.1)
9.029 Requirement already satisfied: colorclass&lt;2.3,&gt;=2.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.2.2)
9.029 Requirement already satisfied: questionary&lt;1.11.0,&gt;=1.5.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.10.0)
9.031 Requirement already satisfied: ujson&lt;6.0,&gt;=1.35 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (5.8.0)
9.058 Requirement already satisfied: aiogram&lt;2.26 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.15)
9.058 Requirement already satisfied: numpy&lt;1.25.0,&gt;=1.19.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.23.5)
9.093 Requirement already satisfied: redis&lt;5.0,&gt;=4.5.3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.6.0)
9.093 Requirement already satisfied: structlog&lt;24.0.0,&gt;=23.1.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (23.1.0)
9.093 Requirement already satisfied: twilio&lt;8.3,&gt;=6.26 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (8.2.2)
9.093 Requirement already satisfied: slack-sdk&lt;4.0.0,&gt;=3.19.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.21.3)
9.093 Requirement already satisfied: tensorflow==2.12.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.12.0)
9.093 Requirement already satisfied: pydot&lt;1.5,&gt;=1.4 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.4.2)
9.093 Requirement already satisfied: wheel&gt;=0.38.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.40.0)
9.093 Requirement already satisfied: pyyaml&gt;=6.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (6.0.1)
9.093 Requirement already satisfied: regex&lt;2022.11,&gt;=2020.6 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2022.10.31)
9.093 Requirement already satisfied: matplotlib&lt;3.6,&gt;=3.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.5.3)
9.093 Requirement already satisfied: python-dateutil&lt;2.9,&gt;=2.8 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.8.2)
9.093 Requirement already satisfied: dnspython==2.3.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.3.0)
9.121 Requirement already satisfied: scikit-learn&lt;1.2,&gt;=0.22 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.1.3)
9.121 Requirement already satisfied: fbmessenger&lt;6.1.0,&gt;=6.0.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (6.0.0)
9.121 Requirement already satisfied: dask==2022.10.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2022.10.2)
9.121 Requirement already satisfied: pymongo[srv,tls]&lt;4.4,&gt;=3.8 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.3.3)
9.121 Requirement already satisfied: sentry-sdk&lt;1.15.0,&gt;=0.17.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.14.0)
9.121 Requirement already satisfied: absl-py&lt;1.5,&gt;=0.9 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.4.0)
9.121 Requirement already satisfied: CacheControl&lt;0.13.0,&gt;=0.12.9 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.12.14)
9.121 Requirement already satisfied: python-socketio&lt;6,&gt;=4.4 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (5.8.0)
9.121 Requirement already satisfied: tensorflow-io-gcs-filesystem==0.32 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.32.0)
9.121 Requirement already satisfied: randomname&lt;0.2.0,&gt;=0.1.5 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.1.5)
9.159 Requirement already satisfied: cryptography&gt;=41.0.7 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (41.0.7)
9.159 Requirement already satisfied: tqdm&lt;5.0,&gt;=4.31 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.65.0)
9.159 Requirement already satisfied: SQLAlchemy&lt;1.5.0,&gt;=1.4.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.4.49)
9.159 Requirement already satisfied: rocketchat_API&lt;1.31.0,&gt;=0.6.31 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.30.0)
9.159 Requirement already satisfied: boto3&lt;2.0.0,&gt;=1.26.136 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.27.1)
9.159 Requirement already satisfied: sanic-jwt&lt;2.0.0,&gt;=1.6.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.8.0)
9.159 Requirement already satisfied: PyJWT[crypto]&lt;3.0.0,&gt;=2.0.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.7.0)
9.159 Requirement already satisfied: colorhash&lt;1.3.0,&gt;=1.0.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.2.1)
9.159 Requirement already satisfied: apscheduler&lt;3.10,&gt;=3.6 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.9.1.post1)
9.159 Requirement already satisfied: networkx&lt;2.7,&gt;=2.4 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.6.3)
9.159 Requirement already satisfied: portalocker&lt;3.0.0,&gt;=2.7.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.7.0)
9.159 Requirement already satisfied: confluent-kafka&lt;3.0.0,&gt;=1.9.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.1.1)
9.159 Requirement already satisfied: jsonschema&lt;4.18,&gt;=3.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.17.3)
9.159 Requirement already satisfied: structlog-sentry&lt;3.0.0,&gt;=2.0.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.0.3)
9.190 Requirement already satisfied: sanic-cors&lt;2.1.0,&gt;=2.0.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.0.1)
9.190 Requirement already satisfied: attrs&lt;22.2,&gt;=19.3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (22.1.0)
9.190 Requirement already satisfied: protobuf&lt;4.23.4,&gt;=4.23.3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.23.3)
9.190 Requirement already satisfied: webexteamssdk&lt;1.7.0,&gt;=1.1.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.6.1)
9.190 Requirement already satisfied: pytz&lt;2023.0,&gt;=2019.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2022.7.1)
9.190 Requirement already satisfied: prompt-toolkit&lt;3.0.29,&gt;=3.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.0.28)
9.190 Requirement already satisfied: typing-utils&lt;0.2.0,&gt;=0.1.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.1.0)
9.190 Requirement already satisfied: sanic&lt;21.13,&gt;=21.12 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (21.12.2)
9.190 Requirement already satisfied: google-auth&lt;3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.21.0)
9.190 Requirement already satisfied: aiohttp&lt;3.10,&gt;=3.9.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.9.3)
9.190 Requirement already satisfied: pykwalify&lt;1.9,&gt;=1.7 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.8.0)
9.357 Collecting httplib2&lt;1.0.0,&gt;=0.19.0
9.398   Downloading httplib2-0.30.0-py3-none-any.whl (91 kB)
9.406      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 91.1/91.1 kB 110.3 MB/s eta 0:00:00
9.538 Collecting google-auth-httplib2&lt;1.0.0,&gt;=0.2.0
9.599   Downloading google_auth_httplib2-0.2.0-py2.py3-none-any.whl (9.3 kB)
9.956 Collecting google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,&lt;3.0.0,&gt;=1.31.5
10.00   Downloading google_api_core-2.25.1-py3-none-any.whl (160 kB)
10.01      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 160.8/160.8 kB 210.2 MB/s eta 0:00:00
10.14 Collecting uritemplate&lt;5,&gt;=3.0.1
10.20   Downloading uritemplate-4.2.0-py3-none-any.whl (11 kB)
10.20 Requirement already satisfied: requests-oauthlib&gt;=0.7.0 in /opt/venv/lib/python3.10/site-packages (from google-auth-oauthlib==1.0.0-&gt;-r requirements.txt (line 8)) (1.3.1)
10.34 Collecting cachetools==4.2.2
10.38   Downloading cachetools-4.2.2-py3-none-any.whl (11 kB)
10.66 Collecting tornado==6.1
10.71   Downloading tornado-6.1.tar.gz (497 kB)
10.73      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 497.4/497.4 kB 125.3 MB/s eta 0:00:00
10.99   Preparing metadata (setup.py): started
12.32   Preparing metadata (setup.py): finished with status &#39;done&#39;
12.41 Collecting apscheduler&lt;3.10,&gt;=3.6
12.45   Downloading APScheduler-3.6.3-py2.py3-none-any.whl (58 kB)
12.45      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 58.9/58.9 kB 150.7 MB/s eta 0:00:00
12.67 Collecting tzdata&gt;=2022.7
12.71   Downloading tzdata-2025.2-py2.py3-none-any.whl (347 kB)
12.72      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 347.8/347.8 kB 182.5 MB/s eta 0:00:00
12.74 Requirement already satisfied: idna&lt;4,&gt;=2.5 in /opt/venv/lib/python3.10/site-packages (from requests==2.32.4-&gt;-r requirements.txt (line 15)) (3.4)
12.78 Requirement already satisfied: urllib3&lt;3,&gt;=1.21.1 in /opt/venv/lib/python3.10/site-packages (from requests==2.32.4-&gt;-r requirements.txt (line 15)) (1.26.16)
12.78 Requirement already satisfied: charset_normalizer&lt;4,&gt;=2 in /opt/venv/lib/python3.10/site-packages (from requests==2.32.4-&gt;-r requirements.txt (line 15)) (3.1.0)
12.82 Requirement already satisfied: tzlocal&gt;=1.2 in /opt/venv/lib/python3.10/site-packages (from apscheduler&lt;3.10,&gt;=3.6-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (5.0.1)
12.82 Requirement already satisfied: six&gt;=1.4.0 in /opt/venv/lib/python3.10/site-packages (from apscheduler&lt;3.10,&gt;=3.6-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.16.0)
12.86 Requirement already satisfied: click&gt;=7.0 in /opt/venv/lib/python3.10/site-packages (from dask==2022.10.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (8.1.3)
12.86 Requirement already satisfied: cloudpickle&gt;=1.1.1 in /opt/venv/lib/python3.10/site-packages (from dask==2022.10.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.2.1)
12.86 Requirement already satisfied: toolz&gt;=0.8.2 in /opt/venv/lib/python3.10/site-packages (from dask==2022.10.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.12.0)
12.86 Requirement already satisfied: fsspec&gt;=0.6.0 in /opt/venv/lib/python3.10/site-packages (from dask==2022.10.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2023.6.0)
12.86 Requirement already satisfied: partd&gt;=0.3.10 in /opt/venv/lib/python3.10/site-packages (from dask==2022.10.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.4.0)
12.92 Requirement already satisfied: tabulate&gt;=0.8.8 in /opt/venv/lib/python3.10/site-packages (from skops==0.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.9.0)
12.93 Requirement already satisfied: huggingface-hub&gt;=0.17.0 in /opt/venv/lib/python3.10/site-packages (from skops==0.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.27.0)
12.96 Requirement already satisfied: libclang&gt;=13.0.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (16.0.0)
12.96 Requirement already satisfied: astunparse&gt;=1.6.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.6.3)
12.97 Requirement already satisfied: termcolor&gt;=1.1.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.3.0)
12.97 Requirement already satisfied: google-pasta&gt;=0.1.1 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.2.0)
12.97 Requirement already satisfied: flatbuffers&gt;=2.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (23.5.26)
12.97 Requirement already satisfied: tensorflow-estimator&lt;2.13,&gt;=2.12.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.12.0)
12.97 Requirement already satisfied: gast&lt;=0.4.0,&gt;=0.2.1 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.4.0)
12.98 Requirement already satisfied: keras&lt;2.13,&gt;=2.12.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.12.0)
12.98 Requirement already satisfied: h5py&gt;=2.9.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.9.0)
12.98 Requirement already satisfied: jax&gt;=0.3.15 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.4.13)
12.98 Requirement already satisfied: wrapt&lt;1.15,&gt;=1.11.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.14.1)
12.98 Requirement already satisfied: grpcio&lt;2.0,&gt;=1.24.3 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.56.0)
12.98 Requirement already satisfied: tensorboard&lt;2.13,&gt;=2.12 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.12.3)
12.99 Requirement already satisfied: opt-einsum&gt;=2.3.2 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.3.0)
13.05 Requirement already satisfied: aiormq~=6.4.0 in /opt/venv/lib/python3.10/site-packages (from aio-pika&lt;8.2.4,&gt;=6.7.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (6.4.2)
13.05 Requirement already satisfied: yarl in /opt/venv/lib/python3.10/site-packages (from aio-pika&lt;8.2.4,&gt;=6.7.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.9.2)
13.06 Requirement already satisfied: Babel&gt;=2.8.0 in /opt/venv/lib/python3.10/site-packages (from aiogram&lt;2.26-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.9.1)
13.08 Requirement already satisfied: aiosignal&gt;=1.1.2 in /opt/venv/lib/python3.10/site-packages (from aiohttp&lt;3.10,&gt;=3.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.3.1)
13.08 Requirement already satisfied: multidict&lt;7.0,&gt;=4.5 in /opt/venv/lib/python3.10/site-packages (from aiohttp&lt;3.10,&gt;=3.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (5.2.0)
13.09 Requirement already satisfied: frozenlist&gt;=1.1.1 in /opt/venv/lib/python3.10/site-packages (from aiohttp&lt;3.10,&gt;=3.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.3.3)
13.09 Requirement already satisfied: async-timeout&lt;5.0,&gt;=4.0 in /opt/venv/lib/python3.10/site-packages (from aiohttp&lt;3.10,&gt;=3.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.0.2)
13.15 Requirement already satisfied: s3transfer&lt;0.7.0,&gt;=0.6.0 in /opt/venv/lib/python3.10/site-packages (from boto3&lt;2.0.0,&gt;=1.26.136-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.6.1)
13.15 Requirement already satisfied: botocore&lt;1.31.0,&gt;=1.30.1 in /opt/venv/lib/python3.10/site-packages (from boto3&lt;2.0.0,&gt;=1.26.136-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.30.1)
13.15 Requirement already satisfied: jmespath&lt;2.0.0,&gt;=0.7.1 in /opt/venv/lib/python3.10/site-packages (from boto3&lt;2.0.0,&gt;=1.26.136-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.0.1)
13.16 Requirement already satisfied: msgpack&gt;=0.5.2 in /opt/venv/lib/python3.10/site-packages (from CacheControl&lt;0.13.0,&gt;=0.12.9-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.0.5)
13.19 Requirement already satisfied: humanfriendly&gt;=9.1 in /opt/venv/lib/python3.10/site-packages (from coloredlogs&lt;16,&gt;=10-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (10.0)
13.27 Requirement already satisfied: cffi&gt;=1.12 in /opt/venv/lib/python3.10/site-packages (from cryptography&gt;=41.0.7-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.15.1)
13.40 Collecting googleapis-common-protos&lt;2.0.0,&gt;=1.56.2
13.44   Downloading googleapis_common_protos-1.70.0-py3-none-any.whl (294 kB)
13.45      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 294.5/294.5 kB 155.9 MB/s eta 0:00:00
13.56 Collecting proto-plus&lt;2.0.0,&gt;=1.22.3
13.60   Downloading proto_plus-1.26.1-py3-none-any.whl (50 kB)
13.60      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 50.2/50.2 kB 165.0 MB/s eta 0:00:00
13.64 Requirement already satisfied: rsa&lt;5,&gt;=3.1.4 in /opt/venv/lib/python3.10/site-packages (from google-auth&lt;3-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.9)
13.64 Requirement already satisfied: pyasn1-modules&gt;=0.2.1 in /opt/venv/lib/python3.10/site-packages (from google-auth&lt;3-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.3.0)
13.66 Requirement already satisfied: pyparsing&lt;4,&gt;=3.0.4 in /opt/venv/lib/python3.10/site-packages (from httplib2&lt;1.0.0,&gt;=0.19.0-&gt;google-api-python-client==2.178.0-&gt;-r requirements.txt (line 7)) (3.1.0)
13.73 Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,&gt;=0.14.0 in /opt/venv/lib/python3.10/site-packages (from jsonschema&lt;4.18,&gt;=3.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.19.3)
13.75 Requirement already satisfied: fonttools&gt;=4.22.0 in /opt/venv/lib/python3.10/site-packages (from matplotlib&lt;3.6,&gt;=3.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.40.0)
13.75 Requirement already satisfied: pillow&gt;=6.2.0 in /opt/venv/lib/python3.10/site-packages (from matplotlib&lt;3.6,&gt;=3.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (10.0.1)
13.75 Requirement already satisfied: kiwisolver&gt;=1.0.1 in /opt/venv/lib/python3.10/site-packages (from matplotlib&lt;3.6,&gt;=3.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.4.4)
13.75 Requirement already satisfied: cycler&gt;=0.10 in /opt/venv/lib/python3.10/site-packages (from matplotlib&lt;3.6,&gt;=3.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.11.0)
13.85 Requirement already satisfied: wcwidth in /opt/venv/lib/python3.10/site-packages (from prompt-toolkit&lt;3.0.29,&gt;=3.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.2.6)
13.92 Requirement already satisfied: docopt&gt;=0.6.2 in /opt/venv/lib/python3.10/site-packages (from pykwalify&lt;1.9,&gt;=1.7-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.6.2)
13.98 Requirement already satisfied: bidict&gt;=0.21.0 in /opt/venv/lib/python3.10/site-packages (from python-socketio&lt;6,&gt;=4.4-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.22.1)
14.03 Requirement already satisfied: fire in /opt/venv/lib/python3.10/site-packages (from randomname&lt;0.2.0,&gt;=0.1.5-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.5.0)
14.07 Requirement already satisfied: oauthlib&gt;=3.0.0 in /opt/venv/lib/python3.10/site-packages (from requests-oauthlib&gt;=0.7.0-&gt;google-auth-oauthlib==1.0.0-&gt;-r requirements.txt (line 8)) (3.2.2)
14.10 Requirement already satisfied: ruamel.yaml.clib&gt;=0.2.6 in /opt/venv/lib/python3.10/site-packages (from ruamel.yaml&lt;0.17.22,&gt;=0.16.5-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.2.7)
14.25 Requirement already satisfied: uvloop&gt;=0.5.3 in /opt/venv/lib/python3.10/site-packages (from sanic&lt;21.13,&gt;=21.12-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.17.0)
14.25 Requirement already satisfied: aiofiles&gt;=0.6.0 in /opt/venv/lib/python3.10/site-packages (from sanic&lt;21.13,&gt;=21.12-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (23.1.0)
14.25 Requirement already satisfied: httptools&gt;=0.0.10 in /opt/venv/lib/python3.10/site-packages (from sanic&lt;21.13,&gt;=21.12-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.5.0)
14.34 Requirement already satisfied: threadpoolctl&gt;=2.0.0 in /opt/venv/lib/python3.10/site-packages (from scikit-learn&lt;1.2,&gt;=0.22-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.1.0)
14.34 Requirement already satisfied: joblib&gt;=1.0.0 in /opt/venv/lib/python3.10/site-packages (from scikit-learn&lt;1.2,&gt;=0.22-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.4.2)
14.45 Requirement already satisfied: python-crfsuite&gt;=0.8.3 in /opt/venv/lib/python3.10/site-packages (from sklearn-crfsuite&lt;0.4,&gt;=0.3-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.9.9)
14.59 Requirement already satisfied: greenlet!=0.4.17 in /opt/venv/lib/python3.10/site-packages (from SQLAlchemy&lt;1.5.0,&gt;=1.4.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.0.2)
14.70 Requirement already satisfied: aiohttp-retry&gt;=2.8.3 in /opt/venv/lib/python3.10/site-packages (from twilio&lt;8.3,&gt;=6.26-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.8.3)
14.81 Requirement already satisfied: future in /opt/venv/lib/python3.10/site-packages (from webexteamssdk&lt;1.7.0,&gt;=1.1.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.18.3)
14.88 Requirement already satisfied: requests-toolbelt in /opt/venv/lib/python3.10/site-packages (from webexteamssdk&lt;1.7.0,&gt;=1.1.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.0.0)
14.96 Requirement already satisfied: pamqp==3.2.1 in /opt/venv/lib/python3.10/site-packages (from aiormq~=6.4.0-&gt;aio-pika&lt;8.2.4,&gt;=6.7.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.2.1)
15.10 Requirement already satisfied: pycparser in /opt/venv/lib/python3.10/site-packages (from cffi&gt;=1.12-&gt;cryptography&gt;=41.0.7-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.21)
15.54 Requirement already satisfied: filelock in /opt/venv/lib/python3.10/site-packages (from huggingface-hub&gt;=0.17.0-&gt;skops==0.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.12.2)
15.63 Requirement already satisfied: ml_dtypes&gt;=0.1.0 in /opt/venv/lib/python3.10/site-packages (from jax&gt;=0.3.15-&gt;tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.2.0)
15.81 Requirement already satisfied: locket in /opt/venv/lib/python3.10/site-packages (from partd&gt;=0.3.10-&gt;dask==2022.10.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.0.0)
15.88 Requirement already satisfied: pyasn1&lt;0.6.0,&gt;=0.4.6 in /opt/venv/lib/python3.10/site-packages (from pyasn1-modules&gt;=0.2.1-&gt;google-auth&lt;3-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.5.0)
16.05 Requirement already satisfied: tensorboard-data-server&lt;0.8.0,&gt;=0.7.0 in /opt/venv/lib/python3.10/site-packages (from tensorboard&lt;2.13,&gt;=2.12-&gt;tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.7.1)
16.06 Requirement already satisfied: werkzeug&gt;=1.0.1 in /opt/venv/lib/python3.10/site-packages (from tensorboard&lt;2.13,&gt;=2.12-&gt;tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.3.6)
16.09 Requirement already satisfied: markdown&gt;=2.6.8 in /opt/venv/lib/python3.10/site-packages (from tensorboard&lt;2.13,&gt;=2.12-&gt;tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.4.3)
16.47 Requirement already satisfied: MarkupSafe&gt;=2.1.1 in /opt/venv/lib/python3.10/site-packages (from werkzeug&gt;=1.0.1-&gt;tensorboard&lt;2.13,&gt;=2.12-&gt;tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.1.3)
16.65 Building wheels for collected packages: tornado
16.65   Building wheel for tornado (setup.py): started
18.17   Building wheel for tornado (setup.py): finished with status &#39;done&#39;
18.17   Created wheel for tornado: filename=tornado-6.1-cp310-cp310-linux_x86_64.whl size=421978 sha256=93b5acdbc7da19f8ef4900c34088e92d360f4e6b295fd02b1ffd70f1a8b5d5c2
18.17   Stored in directory: /tmp/pip-ephem-wheel-cache-bfg5f3ry/wheels/34/83/69/b89863a68e62add6e149dbaadcc049886105ce2405c1979bf2
18.17 Successfully built tornado
18.52 Installing collected packages: uritemplate, tzdata, tornado, requests, pydantic, psycopg2-binary, proto-plus, httplib2, googleapis-common-protos, cachetools, apscheduler, python-telegram-bot, pandas, google-auth-httplib2, google-api-core, gspread, google-api-python-client
18.53 ERROR: Could not install packages due to an OSError: [Errno 13] Permission denied: &#39;/opt/venv/lib/python3.10/site-packages/uritemplate&#39;
18.53 Check the permissions.
18.53 
19.38 
19.38 [notice] A new release of pip available: 22.3.1 -&gt; 25.2
19.38 [notice] To update, run: pip install --upgrade pip
------
failed to solve: process &quot;/bin/bash -o pipefail -c pip install --no-cache-dir -r requirements.txt&quot; did not complete successfully: exit code: 1
✅ Deployment complete!

📊 Service Status:
NAME      IMAGE     COMMAND   SERVICE   CREATED   STATUS    PORTS

🌐 Your services are running on:
- Rasa Server: http://your-azure-vm-ip:80
- Action Server: http://your-azure-vm-ip:5055
- Telegram Bridge: http://your-azure-vm-ip:5006

📝 To check logs: docker-compose -f azure-compose.yml logs -f
🛑 To stop services: docker-compose -f azure-compose.yml down
azureuser@Remin

---

I see the issue is still persisting. The problem is that we're still using the Rasa base image which has the virtual environment issue. Let me check the current Dockerfile and fix it completely:

---

The Dockerfile looks correct now, but the error shows it's still trying to use the Rasa image. Let me check if there are cached layers. Let's force a complete rebuild:

```bash
# Remove all Docker images and containers
docker system prune -a -f

# Remove any cached build layers
docker builder prune -a -f

# Now run the deployment
./deploy-azure.sh
```

If this still fails, let's create a minimal working version without the training step:

---

Removing the training step to avoid potential issues and get the basic deployment working first

---


Now try:

```bash
docker system prune -a -f
./deploy-azure.sh
```

---

Downloading tensorflow-2.12.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (585.9 MB)
381.2      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━      514.8/585.9 MB 1.2 MB/s eta 0:01:01
381.2 ERROR: Exception:
381.2 Traceback (most recent call last):
381.2   File &quot;/usr/local/lib/python3.9/site-packages/pip/_vendor/urllib3/response.py&quot;, line 438, in _error_catcher
381.2     yield
381.2   File &quot;/usr/local/lib/python3.9/site-packages/pip/_vendor/urllib3/response.py&quot;, line 561, in read
381.2     data = self._fp_read(amt) if not fp_closed else b&quot;&quot;
381.2   File &quot;/usr/local/lib/python3.9/site-packages/pip/_vendor/urllib3/response.py&quot;, line 527, in _fp_read
381.2     return self._fp.read(amt) if amt is not None else self._fp.read()
381.2   File &quot;/usr/local/lib/python3.9/http/client.py&quot;, line 463, in read
381.2     n = self.readinto(b)
381.2   File &quot;/usr/local/lib/python3.9/http/client.py&quot;, line 507, in readinto
381.2     n = self.fp.readinto(b)
381.2   File &quot;/usr/local/lib/python3.9/socket.py&quot;, line 716, in readinto
381.2     return self._sock.recv_into(b)
381.2   File &quot;/usr/local/lib/python3.9/ssl.py&quot;, line 1275, in recv_into
381.2     return self.read(nbytes, buffer)
381.2   File &quot;/usr/local/lib/python3.9/ssl.py&quot;, line 1133, in read
381.2     return self._sslobj.read(len, buffer)
381.2 socket.timeout: The read operation timed out
381.2 
381.2 During handling of the above exception, another exception occurred:
381.2 
381.2 Traceback (most recent call last):
381.2   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/cli/base_command.py&quot;, line 160, in exc_logging_wrapper
381.2     status = run_func(*args)
381.2   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/cli/req_command.py&quot;, line 247, in wrapper
381.2     return func(self, options, args)
381.2   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/commands/install.py&quot;, line 419, in run
381.2     requirement_set = resolver.resolve(
381.2   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/resolver.py&quot;, line 92, in resolve
381.2     result = self._result = resolver.resolve(
381.2   File &quot;/usr/local/lib/python3.9/site-packages/pip/_vendor/resolvelib/resolvers.py&quot;, line 481, in resolve
381.2     state = resolution.resolve(requirements, max_rounds=max_rounds)
381.2   File &quot;/usr/local/lib/python3.9/site-packages/pip/_vendor/resolvelib/resolvers.py&quot;, line 373, in resolve
381.2     failure_causes = self._attempt_to_pin_criterion(name)
381.2   File &quot;/usr/local/lib/python3.9/site-packages/pip/_vendor/resolvelib/resolvers.py&quot;, line 213, in _attempt_to_pin_criterion
381.2     criteria = self._get_updated_criteria(candidate)
381.2   File &quot;/usr/local/lib/python3.9/site-packages/pip/_vendor/resolvelib/resolvers.py&quot;, line 204, in _get_updated_criteria
381.2     self._add_to_criteria(criteria, requirement, parent=candidate)
381.2   File &quot;/usr/local/lib/python3.9/site-packages/pip/_vendor/resolvelib/resolvers.py&quot;, line 172, in _add_to_criteria
381.2     if not criterion.candidates:
381.2   File &quot;/usr/local/lib/python3.9/site-packages/pip/_vendor/resolvelib/structs.py&quot;, line 151, in __bool__
381.2     return bool(self._sequence)
381.2   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/found_candidates.py&quot;, line 155, in __bool__
381.2     return any(self)
381.2   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/found_candidates.py&quot;, line 143, in &lt;genexpr&gt;
381.2     return (c for c in iterator if id(c) not in self._incompatible_ids)
381.2   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/found_candidates.py&quot;, line 47, in _iter_built
381.2     candidate = func()
381.2   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/factory.py&quot;, line 206, in _make_candidate_from_link
381.2     self._link_candidate_cache[link] = LinkCandidate(
381.2   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/candidates.py&quot;, line 297, in __init__
381.2     super().__init__(
381.2   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/candidates.py&quot;, line 162, in __init__
381.2     self.dist = self._prepare()
381.2   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/candidates.py&quot;, line 231, in _prepare
381.2     dist = self._prepare_distribution()
381.2   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/candidates.py&quot;, line 308, in _prepare_distribution
381.2     return preparer.prepare_linked_requirement(self._ireq, parallel_builds=True)
381.2   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/operations/prepare.py&quot;, line 491, in prepare_linked_requirement
381.2     return self._prepare_linked_requirement(req, parallel_builds)
381.2   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/operations/prepare.py&quot;, line 536, in _prepare_linked_requirement
381.2     local_file = unpack_url(
381.2   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/operations/prepare.py&quot;, line 166, in unpack_url
381.2     file = get_http_url(
381.2   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/operations/prepare.py&quot;, line 107, in get_http_url
381.2     from_path, content_type = download(link, temp_dir.path)
381.2   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/network/download.py&quot;, line 147, in __call__
381.2     for chunk in chunks:
381.2   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/cli/progress_bars.py&quot;, line 53, in _rich_progress_bar
381.2     for chunk in iterable:
381.2   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/network/utils.py&quot;, line 63, in response_chunks
381.2     for chunk in response.raw.stream(
381.2   File &quot;/usr/local/lib/python3.9/site-packages/pip/_vendor/urllib3/response.py&quot;, line 622, in stream
381.2     data = self.read(amt=amt, decode_content=decode_content)
381.2   File &quot;/usr/local/lib/python3.9/site-packages/pip/_vendor/urllib3/response.py&quot;, line 587, in read
381.2     raise IncompleteRead(self._fp_bytes_read, self.length_remaining)
381.2   File &quot;/usr/local/lib/python3.9/contextlib.py&quot;, line 137, in __exit__
381.2     self.gen.throw(typ, value, traceback)
381.2   File &quot;/usr/local/lib/python3.9/site-packages/pip/_vendor/urllib3/response.py&quot;, line 443, in _error_catcher
381.2     raise ReadTimeoutError(self._pool, None, &quot;Read timed out.&quot;)
381.2 pip._vendor.urllib3.exceptions.ReadTimeoutError: HTTPSConnectionPool(host=&#39;files.pythonhosted.org&#39;, port=443): Read timed out.
381.5 
381.5 [notice] A new release of pip is available: 23.0.1 -&gt; 25.2
381.5 [notice] To update, run: pip install --upgrade pip
------
failed to solve: process &quot;/bin/sh -c pip install --no-cache-dir -r requirements.txt&quot; did not complete successfully: exit code: 2
✅ Deployment complete!

📊 Service Status:
NAME      IMAGE     COMMAND   SERVICE   CREATED   STATUS    PORTS

🌐 Your services are running on:
- Rasa Server: http://your-azure-vm-ip:80
- Action Server: http://your-azure-vm-ip:5055
- Telegram Bridge: http://your-azure-vm-ip:5006

📝 To check logs: docker-compose -f azure-compose.yml logs -f
🛑 To stop services: docker-compose -f azure-compose.yml down

---

The issue is a network timeout while downloading TensorFlow (585MB). This is common with large packages on slower connections. Let's optimize the installation:

---

Adding pip timeout and retry options to handle large package downloads

---

Also, let's create a minimal requirements file to test the deployment first:

---

Creating a minimal requirements file for testing without heavy packages like Rasa

---

Let's test with the minimal requirements first:

---

Using minimal requirements for testing the deployment

---

Also update the CMD to just run a simple Python server instead of Rasa:

---

Using a simple Python HTTP server for testing instead of Rasa

---


Now test the deployment:

```bash
docker system prune -f
./deploy-azure.sh
```

This should work much faster and help us verify the basic deployment is working before adding the heavy Rasa components.

---

azureuser@Remindbot:~/Remind_Bot/Remind_Bot$ ./deploy-azure.sh
🚀 Starting Azure deployment for Rasa chatbot...
✅ Environment variables loaded
🔨 Building Docker images...
[+] Building 36.8s (8/10)                                                                                                                  docker:default
 =&gt; [action-server internal] load build definition from Dockerfile.actions                                                                           0.1s
 =&gt; =&gt; transferring dockerfile: 297B                                                                                                                 0.0s
 =&gt; [action-server internal] load metadata for docker.io/library/python:3.9-slim                                                                     2.7s
 =&gt; [action-server internal] load .dockerignore                                                                                                      0.1s
 =&gt; =&gt; transferring context: 154B                                                                                                                    0.0s
 =&gt; [action-server 1/6] FROM docker.io/library/python:3.9-slim@sha256:71b97a8eed69cddd132431327ff7c204fd6ea3d38e0c5d11d52f9661482bc8a3               6.6s
 =&gt; =&gt; resolve docker.io/library/python:3.9-slim@sha256:71b97a8eed69cddd132431327ff7c204fd6ea3d38e0c5d11d52f9661482bc8a3                             0.1s
 =&gt; =&gt; sha256:71b97a8eed69cddd132431327ff7c204fd6ea3d38e0c5d11d52f9661482bc8a3 10.36kB / 10.36kB                                                     0.0s
 =&gt; =&gt; sha256:161727d2d61fdfe4836d11f82fb437a3fcb2f4ce5b85951805f0717687ce110f 1.74kB / 1.74kB                                                       0.0s
 =&gt; =&gt; sha256:56cea0119ab69043114ce215d355f9f343a55b74b58001450df2e00478fb3529 5.30kB / 5.30kB                                                       0.0s
 =&gt; =&gt; sha256:ce1261c6d567efa8e3b457673eeeb474a0a8066df6bb95ca9a6a94a31e219dd3 29.77MB / 29.77MB                                                     1.5s
 =&gt; =&gt; sha256:1d454ace0e384876850a0aa5ef6b8c45705445114ab233959bdab71a577b9200 1.29MB / 1.29MB                                                       0.8s
 =&gt; =&gt; sha256:41dc2499d8fe1ea2351cc01f3716ce6a95ad0e9bf90c0819fd0c4a93cf4e9b24 13.37MB / 13.37MB                                                     1.5s
 =&gt; =&gt; sha256:7fcdf9369fa96e0413fe19da3d316fb6c3bfb0d7371fa4ce617617cac3e8de12 249B / 249B                                                           1.5s
 =&gt; =&gt; extracting sha256:ce1261c6d567efa8e3b457673eeeb474a0a8066df6bb95ca9a6a94a31e219dd3                                                            1.9s
 =&gt; =&gt; extracting sha256:1d454ace0e384876850a0aa5ef6b8c45705445114ab233959bdab71a577b9200                                                            0.4s
 =&gt; =&gt; extracting sha256:41dc2499d8fe1ea2351cc01f3716ce6a95ad0e9bf90c0819fd0c4a93cf4e9b24                                                            1.3s
 =&gt; =&gt; extracting sha256:7fcdf9369fa96e0413fe19da3d316fb6c3bfb0d7371fa4ce617617cac3e8de12                                                            0.0s
 =&gt; [action-server internal] load build context                                                                                                      0.1s
 =&gt; =&gt; transferring context: 48.36kB                                                                                                                 0.0s
 =&gt; [action-server 2/6] WORKDIR /app                                                                                                                 0.1s
 =&gt; [action-server 3/6] COPY requirements.txt .                                                                                                      0.1s
 =&gt; ERROR [action-server 4/6] RUN pip install --no-cache-dir -r requirements.txt                                                                    26.7s
------
 &gt; [action-server 4/6] RUN pip install --no-cache-dir -r requirements.txt:
4.467 Collecting rasa==3.6.21
4.636   Downloading rasa-3.6.21-py3-none-any.whl (843 kB)
4.784      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 843.4/843.4 kB 5.9 MB/s eta 0:00:00
5.212 Collecting rasa-sdk==3.6.2
5.253   Downloading rasa_sdk-3.6.2-py3-none-any.whl (45 kB)
5.258      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 45.3/45.3 kB 102.3 MB/s eta 0:00:00
5.615 Collecting gspread==6.2.1
5.658   Downloading gspread-6.2.1-py3-none-any.whl (59 kB)
5.663      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 60.0/60.0 kB 111.5 MB/s eta 0:00:00
5.936 Collecting google-api-python-client==2.178.0
5.977   Downloading google_api_python_client-2.178.0-py3-none-any.whl (13.8 MB)
6.159      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 13.8/13.8 MB 102.2 MB/s eta 0:00:00
6.559 Collecting google-auth-oauthlib==1.0.0
6.599   Downloading google_auth_oauthlib-1.0.0-py2.py3-none-any.whl (18 kB)
6.743 Collecting python-telegram-bot==13.15
6.788   Downloading python_telegram_bot-13.15-py3-none-any.whl (519 kB)
6.796      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 519.2/519.2 kB 151.0 MB/s eta 0:00:00
7.408 Collecting pandas==2.3.1
7.448   Downloading pandas-2.3.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (12.4 MB)
7.569      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.4/12.4 MB 107.8 MB/s eta 0:00:00
7.746 Collecting requests==2.32.4
7.786   Downloading requests-2.32.4-py3-none-any.whl (64 kB)
7.790      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 64.8/64.8 kB 129.7 MB/s eta 0:00:00
8.132 Collecting psycopg2-binary==2.9.10
8.176   Downloading psycopg2_binary-2.9.10-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.0 MB)
8.204      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.0/3.0 MB 129.6 MB/s eta 0:00:00
9.268 Collecting protobuf&lt;4.23.4,&gt;=4.23.3
9.565   Downloading protobuf-4.23.3-cp37-abi3-manylinux2014_x86_64.whl (304 kB)
9.572      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 304.5/304.5 kB 134.9 MB/s eta 0:00:00
10.25 Collecting matplotlib&lt;3.6,&gt;=3.1
10.29   Downloading matplotlib-3.5.3-cp39-cp39-manylinux_2_5_x86_64.manylinux1_x86_64.whl (11.2 MB)
26.14      ━━━━━━━━━━━━━━━━━━━━━━                   6.3/11.2 MB 7.6 MB/s eta 0:00:01
26.14 ERROR: Exception:
26.14 Traceback (most recent call last):
26.14   File &quot;/usr/local/lib/python3.9/site-packages/pip/_vendor/urllib3/response.py&quot;, line 438, in _error_catcher
26.14     yield
26.14   File &quot;/usr/local/lib/python3.9/site-packages/pip/_vendor/urllib3/response.py&quot;, line 561, in read
26.14     data = self._fp_read(amt) if not fp_closed else b&quot;&quot;
26.14   File &quot;/usr/local/lib/python3.9/site-packages/pip/_vendor/urllib3/response.py&quot;, line 527, in _fp_read
26.14     return self._fp.read(amt) if amt is not None else self._fp.read()
26.14   File &quot;/usr/local/lib/python3.9/http/client.py&quot;, line 463, in read
26.14     n = self.readinto(b)
26.14   File &quot;/usr/local/lib/python3.9/http/client.py&quot;, line 507, in readinto
26.14     n = self.fp.readinto(b)
26.14   File &quot;/usr/local/lib/python3.9/socket.py&quot;, line 716, in readinto
26.14     return self._sock.recv_into(b)
26.14   File &quot;/usr/local/lib/python3.9/ssl.py&quot;, line 1275, in recv_into
26.14     return self.read(nbytes, buffer)
26.14   File &quot;/usr/local/lib/python3.9/ssl.py&quot;, line 1133, in read
26.14     return self._sslobj.read(len, buffer)
26.14 socket.timeout: The read operation timed out
26.14 
26.14 During handling of the above exception, another exception occurred:
26.14 
26.14 Traceback (most recent call last):
26.14   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/cli/base_command.py&quot;, line 160, in exc_logging_wrapper
26.14     status = run_func(*args)
26.14   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/cli/req_command.py&quot;, line 247, in wrapper
26.14     return func(self, options, args)
26.14   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/commands/install.py&quot;, line 419, in run
26.14     requirement_set = resolver.resolve(
26.14   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/resolver.py&quot;, line 92, in resolve
26.14     result = self._result = resolver.resolve(
26.14   File &quot;/usr/local/lib/python3.9/site-packages/pip/_vendor/resolvelib/resolvers.py&quot;, line 481, in resolve
26.14     state = resolution.resolve(requirements, max_rounds=max_rounds)
26.14   File &quot;/usr/local/lib/python3.9/site-packages/pip/_vendor/resolvelib/resolvers.py&quot;, line 373, in resolve
26.14     failure_causes = self._attempt_to_pin_criterion(name)
26.14   File &quot;/usr/local/lib/python3.9/site-packages/pip/_vendor/resolvelib/resolvers.py&quot;, line 213, in _attempt_to_pin_criterion
26.14     criteria = self._get_updated_criteria(candidate)
26.14   File &quot;/usr/local/lib/python3.9/site-packages/pip/_vendor/resolvelib/resolvers.py&quot;, line 204, in _get_updated_criteria
26.14     self._add_to_criteria(criteria, requirement, parent=candidate)
26.14   File &quot;/usr/local/lib/python3.9/site-packages/pip/_vendor/resolvelib/resolvers.py&quot;, line 172, in _add_to_criteria
26.14     if not criterion.candidates:
26.14   File &quot;/usr/local/lib/python3.9/site-packages/pip/_vendor/resolvelib/structs.py&quot;, line 151, in __bool__
26.14     return bool(self._sequence)
26.14   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/found_candidates.py&quot;, line 155, in __bool__
26.14     return any(self)
26.14   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/found_candidates.py&quot;, line 143, in &lt;genexpr&gt;
26.14     return (c for c in iterator if id(c) not in self._incompatible_ids)
26.14   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/found_candidates.py&quot;, line 47, in _iter_built
26.14     candidate = func()
26.14   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/factory.py&quot;, line 206, in _make_candidate_from_link
26.14     self._link_candidate_cache[link] = LinkCandidate(
26.14   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/candidates.py&quot;, line 297, in __init__
26.14     super().__init__(
26.14   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/candidates.py&quot;, line 162, in __init__
26.14     self.dist = self._prepare()
26.14   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/candidates.py&quot;, line 231, in _prepare
26.14     dist = self._prepare_distribution()
26.14   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/candidates.py&quot;, line 308, in _prepare_distribution
26.14     return preparer.prepare_linked_requirement(self._ireq, parallel_builds=True)
26.14   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/operations/prepare.py&quot;, line 491, in prepare_linked_requirement
26.14     return self._prepare_linked_requirement(req, parallel_builds)
26.14   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/operations/prepare.py&quot;, line 536, in _prepare_linked_requirement
26.14     local_file = unpack_url(
26.14   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/operations/prepare.py&quot;, line 166, in unpack_url
26.14     file = get_http_url(
26.14   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/operations/prepare.py&quot;, line 107, in get_http_url
26.14     from_path, content_type = download(link, temp_dir.path)
26.14   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/network/download.py&quot;, line 147, in __call__
26.14     for chunk in chunks:
26.14   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/cli/progress_bars.py&quot;, line 53, in _rich_progress_bar
26.14     for chunk in iterable:
26.14   File &quot;/usr/local/lib/python3.9/site-packages/pip/_internal/network/utils.py&quot;, line 63, in response_chunks
26.14     for chunk in response.raw.stream(
26.14   File &quot;/usr/local/lib/python3.9/site-packages/pip/_vendor/urllib3/response.py&quot;, line 622, in stream
26.14     data = self.read(amt=amt, decode_content=decode_content)
26.14   File &quot;/usr/local/lib/python3.9/site-packages/pip/_vendor/urllib3/response.py&quot;, line 587, in read
26.14     raise IncompleteRead(self._fp_bytes_read, self.length_remaining)
26.14   File &quot;/usr/local/lib/python3.9/contextlib.py&quot;, line 137, in __exit__
26.14     self.gen.throw(typ, value, traceback)
26.14   File &quot;/usr/local/lib/python3.9/site-packages/pip/_vendor/urllib3/response.py&quot;, line 443, in _error_catcher
26.14     raise ReadTimeoutError(self._pool, None, &quot;Read timed out.&quot;)
26.14 pip._vendor.urllib3.exceptions.ReadTimeoutError: HTTPSConnectionPool(host=&#39;files.pythonhosted.org&#39;, port=443): Read timed out.
26.40 
26.40 [notice] A new release of pip is available: 23.0.1 -&gt; 25.2
26.40 [notice] To update, run: pip install --upgrade pip
------
failed to solve: process &quot;/bin/sh -c pip install --no-cache-dir -r requirements.txt&quot; did not complete successfully: exit code: 2
🚀 Starting services...
[+] Building 447.3s (19/22)                                                                                                                docker:default
 =&gt; [action-server internal] load build definition from Dockerfile.actions                                                                           0.0s
 =&gt; =&gt; transferring dockerfile: 297B                                                                                                                 0.0s
 =&gt; [action-server internal] load metadata for docker.io/library/python:3.9-slim                                                                     0.8s
 =&gt; [action-server internal] load .dockerignore                                                                                                      0.0s
 =&gt; =&gt; transferring context: 154B                                                                                                                    0.0s
 =&gt; [action-server 1/6] FROM docker.io/library/python:3.9-slim@sha256:71b97a8eed69cddd132431327ff7c204fd6ea3d38e0c5d11d52f9661482bc8a3               0.0s
 =&gt; [action-server internal] load build context                                                                                                      0.0s
 =&gt; =&gt; transferring context: 284B                                                                                                                    0.0s
 =&gt; CACHED [action-server 2/6] WORKDIR /app                                                                                                          0.0s
 =&gt; CACHED [action-server 3/6] COPY requirements.txt .                                                                                               0.0s
 =&gt; [action-server 4/6] RUN pip install --no-cache-dir -r requirements.txt                                                                         225.7s
 =&gt; [action-server 5/6] COPY actions/ ./actions/                                                                                                     0.3s
 =&gt; [action-server 6/6] COPY config.json .                                                                                                           0.1s
 =&gt; [action-server] exporting to image                                                                                                              94.9s
 =&gt; =&gt; exporting layers                                                                                                                             94.8s
 =&gt; =&gt; writing image sha256:3f16313fb76d2121f41b0aac5313158a684e82b19c27bccc0ec4b13c976631bd                                                         0.0s
 =&gt; =&gt; naming to docker.io/library/remind_bot-action-server                                                                                          0.0s
 =&gt; [rasa-server internal] load build definition from Dockerfile.rasa                                                                                0.0s
 =&gt; =&gt; transferring dockerfile: 344B                                                                                                                 0.0s
 =&gt; [rasa-server internal] load metadata for docker.io/rasa/rasa:3.6.21                                                                              2.7s
 =&gt; [rasa-server internal] load .dockerignore                                                                                                        0.0s
 =&gt; =&gt; transferring context: 154B                                                                                                                    0.0s
 =&gt; [rasa-server 1/7] FROM docker.io/rasa/rasa:3.6.21@sha256:7c0204065d4859e1b7a691c972ca3d26f5d39ad23fbd992b654084721226d813                      106.1s
 =&gt; =&gt; resolve docker.io/rasa/rasa:3.6.21@sha256:7c0204065d4859e1b7a691c972ca3d26f5d39ad23fbd992b654084721226d813                                    0.0s
 =&gt; =&gt; sha256:7c0204065d4859e1b7a691c972ca3d26f5d39ad23fbd992b654084721226d813 1.61kB / 1.61kB                                                       0.0s
 =&gt; =&gt; sha256:0e5aa551ea881f1b6fcfab87032007ac64da8563632b87173b618b086a7a0cf0 1.82kB / 1.82kB                                                       0.0s
 =&gt; =&gt; sha256:e4ea2b9d9dc38044ee4038855f5593313ecfcb0a3c652cf686c3f85b9b93ec63 6.96kB / 6.96kB                                                       0.0s
 =&gt; =&gt; sha256:445a6a12be2be54b4da18d7c77d4a41bc4746bc422f1f4325a60ff4fc7ea2e5d 29.54MB / 29.54MB                                                     1.5s
 =&gt; =&gt; sha256:50532f3355eccaa7f184475b4da83a263ac11f86cc1c6618d28b6567c3fe7675 284.83MB / 284.83MB                                                   7.1s
 =&gt; =&gt; sha256:24e4804a1dbf7990aa9d9ec6e01b2a56aadfdfb721f7c1c1f9207adfe2943052 1.46MB / 1.46MB                                                       2.0s
 =&gt; =&gt; sha256:5c0e8d16e4048876e4b65942adc6035d36abd48d50643659e6e8b25d12c641c9 1.09kB / 1.09kB                                                       4.1s
 =&gt; =&gt; sha256:01639847809681d4e0ac6dad6d2efcfe1fc34aa0b0d46dfc5bd9d41483e01c7b 4.22kB / 4.22kB                                                       5.1s
 =&gt; =&gt; extracting sha256:445a6a12be2be54b4da18d7c77d4a41bc4746bc422f1f4325a60ff4fc7ea2e5d                                                           19.1s
 =&gt; =&gt; sha256:01029823f2260f38ea9d97d01059d16f7184edee64e335ce1811fa611380484d 807.93MB / 807.93MB                                                  22.4s
 =&gt; =&gt; sha256:4f4fb700ef54461cfa02571ae0db9a0dc1e0cdb5577484a6d75e68dc38e8acc1 32B / 32B                                                             6.5s
 =&gt; =&gt; sha256:903b9bd8420885647ab87a8d4beb3496b9d79835baf6ba9086470c0caa4cb631 2.30kB / 2.30kB                                                       8.0s
 =&gt; =&gt; extracting sha256:50532f3355eccaa7f184475b4da83a263ac11f86cc1c6618d28b6567c3fe7675                                                           20.4s
 =&gt; =&gt; extracting sha256:24e4804a1dbf7990aa9d9ec6e01b2a56aadfdfb721f7c1c1f9207adfe2943052                                                            0.2s
 =&gt; =&gt; extracting sha256:5c0e8d16e4048876e4b65942adc6035d36abd48d50643659e6e8b25d12c641c9                                                            0.0s
 =&gt; =&gt; extracting sha256:01639847809681d4e0ac6dad6d2efcfe1fc34aa0b0d46dfc5bd9d41483e01c7b                                                            0.0s
 =&gt; =&gt; extracting sha256:01029823f2260f38ea9d97d01059d16f7184edee64e335ce1811fa611380484d                                                           60.3s
 =&gt; =&gt; extracting sha256:4f4fb700ef54461cfa02571ae0db9a0dc1e0cdb5577484a6d75e68dc38e8acc1                                                            0.0s
 =&gt; =&gt; extracting sha256:903b9bd8420885647ab87a8d4beb3496b9d79835baf6ba9086470c0caa4cb631                                                            0.0s
 =&gt; [rasa-server internal] load build context                                                                                                        0.1s
 =&gt; =&gt; transferring context: 81.65kB                                                                                                                 0.0s
 =&gt; [rasa-server 2/7] WORKDIR /app                                                                                                                   0.1s
 =&gt; [rasa-server 3/7] COPY requirements.txt .                                                                                                        0.1s
 =&gt; ERROR [rasa-server 4/7] RUN pip install --no-cache-dir -r requirements.txt                                                                      15.0s
------
 &gt; [rasa-server 4/7] RUN pip install --no-cache-dir -r requirements.txt:
2.404 Requirement already satisfied: rasa==3.6.21 in /opt/venv/lib/python3.10/site-packages (from -r requirements.txt (line 2)) (3.6.21)
2.406 Requirement already satisfied: rasa-sdk==3.6.2 in /opt/venv/lib/python3.10/site-packages (from -r requirements.txt (line 3)) (3.6.2)
2.696 Collecting gspread==6.2.1
2.935   Downloading gspread-6.2.1-py3-none-any.whl (59 kB)
2.990      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 60.0/60.0 kB 1.0 MB/s eta 0:00:00
3.247 Collecting google-api-python-client==2.178.0
3.285   Downloading google_api_python_client-2.178.0-py3-none-any.whl (13.8 MB)
3.546      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 13.8/13.8 MB 115.2 MB/s eta 0:00:00
3.614 Requirement already satisfied: google-auth-oauthlib==1.0.0 in /opt/venv/lib/python3.10/site-packages (from -r requirements.txt (line 8)) (1.0.0)
3.741 Collecting python-telegram-bot==13.15
3.780   Downloading python_telegram_bot-13.15-py3-none-any.whl (519 kB)
3.787      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 519.2/519.2 kB 203.4 MB/s eta 0:00:00
4.306 Collecting pandas==2.3.1
4.345   Downloading pandas-2.3.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (12.3 MB)
4.450      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.3/12.3 MB 119.6 MB/s eta 0:00:00
4.605 Collecting requests==2.32.4
4.640   Downloading requests-2.32.4-py3-none-any.whl (64 kB)
4.647      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 64.8/64.8 kB 179.2 MB/s eta 0:00:00
4.891 Collecting psycopg2-binary==2.9.10
4.930   Downloading psycopg2_binary-2.9.10-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.0 MB)
4.957      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.0/3.0 MB 140.9 MB/s eta 0:00:00
5.180 Requirement already satisfied: typing-utils&lt;0.2.0,&gt;=0.1.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.1.0)
5.182 Requirement already satisfied: sanic&lt;21.13,&gt;=21.12 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (21.12.2)
5.184 Requirement already satisfied: boto3&lt;2.0.0,&gt;=1.26.136 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.27.1)
5.185 Requirement already satisfied: tensorflow_hub&lt;0.14.0,&gt;=0.13.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.13.0)
5.187 Requirement already satisfied: google-auth&lt;3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.21.0)
5.188 Requirement already satisfied: typing-extensions&lt;5.0.0,&gt;=4.1.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.7.1)
5.190 Requirement already satisfied: prompt-toolkit&lt;3.0.29,&gt;=3.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.0.28)
5.190 Requirement already satisfied: safetensors&lt;0.5.0,&gt;=0.4.5 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.4.5)
5.195 Requirement already satisfied: scipy&lt;1.11.0,&gt;=1.10.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.10.1)
5.201 Requirement already satisfied: coloredlogs&lt;16,&gt;=10 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (15.0.1)
5.663 Collecting pydantic&lt;1.10.10
5.702   Downloading pydantic-1.10.9-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.1 MB)
5.737      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.1/3.1 MB 131.5 MB/s eta 0:00:00
5.758 Requirement already satisfied: aio-pika&lt;8.2.4,&gt;=6.7.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (8.2.3)
5.763 Requirement already satisfied: PyJWT[crypto]&lt;3.0.0,&gt;=2.0.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.7.0)
5.767 Requirement already satisfied: scikit-learn&lt;1.2,&gt;=0.22 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.1.3)
5.771 Requirement already satisfied: webexteamssdk&lt;1.7.0,&gt;=1.1.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.6.1)
5.773 Requirement already satisfied: attrs&lt;22.2,&gt;=19.3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (22.1.0)
5.774 Requirement already satisfied: skops==0.9.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.9.0)
5.776 Requirement already satisfied: sentry-sdk&lt;1.15.0,&gt;=0.17.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.14.0)
5.777 Requirement already satisfied: sanic-jwt&lt;2.0.0,&gt;=1.6.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.8.0)
5.778 Requirement already satisfied: sklearn-crfsuite&lt;0.4,&gt;=0.3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.3.6)
5.780 Requirement already satisfied: python-dateutil&lt;2.9,&gt;=2.8 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.8.2)
5.782 Requirement already satisfied: aiogram&lt;2.26 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.15)
5.782 Requirement already satisfied: structlog-sentry&lt;3.0.0,&gt;=2.0.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.0.3)
5.786 Requirement already satisfied: absl-py&lt;1.5,&gt;=0.9 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.4.0)
5.788 Requirement already satisfied: slack-sdk&lt;4.0.0,&gt;=3.19.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.21.3)
5.791 Requirement already satisfied: mattermostwrapper&lt;2.3,&gt;=2.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.2)
5.986 Requirement already satisfied: protobuf&lt;4.23.4,&gt;=4.23.3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.23.3)
5.986 Requirement already satisfied: aiohttp&lt;3.10,&gt;=3.9.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.9.3)
5.986 Requirement already satisfied: networkx&lt;2.7,&gt;=2.4 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.6.3)
5.986 Requirement already satisfied: terminaltables&lt;3.2.0,&gt;=3.1.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.1.10)
5.986 Requirement already satisfied: python-socketio&lt;6,&gt;=4.4 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (5.8.0)
5.986 Requirement already satisfied: randomname&lt;0.2.0,&gt;=0.1.5 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.1.5)
5.986 Requirement already satisfied: certifi&gt;=2023.7.22 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2023.7.22)
5.986 Requirement already satisfied: apscheduler&lt;3.10,&gt;=3.6 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.9.1.post1)
5.986 Requirement already satisfied: cryptography&gt;=41.0.7 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (41.0.7)
5.986 Requirement already satisfied: sanic-cors&lt;2.1.0,&gt;=2.0.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.0.1)
5.986 Requirement already satisfied: rocketchat_API&lt;1.31.0,&gt;=0.6.31 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.30.0)
5.986 Requirement already satisfied: confluent-kafka&lt;3.0.0,&gt;=1.9.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.1.1)
5.986 Requirement already satisfied: fbmessenger&lt;6.1.0,&gt;=6.0.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (6.0.0)
5.986 Requirement already satisfied: pydot&lt;1.5,&gt;=1.4 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.4.2)
5.986 Requirement already satisfied: portalocker&lt;3.0.0,&gt;=2.7.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.7.0)
5.986 Requirement already satisfied: ruamel.yaml&lt;0.17.22,&gt;=0.16.5 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.17.21)
5.986 Requirement already satisfied: pykwalify&lt;1.9,&gt;=1.7 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.8.0)
5.986 Requirement already satisfied: pytz&lt;2023.0,&gt;=2019.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2022.7.1)
5.986 Requirement already satisfied: redis&lt;5.0,&gt;=4.5.3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.6.0)
5.986 Requirement already satisfied: SQLAlchemy&lt;1.5.0,&gt;=1.4.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.4.49)
5.986 Requirement already satisfied: websockets&lt;11.0,&gt;=10.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (10.4)
5.986 Requirement already satisfied: questionary&lt;1.11.0,&gt;=1.5.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.10.0)
5.986 Requirement already satisfied: tensorflow-text==2.12.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.12.0)
5.986 Requirement already satisfied: matplotlib&lt;3.6,&gt;=3.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.5.3)
5.986 Requirement already satisfied: numpy&lt;1.25.0,&gt;=1.19.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.23.5)
5.986 Requirement already satisfied: tqdm&lt;5.0,&gt;=4.31 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.65.0)
5.986 Requirement already satisfied: setuptools&lt;70.4.0,&gt;=70.3.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (70.3.0)
5.986 Requirement already satisfied: tensorflow-io-gcs-filesystem==0.32 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.32.0)
5.986 Requirement already satisfied: structlog&lt;24.0.0,&gt;=23.1.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (23.1.0)
5.986 Requirement already satisfied: dnspython==2.3.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.3.0)
5.986 Requirement already satisfied: colorhash&lt;1.3.0,&gt;=1.0.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.2.1)
5.986 Requirement already satisfied: sanic-routing&lt;0.8.0,&gt;=0.7.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.7.2)
5.986 Requirement already satisfied: ujson&lt;6.0,&gt;=1.35 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (5.8.0)
5.986 Requirement already satisfied: colorclass&lt;2.3,&gt;=2.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.2.2)
5.986 Requirement already satisfied: twilio&lt;8.3,&gt;=6.26 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (8.2.2)
5.986 Requirement already satisfied: pymongo[srv,tls]&lt;4.4,&gt;=3.8 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.3.3)
5.986 Requirement already satisfied: packaging&lt;21.0,&gt;=20.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (20.9)
5.986 Requirement already satisfied: python-engineio!=5.0.0,&lt;6,&gt;=4 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.5.1)
5.986 Requirement already satisfied: wheel&gt;=0.38.1 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.40.0)
5.986 Requirement already satisfied: jsonpickle&lt;3.1,&gt;=1.3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.0.4)
5.986 Requirement already satisfied: pluggy&lt;2.0.0,&gt;=1.0.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.2.0)
5.986 Requirement already satisfied: pyyaml&gt;=6.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (6.0.1)
5.986 Requirement already satisfied: regex&lt;2022.11,&gt;=2020.6 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2022.10.31)
5.986 Requirement already satisfied: tensorflow==2.12.0 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.12.0)
5.986 Requirement already satisfied: tarsafe&lt;0.0.5,&gt;=0.0.3 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.0.4)
5.986 Requirement already satisfied: jsonschema&lt;4.18,&gt;=3.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.17.3)
5.986 Requirement already satisfied: CacheControl&lt;0.13.0,&gt;=0.12.9 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.12.14)
5.986 Requirement already satisfied: dask==2022.10.2 in /opt/venv/lib/python3.10/site-packages (from rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2022.10.2)
6.239 Collecting google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,&lt;3.0.0,&gt;=1.31.5
6.276   Downloading google_api_core-2.25.1-py3-none-any.whl (160 kB)
6.283      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 160.8/160.8 kB 164.2 MB/s eta 0:00:00
6.344 Collecting httplib2&lt;1.0.0,&gt;=0.19.0
6.381   Downloading httplib2-0.30.0-py3-none-any.whl (91 kB)
6.387      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 91.1/91.1 kB 164.7 MB/s eta 0:00:00
6.441 Collecting uritemplate&lt;5,&gt;=3.0.1
6.478   Downloading uritemplate-4.2.0-py3-none-any.whl (11 kB)
6.537 Collecting google-auth-httplib2&lt;1.0.0,&gt;=0.2.0
6.574   Downloading google_auth_httplib2-0.2.0-py2.py3-none-any.whl (9.3 kB)
6.585 Requirement already satisfied: requests-oauthlib&gt;=0.7.0 in /opt/venv/lib/python3.10/site-packages (from google-auth-oauthlib==1.0.0-&gt;-r requirements.txt (line 8)) (1.3.1)
6.758 Collecting tornado==6.1
6.798   Downloading tornado-6.1.tar.gz (497 kB)
6.804      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 497.4/497.4 kB 228.0 MB/s eta 0:00:00
6.931   Preparing metadata (setup.py): started
7.752   Preparing metadata (setup.py): finished with status &#39;done&#39;
7.837 Collecting apscheduler&lt;3.10,&gt;=3.6
7.875   Downloading APScheduler-3.6.3-py2.py3-none-any.whl (58 kB)
7.880      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 58.9/58.9 kB 155.5 MB/s eta 0:00:00
7.955 Collecting cachetools==4.2.2
7.989   Downloading cachetools-4.2.2-py3-none-any.whl (11 kB)
8.183 Collecting tzdata&gt;=2022.7
8.219   Downloading tzdata-2025.2-py2.py3-none-any.whl (347 kB)
8.225      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 347.8/347.8 kB 199.4 MB/s eta 0:00:00
8.288 Requirement already satisfied: charset_normalizer&lt;4,&gt;=2 in /opt/venv/lib/python3.10/site-packages (from requests==2.32.4-&gt;-r requirements.txt (line 15)) (3.1.0)
8.291 Requirement already satisfied: urllib3&lt;3,&gt;=1.21.1 in /opt/venv/lib/python3.10/site-packages (from requests==2.32.4-&gt;-r requirements.txt (line 15)) (1.26.16)
8.292 Requirement already satisfied: idna&lt;4,&gt;=2.5 in /opt/venv/lib/python3.10/site-packages (from requests==2.32.4-&gt;-r requirements.txt (line 15)) (3.4)
8.335 Requirement already satisfied: six&gt;=1.4.0 in /opt/venv/lib/python3.10/site-packages (from apscheduler&lt;3.10,&gt;=3.6-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.16.0)
8.337 Requirement already satisfied: tzlocal&gt;=1.2 in /opt/venv/lib/python3.10/site-packages (from apscheduler&lt;3.10,&gt;=3.6-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (5.0.1)
8.373 Requirement already satisfied: cloudpickle&gt;=1.1.1 in /opt/venv/lib/python3.10/site-packages (from dask==2022.10.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.2.1)
8.374 Requirement already satisfied: partd&gt;=0.3.10 in /opt/venv/lib/python3.10/site-packages (from dask==2022.10.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.4.0)
8.376 Requirement already satisfied: click&gt;=7.0 in /opt/venv/lib/python3.10/site-packages (from dask==2022.10.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (8.1.3)
8.378 Requirement already satisfied: fsspec&gt;=0.6.0 in /opt/venv/lib/python3.10/site-packages (from dask==2022.10.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2023.6.0)
8.379 Requirement already satisfied: toolz&gt;=0.8.2 in /opt/venv/lib/python3.10/site-packages (from dask==2022.10.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.12.0)
8.442 Requirement already satisfied: huggingface-hub&gt;=0.17.0 in /opt/venv/lib/python3.10/site-packages (from skops==0.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.27.0)
8.443 Requirement already satisfied: tabulate&gt;=0.8.8 in /opt/venv/lib/python3.10/site-packages (from skops==0.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.9.0)
8.479 Requirement already satisfied: grpcio&lt;2.0,&gt;=1.24.3 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.56.0)
8.482 Requirement already satisfied: astunparse&gt;=1.6.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.6.3)
8.483 Requirement already satisfied: libclang&gt;=13.0.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (16.0.0)
8.485 Requirement already satisfied: tensorboard&lt;2.13,&gt;=2.12 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.12.3)
8.486 Requirement already satisfied: wrapt&lt;1.15,&gt;=1.11.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.14.1)
8.488 Requirement already satisfied: termcolor&gt;=1.1.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.3.0)
8.489 Requirement already satisfied: opt-einsum&gt;=2.3.2 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.3.0)
8.491 Requirement already satisfied: google-pasta&gt;=0.1.1 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.2.0)
8.492 Requirement already satisfied: tensorflow-estimator&lt;2.13,&gt;=2.12.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.12.0)
8.494 Requirement already satisfied: jax&gt;=0.3.15 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.4.13)
8.496 Requirement already satisfied: keras&lt;2.13,&gt;=2.12.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.12.0)
8.498 Requirement already satisfied: flatbuffers&gt;=2.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (23.5.26)
8.499 Requirement already satisfied: h5py&gt;=2.9.0 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.9.0)
8.501 Requirement already satisfied: gast&lt;=0.4.0,&gt;=0.2.1 in /opt/venv/lib/python3.10/site-packages (from tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.4.0)
8.554 Requirement already satisfied: aiormq~=6.4.0 in /opt/venv/lib/python3.10/site-packages (from aio-pika&lt;8.2.4,&gt;=6.7.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (6.4.2)
8.555 Requirement already satisfied: yarl in /opt/venv/lib/python3.10/site-packages (from aio-pika&lt;8.2.4,&gt;=6.7.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.9.2)
8.575 Requirement already satisfied: Babel&gt;=2.8.0 in /opt/venv/lib/python3.10/site-packages (from aiogram&lt;2.26-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.9.1)
8.598 Requirement already satisfied: multidict&lt;7.0,&gt;=4.5 in /opt/venv/lib/python3.10/site-packages (from aiohttp&lt;3.10,&gt;=3.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (5.2.0)
8.600 Requirement already satisfied: frozenlist&gt;=1.1.1 in /opt/venv/lib/python3.10/site-packages (from aiohttp&lt;3.10,&gt;=3.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.3.3)
8.602 Requirement already satisfied: aiosignal&gt;=1.1.2 in /opt/venv/lib/python3.10/site-packages (from aiohttp&lt;3.10,&gt;=3.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.3.1)
8.604 Requirement already satisfied: async-timeout&lt;5.0,&gt;=4.0 in /opt/venv/lib/python3.10/site-packages (from aiohttp&lt;3.10,&gt;=3.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.0.2)
8.665 Requirement already satisfied: jmespath&lt;2.0.0,&gt;=0.7.1 in /opt/venv/lib/python3.10/site-packages (from boto3&lt;2.0.0,&gt;=1.26.136-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.0.1)
8.666 Requirement already satisfied: botocore&lt;1.31.0,&gt;=1.30.1 in /opt/venv/lib/python3.10/site-packages (from boto3&lt;2.0.0,&gt;=1.26.136-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.30.1)
8.668 Requirement already satisfied: s3transfer&lt;0.7.0,&gt;=0.6.0 in /opt/venv/lib/python3.10/site-packages (from boto3&lt;2.0.0,&gt;=1.26.136-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.6.1)
8.676 Requirement already satisfied: msgpack&gt;=0.5.2 in /opt/venv/lib/python3.10/site-packages (from CacheControl&lt;0.13.0,&gt;=0.12.9-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.0.5)
8.702 Requirement already satisfied: humanfriendly&gt;=9.1 in /opt/venv/lib/python3.10/site-packages (from coloredlogs&lt;16,&gt;=10-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (10.0)
8.817 Requirement already satisfied: cffi&gt;=1.12 in /opt/venv/lib/python3.10/site-packages (from cryptography&gt;=41.0.7-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.15.1)
8.964 Collecting googleapis-common-protos&lt;2.0.0,&gt;=1.56.2
9.001   Downloading googleapis_common_protos-1.70.0-py3-none-any.whl (294 kB)
9.007      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 294.5/294.5 kB 143.8 MB/s eta 0:00:00
9.087 Collecting proto-plus&lt;2.0.0,&gt;=1.22.3
9.125   Downloading proto_plus-1.26.1-py3-none-any.whl (50 kB)
9.129      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 50.2/50.2 kB 161.5 MB/s eta 0:00:00
9.157 Requirement already satisfied: rsa&lt;5,&gt;=3.1.4 in /opt/venv/lib/python3.10/site-packages (from google-auth&lt;3-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.9)
9.165 Requirement already satisfied: pyasn1-modules&gt;=0.2.1 in /opt/venv/lib/python3.10/site-packages (from google-auth&lt;3-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.3.0)
9.180 Requirement already satisfied: pyparsing&lt;4,&gt;=3.0.4 in /opt/venv/lib/python3.10/site-packages (from httplib2&lt;1.0.0,&gt;=0.19.0-&gt;google-api-python-client==2.178.0-&gt;-r requirements.txt (line 7)) (3.1.0)
9.258 Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,&gt;=0.14.0 in /opt/venv/lib/python3.10/site-packages (from jsonschema&lt;4.18,&gt;=3.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.19.3)
9.274 Requirement already satisfied: pillow&gt;=6.2.0 in /opt/venv/lib/python3.10/site-packages (from matplotlib&lt;3.6,&gt;=3.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (10.0.1)
9.276 Requirement already satisfied: fonttools&gt;=4.22.0 in /opt/venv/lib/python3.10/site-packages (from matplotlib&lt;3.6,&gt;=3.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (4.40.0)
9.277 Requirement already satisfied: cycler&gt;=0.10 in /opt/venv/lib/python3.10/site-packages (from matplotlib&lt;3.6,&gt;=3.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.11.0)
9.279 Requirement already satisfied: kiwisolver&gt;=1.0.1 in /opt/venv/lib/python3.10/site-packages (from matplotlib&lt;3.6,&gt;=3.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.4.4)
9.367 Requirement already satisfied: wcwidth in /opt/venv/lib/python3.10/site-packages (from prompt-toolkit&lt;3.0.29,&gt;=3.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.2.6)
9.434 Requirement already satisfied: docopt&gt;=0.6.2 in /opt/venv/lib/python3.10/site-packages (from pykwalify&lt;1.9,&gt;=1.7-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.6.2)
9.489 Requirement already satisfied: bidict&gt;=0.21.0 in /opt/venv/lib/python3.10/site-packages (from python-socketio&lt;6,&gt;=4.4-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.22.1)
9.533 Requirement already satisfied: fire in /opt/venv/lib/python3.10/site-packages (from randomname&lt;0.2.0,&gt;=0.1.5-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.5.0)
9.574 Requirement already satisfied: oauthlib&gt;=3.0.0 in /opt/venv/lib/python3.10/site-packages (from requests-oauthlib&gt;=0.7.0-&gt;google-auth-oauthlib==1.0.0-&gt;-r requirements.txt (line 8)) (3.2.2)
9.605 Requirement already satisfied: ruamel.yaml.clib&gt;=0.2.6 in /opt/venv/lib/python3.10/site-packages (from ruamel.yaml&lt;0.17.22,&gt;=0.16.5-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.2.7)
9.752 Requirement already satisfied: aiofiles&gt;=0.6.0 in /opt/venv/lib/python3.10/site-packages (from sanic&lt;21.13,&gt;=21.12-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (23.1.0)
9.754 Requirement already satisfied: httptools&gt;=0.0.10 in /opt/venv/lib/python3.10/site-packages (from sanic&lt;21.13,&gt;=21.12-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.5.0)
9.758 Requirement already satisfied: uvloop&gt;=0.5.3 in /opt/venv/lib/python3.10/site-packages (from sanic&lt;21.13,&gt;=21.12-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.17.0)
9.840 Requirement already satisfied: joblib&gt;=1.0.0 in /opt/venv/lib/python3.10/site-packages (from scikit-learn&lt;1.2,&gt;=0.22-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.4.2)
9.841 Requirement already satisfied: threadpoolctl&gt;=2.0.0 in /opt/venv/lib/python3.10/site-packages (from scikit-learn&lt;1.2,&gt;=0.22-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.1.0)
9.941 Requirement already satisfied: python-crfsuite&gt;=0.8.3 in /opt/venv/lib/python3.10/site-packages (from sklearn-crfsuite&lt;0.4,&gt;=0.3-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.9.9)
10.08 Requirement already satisfied: greenlet!=0.4.17 in /opt/venv/lib/python3.10/site-packages (from SQLAlchemy&lt;1.5.0,&gt;=1.4.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.0.2)
10.21 Requirement already satisfied: aiohttp-retry&gt;=2.8.3 in /opt/venv/lib/python3.10/site-packages (from twilio&lt;8.3,&gt;=6.26-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.8.3)
10.33 Requirement already satisfied: future in /opt/venv/lib/python3.10/site-packages (from webexteamssdk&lt;1.7.0,&gt;=1.1.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.18.3)
10.35 Requirement already satisfied: requests-toolbelt in /opt/venv/lib/python3.10/site-packages (from webexteamssdk&lt;1.7.0,&gt;=1.1.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.0.0)
10.43 Requirement already satisfied: pamqp==3.2.1 in /opt/venv/lib/python3.10/site-packages (from aiormq~=6.4.0-&gt;aio-pika&lt;8.2.4,&gt;=6.7.1-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.2.1)
10.63 Requirement already satisfied: pycparser in /opt/venv/lib/python3.10/site-packages (from cffi&gt;=1.12-&gt;cryptography&gt;=41.0.7-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.21)
11.09 Requirement already satisfied: filelock in /opt/venv/lib/python3.10/site-packages (from huggingface-hub&gt;=0.17.0-&gt;skops==0.9.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.12.2)
11.17 Requirement already satisfied: ml_dtypes&gt;=0.1.0 in /opt/venv/lib/python3.10/site-packages (from jax&gt;=0.3.15-&gt;tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.2.0)
11.34 Requirement already satisfied: locket in /opt/venv/lib/python3.10/site-packages (from partd&gt;=0.3.10-&gt;dask==2022.10.2-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (1.0.0)
11.41 Requirement already satisfied: pyasn1&lt;0.6.0,&gt;=0.4.6 in /opt/venv/lib/python3.10/site-packages (from pyasn1-modules&gt;=0.2.1-&gt;google-auth&lt;3-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.5.0)
11.59 Requirement already satisfied: werkzeug&gt;=1.0.1 in /opt/venv/lib/python3.10/site-packages (from tensorboard&lt;2.13,&gt;=2.12-&gt;tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.3.6)
11.62 Requirement already satisfied: tensorboard-data-server&lt;0.8.0,&gt;=0.7.0 in /opt/venv/lib/python3.10/site-packages (from tensorboard&lt;2.13,&gt;=2.12-&gt;tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (0.7.1)
11.62 Requirement already satisfied: markdown&gt;=2.6.8 in /opt/venv/lib/python3.10/site-packages (from tensorboard&lt;2.13,&gt;=2.12-&gt;tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (3.4.3)
12.03 Requirement already satisfied: MarkupSafe&gt;=2.1.1 in /opt/venv/lib/python3.10/site-packages (from werkzeug&gt;=1.0.1-&gt;tensorboard&lt;2.13,&gt;=2.12-&gt;tensorflow==2.12.0-&gt;rasa==3.6.21-&gt;-r requirements.txt (line 2)) (2.1.3)
12.19 Building wheels for collected packages: tornado
12.20   Building wheel for tornado (setup.py): started
13.64   Building wheel for tornado (setup.py): finished with status &#39;done&#39;
13.64   Created wheel for tornado: filename=tornado-6.1-cp310-cp310-linux_x86_64.whl size=421981 sha256=ac50d3ab2f6275420540dcf2bcd777e6b56e8672cefed126671454743dc3213c
13.64   Stored in directory: /tmp/pip-ephem-wheel-cache-qw2ui2cr/wheels/34/83/69/b89863a68e62add6e149dbaadcc049886105ce2405c1979bf2
13.65 Successfully built tornado
13.97 Installing collected packages: uritemplate, tzdata, tornado, requests, pydantic, psycopg2-binary, proto-plus, httplib2, googleapis-common-protos, cachetools, apscheduler, python-telegram-bot, pandas, google-auth-httplib2, google-api-core, gspread, google-api-python-client
13.97 ERROR: Could not install packages due to an OSError: [Errno 13] Permission denied: &#39;/opt/venv/lib/python3.10/site-packages/uritemplate&#39;
13.97 Check the permissions.
13.97 
14.59 
14.59 [notice] A new release of pip available: 22.3.1 -&gt; 25.2
14.59 [notice] To update, run: pip install --upgrade pip
------
failed to solve: process &quot;/bin/bash -o pipefail -c pip install --no-cache-dir -r requirements.txt&quot; did not complete successfully: exit code: 1
✅ Deployment complete!

📊 Service Status:
NAME      IMAGE     COMMAND   SERVICE   CREATED   STATUS    PORTS

🌐 Your services are running on:
- Rasa Server: http://your-azure-vm-ip:80
- Action Server: http://your-azure-vm-ip:5055
- Telegram Bridge: http://your-azure-vm-ip:5006

📝 To check logs: docker-compose -f azure-compose.yml logs -f
🛑 To stop services: docker-compose -f azure-compose.yml down
azureuser@Remindbot:~/Remind_Bot/Remind_Bot$ 


check once stll gettinf error

---

I see the issue. The Rasa server is still using the old Rasa image with virtual environment issues, but the action server built successfully. Let me check the current Dockerfile.rasa:

---

The Dockerfile looks correct, but Docker is still using cached layers from the old Rasa image. Let's force a complete rebuild:

```bash
# Remove all Docker data completely
docker system prune -a -f --volumes

# Remove any build cache
docker builder prune -a -f

# Now rebuild everything from scratch
./deploy-azure.sh
```

If this still doesn't work, let's check what's actually being built by looking at the docker-compose file:

---


The compose file is correct. The issue is Docker cache. Run these commands:

```bash
# Stop any running containers
docker-compose -f azure-compose.yml down

# Remove all Docker data
docker system prune -a -f --volumes

# Remove build cache
docker builder prune -a -f

# Now rebuild
./deploy-azure.sh
```

This should force Docker to use your updated Ubuntu-based Dockerfile instead of the cached Rasa image.

---

14.46 Installing collected packages: uritemplate, tzdata, tornado, requests, pydantic, psycopg2-binary, proto-plus, httplib2, googleapis-common-protos, cachetools, apscheduler, python-telegram-bot, pandas, google-auth-httplib2, google-api-core, gspread, google-api-python-client
14.47 ERROR: Could not install packages due to an OSError: [Errno 13] Permission denied: &#39;/opt/venv/lib/python3.10/site-packages/uritemplate&#39;
14.47 Check the permissions.

check once rasa dockerfile action server image is build but failed rasa server

---

The issue is that Docker is still using the old Rasa image despite our changes. Let me check what's happening. The error shows it's still trying to install to `/opt/venv/` which means it's using the Rasa base image, not our Ubuntu image.

Let's force Docker to rebuild by changing the Dockerfile name:

---

Creating a new Dockerfile with a different name to force Docker to rebuild

---

Now update the compose file to use the new Dockerfile:

---

Updating compose file to use the new Dockerfile name

---


Now run:

```bash
docker system prune -a -f
./deploy-azure.sh
```

This should force Docker to use our Ubuntu-based image instead of the cached Rasa image.

---

in  the new file you didnot add activation commands

---

You're right. Let me add the activation commands to the new Dockerfile:

---

Adding activation commands to make the Python HTTP server accessible from outside the container

---


Now run the deployment:

```bash
docker system prune -a -f
./deploy-azure.sh
```

The `--bind 0.0.0.0` flag ensures the HTTP server listens on all network interfaces, making it accessible from outside the container.

---

rasa run enable api core this is the command

---

You're right. Let me update the CMD to use the proper Rasa command:

---

Using the correct Rasa command to run the server with API enabled

---


Now run the deployment:

```bash
docker system prune -a -f
./deploy-azure.sh
```

This will use the proper Rasa command: `rasa run --enable-api --cors * --host 0.0.0.0 --port 5005`

---

can i delete old rasa dockerfile

---


Yes, you can delete the old Dockerfile.rasa since we're now using Dockerfile.rasa-new. But first, let's make sure the new deployment works properly.

Run the deployment first:

```bash
docker system prune -a -f
./deploy-azure.sh
```

If it works successfully, then you can delete the old file:

```bash
rm Dockerfile.rasa
```

And optionally rename the new one to the original name:

```bash
mv Dockerfile.rasa-new Dockerfile.rasa
```

Then update the compose file back to use `Dockerfile.rasa`:

```yaml
dockerfile: Dockerfile.rasa
```

But let's test the deployment first to make sure everything works before cleaning up the files.