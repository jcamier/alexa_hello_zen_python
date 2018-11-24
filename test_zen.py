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
pep_20_speach_prefix = "Hello Zen of Python PEP 20, "

reprompt = "Say Yes to ask another or no to end"

zen_number = 19
zen_number = str(zen_number)
speech_text_number = [zen for zen in pep_20_dict if zen==zen_number]
try:
    speech_text = f"{pep_20_speach_prefix} {pep_20_dict[speech_text_number[0]]}"
except (TypeError, IndexError):
    speech_text = "There are only 19 zens in Pep 20"

print(speech_text)