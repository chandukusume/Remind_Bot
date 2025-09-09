# Quick Azure Deployment (No Domain Required)

## 1. Create Azure VM
```bash
az group create --name rasa-bot --location eastus
az vm create --resource-group rasa-bot --name rasa-vm --image Ubuntu2004 --admin-username azureuser --generate-ssh-keys --size Standard_B2s
az vm open-port --port 80 --resource-group rasa-bot --name rasa-vm
az vm open-port --port 5006 --resource-group rasa-bot --name rasa-vm
```

## 2. Get VM IP
```bash
az vm show -d -g rasa-bot -n rasa-vm --query publicIps -o tsv
```

## 3. Setup VM
```bash
# SSH to VM
ssh azureuser@<VM_IP>

# Install Docker
sudo apt update && sudo apt install -y docker.io docker-compose
sudo usermod -aG docker $USER
newgrp docker
```

## 4. Deploy Bot
```bash
# Upload files (from local machine)
scp -r Remind_Bot azureuser@<VM_IP>:~/

# On VM
cd ~/Remind_Bot
cp .env.example .env
nano .env  # Add your tokens

# Add credentials.json file
# Then run:
chmod +x deploy-azure.sh
./deploy-azure.sh
```

## 5. Set Telegram Webhook
```bash
curl -X POST "https://api.telegram.org/bot<BOT_TOKEN>/setWebhook" \
     -d '{"url": "http://<VM_IP>:5006/webhooks/telegram/webhook"}'
```

## Your bot will be accessible at:
- Rasa API: `http://<VM_IP>:80`
- Telegram webhook: `http://<VM_IP>:5006`