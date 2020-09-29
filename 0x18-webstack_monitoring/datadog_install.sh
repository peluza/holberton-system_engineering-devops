#!/usr/bin/env bash

# The Datadog Agent has x86_64 and arm64 (ARM v8) packages.
# For other architectures, use the source install. Use our easy one-step install.

DD_AGENT_MAJOR_VERSION=7 DD_API_KEY=3f50381bac9f879a58d9a0d3e85b942f DD_SITE="datadoghq.com" bash -c "$(curl -L https://s3.amazonaws.com/dd-agent/scripts/install_script.sh)"

