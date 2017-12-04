import unittest, time
from pooltable import *

class TestPoolTable(unittest.TestCase):

    def setUp(self):
        pooltable[0] = PoolTable()

    def test_creates_pooltable_array(self):
        self.assertNotEqual(pooltable,None)

    def test_array_length_is_twelve_as_expected(self):
        self.assertEqual(len(pooltable),12)

    def test_initial_status_unoccupied(self):
        self.assertEqual(pooltable[0].occupied,"NOT OCCUPIED")

    def test_table_can_be_given_when_unoccupied(self):
        pooltable[0].giveOut()
        self.assertEqual(pooltable[0].occupied,"OCCUPIED")

    def test_table_can_not_be_given_when_occupied(self):
        pooltable[0].giveOut()
        self.assertEqual(pooltable[0].occupied,"OCCUPIED")
        self.occupied_refusal = pooltable[0].giveOut()
        self.assertTrue(self.occupied_refusal.endswith("is currently occupied."))

    def test_start_time_recorded_when_table_opened(self):
        pooltable[0].giveOut()
        self.assertNotEqual(pooltable[0].start_time,None)

    def test_timer_tally_was_close_to_a_half_second(self):
        pooltable[0].giveOut()
        time.sleep(.5)
        pooltable[0].gatherTimeElapsed()
        self.assertTrue(.5 < pooltable[0].seconds < .6)

    def test_table_sets_back_to_unoccupied_when_closed(self):
        pooltable[0].giveOut()
        pooltable[0].closeOut()
        self.assertEqual(pooltable[0].occupied,"NOT OCCUPIED")

    def test_can_return_monetary_amount_given_mins(self):
        pooltable[0].minutes = 20
        self.assertEqual(pooltable[0].incurredCost(),"$10.00")

    def test_can_return_in_minutes_when_under_60min(self):
        pooltable[0].minutes = 59
        self.assertEqual(pooltable[0].readableTime(),"59min")

    def test_can_return_in_hour_min_when_over_60min(self):
        pooltable[0].minutes = 61
        self.assertEqual(pooltable[0].readableTime(),"1hr1min")

    def test_can_return_timedelta(self):
        pooltable[0].giveOut()
        time.sleep(.5)
        pooltable[0].closeOut()
        self.assertTrue(pooltable[0].time_elapsed,not(None))

#    def test_can_return_correct_JSON_string(self):
#        pooltable[0].giveOut()
#        time.sleep(.5)
#        # pooltable[0].closeOut() section
#        pooltable[0].occupied = "NOT OCCUPIED"
#        pooltable[0].stopTimer()
#        pooltable[0].gatherTimeElapsed()
#        pooltable[0].incurredCost()
#        resultingJSON = pooltable[0].toDictionary()
#        print resultingJSON
#        self.assertIn(("Cost" and "End Date Time" and "Start Date Time" and "Pool Table Number" and "Total Time Played"),resultingJSON)
#        self.assertEqual(resultingJSON.items['Cost'], "$0.01")

unittest.main(verbosity=2)
