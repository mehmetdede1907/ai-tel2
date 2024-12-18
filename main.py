from src.telemetry import setup_telemetry, setup_exporters
from src.ai_client import AIClient
from src.data_collector import DataCollector
from src.config import Config
from opentelemetry import trace

def main():
    # Setup OpenTelemetry
    provider = setup_telemetry(Config.SERVICE_NAME, Config.SERVICE_VERSION)
    setup_exporters(provider)
    
    # Initialize clients
    ai_client = AIClient(model=Config.DEFAULT_MODEL)
    data_collector = DataCollector()
    
    # Sample prompts
    prompts = [
        "Explain what is OpenTelemetry in one sentence.",
        "Write a haiku about software monitoring.",
        "List three benefits of using OpenTelemetry."
    ]
    
    # Process prompts
    for prompt in prompts:
        print(f"\nProcessing prompt: {prompt}")
        try:
            result = ai_client.generate_response(prompt)
            
            # Save telemetry data
            filename = data_collector.save_telemetry({
                "prompt": prompt,
                **result
            })
            
            print(f"Response: {result['content']}")
            print(f"Telemetry saved to: {filename}")
            print(f"Tokens used: {result['tokens']['total']}")
            print(f"Latency: {result['latency_ms']:.2f}ms\n")
            
        except Exception as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()