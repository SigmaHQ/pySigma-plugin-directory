import json
from sigma.plugins import SigmaPluginDirectory

print("• Loading file")
with open("pySigma-plugins-v1.json", "rt") as f:
    directory = f.read()

print("• Parsing JSON")
parsed = json.loads(directory)

print("• Parsing with pySigma")
plugins = SigmaPluginDirectory.from_dict(parsed)