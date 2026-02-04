contacts = {
    "Alice": "55-1234",
    "Bob": "55-5678",
    "Charlie": "55-8765"
}

print(f"Alice's contact: {contacts['Alice']}")
contacts["Diana"] = "55-4321"
print(f"Contacts after adding Diana: {contacts}")
contacts["Bob"] = "55-0000"
print(f"Contacts after updating Bob's number: {contacts}")
del contacts["Charlie"]
print(f"Contacts after deleting Charlie: {contacts}")

print(f"All names: {list(contacts.keys())}")
print(f"All numbers: {list(contacts.values())}")
print(f"All contacts: {len(contacts)}")