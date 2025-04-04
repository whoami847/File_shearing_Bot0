from typing import List, Dict

def generate_buttons(button_config: List[Dict[str, str]]):
    return [
        {"text": btn["text"], "callback_data": btn["action"]}
        for btn in button_config
    ]
