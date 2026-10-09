# AgentCore Masterclass — Installation

> Venkata Bhattaram (c) 2026

## Contents

- Checking the Python Version
- Creating a Python Virtual Environment
- Installing Dependencies
- Installing the Amazon Bedrock AgentCore SDK
- Verifying the Installation
- Installation Checklist

## Overview

This Masterclass uses a shared Python environment for all lessons. The environment is configured once and reused throughout the tutorial.

The installation consists of:

- **Python 3.13** — the recommended Python version for this Masterclass.
- **Amazon Bedrock AgentCore SDK** — the Python SDK for integrating agents with Amazon Bedrock AgentCore.
- **Strands Agents SDK** — a framework for building AI agents and exploring agent orchestration.
- **Virtual Environment** — isolates project dependencies inside `.venv`.
- **Requirements File** — records the packages needed to reproduce the environment.

The Amazon Bedrock AgentCore SDK supports Python 3.10 and later. Python 3.13 is selected as the recommended baseline for this Masterclass.

## 1. Check the Python Version

Check the Python versions installed on your machine:

```powershell
py --list
```

Check the active Python interpreter:

```powershell
python --version
```

For this Masterclass, Python 3.13 is the recommended baseline.

If Python 3.13 is installed, select it explicitly when creating the virtual environment.

If it is not installed, install Python 3.13 before proceeding.

## 2. Create a Virtual Environment

Open PowerShell in the root directory of the repository.

Create the virtual environment:

```powershell
py -3.13 -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Upgrade pip:

```powershell
python -m pip install --upgrade pip
```

Verify the active interpreter:

```powershell
python --version
```

The terminal should display the `(.venv)` prefix when the virtual environment is active.

## 3. Install Dependencies

Create a `requirements.txt` file in the root directory of the repository.

Add the following packages:

```text
bedrock-agentcore
strands-agents
boto3
```

Install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

Verify the installed packages:

```powershell
python -m pip show bedrock-agentcore
python -m pip show strands-agents
python -m pip show boto3
```

These packages provide the foundation for exploring AgentCore integration, agent development, and AWS SDK functionality.

## 4. Install the Amazon Bedrock AgentCore SDK

The SDK can also be installed independently:

```powershell
python -m pip install bedrock-agentcore
```

Verify the installed package:

```powershell
python -m pip show bedrock-agentcore
```

Verify that Python can import the SDK:

```powershell
python -c "from bedrock_agentcore import BedrockAgentCoreApp; print('Amazon Bedrock AgentCore SDK imported successfully.')"
```

Expected output:

```text
Amazon Bedrock AgentCore SDK imported successfully.
```

Verify the Strands Agents SDK:

```powershell
python -c "from strands import Agent; print('Strands Agents SDK imported successfully.')"
```

Expected output:

```text
Strands Agents SDK imported successfully.
```

## 5. Verify the Installation

Create the following file:

Add the following code to `verify_installation.py`:

```python
import sys
from importlib.metadata import version

from bedrock_agentcore import BedrockAgentCoreApp
from strands import Agent


def main():
    print("Python version:")
    print(sys.version)

    print("\nAmazon Bedrock AgentCore SDK:")
    print(f"Version: {version('bedrock-agentcore')}")

    print("\nStrands Agents SDK:")
    print(f"Version: {version('strands-agents')}")

    print("\nAWS SDK for Python:")
    print(f"Version: {version('boto3')}")

    print("\nImport verification:")
    print("BedrockAgentCoreApp imported successfully.")
    print("Strands Agent imported successfully.")

    print("\nInstallation verified.")


if __name__ == "__main__":
    main()
```

Run the script from the repository root:

Expected output will resemble:

```text
Python version:
3.13.x ...

Amazon Bedrock AgentCore SDK:
Version: <installed-version>

Strands Agents SDK:
Version: <installed-version>

AWS SDK for Python:
Version: <installed-version>

Import verification:
BedrockAgentCoreApp imported successfully.
Strands Agent imported successfully.

Installation verified.
```

The displayed versions will depend on the packages installed in your environment.

## 6. Installation Checklist

Before proceeding to the next lesson, verify the following:

```text
[ ] Python 3.13 installed
[ ] Virtual environment created
[ ] Virtual environment activated
[ ] pip upgraded
[ ] requirements.txt created
[ ] Amazon Bedrock AgentCore SDK installed
[ ] Strands Agents SDK installed
[ ] Boto3 installed
[ ] SDK imports verified
[ ] verify_installation.py executed successfully
```

## Conclusion

The installation process for this Masterclass is:

```text
Python 3.13
     ↓
Virtual Environment
     ↓
Dependency Configuration
     ↓
Amazon Bedrock AgentCore SDK
     ↓
Strands Agents SDK + Boto3
     ↓
Installation Verification
```

The core installation is complete when `verify_installation.py` prints:

```text
Installation verified.
```

**Important:** Installing the SDK does not require you to configure AWS credentials immediately. However, AWS credentials, suitable IAM permissions, and access to the relevant AWS services will be needed when you start using AWS-hosted features or deploying agents. API credentials for other model providers may also be required, depending on the lessons and models you choose.