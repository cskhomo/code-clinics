from os import path, remove, environ
from json import load
from unittest import TestCase, main
from src.storage.data import refresh
from src.api import account
from datetime import datetime, timedelta
from warnings import simplefilter


class TestRefresh(TestCase):
    """
    Test class for the refresh function in the data module.
    """

    def setUp(self):
        """Sets up the test environment by logging in and refreshing data."""
        
        self.service = account.login('student')
        refresh(self.service)


    def tearDown(self):
        """Clean up the local storage by removing the test files."""
        
        for calendar in ['primary', 'clinic']:
            cache = path.join(environ.get("CACHE"), f'{calendar}.json')
            if path.exists(cache):
                remove(cache)


    def test_events_stored(self):
        """Tests that the cache files are created after calling the refresh function."""
        
        for calendar in ['primary', 'clinic']:
            cache = path.join(environ.get("CACHE"), f'{calendar}.json')
            self.assertTrue(path.exists(cache))


    def test_relevant_events(self):
        """Tests that the events in the cache files have the expected keys."""
        
        for calendar in ['primary', 'clinic']:
            cache = path.join(environ.get("CACHE"), f'{calendar}.json')
           
            with open(cache, 'r') as file:
                events = load(file)
        
                for event in events:
                    self.assertIn('id', event)
                    self.assertIn('start', event)
                    self.assertIn('end', event)
                    self.assertIn('summary', event)
                    self.assertIn('creator', event)
                    
                    if calendar == 'clinic':
                        self.assertIn('attendees', event)


    def test_event_range(self):
        """Tests that the events in the cache files are within the expected date range."""
        
        today = datetime.now().date()
        seven_days = today + timedelta(days=7)

        for calendar in ['primary', 'clinic']:
            cache = path.join(environ.get("CACHE"), f'{calendar}.json')
            
            with open(cache, 'r') as file:
                events = load(file)
                
                dates = [
                    datetime.strptime(event['start'].split('T')[0],
                    '%Y-%m-%d').date() if 'T' in event['start'] else datetime.strptime(event['start'],
                    '%Y-%m-%d').date() for event in events
                ]

                self.assertGreaterEqual(min(dates), today)
                self.assertLessEqual(max(dates), seven_days)


if __name__ == '__main__':
    simplefilter("ignore", ResourceWarning)
    simplefilter("ignore", DeprecationWarning)
    main(warnings='ignore')