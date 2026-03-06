"""
Groq model registry with automatic fallback.

Models are tried in order. If a model is unavailable or rate-limited,
the next one is attempted. Gemini is used as the final fallback in app.py.

Model list: https://console.groq.com/docs/models
"""

# Ordered list: best/fastest first, then fallbacks
GROQ_MODELS = [
    "llama-3.3-70b-versatile",       # Primary: Llama 3.3 70B (128k ctx)
    "deepseek-r1-distill-llama-70b", # Fallback 1: DeepSeek R1 distilled
    "llama-3.1-70b-versatile",       # Fallback 2: Llama 3.1 70B
    "mixtral-8x7b-32768",            # Fallback 3: Mixtral 8x7B (32k ctx)
    "llama3-70b-8192",               # Fallback 4: Llama 3 70B (8k ctx)
    "gemma2-9b-it",                  # Fallback 5: Gemma 2 9B (fastest, lightest)
]


def get_groq_stream(client, messages, max_tokens=1024, temperature=0.7):
    """
    Try each Groq model in order and return (stream, model_name) for the
    first one that succeeds.

    Raises the last exception if all models fail.
    """
    last_error = None

    for model in GROQ_MODELS:
        try:
            stream = client.chat.completions.create(
                model=model,
                messages=messages,
                stream=True,
                max_tokens=max_tokens,
                temperature=temperature,
            )
            print(f"[Groq] Using model: {model}")
            return stream, model

        except Exception as e:
            print(f"[Groq] Model '{model}' failed: {e}")
            last_error = e

    raise last_error or RuntimeError("All Groq models exhausted")
