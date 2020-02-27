from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions .action import Action
from rasa_core.events import SlotSet

class ActionWeather(Action):
    def name(self):
        return 'action_weather'

    def run(self, dispatcher, tracker, domain):
        # from apixu.client import ApixuClient
        # api_key = ""
        # client = ApixuClient(api_key)

        loc = tracker.get_slot('location')
        # current = client.getCurrentWeather(q=loc)

        dispatcher.utter_message("The Input is :"+str(loc))
        return [SlotSet('location', loc)]