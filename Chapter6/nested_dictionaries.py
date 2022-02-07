ttrpgs={
    "Dungeons & Dragons":{
    "genre": "Medieval Fantasy",
    "created": "1974",
    "company": "Wizards of the Coast"
    },
    "Pathfinder":{
    "genre": "Medieval Fantasy",
    "created": "2009",
    "company": "Piazo"
    },
    "Starfinder":{
    "genre": "Sci-Fi",
    "created": "2017",
    "company": "Piazo"
    },
    "Call of Cthulhu":{
    "genre": "Horror",
    "created": "1981",
    "company": "Chaosium"
    }
}

for key, value in ttrpgs.items():
    print(f"""\nGame: {key}
    Genre: {value["genre"]}
    Created: {value["created"]}
    Company: {value["company"]}""")