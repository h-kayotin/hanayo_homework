"""
自定义__format__ - 

Author: kayotin
Date 2024/2/4
"""


class Verb:
    def __init__(self, present, past):
        self.present = present
        self.past = past

    def __format__(self, format_spec):
        if format_spec == 'past':
            return self.past
        else:
            return self.present


go = Verb('go', 'gone')
content = 'You can {0:present} where you have {0:past}.'
print(content.format(go))
# You can go where you have gone.
