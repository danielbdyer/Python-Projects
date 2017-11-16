airports = {"IAH":"George H. Bush Intercontinental Airport",
            "SEATAC":"Seattle-Tacoma Airport"}
print(airports["SEATAC"])

for key in airports:
    print(airports[key])

customer = {"firstName": "John",
            "lastname": "Doe",
            "address": {
                "street": "1200 Richmond",
                "state": "TX",
                "geo": {
                    "latitude":123,
                    "longitude":123.122
                    }
                }
            }

print(customer)

listing1 = {
"city":"Houston",
"state":"TX",
"noOfRooms":5
}

listing2 = {
"city":"Austin",
"state":"TX",
"noOfRooms":3
}

listings = [listing1,listing2]
print listings

for listing in listings:
    print(listing)
