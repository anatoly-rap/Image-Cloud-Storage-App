#!/bin/bash

while true; do
    usb_device=$(lsblk -o NAME,SIZE,TYPE -d | grep -e "sd[b-z][[:digit:]]\s*disk" | awk '{print $1}')
    if [[ -n $usb_device ]]; then
        echo "USB stick inserted: /dev/$usb_device"
        mount_point=$(mktemp -d)
        mount /dev/$usb_device $mount_point
        if [[ -f "$mount_point/config.yaml" ]]; then
            echo "Found config file: $mount_point/config.yaml"
            STORAGE_ACCOUNT_KEY=$(cat $mount_point/config.yaml | yq -r .azure.storage_account_key)
            STORAGE_ACCOUNT_NAME=$(cat $mount_point/config.yaml | yq -r .azure.storage_account_name)
            CON_STR=$(cat $mount_point/config.yaml | yq -r .azure.connection_string)
            echo "Storage account key: $STORAGE_ACCOUNT_KEY"
            echo "Storage account name: $STORAGE_ACCOUNT_NAME"
            echo "Connection string: $CON_STR"
            python image_uploader.py --storage-account-key "$STORAGE_ACCOUNT_KEY" --storage-account-name "$STORAGE_ACCOUNT_NAME" --connection-string "$CON_STR" --local-path "$LOCAL_PATH"
        else
            echo "Config file not found on USB stick."
        fi
        umount $mount_point
        rm -rf $mount_point
    fi
    sleep 1
done

