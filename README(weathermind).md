Notebook Structure

1. Setup and Imports
Installs and imports necessary libraries.
Loads environment variables and API keys.
2. Tool Definitions
Defines tools for:
Weather data retrieval
Fashion advice generation
Calendar-based outfit planning
3. Agent Definitions
Creates agent nodes using LangGraph:
WeatherToolAgent
FashionToolAgent
PlannerAgent
4. Graph Construction
Builds a multi-step agent workflow using langgraph:
Routes input through weather and fashion nodes.
Returns a final response.
5. Execution
Executes the graph with sample queries.
Demonstrates the end-to-end system output
