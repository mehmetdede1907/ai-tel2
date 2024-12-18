from datetime import datetime
from typing import Dict, Any
from openai import OpenAI
from opentelemetry import trace
from opentelemetry.trace import Status, StatusCode

class AIClient:
    def __init__(self, model: str = "gpt-3.5-turbo"):
        self.client = OpenAI()
        self.model = model
        self.tracer = trace.get_tracer(__name__)
    
    def generate_response(self, prompt: str) -> Dict[str, Any]:
        """Generate response with OpenAI and collect telemetry"""
        with self.tracer.start_as_current_span("ai_generation") as span:
            try:
                span.set_attribute("prompt.length", len(prompt))
                span.set_attribute("model", self.model)
                
                start_time = datetime.now()
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7
                )
                end_time = datetime.now()
                
                # Record metrics
                metrics = {
                    "tokens": {
                        "total": response.usage.total_tokens,
                        "completion": response.usage.completion_tokens,
                        "prompt": response.usage.prompt_tokens
                    },
                    "latency_ms": (end_time - start_time).total_seconds() * 1000,
                    "content": response.choices[0].message.content
                }
                
                # Set span attributes for monitoring
                for key, value in metrics["tokens"].items():
                    span.set_attribute(f"tokens.{key}", value)
                span.set_attribute("latency_ms", metrics["latency_ms"])
                
                span.set_status(Status(StatusCode.OK))
                return metrics
                
            except Exception as e:
                span.set_status(Status(StatusCode.ERROR, str(e)))
                raise