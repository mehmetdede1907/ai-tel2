from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.export import ConsoleSpanExporter

def setup_exporters(provider: TracerProvider) -> None:
    """Setup OTLP and Console exporters"""
    otlp_exporter = OTLPSpanExporter()
    console_exporter = ConsoleSpanExporter()
    
    provider.add_span_processor(BatchSpanProcessor(otlp_exporter))
    provider.add_span_processor(BatchSpanProcessor(console_exporter))