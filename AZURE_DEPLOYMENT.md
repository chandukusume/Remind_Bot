# Azure Deployment Guide for Rasa Chatbot

## Prerequisites

1. **Azure Account** with an active subscription
2. **Google Service Account** credentials file (`credentials.json`)
3. **Telegram Bot Token** and Chat ID
4. **Domain name** (optional but recommended)

## Step 1: Create Azure Virtual Machine

```bash
# Create resource group
az group create --name rasa-chatbot-rg --location eastus

# Create VM
az vm create \
  --resource-group rasa-chatbot-rg \
  --name rasa-chatbot-vm \
  --image Ubuntu2004 \
  --admin-username azureuser \
  --generate-ssh-keys \
  --size Standard_B2s

# Open ports
az vm open-port --port 80 --resource-group rasa-chatbot-rg --name rasa-chatbot-vm
az vm open-port --port 443 --resource-group rasa-chatbot-rg --name rasa-chatbot-vm
az vm open-port --port 5006 --resource-group rasa-chatbot-rg --name rasa-chatbot-vm
```

## Step 2: Setup VM Environment

SSH into your VM and install Docker:

```bash
# SSH to VM
ssh azureuser@<your-vm-public-ip>

# Install Docker
sudo apt update
sudo apt install -y docker.io docker-compose
sudo usermod -aG docker $USER
sudo systemctl enable docker
sudo systemctl start docker

# Install nginx (optional, for reverse proxy)
sudo apt install -y nginx
```

## Step 3: Deploy Your Application

1. **Upload your code** to the VM:
```bash
# From your local machine
scp -r /home/chandu/Remind_bot/Remind_Bot azureuser@<vm-ip>:~/
```

2. **Create environment file**:
```bash
# On the VM
cd ~/Remind_Bot
cp .env.example .env
nano .env  # Edit with your actual values
```

3. **Add your Google credentials**:
```bash
# Upload credentials.json to the VM
scp credentials.json azureuser@<vm-ip>:~/Remind_Bot/
```

4. **Deploy the application**:
```bash
# On the VM
cd ~/Remind_Bot
chmod +x deploy-azure.sh
./deploy-azure.sh
```

## Step 4: Configure Nginx (Optional)

```bash
# Copy nginx config
sudo cp nginx.conf /etc/nginx/sites-available/rasa-chatbot
sudo ln -s /etc/nginx/sites-available/rasa-chatbot /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default

# Test and restart nginx
sudo nginx -t
sudo systemctl restart nginx
```

## Step 5: Configure Telegram Webhook

Update your Telegram webhook URL:

```bash
curl -X POST "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook" \
     -H "Content-Type: application/json" \
     -d '{"url": "http://<your-vm-ip>:5006/webhooks/telegram/webhook"}'
```

## Step 6: SSL Certificate (Production)

For production, use Let's Encrypt:

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

## Monitoring and Maintenance

### Check service status:
```bash
docker-compose -f azure-compose.yml ps
```

### View logs:
```bash
docker-compose -f azure-compose.yml logs -f
```

### Update deployment:
```bash
git pull  # if using git
docker-compose -f azure-compose.yml down
docker-compose -f azure-compose.yml build
docker-compose -f azure-compose.yml up -d
```

### Backup important data:
```bash
# Backup models and logs
tar -czf backup-$(date +%Y%m%d).tar.gz models/ actions/reminder.log
```

## Troubleshooting

1. **Services not starting**: Check logs with `docker-compose logs`
2. **Telegram webhook issues**: Verify the webhook URL and bot token
3. **Google Sheets access**: Ensure credentials.json is properly mounted
4. **Port access**: Verify Azure NSG rules allow traffic on required ports

## Security Considerations

1. Use environment variables for sensitive data
2. Enable Azure Security Center
3. Configure firewall rules to restrict access
4. Regular security updates: `sudo apt update && sudo apt upgrade`
5. Use SSL certificates for production
6. Monitor logs for suspicious activity

## Cost Optimization

1. Use Azure Reserved Instances for long-term deployments
2. Consider Azure Container Instances for smaller workloads
3. Set up auto-shutdown for development environments
4. Monitor resource usage with Azure Monitor