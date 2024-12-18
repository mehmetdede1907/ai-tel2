import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    SERVICE_NAME = os.getenv("OTEL_SERVICE_NAME", "genai-demo-service")
    SERVICE_VERSION = "0.1.0"
    
    # OpenTelemetry configuration
    OTEL_EXPORTER_OTLP_ENDPOINT = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "http://localhost:4318")
    OTEL_EXPORTER_OTLP_PROTOCOL = os.getenv("OTEL_EXPORTER_OTLP_PROTOCOL", "http/protobuf")
    CAPTURE_MESSAGE_CONTENT = os.getenv("OTEL_INSTRUMENTATION_GENAI_CAPTURE_MESSAGE_CONTENT", "true").lower() == "true"
    
    # Model configuration
    DEFAULT_MODEL = "gpt-3.5-turbo"
    DEFAULT_TEMPERATURE = 0.7