import time
from datetime import datetime, timedelta, date
import pywhatkit as kit
from ClockTime import ClockTime



class Message:
    def __init__(self, text: str, clocktime: ClockTime = ClockTime(), date: date = date.today()) -> None:
        self.text = text
        self.clocktime = clocktime
        self.date = date



class TimedMessagesBot:
    def __init__(self, receiver_phone: str, messages: list[Message] = []) -> None:
        self.receiver_phone = receiver_phone
        self.messages = messages
        self.next_message = Message('')  # most recent message

    @staticmethod
    def send_message(receiver_phone:str, message:Message):
        kit.sendwhatmsg(receiver_phone,
                        message.text,
                        message.clocktime.hour,
                        message.clocktime.minute+1, 15, True)

    def add_message(self, message: Message):
        self.messages.append(message)

    def calculate_waittime(self):
        '''Calculates the sleep duration in seconds until the next message.'''
        return (self.get_sendtime() - datetime.now()).total_seconds()


    # will run 24/7
    def run(self):
        if not len(self.messages):
            raise ValueError('There is no messages to send !')
        
        # sort messages
        self.messages.sort(key=lambda msg: msg.clocktime.to_seconds())
        
        # start
        while True:
            try:
                # Sleep until time to send the next message
                time.sleep(self.calculate_waittime())
                # Send the message
                TimedMessagesBot.send_message(self.receiver_phone, self.next_message)
            except Exception as e:
                print(f'Error occurred: {e}')
                time.sleep(60) # Wait a minute before retrying


    # get most recent message to send
    def get_sendtime(self):
        '''Get the most recent time to send a message (and caches that message).'''
        # After all times for today, send the first message tomorrow
        if datetime.now() > self.messages[-1].clocktime.to_datetime():
            self.next_message = self.messages[0] # first message
            return self.messages[0].clocktime.to_datetime() + timedelta(days=1)

        # Get the next message time in the future
        for message in self.messages:
            if datetime.now() < message.clocktime.to_datetime():
                self.next_message = message
                break
            
        print(f'Will send message `{self.next_message.text}` at {self.next_message.clocktime.to_datetime()}')
        return self.next_message.clocktime.to_datetime()
    

if __name__ == '__main__':
    bot = TimedMessagesBot('+1234567890')
    bot.add_message(Message('TAKE YOUR *IRON* AND *OMEGA 3*', ClockTime(9)))
    bot.add_message(Message('TAKE YOUR *IRON* AND *OMEGA 3*', ClockTime(14)))
    bot.run()
