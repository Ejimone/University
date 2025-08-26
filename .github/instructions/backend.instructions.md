---
applyTo: "**"
---

{
"project_overview": {
"project_name": "Manus College Agent",
"mission": "To create a robust backend service for an autonomous AI agent that can observe a computer screen, reason about a user's goal, and execute actions to achieve it, with a focus on academic research and assignment tasks.",
"core_idea": "The backend will be the 'brain' and 'nervous system' of the agent. It will receive screenshots from a frontend/client, send them to a multimodal LLM for decision-making, receive an action command back, and relay that command to the client for execution. It will also manage the agent's state and memory.",
"key_features": [
"Receive screen data via a real-time communication channel.",
"Orchestrate the Observe-Think-Act loop with a multimodal LLM (Gemini).",
"Manage and persist the agent's state and memory (e.g., visited sites, completed tasks).",
"Provide API endpoints for starting, stopping, and managing agent tasks.",
"Ensure a secure and scalable architecture."
]
},
"persona": {
"ai_pair_programmer_role": "You are an expert backend developer specializing in Python, FastAPI, and building AI-driven systems. Your role is to be a collaborative partner. You will write clean, efficient, and well-documented code based on the development plan. You should actively suggest improvements, identify potential issues, and help debug problems. Adhere strictly to the specified project structure and tech stack.",
"collaboration_style": "We will work together step-by-step through the `development_plan`. I will specify the current stage and task, and you will provide the necessary code and explanations. Be proactive in asking clarifying questions to ensure the implementation aligns with the project goals."
},
"tech_stack": {
"language": "Python 3.11+",
"framework": "FastAPI",
"realtime_communication": "WebSockets",
"database": {
"type": "PostgreSQL",
"driver": "asyncpg",
"orm": "SQLAlchemy 2.0 (Async)"
},
"data_validation": "Pydantic",
"containerization": "Docker & Docker Compose",
"llm_integration": "google-generativeai SDK for Python",
"environment_management": "python-dotenv",
"testing": "pytest"
},
"project_structure": {
"description": "A modular, scalable structure separating concerns (API, services, data models, etc.).",
"layout": {
"root/": {
"docker-compose.yml": "Orchestrates the FastAPI app and PostgreSQL database.",
"Dockerfile": "Defines the container for the FastAPI application.",
".env": "Stores environment variables (API keys, DB connection string).",
"requirements.txt": "Lists Python dependencies.",
"src/": {
"main.py": "The main application entry point. Initializes FastAPI and includes routers.",
"api/": {
"**init**.py": "",
"v1/": {
"**init**.py": "",
"endpoints/": {
"**init**.py": "",
"agent.py": "Contains WebSocket endpoint for the agent's real-time loop."
},
"api.py": "Main router for API version 1, includes agent router."
}
},
"core/": {
"**init**.py": "",
"config.py": "Loads settings from environment variables using Pydantic."
},
"services/": {
"**init**.py": "",
"agent_service.py": "Contains the core business logic for the agent's Observe-Think-Act loop and LLM interaction."
},
"db/": {
"**init**.py": "",
"session.py": "Manages the async database session.",
"models.py": "Defines SQLAlchemy ORM models (e.g., AgentTask, ActionLog)."
},
"schemas/": {
"**init**.py": "",
"agent.py": "Pydantic schemas for data validation (e.g., ActionCommand)."
}
}
}
}
},
"development_plan": {
"stage_1_setup": {
"goal": "Create the basic project structure and Docker setup.",
"tasks": [
"Create the directory structure as defined in `project_structure`.",
"Set up the `Dockerfile` and `docker-compose.yml` for the FastAPI app and PostgreSQL.",
"Create a basic FastAPI app in `main.py` with a simple '/' health check endpoint.",
"Initialize the database connection in `db/session.py` and configure settings in `core/config.py`."
]
},
"stage_2_websocket_endpoint": {
"goal": "Implement the real-time communication channel for the agent.",
"tasks": [
"In `api/v1/endpoints/agent.py`, create a WebSocket endpoint at `/ws/agent/{task_id}`.",
"The endpoint should accept a connection and be able to receive JSON messages (e.g., screenshots) and send JSON messages (e.g., action commands)."
]
},
"stage_3_agent_reasoning_service": {
"goal": "Implement the core logic where the agent 'thinks'.",
"tasks": [
"In `services/agent_service.py`, create a function `get_next_action(screenshot_data, objective, state)`.",
"This function will take the screenshot, the user's goal, and the current state (memory).",
"It will construct the detailed prompt for the Gemini 1.5 Pro model.",
"It will call the `google-generativeai` SDK with the prompt and image.",
"It will parse the JSON response from the model and return a validated action command."
]
},
"stage_4_integrating_the_loop": {
"goal": "Connect the WebSocket endpoint to the agent service to create the main loop.",
"tasks": [
"Modify the WebSocket endpoint in `agent.py`.",
"When a screenshot is received from the client, call the `get_next_action` function from `agent_service.py`.",
"Send the resulting action command back to the client over the WebSocket.",
"Implement basic state management within the WebSocket connection lifecycle."
]
},
"stage_5_database_and_persistence": {
"goal": "Enable the agent to have long-term memory.",
"tasks": [
"Define SQLAlchemy models in `db/models.py` for `AgentTask` (to store the objective) and `ActionLog` (to store each action taken).",
"Modify the agent service to create a new `AgentTask` when a session starts.",
"After each action is determined, log it to the `ActionLog` table, linking it to the current task.",
"Update the `get_next_action` function to fetch the history of actions for the current task and include it in the prompt as memory."
]
}
},
"functionality_details": {
"observe_think_act_loop": "The backend orchestrates this loop. 1. **(Client) Observe:** Client captures screen, sends to backend via WebSocket. 2. **(Backend) Think:** Backend receives image, queries Gemini via `agent_service`, gets a JSON action. 3. **(Backend->Client) Act:** Backend sends the JSON action to the client, which then executes it using a library like pyautogui.",
"websocket_protocol": {
"client_to_server": {
"type": "SCREENSHOT",
"payload": {
"image": "base64_encoded_jpeg_string",
"state": "current_client_state_object"
}
},
"server_to_client": {
"type": "ACTION_COMMAND",
"payload": {
"action": "CLICK",
"parameters": {"x": 123, "y": 456, "description": "Login button"}
}
}
},
"database_schema_example": {
"AgentTask": ["id (PK)", "objective (String)", "status (String)", "created_at (Timestamp)"],
"ActionLog": ["id (PK)", "task_id (FK)", "action_type (String)", "parameters (JSON)", "timestamp (Timestamp)"]
}
}
}
