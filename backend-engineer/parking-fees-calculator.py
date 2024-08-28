'''
Requirements : 
Develop a function that computes and returns the parking charges for a given vehicle parking duration based on the following rate structure:

+--------------------------------------------------------------------------------------------------------------------+
| Day of week            | Tariff                                                     | Maximum Daily Charge         |
+------------------------+------------------------------------------------------------+------------------------------+
| Weekdays               | First 3 Hours: MYR 3.00 per hour                           | MYR 20.00                    |
|                        | Each Additional Hour: MYR 1.50 per hour                    |                              |
+------------------------+------------------------------------------------------------+------------------------------+
| Weekends               | First 3 Hours: MYR 5.00 per hour                           | MYR 30.00                    |
|                        | Each Additional Hour: MYR 2.00 per hour                    |                              |
+--------------------------------------------------------------------------------------------------------------------+
| Additional Conditions                                                                                              |
| 1. No charge for exits within 15 minutes of entry.                                                                 |
| 2. A 5-minute grace period is applied to the payment time.                                                         |
+--------------------------------------------------------------------------------------------------------------------+


Expected Output:

Scenarios 1 : Vehicle exit within 15 minutes
+------------------------------------+
| Enter : 2023-10-25 08:16           |
| Exit  : 2023-10-25 08:27           |
|                                    |
| Total Duration : 11 minutes        |
| Amount to paid : MYR 0.00          |
+------------------------------------+

Scenarios 2 : Vehicle exit after 15 minutes and within grace period minutes on weekday
+------------------------------------+
| Enter : 2023-01-25 08:16           |
| Exit  : 2023-01-25 12:19           |
|                                    |
| Total Duration : 4 hours 3 minutes |
| Amount to paid : MYR 4.50          |
+------------------------------------+


Notes/Hints:
 * Do consider that this function might be utilized across various car parks in multiple states within Malaysia.
 * Harcoded Logic are not allowed.
 * You may create as much as function or classes as you need.

'''


def getParkingTariff():
  '''
  this function simulates querying a tariff dataset required for fee calculation and 
  returns a JSON dictionary or a list of objects containing the tariff data.
  '''
  return {}


def calculateParkingFees(datetime_enter, datetime_exit):
  return {
    "parking_duration" : "0 hours 0 minutes",
    "parking_fees" : 0.00
  }





