# Flight and Hotel Booking Engine

A comprehensive command-line booking system for flights and hotels with persistent data storage.

## Features

### Flight Booking
- 🔍 **Search Flights**: Find flights by origin and/or destination
- ✈️ **Book Flights**: Reserve seats for one or multiple passengers
- 💺 **Real-time Availability**: Track available seats
- 💰 **Automatic Pricing**: Calculate total price based on number of passengers

### Hotel Booking
- 🔍 **Search Hotels**: Find hotels by location, star rating, and price range
- 🏨 **Book Hotels**: Reserve rooms with check-in/check-out dates
- 🛏️ **Real-time Availability**: Track available rooms
- 💰 **Automatic Pricing**: Calculate total price based on nights and rooms

### Booking Management
- 📋 **View Bookings**: Check all bookings or filter by customer email
- 💾 **Persistent Storage**: All data saved to JSON file
- 🎫 **Unique Booking IDs**: Each booking gets a unique identifier
- 📧 **Customer Tracking**: Track bookings by customer email

## Installation

### Prerequisites
- Python 3.7 or higher

### Setup
```bash
# Clone the repository
git clone https://github.com/ideaholiday/55.git
cd 55

# No additional dependencies needed - uses Python standard library only
```

## Usage

### Running the Booking Engine

```bash
python3 booking_engine.py
```

### Main Menu Options

1. **Search Flights**: Find available flights
   - Filter by origin city
   - Filter by destination city
   - View flight details including airline, times, price, and availability

2. **Search Hotels**: Find available hotels
   - Filter by location
   - Filter by minimum star rating (1-5)
   - Filter by maximum price per night
   - View hotel details including name, location, rating, and pricing

3. **Book a Flight**: Reserve flight tickets
   - Enter flight ID from search results
   - Provide customer name and email
   - Specify number of passengers
   - Receive booking confirmation with unique booking ID

4. **Book a Hotel**: Reserve hotel rooms
   - Enter hotel ID from search results
   - Provide customer name and email
   - Specify check-in and check-out dates (YYYY-MM-DD format)
   - Specify number of rooms
   - Receive booking confirmation with total price and nights

5. **View My Bookings**: Check your reservations
   - Enter your email to see all your bookings
   - View complete details of each booking

6. **View All Bookings**: Admin view of all bookings
   - See all bookings in the system
   - Useful for management and reporting

7. **Exit**: Close the application

### Example Usage

#### Searching for Flights
```
Enter your choice (1-7): 1

--- Search Flights ---
Origin (or press Enter to skip): New York
Destination (or press Enter to skip): London

Found 1 flight(s):
  Flight FL001: SkyAir | New York → London | 2025-11-01 10:00 - 2025-11-01 22:00 | $599.99 | 150 seats
```

#### Booking a Flight
```
Enter your choice (1-7): 3

--- Book a Flight ---
Enter Flight ID: FL001
Your name: John Doe
Your email: john@example.com
Number of passengers (default 1): 2

✅ Flight booked successfully!
Booking BK0001 (flight)
  Customer: John Doe (john@example.com)
  Details: flight_id: FL001, airline: SkyAir, route: New York → London, departure: 2025-11-01 10:00, arrival: 2025-11-01 22:00, passengers: 2
  Total: $1199.98
  Date: 2025-10-21 09:15:30
```

#### Searching for Hotels
```
Enter your choice (1-7): 2

--- Search Hotels ---
Location (or press Enter to skip): Paris
Minimum star rating (1-5, or press Enter to skip): 4
Maximum price per night (or press Enter to skip): 300

Found 1 hotel(s):
  Hotel HT003: City Center Hotel | Paris | ⭐⭐⭐⭐ | $249.99/night | 60 rooms
```

#### Booking a Hotel
```
Enter your choice (1-7): 4

--- Book a Hotel ---
Enter Hotel ID: HT003
Your name: Jane Smith
Your email: jane@example.com
Check-in date (YYYY-MM-DD): 2025-11-10
Check-out date (YYYY-MM-DD): 2025-11-15
Number of rooms (default 1): 1

✅ Hotel booked successfully!
Booking BK0002 (hotel)
  Customer: Jane Smith (jane@example.com)
  Details: hotel_id: HT003, hotel_name: City Center Hotel, location: Paris, check_in: 2025-11-10, check_out: 2025-11-15, nights: 5, rooms: 1, rating: 4
  Total: $1249.95
  Date: 2025-10-21 09:20:45
```

## Sample Data

The system comes pre-loaded with sample flights and hotels:

### Sample Flights
- New York ↔ London (SkyAir)
- New York → Paris (GlobalJet)
- Paris → Tokyo (GlobalJet)
- Los Angeles → Miami (AirExpress)

### Sample Hotels
- Grand Plaza Hotel (New York, 5⭐)
- Riverside Inn (London, 4⭐)
- City Center Hotel (Paris, 4⭐)
- Ocean View Resort (Miami, 5⭐)
- Budget Stay (Los Angeles, 3⭐)
- Tokyo Tower Hotel (Tokyo, 5⭐)

## Testing

Run the comprehensive test suite:

```bash
python3 test_booking_engine.py
```

### Test Coverage
- Flight class functionality
- Hotel class functionality
- Booking class functionality
- Search operations (flights and hotels)
- Booking operations (flights and hotels)
- Data persistence and loading
- Error handling (insufficient availability, invalid dates, etc.)

### Expected Output
```
...........................
----------------------------------------------------------------------
Ran 27 tests in 0.XXXs

OK
```

## Data Storage

All data is stored in `booking_data.json` in the current directory. This includes:
- Available flights and their seat inventory
- Available hotels and their room inventory
- All bookings with complete details
- Booking counter for unique ID generation

The data persists across sessions, so bookings and availability updates are maintained.

## Architecture

### Classes

#### `Flight`
Represents a flight with properties:
- `flight_id`: Unique identifier
- `airline`: Airline name
- `origin`: Departure city
- `destination`: Arrival city
- `departure_time`: Departure date and time
- `arrival_time`: Arrival date and time
- `price`: Ticket price per passenger
- `seats_available`: Number of available seats

#### `Hotel`
Represents a hotel with properties:
- `hotel_id`: Unique identifier
- `name`: Hotel name
- `location`: City/location
- `star_rating`: 1-5 star rating
- `price_per_night`: Price per room per night
- `rooms_available`: Number of available rooms

#### `Booking`
Represents a booking (flight or hotel) with properties:
- `booking_id`: Unique booking identifier
- `booking_type`: "flight" or "hotel"
- `customer_name`: Customer's name
- `customer_email`: Customer's email
- `details`: Dictionary with booking-specific details
- `total_price`: Total booking price
- `booking_date`: When the booking was made

#### `BookingEngine`
Main engine that manages:
- Flight inventory and searches
- Hotel inventory and searches
- Booking creation and management
- Data persistence (load/save)

## File Structure

```
55/
├── README.md                 # This file
├── booking_engine.py         # Main booking engine implementation
├── test_booking_engine.py    # Comprehensive test suite
├── requirements.txt          # Python dependencies (standard library only)
└── booking_data.json         # Persistent data storage (created on first run)
```

## Future Enhancements

Potential features for future versions:
- Web interface (Flask/Django)
- Payment processing integration
- Email confirmation system
- Multi-user authentication
- Advanced search filters (dates, price ranges, amenities)
- Booking cancellation and refunds
- Reviews and ratings system
- Calendar integration
- Database backend (PostgreSQL/MySQL)
- REST API
- Mobile app

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues, questions, or suggestions, please open an issue on GitHub.
