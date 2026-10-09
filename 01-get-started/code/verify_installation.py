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
