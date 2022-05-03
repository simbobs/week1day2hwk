users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
print(users["Jonathan"]["twitter"])

# 2. Get Erik's hometown
print(users["Erik"]["home_town"])

# 3. Get the list of Erik's lottery numbers
print(users["Erik"]["lottery_numbers"])

# 4. Get the species of Avril's pet Monty
print(users["Avril"]["pets"][0]["species"])

# 5. Get the smallest of Erik's lottery numbers
print(min(users["Erik"]["lottery_numbers"]))


# 6. Return an list of Avril's lottery numbers that are even

avrils_numbers = users["Avril"]["lottery_numbers"]
for num in avrils_numbers:
  if num % 2 == 0:
    print(num)


# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
erik_lotto = users["Erik"]["lottery_numbers"]
erik_lotto.append(7)
print(erik_lotto)

# 8. Change Erik's hometown to Edinburgh
users["Erik"]["home_town"] = "Edinburgh"
print(users["Erik"]["home_town"])

# 9. Add a pet dog to Erik called "fluffy"
erik_pets = users["Erik"]["pets"]
eriks_new_pet = {"name":"fluffy","species":"dog"}
erik_pets.append(eriks_new_pet)
print(erik_pets)

# 10. Add another person to the users dictionary
simonas_info = {
  "twitter": "simbobs",
  "lottery_numbers": "[1,2,3,4,5,6,7,8]",
  "hometown":"Glasgow",
  "pets":[{
    "name":"Pepe",
    "species":"dog"

  }],
}

print(simonas_info)
users["Simona"] = simonas_info
print(users)
