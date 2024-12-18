from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.semconv.resource import ResourceAttributes

def setup_telemetry(service_name: str, service_version: str) -> None:
    """Setup OpenTelemetry tracer provider with resource information"""
    resource = Resource.create({
        ResourceAttributes.SERVICE_NAME: service_name,
        ResourceAttributes.SERVICE_VERSION: service_version
    })
    
    provider = TracerProvider(resource=resource)
    trace.set_tracer_provider(provider)
    return provider

def get_tracer(name: str):
    """Get a tracer instance"""
    return trace.get_tracer(name)