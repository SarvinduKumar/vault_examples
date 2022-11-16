# Vault + Informatica Examples

This project is a collection of scripts that demonstrate various ways that informatica can integration with HCV and utilize secrets with connections

## update_infa_from_vault.py

### Prequisties
* Install hvac, requests to your python environment 
* Four environment variables need to be set:
    * Vault URL: URL of your Vault including port
    * Login URL: The informatica login URL for your ORG
    * Vault Token: Access Token to the Vault
    * Vault Namespace: The namespace in which the account should operate

### Usage
1. Deploy this script to every secure agent in the group.
2. Execute the script as a Pre-Processing Command.


## Disclaimer
This sample source code is offered only as an example of what can or might be built using the IICS Github APIs, and is provided for educational purposes only. This source code is provided "as-is"  and without representations or warrantees of any kind, is not supported by Informatica. Users of this sample code in whole or in part or any extraction or derivative of it assume all the risks attendant thereto, and Informatica disclaims any/all liabilities arising from any such use to the fullest extent permitted by law.