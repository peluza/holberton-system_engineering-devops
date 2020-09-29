#!/usr/bin/env bash

# verification in API the status the server

# Curl command

curl -X GET "https://api.datadoghq.com/api/v1/hosts" \
-H "Content-Type: application/json" \
-H "DD-API-KEY: 3f50381bac9f879a58d9a0d3e85b942f" \
-H "DD-APPLICATION-KEY: a6135bdadbf22400fc9f1bfa28380028d83f3b3f"
