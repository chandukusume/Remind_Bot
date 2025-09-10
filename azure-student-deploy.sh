#!/bin/bash

# Azure Student Account VM Creation

echo "Creating VM for Azure Student Account..."

# Try different regions that work with student accounts
REGIONS=("eastus2" "westus2" "westeurope" "southeastasia")
VM_SIZES=("Standard_B1s" "Standard_B1ms" "Standard_DS1_v2")

for region in "${REGIONS[@]}"; do
    echo "Trying region: $region"
    
    # Create resource group
    az group create --name rasa-bot-rg --location $region
    
    for size in "${VM_SIZES[@]}"; do
        echo "Trying VM size: $size in $region"
        
        # Try to create VM
        if az vm create \
            --resource-group rasa-bot-rg \
            --name rasa-vm \
            --image Ubuntu2004 \
            --admin-username azureuser \
            --generate-ssh-keys \
            --size $size \
            --location $region; then
            
            echo "✅ VM created successfully!"
            echo "Region: $region"
            echo "Size: $size"
            
            # Open ports
            az vm open-port --port 80 --resource-group rasa-bot-rg --name rasa-vm
            az vm open-port --port 5006 --resource-group rasa-bot-rg --name rasa-vm
            
            # Get IP
            VM_IP=$(az vm show -d -g rasa-bot-rg -n rasa-vm --query publicIps -o tsv)
            echo "VM IP: $VM_IP"
            
            exit 0
        fi
    done
done

echo "❌ Failed to create VM in all regions/sizes"