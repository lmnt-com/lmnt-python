# Hackathon Template

We’re excited to see you using LMNT during the hackathon! To make your experience seamless, we have created this quick onboarding template.

This template includes a simple agent that uses LMNT to synthesize audio. If whisper audio transcription and an llm are configured, the agent does the following:

1. Accepts as input an audio file or a text prompt
2. Whisper transcribes the audio file to extract text from the spoken input
3. The transcribed text prompt is sent to the LLM and the text response is streamed back
4. The text is streamed to LMNT and the synthesized audio is streamed back

You can change the configuration/input to skip certain steps. For example, you can pass text straight to LMNT by disabling whisper and the llm.

## Installation

To get started, follow these steps:

1. Ensure you're using Python 3.6 or higher, but less than 3.12.

2. Set up your api keys as environment variables. You can get your api keys from the [LMNT website](https://app.lmnt.com/account).

    ```bash
    export LMNT_API_KEY=<your_api_key>
    ```

    If you are using Mistral, set up your Mistral api key as well.

    ```bash
    export MISTRAL_API_KEY=<your_mistral_api_key>
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Basic Usage**

After installing the dependencies, you can run the script.

    ```bash
    python scripts/lmnt_agent.py --config config/config.yaml
    ```

Checkout our [documentation](https://docs.lmnt.com/introduction) for exploring more of our model's capabilities.

## Contributing

We welcome contributions! If you have any ideas, bug fixes, or improvements, please submit a pull request.

Happy hacking!
