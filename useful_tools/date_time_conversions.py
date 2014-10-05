import datetime
import time

class DateTimeTricks:
    #create a random phone number using datetime
    def random_phone_number(self):
        phone = datetime.datetime.now().strftime("%M%S%f")
        if (phone[0] == '0') or (phone[0] == '1'):
            s = list(phone)
            s[0] = '2'
            phone = "".join(s)
        return phone
    
    #to get the date of the future just pass the number of days ahead you would like
    def future_date(self, num_of_days):
        future_day = datetime.date.today() + datetime.timedelta(days=num_of_days)
        return future_day 
    
    #same as above except it will give you the accurate date in the past
    def days_ago(self, num_of_days):
        past_day = datetime.date.today() - datetime.timedelta(days=num_of_days)
        return past_day