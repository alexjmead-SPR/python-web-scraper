#!/bin/bash

az account set --subscription 'SPR Internal Projects – CSP'
# az group list

# echo ""
# echo ""
# echo ""

export RES_GROUP="BuiltInChicagoProject"
export ACCT_NAME="builtin-chicago"

export ACCOUNT_URI=$(az cosmosdb show --resource-group $RES_GROUP --name $ACCT_NAME --query documentEndpoint --output tsv)

export ACCOUNT_KEY=$(az cosmosdb keys list --resource-group $RES_GROUP --name $ACCT_NAME --query primaryMasterKey --output tsv)

# echo $ACCOUNT_URI
# echo $ACCOUNT_KEY