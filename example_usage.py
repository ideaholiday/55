#!/usr/bin/env python3
"""
Example script demonstrating the Flight and Hotel Booking Engine API
"""

from booking_engine import BookingEngine


def main():
    # Initialize the booking engine
    print("Initializing Flight and Hotel Booking Engine...")
    engine = BookingEngine()
    
    print("\n" + "="*60)
    print("AVAILABLE FLIGHTS")
    print("="*60)
    
    # Display all flights
    for flight in engine.flights:
        print(flight)
    
    print("\n" + "="*60)
    print("AVAILABLE HOTELS")
    print("="*60)
    
    # Display all hotels
    for hotel in engine.hotels:
        print(hotel)
    
    print("\n" + "="*60)
    print("SEARCH EXAMPLE: Flights from New York")
    print("="*60)
    
    # Search for flights from New York
    ny_flights = engine.search_flights(origin="New York")
    for flight in ny_flights:
        print(flight)
    
    print("\n" + "="*60)
    print("SEARCH EXAMPLE: 5-star Hotels")
    print("="*60)
    
    # Search for 5-star hotels
    luxury_hotels = engine.search_hotels(min_rating=5)
    for hotel in luxury_hotels:
        print(hotel)
    
    print("\n" + "="*60)
    print("BOOKING EXAMPLE: Flight Booking")
    print("="*60)
    
    # Book a flight
    booking = engine.book_flight(
        flight_id="FL001",
        customer_name="Alice Johnson",
        customer_email="alice@example.com",
        num_passengers=2
    )
    
    if booking:
        print("✅ Flight booked successfully!")
        print(booking)
    
    print("\n" + "="*60)
    print("BOOKING EXAMPLE: Hotel Booking")
    print("="*60)
    
    # Book a hotel
    booking = engine.book_hotel(
        hotel_id="HT001",
        customer_name="Bob Smith",
        customer_email="bob@example.com",
        check_in="2025-12-01",
        check_out="2025-12-05",
        num_rooms=1
    )
    
    if booking:
        print("✅ Hotel booked successfully!")
        print(booking)
    
    print("\n" + "="*60)
    print("VIEW BOOKINGS FOR ALICE")
    print("="*60)
    
    # View bookings for a specific customer
    alice_bookings = engine.get_bookings("alice@example.com")
    for booking in alice_bookings:
        print(f"\n{booking}")
    
    print("\n" + "="*60)
    print("ALL BOOKINGS IN SYSTEM")
    print("="*60)
    
    # View all bookings
    all_bookings = engine.get_bookings()
    print(f"\nTotal bookings: {len(all_bookings)}")
    for booking in all_bookings:
        print(f"\n{booking}")


if __name__ == "__main__":
    main()
