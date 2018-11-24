# -*- coding: utf-8 -*-

# This is a simple Hello World Alexa Skill, built using
# the implementation of handler classes approach in skill builder.
import logging

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response

sb = SkillBuilder()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Variables

pep_20_dict = {"1": "Beautiful is better than ugly.",
                   "2": "Explicit is better than implicit.",
                   "3": "Simple is better than complex.",
                   "4": "Beautiful is better than ugly.",
                   "5": "Complex is better than complicated.",
                   "6": "Sparse is better than dense.",
                   "7": "Readability counts.",
                   "8": "Special cases aren't special enough to break the rules.",
                   "9": "Although practicality beats purity.",
                   "10": "Errors should never pass silently.",
                   "11": "Unless explicitly silenced.",
                   "12": "In the face of ambiguity, refuse the temptation to guess.",
                   "13": "There should be one-- and preferably only one obvious way to do it.",
                   "14": "Although that way may not be obvious at first unless you're Dutch.",
                   "15": "Now is better than never.",
                   "16": "Although never is often better than right now.",
                   "17": "If the implementation is hard to explain, it's a bad idea.",
                   "18": "If the implementation is easy to explain, it may be a good idea.",
                   "19": "Namespaces are one honking great idea let's do more of those!"
                   }
pep_20_speech_prefix = "Hello Zen of Python PEP 20, "

reprompt_speech = "Say Yes to ask another or no to end"

# Classes:


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "Welcome to the Alexa Skills Kit using Python, you can say tell" \
                      " me zen followed by the zen number!"

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Hello Zen", speech_text)).set_should_end_session(
            False)
        return handler_input.response_builder.response


class HelloZenIntentHandler(AbstractRequestHandler):
    """ Python Hello Zen Alexa Text Request Handler
    Zen of Python:
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!"""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("HelloZenIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        zen_number = int(slots["zen_number"].value)
        zen_number = str(zen_number)
        speech_text_number = [zen for zen in pep_20_dict if zen == zen_number]
        reprompt = reprompt_speech
        try:
            speech_text = f"{pep_20_speech_prefix} {pep_20_dict[speech_text_number[0]]}"
        except (TypeError, IndexError):
            speech_text = "There are only 19 zens in Pep 20"
        handler_input.response_builder.speak(speech_text).ask(reprompt)
        return handler_input.response_builder.response


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "You can say hello zen to me!"

        handler_input.response_builder.speak(speech_text).ask(
            speech_text).set_card(SimpleCard(
                "Hello Zen", speech_text))
        return handler_input.response_builder.response


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("AMAZON.CancelIntent")(handler_input) or
                is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "Goodbye!"

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Hello Zen", speech_text))
        return handler_input.response_builder.response


class FallbackIntentHandler(AbstractRequestHandler):
    """AMAZON.FallbackIntent is only available in en-US locale.
    This handler will not be triggered except in that locale,
    so it is safe to deploy on any locale.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = (
            "The Hello Zen skill can't help you with that.  "
            "You can say hello zen!!")
        reprompt = "You can say hello zen!!"
        handler_input.response_builder.speak(speech_text).ask(reprompt)
        return handler_input.response_builder.response


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        return handler_input.response_builder.response


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Catch all exception handler, log exception and
    respond with custom message.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speech = "Sorry, there was some problem. Please try again!!"
        handler_input.response_builder.speak(speech).ask(speech)

        return handler_input.response_builder.response


sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelloZenIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())

sb.add_exception_handler(CatchAllExceptionHandler())

handler = sb.lambda_handler()