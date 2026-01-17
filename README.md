# LoreGeneration

**LoreGeneration** is a procedural world and history generator written in Python.  
The goal is to simulate cultures, religions, characters, and factions over long spans of time and generate emergent lore from their interactions.

---

## Core Concept

The engine models a living world using interacting systems rather than scripted events.  
Each entity has internal pressures that build over time, eventually producing wars, schisms, collapses, and golden ages.

---

## Simulation Systems

The world is driven by several layered systems:

- **Cultures** : Behavioral traits that shape how societies act  
- **Religions** : Tolerance, zeal, and tendency to fracture  
- **Factions** : Stability, war pressure, wealth, and unrest  
- **Characters** : Ambition, stress, legitimacy, and influence  

Each simulated year, these values shift based on traits, relationships, and past events.

When pressures cross thresholds, major historical events are triggered:
- Wars  
- Religious schisms  
- Rebellions  
- State collapse  
