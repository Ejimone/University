import os
import json
import time
import base64
import io

import mss
import pyautogui
from PIL import Image
import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv()


# --- Configuration ---
# Configure the Gemini API key
def check_api_key():
    """Check if the API key is properly configured"""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("❌ ERROR: GEMINI_API_KEY environment variable not set!")
        print("Please set your API key with: export GEMINI_API_KEY='your_api_key_here'")
        return False
    if len(api_key) < 20:  # Basic sanity check
        print("❌ ERROR: GEMINI_API_KEY appears to be invalid (too short)")
        return False
    print(f"✅ API key found (length: {len(api_key)})")
    return True

# Check API key before configuring
if not check_api_key():
    exit(1)

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# The user's high-level goal for the agent
# The user's high-level goal for the agent
USER_GOAL = "My goal is to check for any new assignments in the 'Design and Analysis of Algms' course. https://classroom.google.com/"

# --- The Agent's "Body and Mind" ---

def take_screenshot():
    """
    The "Eyes" of the agent. Captures the screen and returns it in a format the model can understand.
    """
    print("👀 Taking screenshot...")
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # The primary monitor
        sct_img = sct.grab(monitor)
        
        # Convert to PIL Image
        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        
        # Convert to bytes
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='JPEG')
        
        return {
            'mime_type': 'image/jpeg',
            'data': base64.b64encode(img_byte_arr.getvalue()).decode()
        }

def get_agent_action(screenshot, objective, history):
    """
    The "Brain" of the agent. It sends the current view (screenshot), the objective,
    and the history of previous actions to the Gemini model and asks for the next action.
    """
    print("🧠 Thinking about the next action...")

    # This is the core prompt that guides the agent
    prompt = f"""
    You are an autonomous AI agent controlling a computer. Your high-level objective is: '{objective}'.

    You have already taken the following actions:
    {history}

    Based on the provided screenshot and your past actions, what is the single next action you should take to move towards your objective?
    If you are stuck in a loop, try a different action. For example, if you are clicking the same button repeatedly, try scrolling or typing something different.

    Your available actions are:
    - TYPE(text_to_type): Types a given string.
    - CLICK(x, y, description): Clicks on a specific coordinate on the screen. Provide a brief description of what you are clicking on.
    - SCROLL(direction, description): Scrolls the page up or down. The direction can be 'up' or 'down'.
    - FINISH(final_answer): Use this action when you have successfully completed the objective. The final_answer should be the information you were asked to find.

    Analyze the screenshot and your history, then respond ONLY with a single, valid JSON object representing your next action.
    Do not include any other text or explanations.


    in google classroom, you'll see the list of clases enrolled in, for example  CSE, 5CSE A, Web Techologies etc. You can click on any of the classes to see the classwork and assignments given.

    Example response for typing:
    {{"action": "TYPE", "parameters": {{"text_to_type": "latest news about ISRO"}}}}

    Example response for clicking:
    {{"action": "CLICK", "parameters": {{"x": 500, "y": 350, "description": "Google search bar"}}}}

    Example response for scrolling:
    {{"action": "SCROLL", "parameters": {{"direction": "down", "description": "scrolling to see more news articles"}}}}

    Example response when finished:
    {{"action": "FINISH", "parameters": {{"final_answer": "Chandrayaan-4 mission approved by government."}}}}
    """

    # Create the proper image content format for Gemini API
    image_content = {
        "mime_type": screenshot["mime_type"],
        "data": screenshot["data"]
    }

    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content([prompt, image_content])

        # Clean up the model's response to extract only the JSON
        clean_response = response.text.strip().replace("```json", "").replace("```", "").strip()
        return json.loads(clean_response)
    except (json.JSONDecodeError, AttributeError) as e:
        print(f"Error decoding model response: {e}")
        print(f"Raw response: {response.text if hasattr(response, 'text') else 'No response text'}")
        return None
    except Exception as e:
        print(f"API Error: {e}")
        print("This might be due to:")
        print("1. Invalid API key - check your GEMINI_API_KEY environment variable")
        print("2. API quota exceeded")
        print("3. Invalid image format")
        return None

def execute_action(action_command):
    """
    The "Hands" of the agent. It takes the JSON command from the "Brain"
    and uses pyautogui to execute it.
    """
    if not action_command:
        print("No action to execute.")
        return True # Continue the loop

    action_type = action_command.get("action")
    params = action_command.get("parameters")
    
    print(f"Executing action: {action_type} with parameters: {params}")

    if action_type == "TYPE":
        text_to_type = params.get("text_to_type", "")
        pyautogui.write(text_to_type, interval=0.05)
        pyautogui.press('enter')
        
    elif action_type == "CLICK":
        x = params.get("x")
        y = params.get("y")
        pyautogui.click(x=x, y=y)

    elif action_type == "SCROLL":
        direction = params.get("direction")
        if direction == "up":
            pyautogui.scroll(1000)
        else:
            pyautogui.scroll(-1000)
        
    elif action_type == "FINISH":
        final_answer = params.get("final_answer", "")
        print(f"✅ GOAL ACHIEVED! Final Answer: {final_answer}")
        return False # End the loop
        
    else:
        print(f"Unknown action type: {action_type}")

    return True # Continue the loop

# --- Main Agent Loop ---
if __name__ == "__main__":
    
    # Add a delay before starting to give you time to switch windows
    print("Agent starting in 5 seconds... Switch to the window you want it to control.")
    time.sleep(5)

    is_running = True
    action_history = []
    while is_running:
        # 1. Observe
        screenshot_data = take_screenshot()
        
        # 2. Think
        action = get_agent_action(screenshot_data, USER_GOAL, action_history)
        
        # 3. Act
        is_running = execute_action(action)
        
        # Add the action to the history
        action_history.append(action)
        
        # Wait a moment for the screen to update after the action
        time.sleep(2)