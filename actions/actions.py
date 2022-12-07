# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionShowMissing(Action):

  def name(self) -> Text:
    return "action_show_missing"

  def run(self, dispatcher: CollectingDispatcher,
          tracker: Tracker,
          domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    something_missed = False
    name = tracker.get_slot("no_reaction")
    if not name:
      dispatcher.utter_message(text="You forgot to check for reaction")
      something_missed = True
    name = tracker.get_slot("no_breathing")
    if not name:
      dispatcher.utter_message(text="You forgot to check for breathing")
      something_missed = True
    name = tracker.get_slot("cpr_given")
    if not name:
      dispatcher.utter_message(text="You forgot to give cpr")
      something_missed = True
    name = tracker.get_slot("measures")
    if not name:
      dispatcher.utter_message(text="You forgot to do enhanced measures")
      something_missed = True
    name = tracker.get_slot("medication_access")
    if not name:
      dispatcher.utter_message(text="You forgot to give medication access")
      something_missed = True
    name = tracker.get_slot("ventilation")
    if not name:
      dispatcher.utter_message(text="You forgot to give enhanced ventilation")
      something_missed = True
    name = tracker.get_slot("ecg_diagnostics")
    if not name:
      dispatcher.utter_message(text="You forgot to do ecg diagnostics")
      something_missed = True
    name = tracker.get_slot("medication_administration")
    if not name:
      dispatcher.utter_message(text="You forgot to administrate medication")
      something_missed = True
    name = tracker.get_slot("shock_administration")
    if not name:
      dispatcher.utter_message(text="You forgot to administrate shock if necessary")
      something_missed = True
    name = tracker.get_slot("epinephrine")
    if not name:
      dispatcher.utter_message(text="You forgot to give 1 mg epinephrine")
      something_missed = True
    name = tracker.get_slot("defibrillation")
    if not name:
      dispatcher.utter_message(text="You forgot to place and connect the defibrillation electrodes.")
      something_missed = True
    name = tracker.get_slot("rinse")
    if not name:
      dispatcher.utter_message(text="You forgot to rinse with at least 20 mL NaCl 0.9% and elevate the extremity when administering peripherally.")
      something_missed = True
    if something_missed:
      return []
    else:
      dispatcher.utter_message(text="You have done everything correct!")
      return []

class ActionCountMissing(Action):

  def name(self) -> Text:
    return "action_count_missing"

  def run(self, dispatcher: CollectingDispatcher,
          tracker: Tracker,
          domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    counter = 0
    name = tracker.get_slot("no_reaction")
    if not name:
      counter += 1
    name = tracker.get_slot("no_breathing")
    if not name:
      counter += 1
    name = tracker.get_slot("cpr_given")
    if not name:
      counter += 1
    name = tracker.get_slot("measures")
    if not name:
      counter += 1
    name = tracker.get_slot("medication_access")
    if not name:
      counter += 1
    name = tracker.get_slot("ventilation")
    if not name:
      counter += 1
    name = tracker.get_slot("ecg_diagnostics")
    if not name:
      counter += 1
    name = tracker.get_slot("medication_administration")
    if not name:
      counter += 1
    name = tracker.get_slot("shock_administration")
    if not name:
      counter += 1
    name = tracker.get_slot("epinephrine")
    if not name:
      counter += 1
    name = tracker.get_slot("defibrillation")
    if not name:
      counter += 1
    name = tracker.get_slot("rinse")
    if not name:
      counter += 1
    if counter == 0:
      dispatcher.utter_message(text="Very good! You have done everything correct!")
      return []
    elif counter < 5:
      dispatcher.utter_message(text=f"That was already quite good. You forgot {counter} things. Would you like to see what was missing?")
    else:
      dispatcher.utter_message(text=f"You still have some work to do. You forgot {counter} things. Would you like to see what was missing?")
      return []
    