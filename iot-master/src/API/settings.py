settings={}
settings["METEOSTAT_API_KEY"] = "W1Iocfp15ZJC7mvGN9AI4eHHnQkEeDs1"
settings["WEATHER_STATION"] = "72228"

settings["TAGS_METADATA"] = [


    {
        "name": "water",
        "description": "Records and operations for water and electric usage.",
    },

    {
        "name": "electricity",
        "description": "Records and operations for water and electric usage.",
    },


    {
        "name": "weather",
        "description": "Daily weather records and operations associated with them."
                        "Important Note: Meteostat API data is in metric units (degrees C, KM, KM/H, mm, etc)"

    
    },

    {
        "name": "root",
        "description": "This is the root URL of the API. This currently redirects visitors to the Swagger API endpoint."
    },
    {
        "name": "ButlerAPI documentation: Swagger version",
        "description": "Swagger provides interactive API documentation.",
        "externalDocs": {
            "description": "ButlerAPI Swagger documentation endpoint",
            "url": "http://localhost:8000/docs",
        }
        
    },

    {
        "name": "ButlerAPI documentation: Redoc version",
        "description": "Redoc provides API documentation.",
            "externalDocs": {
            "description": "ButlerAPI Redoc endpoint:",
            "url": "http://localhost:8000/redoc",
        }
    },

        {
        "name": "Project wiki",
        "description": "Butler API has a project Wiki with documentation and helpful information. This is hosted at UAB's GitLab repository.",
            "externalDocs": {
            "description": "ButlerAPI Readme:",
            "url": "https://gitlab.cs.uab.edu/CS499S2021/Team5/iot/wikis/IoT-Project-Wiki",
        }
    },

    {
        "name": "Project Readme.md",
        "description": "The ButlerAPI README.md is available at the project's GitLab repository, which is hosted by UAB.",
            "externalDocs": {
            "description": "ButlerAPI Readme:",
            "url": "https://gitlab.cs.uab.edu/CS499S2021/Team5/iot/blob/master/README.md",
        }
    },
    
]




settings["DB_PARAMS"] = {
    'database': 'Team5DB',
    'user': 'Team5',
    'password': 'team5',
    'host': '164.111.161.243',
    'port': '5432'
}

