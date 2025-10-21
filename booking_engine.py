#!/usr/bin/env python3
"""
Flight and Hotel Booking Engine
A simple command-line booking system for flights and hotels.
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional


class Flight:
    """Represents a flight with its details."""
    
    def __init__(self, flight_id: str, airline: str, origin: str, destination: str,
                 departure_time: str, arrival_time: str, price: float, seats_available: int):
        self.flight_id = flight_id
        self.airline = airline
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.price = price
        self.seats_available = seats_available
    
    def to_dict(self) -> Dict:
        """Convert flight to dictionary."""
        return {
            'flight_id': self.flight_id,
            'airline': self.airline,
            'origin': self.origin,
            'destination': self.destination,
            'departure_time': self.departure_time,
            'arrival_time': self.arrival_time,
            'price': self.price,
            'seats_available': self.seats_available
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Flight':
        """Create flight from dictionary."""
        return cls(**data)
    
    def __str__(self) -> str:
        return (f"Flight {self.flight_id}: {self.airline} | "
                f"{self.origin} → {self.destination} | "
                f"{self.departure_time} - {self.arrival_time} | "
                f"${self.price:.2f} | {self.seats_available} seats")


class Hotel:
    """Represents a hotel with its details."""
    
    def __init__(self, hotel_id: str, name: str, location: str,
                 star_rating: int, price_per_night: float, rooms_available: int):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.star_rating = star_rating
        self.price_per_night = price_per_night
        self.rooms_available = rooms_available
    
    def to_dict(self) -> Dict:
        """Convert hotel to dictionary."""
        return {
            'hotel_id': self.hotel_id,
            'name': self.name,
            'location': self.location,
            'star_rating': self.star_rating,
            'price_per_night': self.price_per_night,
            'rooms_available': self.rooms_available
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Hotel':
        """Create hotel from dictionary."""
        return cls(**data)
    
    def __str__(self) -> str:
        stars = "⭐" * self.star_rating
        return (f"Hotel {self.hotel_id}: {self.name} | "
                f"{self.location} | {stars} | "
                f"${self.price_per_night:.2f}/night | {self.rooms_available} rooms")


class Booking:
    """Represents a booking (flight or hotel)."""
    
    def __init__(self, booking_id: str, booking_type: str, customer_name: str,
                 customer_email: str, details: Dict, total_price: float,
                 booking_date: str):
        self.booking_id = booking_id
        self.booking_type = booking_type
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.details = details
        self.total_price = total_price
        self.booking_date = booking_date
    
    def to_dict(self) -> Dict:
        """Convert booking to dictionary."""
        return {
            'booking_id': self.booking_id,
            'booking_type': self.booking_type,
            'customer_name': self.customer_name,
            'customer_email': self.customer_email,
            'details': self.details,
            'total_price': self.total_price,
            'booking_date': self.booking_date
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Booking':
        """Create booking from dictionary."""
        return cls(**data)
    
    def __str__(self) -> str:
        details_str = ", ".join([f"{k}: {v}" for k, v in self.details.items()])
        return (f"Booking {self.booking_id} ({self.booking_type})\n"
                f"  Customer: {self.customer_name} ({self.customer_email})\n"
                f"  Details: {details_str}\n"
                f"  Total: ${self.total_price:.2f}\n"
                f"  Date: {self.booking_date}")


class BookingEngine:
    """Main booking engine that manages flights, hotels, and bookings."""
    
    def __init__(self, data_file: str = 'booking_data.json'):
        self.data_file = data_file
        self.flights: List[Flight] = []
        self.hotels: List[Hotel] = []
        self.bookings: List[Booking] = []
        self.booking_counter = 1
        self.load_data()
        self._initialize_sample_data()
    
    def _initialize_sample_data(self):
        """Initialize with sample flights and hotels if empty."""
        if not self.flights:
            self.flights = [
                Flight("FL001", "SkyAir", "New York", "London", "2025-11-01 10:00", 
                       "2025-11-01 22:00", 599.99, 150),
                Flight("FL002", "SkyAir", "London", "New York", "2025-11-05 14:00", 
                       "2025-11-05 18:00", 649.99, 120),
                Flight("FL003", "GlobalJet", "New York", "Paris", "2025-11-02 09:00", 
                       "2025-11-02 21:00", 699.99, 100),
                Flight("FL004", "GlobalJet", "Paris", "Tokyo", "2025-11-10 11:00", 
                       "2025-11-11 07:00", 899.99, 80),
                Flight("FL005", "AirExpress", "Los Angeles", "Miami", "2025-11-03 08:00", 
                       "2025-11-03 16:00", 299.99, 200),
            ]
        
        if not self.hotels:
            self.hotels = [
                Hotel("HT001", "Grand Plaza Hotel", "New York", 5, 299.99, 50),
                Hotel("HT002", "Riverside Inn", "London", 4, 199.99, 75),
                Hotel("HT003", "City Center Hotel", "Paris", 4, 249.99, 60),
                Hotel("HT004", "Ocean View Resort", "Miami", 5, 349.99, 40),
                Hotel("HT005", "Budget Stay", "Los Angeles", 3, 89.99, 100),
                Hotel("HT006", "Tokyo Tower Hotel", "Tokyo", 5, 279.99, 45),
            ]
    
    def load_data(self):
        """Load data from JSON file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.flights = [Flight.from_dict(f) for f in data.get('flights', [])]
                    self.hotels = [Hotel.from_dict(h) for h in data.get('hotels', [])]
                    self.bookings = [Booking.from_dict(b) for b in data.get('bookings', [])]
                    self.booking_counter = data.get('booking_counter', 1)
            except Exception as e:
                print(f"Error loading data: {e}")
    
    def save_data(self):
        """Save data to JSON file."""
        try:
            data = {
                'flights': [f.to_dict() for f in self.flights],
                'hotels': [h.to_dict() for h in self.hotels],
                'bookings': [b.to_dict() for b in self.bookings],
                'booking_counter': self.booking_counter
            }
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def search_flights(self, origin: Optional[str] = None, 
                      destination: Optional[str] = None) -> List[Flight]:
        """Search for flights by origin and/or destination."""
        results = self.flights
        
        if origin:
            results = [f for f in results if origin.lower() in f.origin.lower()]
        
        if destination:
            results = [f for f in results if destination.lower() in f.destination.lower()]
        
        return results
    
    def search_hotels(self, location: Optional[str] = None, 
                     min_rating: Optional[int] = None,
                     max_price: Optional[float] = None) -> List[Hotel]:
        """Search for hotels by location, rating, and price."""
        results = self.hotels
        
        if location:
            results = [h for h in results if location.lower() in h.location.lower()]
        
        if min_rating:
            results = [h for h in results if h.star_rating >= min_rating]
        
        if max_price:
            results = [h for h in results if h.price_per_night <= max_price]
        
        return results
    
    def book_flight(self, flight_id: str, customer_name: str, 
                   customer_email: str, num_passengers: int = 1) -> Optional[Booking]:
        """Book a flight."""
        flight = next((f for f in self.flights if f.flight_id == flight_id), None)
        
        if not flight:
            print(f"Flight {flight_id} not found.")
            return None
        
        if flight.seats_available < num_passengers:
            print(f"Not enough seats available. Only {flight.seats_available} seats left.")
            return None
        
        # Create booking
        booking_id = f"BK{self.booking_counter:04d}"
        self.booking_counter += 1
        
        total_price = flight.price * num_passengers
        details = {
            'flight_id': flight_id,
            'airline': flight.airline,
            'route': f"{flight.origin} → {flight.destination}",
            'departure': flight.departure_time,
            'arrival': flight.arrival_time,
            'passengers': num_passengers
        }
        
        booking = Booking(
            booking_id=booking_id,
            booking_type='flight',
            customer_name=customer_name,
            customer_email=customer_email,
            details=details,
            total_price=total_price,
            booking_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        
        # Update flight availability
        flight.seats_available -= num_passengers
        
        # Save booking
        self.bookings.append(booking)
        self.save_data()
        
        return booking
    
    def book_hotel(self, hotel_id: str, customer_name: str, 
                  customer_email: str, check_in: str, check_out: str,
                  num_rooms: int = 1) -> Optional[Booking]:
        """Book a hotel."""
        hotel = next((h for h in self.hotels if h.hotel_id == hotel_id), None)
        
        if not hotel:
            print(f"Hotel {hotel_id} not found.")
            return None
        
        if hotel.rooms_available < num_rooms:
            print(f"Not enough rooms available. Only {hotel.rooms_available} rooms left.")
            return None
        
        # Calculate number of nights
        try:
            check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
            check_out_date = datetime.strptime(check_out, "%Y-%m-%d")
            num_nights = (check_out_date - check_in_date).days
            
            if num_nights <= 0:
                print("Check-out date must be after check-in date.")
                return None
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")
            return None
        
        # Create booking
        booking_id = f"BK{self.booking_counter:04d}"
        self.booking_counter += 1
        
        total_price = hotel.price_per_night * num_nights * num_rooms
        details = {
            'hotel_id': hotel_id,
            'hotel_name': hotel.name,
            'location': hotel.location,
            'check_in': check_in,
            'check_out': check_out,
            'nights': num_nights,
            'rooms': num_rooms,
            'rating': hotel.star_rating
        }
        
        booking = Booking(
            booking_id=booking_id,
            booking_type='hotel',
            customer_name=customer_name,
            customer_email=customer_email,
            details=details,
            total_price=total_price,
            booking_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        
        # Update hotel availability
        hotel.rooms_available -= num_rooms
        
        # Save booking
        self.bookings.append(booking)
        self.save_data()
        
        return booking
    
    def get_bookings(self, customer_email: Optional[str] = None) -> List[Booking]:
        """Get all bookings or filter by customer email."""
        if customer_email:
            return [b for b in self.bookings if b.customer_email == customer_email]
        return self.bookings


def print_menu():
    """Print the main menu."""
    print("\n" + "="*60)
    print("  FLIGHT AND HOTEL BOOKING ENGINE")
    print("="*60)
    print("1. Search Flights")
    print("2. Search Hotels")
    print("3. Book a Flight")
    print("4. Book a Hotel")
    print("5. View My Bookings")
    print("6. View All Bookings")
    print("7. Exit")
    print("="*60)


def main():
    """Main function to run the booking engine CLI."""
    engine = BookingEngine()
    
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == '1':
            # Search flights
            print("\n--- Search Flights ---")
            origin = input("Origin (or press Enter to skip): ").strip() or None
            destination = input("Destination (or press Enter to skip): ").strip() or None
            
            flights = engine.search_flights(origin, destination)
            if flights:
                print(f"\nFound {len(flights)} flight(s):")
                for flight in flights:
                    print(f"  {flight}")
            else:
                print("No flights found.")
        
        elif choice == '2':
            # Search hotels
            print("\n--- Search Hotels ---")
            location = input("Location (or press Enter to skip): ").strip() or None
            min_rating_str = input("Minimum star rating (1-5, or press Enter to skip): ").strip()
            min_rating = int(min_rating_str) if min_rating_str else None
            max_price_str = input("Maximum price per night (or press Enter to skip): ").strip()
            max_price = float(max_price_str) if max_price_str else None
            
            hotels = engine.search_hotels(location, min_rating, max_price)
            if hotels:
                print(f"\nFound {len(hotels)} hotel(s):")
                for hotel in hotels:
                    print(f"  {hotel}")
            else:
                print("No hotels found.")
        
        elif choice == '3':
            # Book a flight
            print("\n--- Book a Flight ---")
            flight_id = input("Enter Flight ID: ").strip()
            customer_name = input("Your name: ").strip()
            customer_email = input("Your email: ").strip()
            num_passengers_str = input("Number of passengers (default 1): ").strip()
            num_passengers = int(num_passengers_str) if num_passengers_str else 1
            
            booking = engine.book_flight(flight_id, customer_name, customer_email, num_passengers)
            if booking:
                print("\n✅ Flight booked successfully!")
                print(booking)
        
        elif choice == '4':
            # Book a hotel
            print("\n--- Book a Hotel ---")
            hotel_id = input("Enter Hotel ID: ").strip()
            customer_name = input("Your name: ").strip()
            customer_email = input("Your email: ").strip()
            check_in = input("Check-in date (YYYY-MM-DD): ").strip()
            check_out = input("Check-out date (YYYY-MM-DD): ").strip()
            num_rooms_str = input("Number of rooms (default 1): ").strip()
            num_rooms = int(num_rooms_str) if num_rooms_str else 1
            
            booking = engine.book_hotel(hotel_id, customer_name, customer_email, 
                                       check_in, check_out, num_rooms)
            if booking:
                print("\n✅ Hotel booked successfully!")
                print(booking)
        
        elif choice == '5':
            # View my bookings
            print("\n--- View My Bookings ---")
            customer_email = input("Enter your email: ").strip()
            
            bookings = engine.get_bookings(customer_email)
            if bookings:
                print(f"\nFound {len(bookings)} booking(s):")
                for booking in bookings:
                    print(f"\n{booking}")
            else:
                print("No bookings found for this email.")
        
        elif choice == '6':
            # View all bookings
            print("\n--- All Bookings ---")
            bookings = engine.get_bookings()
            if bookings:
                print(f"\nTotal {len(bookings)} booking(s):")
                for booking in bookings:
                    print(f"\n{booking}")
            else:
                print("No bookings in the system.")
        
        elif choice == '7':
            print("\nThank you for using the Flight and Hotel Booking Engine!")
            break
        
        else:
            print("\n❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
