import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any

class DataCollector:
    def __init__(self, output_dir: str = "telemetry_data"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
    
    def save_telemetry(self, data: Dict[str, Any]) -> str:
        """Save telemetry data to a JSON file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = self.output_dir / f"telemetry_{timestamp}.json"
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        
        return str(filename)
    
    def load_telemetry(self, filename: str) -> Dict[str, Any]:
        """Load telemetry data from a JSON file"""
        with open(filename, 'r') as f:
            return json.load(f)