from mcp.context.context_manager import ContextManager
from mcp.llm.gemini_client import GeminiClient


def main():
    # Initialize the MCP context manager
    context = ContextManager()

    # Add structured context
    context.add("role", "You are a helpful assistant")
    context.add(
        "task",
        "Explain what a Model Context Protocol (MCP) is and why it is useful"
    )

    # Build prompt from structured context
    prompt = context.build()

    # Initialize Gemini LLM client
    llm = GeminiClient()

    # Generate response using Gemini
    response = llm.generate(prompt)

    print("=== MCP RESPONSE ===")
    print(response)


if __name__ == "__main__":
    main()
