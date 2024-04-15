# Create a Python function that takes a list of tuples as an argument. 
# Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). 
# The function should format and return a string that lists each itinerary. 
# For example, if the input is [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")], 
# the output should be a string formatted as:

# "Itinerary 1: Alice - From New York to London
#  Itinerary 2: Bob - From Tokyo to San Francisco"


# def format_itineraries(itineraries):
#     formatted = ""
#     itinerary_num = 1
#     for itinerary in itineraries:
#         traveler_name, origin, destination = itinerary
#         formatted += f"Itinerary {itinerary_num}: {traveler_name} - From {origin} to {destination}\n"
#         itinerary_num += 1
#     return formatted
# format_itineraries()

# def flight_itineraries():
#     itineraries = []   
#     while True:
#         itinerary = input("Enter traveler name, origin, and destination for itinerary (or type 'done' to finish): ")
#         if itinerary.lower() == 'done':
#             break
#         traveler_name, origin, destination = itinerary.split()
#         itineraries.append((traveler_name, origin, destination))
#     return itineraries

# flight_itineraries()

print("=========================================================================================")

itineraries = [] 
def flight_itineraries():
    while True:
        itinerary = input("Enter traveler name, origin, and destination for itinerary (or type 'done' to finish): ")
        if itinerary == 'done':
            break
        itinerary_parts = itinerary.split(',', maxsplit=2)     # Split the input string into parts
        traveler_name, origin, destination = itinerary_parts
        itineraries.append((traveler_name.strip(), origin.strip(), destination.strip()))
    return itineraries
flight_itineraries()

formatted_output = ""
for i in range(len(itineraries)):
    traveler_name, origin, destination = itineraries[i]
    formatted_output += f"Itinerary {i+1}: {traveler_name} - From {origin} to {destination}\n"
print(formatted_output)

print("====================================================================================")


# itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
# print(format_itineraries(itineraries))


# formatted_output = ""
# for i, itinerary in enumerate(itineraries, 0):
#         traveler_name, origin, destination = itinerary
#         formatted_output += f"Itinerary {i}: {traveler_name} - From {origin} to {destination}\n"
        
# print(formatted_output)    
# print(flight_itineraries())

# itineraries = []

# formatted_output = ""
# for i in range(len(itineraries)):
#     traveler_name, origin, destination = itineraries[i]
#     formatted_output += f"Itinerary {i+1}: {traveler_name} - From {origin} to {destination}\n"

# print(formatted_output)
# print(flight_itineraries())

print("===============================================================================================")

# You are maintaining a library system where each book is stored as a tuple within a list. 
# Your task is to update this system by adding new books and ensuring no duplicates.

# Existing Library Data:

# library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
# Add functionality to insert new books into library.
# Ensure that adding a duplicate book is handled appropriately.

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# add book function
def add_book(title, author):
    global library
    
    # check if the book in the library already
    if (title, author) in library:
        print("This book is already in the library.")
    else:
        # if the book is not in the library, add it to the library
        library.append((title, author))
        print("Book now in library.")

# display library function
def display_library():
    print("Current Library Books:")
    for book in library:
        print(f"{book[0]} by {book[1]}")

# running my functions
add_book("1984", "George Orwell")  # This should print "This book already exists in the library."
add_book("Rich Dad Poor Dad", "Robert Kiyosaki")  # This should add the book "Rich Dad Poor Dad" to the library
display_library()  # This should display all books in the library

print("==========================================================================================================")

# You have been provided with stock market data, where each data point is a tuple containing a company's stock symbol,
# the date, and the closing price. Your task is to analyze this data to find the average closing price
# of a specified stock over a given period.

# Sample Data:

# stock_data = [
#     ("AAPL", "2021-01-01", 130.0),
#     ("AAPL", "2021-01-02", 132.0),
#     ("MSFT", "2021-01-01", 220.0),
#     # More data...
#]
# Create a function to calculate the average closing price of a specific stock symbol over all dates.
# Ensure your solution handles cases where the stock symbol does not exist in the data.

stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    # More data...
]

def average_closing_price(stock_data, stock_symbol):
    # Filter the stock data for the specified stock symbol
    closing_prices = [data[2] for data in stock_data if data[0] == stock_symbol]
    
    # Check if any data was found for the given stock symbol
    if not closing_prices:
        return f"No data found for stock symbol {stock_symbol}."
    
    # Calculate the average closing price
    average_price = sum(closing_prices) / len(closing_prices)
    return average_price


# Running my function
avg_price_aapl = average_closing_price(stock_data, "AAPL")
print("Average closing price of AAPL:", avg_price_aapl)

avg_price_amzn = average_closing_price(stock_data, "AMZN")
print("Average closing price of GOOG:", avg_price_amzn)

print("=======================================================================================")

# Apply loops and tuples to track and report on event attendance.

# Problem Statement:
# Your goal is to manage an attendance system for various events. 
# Each attendee's data is stored as a tuple containing their name and the event they attended.

# Develop a function to list all attendees of a specific event.
# Implement a feature to count the number of attendees for each event.
# Example Attendee Data:

attendees = [
    ("Alice", "Python Conference"),
    ("Bob", "Python Conference"),
    ("Charlie", "AI Summit"),
    # More attendees...
]

# def list_attendees(attendees, event):
#     event_attendants = [attendant[0] for attendant in attendees if attendant[1] == event]
#     return event_attendants

# event_name = "Python Conference"
# print(f"Attendees of {event_name}: {list_attendees(attendees, event_name)}")
# # print(list_attendees())

# def count_attendees_per_event(attendees):
#     event_counts = {}
#     for attendee in attendees:
#         event_name = attendee[1]
#         if event_name in event_counts:
#             event_counts[event_name] += 1
#         else:
#             event_counts[event_name] = 1
#     return [(event, count) for event, count in event_counts.items()]

# attendees = [
#     ("Alice", "Python Conference"),
#     ("Bob", "Python Conference"),
#     ("Charlie", "AI Summit"),
#     # More attendees...
# ]


# print("Attendees for each event:")
# for event, attendees in list_attendees(attendees):
#     print(f"{event}: {attendees}")


def list_attendees(attendees):
    event_attendees = {}
    for attendee in attendees:
        event_name = attendee[1]
        if event_name in event_attendees:
            event_attendees[event_name].append(attendee[0])
        else:
            event_attendees[event_name] = [attendee[0]]
    return [(event, attendees) for event, attendees in event_attendees.items()]

# list_attendees(attendees)
# print(list_attendees(attendees))
# print("Attendees for each event:")
# for event, attendees in list_attendees(attendees):
#     print(f"{event}: {attendees}")

def attendees_per_event(attendees):
    event_counts = {}
    for attendee in attendees:
        event_name = attendee[1]
        if event_name in event_counts:
            event_counts[event_name] += 1
        else:
            event_counts[event_name] = 1
    return [(event, count) for event, count in event_counts.items()]

# attendees_per_event(attendees)
# print(attendees_per_event(attendees))

# print("Attendees for each event:")
# for event, attendees in list_attendees(attendees):
#     print(f"{event}: {attendees}")

print("\nAttendee counts for each event:")
for event, count in attendees_per_event(attendees):
    print(f"{event}: {count}")

print("Attendees for each event:")
for event, attendees in list_attendees(attendees):
    print(f"{event}: {attendees}")


