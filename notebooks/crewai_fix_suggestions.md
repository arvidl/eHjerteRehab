# Løsninger for CrewAI Rekursjonsproblemer

## Problem
Du opplevde "maximum recursion depth exceeded" når du kjørte CrewAI-eksempelet.

## Mulige Årsaker og Løsninger

### 1. **Agent-konfigurasjon**
```python
# PROBLEM: For komplekse agents
agent = Agent(
    role='Sehr complex role...',
    goal='Very detailed goal...',
    backstory='Extremely long backstory...'
)

# LØSNING: Forenklet agents
agent = Agent(
    role='Data Analyst',
    goal='Identify 3 key insights',
    backstory='You are an experienced analyst.',
    max_iter=3,           # Begrens iterasjoner
    memory=False,         # Deaktiver minne
    allow_delegation=False
)
```

### 2. **Task-beskrivelser**
```python
# PROBLEM: For detaljerte beskrivelser kan skape loops
task = Task(
    description="Very long and complex description with multiple sub-tasks...",
    expected_output="Complex multi-part output..."
)

# LØSNING: Kortere, spesifikke beskrivelser
task = Task(
    description="Analyze patient profile. List 3 insights.",
    expected_output="Numbered list with 3 concrete insights.",
    agent=agent
)
```

### 3. **Versjonsproblemer**
```bash
# Sjekk versjon
pip show crewai

# Hvis problemer, prøv nedgradering
pip install crewai==0.100.0
```

### 4. **Miljøvariabler**
```python
import os
# Sørg for at OPENAI_API_KEY er satt
if not os.getenv("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = "your-key-here"
```

### 5. **Alternative tilnærminger**
- Bruk enkeltstående agents uten Crew
- Implementer egen logikk som vist i `direct_analysis.py`
- Bruk LangChain direkte i stedet for CrewAI

## Anbefalt Feilsøkingsrekkefølge

1. **Start enkelt**: Én agent, én task
2. **Begrens iterasjoner**: `max_iter=3`
3. **Deaktiver minne**: `memory=False`
4. **Forenkle beskrivelser**: Kortere tekster
5. **Sjekk API-tilgang**: Verifiser OPENAI_API_KEY
6. **Bruk fallback**: Direkte Python-løsning som backup

## Eksempel på Fungerende Minimal Konfigurasjon

```python
from crewai import Agent, Task, Crew, Process

# Minimal agent
agent = Agent(
    role='Analyst',
    goal='Provide 3 insights',
    backstory='You analyze data.',
    max_iter=2,
    memory=False,
    allow_delegation=False
)

# Minimal task
task = Task(
    description="Analyze: [data]. Give 3 insights.",
    expected_output="1. Insight one\n2. Insight two\n3. Insight three",
    agent=agent
)

# Minimal crew
crew = Crew(
    agents=[agent],
    tasks=[task],
    process=Process.sequential,
    verbose=False  # Reduserer kompleksitet
)

# Kjør med error handling
try:
    result = crew.kickoff()
    print(result)
except Exception as e:
    print(f"Error: {e}")
    # Fallback til direkte løsning
``` 