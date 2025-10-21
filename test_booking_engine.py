#!/usr/bin/env python3
"""
Unit tests for the Flight and Hotel Booking Engine
"""

import unittest
import os
import json
from datetime import datetime
from booking_engine import Flight, Hotel, Booking, BookingEngine


class TestFlight(unittest.TestCase):
    """Test the Flight class."""
    
    def test_flight_creation(self):
        """Test creating a flight."""
        flight = Flight("FL001", "TestAir", "NYC", "LON", 
                       "2025-11-01 10:00", "2025-11-01 22:00", 599.99, 150)
        self.assertEqual(flight.flight_id, "FL001")
        self.assertEqual(flight.airline, "TestAir")
        self.assertEqual(flight.origin, "NYC")
        self.assertEqual(flight.destination, "LON")
        self.assertEqual(flight.price, 599.99)
        self.assertEqual(flight.seats_available, 150)
    
    def test_flight_to_dict(self):
        """Test converting flight to dictionary."""
        flight = Flight("FL001", "TestAir", "NYC", "LON", 
                       "2025-11-01 10:00", "2025-11-01 22:00", 599.99, 150)
        flight_dict = flight.to_dict()
        self.assertEqual(flight_dict['flight_id'], "FL001")
        self.assertEqual(flight_dict['airline'], "TestAir")
        self.assertEqual(flight_dict['price'], 599.99)
    
    def test_flight_from_dict(self):
        """Test creating flight from dictionary."""
        data = {
            'flight_id': 'FL001',
            'airline': 'TestAir',
            'origin': 'NYC',
            'destination': 'LON',
            'departure_time': '2025-11-01 10:00',
            'arrival_time': '2025-11-01 22:00',
            'price': 599.99,
            'seats_available': 150
        }
        flight = Flight.from_dict(data)
        self.assertEqual(flight.flight_id, "FL001")
        self.assertEqual(flight.airline, "TestAir")


class TestHotel(unittest.TestCase):
    """Test the Hotel class."""
    
    def test_hotel_creation(self):
        """Test creating a hotel."""
        hotel = Hotel("HT001", "Test Hotel", "NYC", 4, 199.99, 50)
        self.assertEqual(hotel.hotel_id, "HT001")
        self.assertEqual(hotel.name, "Test Hotel")
        self.assertEqual(hotel.location, "NYC")
        self.assertEqual(hotel.star_rating, 4)
        self.assertEqual(hotel.price_per_night, 199.99)
        self.assertEqual(hotel.rooms_available, 50)
    
    def test_hotel_to_dict(self):
        """Test converting hotel to dictionary."""
        hotel = Hotel("HT001", "Test Hotel", "NYC", 4, 199.99, 50)
        hotel_dict = hotel.to_dict()
        self.assertEqual(hotel_dict['hotel_id'], "HT001")
        self.assertEqual(hotel_dict['name'], "Test Hotel")
        self.assertEqual(hotel_dict['star_rating'], 4)
    
    def test_hotel_from_dict(self):
        """Test creating hotel from dictionary."""
        data = {
            'hotel_id': 'HT001',
            'name': 'Test Hotel',
            'location': 'NYC',
            'star_rating': 4,
            'price_per_night': 199.99,
            'rooms_available': 50
        }
        hotel = Hotel.from_dict(data)
        self.assertEqual(hotel.hotel_id, "HT001")
        self.assertEqual(hotel.name, "Test Hotel")


class TestBooking(unittest.TestCase):
    """Test the Booking class."""
    
    def test_booking_creation(self):
        """Test creating a booking."""
        details = {'flight_id': 'FL001', 'passengers': 2}
        booking = Booking("BK0001", "flight", "John Doe", "john@example.com",
                         details, 1199.98, "2025-10-21 10:00:00")
        self.assertEqual(booking.booking_id, "BK0001")
        self.assertEqual(booking.booking_type, "flight")
        self.assertEqual(booking.customer_name, "John Doe")
        self.assertEqual(booking.total_price, 1199.98)
    
    def test_booking_to_dict(self):
        """Test converting booking to dictionary."""
        details = {'flight_id': 'FL001', 'passengers': 2}
        booking = Booking("BK0001", "flight", "John Doe", "john@example.com",
                         details, 1199.98, "2025-10-21 10:00:00")
        booking_dict = booking.to_dict()
        self.assertEqual(booking_dict['booking_id'], "BK0001")
        self.assertEqual(booking_dict['customer_name'], "John Doe")


class TestBookingEngine(unittest.TestCase):
    """Test the BookingEngine class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_data_file = '/tmp/test_booking_data.json'
        if os.path.exists(self.test_data_file):
            os.remove(self.test_data_file)
        self.engine = BookingEngine(self.test_data_file)
    
    def tearDown(self):
        """Clean up test fixtures."""
        if os.path.exists(self.test_data_file):
            os.remove(self.test_data_file)
    
    def test_engine_initialization(self):
        """Test that engine initializes with sample data."""
        self.assertGreater(len(self.engine.flights), 0)
        self.assertGreater(len(self.engine.hotels), 0)
    
    def test_search_flights_by_origin(self):
        """Test searching flights by origin."""
        results = self.engine.search_flights(origin="New York")
        self.assertGreater(len(results), 0)
        for flight in results:
            self.assertIn("New York", flight.origin)
    
    def test_search_flights_by_destination(self):
        """Test searching flights by destination."""
        results = self.engine.search_flights(destination="London")
        self.assertGreater(len(results), 0)
        for flight in results:
            self.assertIn("London", flight.destination)
    
    def test_search_flights_by_origin_and_destination(self):
        """Test searching flights by both origin and destination."""
        results = self.engine.search_flights(origin="New York", destination="London")
        for flight in results:
            self.assertIn("New York", flight.origin)
            self.assertIn("London", flight.destination)
    
    def test_search_hotels_by_location(self):
        """Test searching hotels by location."""
        results = self.engine.search_hotels(location="New York")
        self.assertGreater(len(results), 0)
        for hotel in results:
            self.assertIn("New York", hotel.location)
    
    def test_search_hotels_by_rating(self):
        """Test searching hotels by minimum rating."""
        results = self.engine.search_hotels(min_rating=4)
        self.assertGreater(len(results), 0)
        for hotel in results:
            self.assertGreaterEqual(hotel.star_rating, 4)
    
    def test_search_hotels_by_price(self):
        """Test searching hotels by maximum price."""
        results = self.engine.search_hotels(max_price=200)
        self.assertGreater(len(results), 0)
        for hotel in results:
            self.assertLessEqual(hotel.price_per_night, 200)
    
    def test_book_flight_success(self):
        """Test successfully booking a flight."""
        flight = self.engine.flights[0]
        initial_seats = flight.seats_available
        
        booking = self.engine.book_flight(
            flight.flight_id,
            "John Doe",
            "john@example.com",
            2
        )
        
        self.assertIsNotNone(booking)
        self.assertEqual(booking.booking_type, "flight")
        self.assertEqual(booking.customer_name, "John Doe")
        self.assertEqual(booking.details['passengers'], 2)
        self.assertEqual(flight.seats_available, initial_seats - 2)
        self.assertEqual(booking.total_price, flight.price * 2)
    
    def test_book_flight_insufficient_seats(self):
        """Test booking a flight with insufficient seats."""
        flight = self.engine.flights[0]
        
        booking = self.engine.book_flight(
            flight.flight_id,
            "John Doe",
            "john@example.com",
            flight.seats_available + 1
        )
        
        self.assertIsNone(booking)
    
    def test_book_flight_invalid_id(self):
        """Test booking a flight with invalid ID."""
        booking = self.engine.book_flight(
            "INVALID",
            "John Doe",
            "john@example.com",
            1
        )
        
        self.assertIsNone(booking)
    
    def test_book_hotel_success(self):
        """Test successfully booking a hotel."""
        hotel = self.engine.hotels[0]
        initial_rooms = hotel.rooms_available
        
        booking = self.engine.book_hotel(
            hotel.hotel_id,
            "Jane Smith",
            "jane@example.com",
            "2025-11-01",
            "2025-11-05",
            1
        )
        
        self.assertIsNotNone(booking)
        self.assertEqual(booking.booking_type, "hotel")
        self.assertEqual(booking.customer_name, "Jane Smith")
        self.assertEqual(booking.details['nights'], 4)
        self.assertEqual(hotel.rooms_available, initial_rooms - 1)
        self.assertEqual(booking.total_price, hotel.price_per_night * 4)
    
    def test_book_hotel_invalid_dates(self):
        """Test booking a hotel with invalid dates."""
        hotel = self.engine.hotels[0]
        
        # Check-out before check-in
        booking = self.engine.book_hotel(
            hotel.hotel_id,
            "Jane Smith",
            "jane@example.com",
            "2025-11-05",
            "2025-11-01",
            1
        )
        
        self.assertIsNone(booking)
    
    def test_book_hotel_insufficient_rooms(self):
        """Test booking a hotel with insufficient rooms."""
        hotel = self.engine.hotels[0]
        
        booking = self.engine.book_hotel(
            hotel.hotel_id,
            "Jane Smith",
            "jane@example.com",
            "2025-11-01",
            "2025-11-05",
            hotel.rooms_available + 1
        )
        
        self.assertIsNone(booking)
    
    def test_get_bookings_all(self):
        """Test getting all bookings."""
        # Make some bookings
        flight = self.engine.flights[0]
        self.engine.book_flight(flight.flight_id, "John Doe", "john@example.com", 1)
        
        hotel = self.engine.hotels[0]
        self.engine.book_hotel(hotel.hotel_id, "Jane Smith", "jane@example.com",
                              "2025-11-01", "2025-11-05", 1)
        
        bookings = self.engine.get_bookings()
        self.assertEqual(len(bookings), 2)
    
    def test_get_bookings_by_email(self):
        """Test getting bookings filtered by email."""
        # Make some bookings
        flight = self.engine.flights[0]
        self.engine.book_flight(flight.flight_id, "John Doe", "john@example.com", 1)
        
        hotel = self.engine.hotels[0]
        self.engine.book_hotel(hotel.hotel_id, "Jane Smith", "jane@example.com",
                              "2025-11-01", "2025-11-05", 1)
        
        bookings = self.engine.get_bookings("john@example.com")
        self.assertEqual(len(bookings), 1)
        self.assertEqual(bookings[0].customer_email, "john@example.com")
    
    def test_data_persistence(self):
        """Test that data is saved and loaded correctly."""
        # Make a booking
        flight = self.engine.flights[0]
        booking = self.engine.book_flight(flight.flight_id, "John Doe", "john@example.com", 1)
        
        # Create a new engine instance (should load saved data)
        new_engine = BookingEngine(self.test_data_file)
        
        # Check that booking was persisted
        loaded_bookings = new_engine.get_bookings("john@example.com")
        self.assertEqual(len(loaded_bookings), 1)
        self.assertEqual(loaded_bookings[0].booking_id, booking.booking_id)
        
        # Check that seat availability was persisted
        loaded_flight = next(f for f in new_engine.flights if f.flight_id == flight.flight_id)
        self.assertEqual(loaded_flight.seats_available, flight.seats_available)


if __name__ == '__main__':
    unittest.main()
