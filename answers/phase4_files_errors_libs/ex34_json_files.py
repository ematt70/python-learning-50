"""
Exercise 34 — JSON Files

Task:
    Save a dictionary to JSON, then load it back.
"""

import json

def save_profile(filename, profile):
    with open(filename, "w") as f:
        json.dump(profile, f, indent=4)

def load_profile(filename):
    with open(filename, "r") as f:
        return json.load(f)

def main():
    profile = {"name": "Erich", "age": 42}
    save_profile("profile.json", profile)
    print("Saved JSON.")
    loaded = load_profile("profile.json")
    print("Loaded:", loaded)

if __name__ == "__main__":
    main()
