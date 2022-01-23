import json

with open('settings.json') as f:
  settings = json.load(f)

settings['foodWeight'] = 100;

print(settings['foodWeight'])

with open('settings.json', 'w') as f:
  json.dump(settings, f, indent=2)