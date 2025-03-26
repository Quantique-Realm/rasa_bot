from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# Define building locations (Replace with exact coordinates)
CAMPUS_LOCATIONS = {
    "main gate": "22.5297,75.9140",
    "academic block": "22.5289,75.9242",
    "hostel": "22.5322,75.9242",
    "library": "22.5290,75.9220",
    "sports complex": "22.5297,75.9194"
}

class ActionShowMap(Action):
    def name(self) -> Text:
        return "action_show_map"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        place = tracker.get_slot("place_name")

        if place and place.lower() in CAMPUS_LOCATIONS:
            lat, lon = CAMPUS_LOCATIONS[place.lower()].split(',')
            map_url = f"https://www.openstreetmap.org/?mlat={lat}&mlon={lon}#map=18/{lat}/{lon}"

            # Option 1: Send the link as plain text (Simple & Effective)
            dispatcher.utter_message(text=f"Here is the location of {place}: {map_url}")

            # Option 2: Send as a clickable button (If UI supports it)
            dispatcher.utter_message(
                text="Click the button below to view the location:",
                buttons=[{"title": f"Open {place} on Map", "payload": map_url}]
            )

        else:
            dispatcher.utter_message(text="Sorry, I couldn't find that place. Please try again.")

        return []
