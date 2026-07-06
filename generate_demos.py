#!/usr/bin/env python3
"""
Script to generate 20 hotel demos from the casa-ellul.html template.
Run from ~/Desktop/demos-repo/
"""

import os

# Read template
with open('casa-ellul.html', 'r') as f:
    template = f.read()

# Hotels list: (slug, name, location, stars)
hotels = [
    ("xara-palace", "Xara Palace", "Mdina, Malta", "★★★★★"),
    ("thirty-three", "Thirty Three Boutique Hotel", "Sliema, Malta", "★★★★"),
    ("giorgio", "Giorgio Boutique Hotel", "Malta", "★★★★"),
    ("lure-hotel", "Lure Hotel", "Malta", "★★★★"),
    ("tao-domus", "Tao Domus", "Taormina, Italy", "★★★★"),
    ("villa-schuler", "Villa Schuler", "Taormina, Italy", "★★★★"),
    ("villa-fiorita", "Villa Fiorita", "Taormina, Italy", "★★★★"),
    ("villa-carlotta", "Villa Carlotta", "Sicily, Italy", "★★★★"),
    ("gut-hotel", "GUT Hotel", "Italy", "★★★★"),
    ("palazzo-marletta", "Palazzo Marletta", "Catania, Sicily", "★★★★★"),
    ("palazzo-natoli", "Palazzo Natoli", "Sicily, Italy", "★★★★"),
    ("casa-nostra", "Casa Nostra", "Palermo, Sicily", "★★★★"),
    ("kalura", "Hotel Kalura", "Cefalù, Sicily", "★★★★"),
    ("le-calette", "Le Calette", "Cefalù, Sicily", "★★★★★"),
    ("principe-salina", "Principe di Salina", "Salina, Aeolian Islands", "★★★★"),
    ("villa-las-tronas", "Villa Las Tronas", "Alghero, Sardinia", "★★★★★"),
    ("villa-mosca", "Villa Mosca", "Sardinia, Italy", "★★★★"),
    ("sandalia", "Sandalia Boutique Hotel", "Sardinia, Italy", "★★★★"),
    ("faro-spartivento", "Faro Capo Spartivento", "Sardinia, Italy", "★★★★★"),
    ("palazzo-abati", "Palazzo degli Abati", "Matera, Italy", "★★★★"),
]

for slug, name, location, stars in hotels:
    html = template
    
    # Replace title
    html = html.replace('<title>AI Concierge - Casa Ellul</title>', f'<title>AI Concierge - {name}</title>')
    
    # Replace hotel name in header
    html = html.replace('CASA ELLUL', name.upper())
    html = html.replace('Casa Ellul', name)
    
    # Replace stars
    html = html.replace('★★★★★', stars)
    
    # Replace subtitle/location
    html = html.replace('VALLETTA, MALTA', location.upper())
    html = html.replace('Valletta, Malta', location)
    
    # Write file
    filepath = f'{slug}.html'
    with open(filepath, 'w') as f:
        f.write(html)
    print(f"✓ Created {filepath}")

print(f"\n✅ {len(hotels)} demos created!")
print("\nNow run:")
print("  git add -A")
print("  git commit -m 'feat: add 20 hotel demos'")
print("  git push")
