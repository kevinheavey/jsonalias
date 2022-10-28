from jsonalias import Json

d: Json = {"foo": ["bar", {"x": "y"}]}
reveal_type(d)

long_example: Json = {
    "info": {
        "clockSysvar": "SysvarC1ock11111111111111111111111111111111",
        "slotHashesSysvar": "SysvarS1otHashes111111111111111111111111111",
        "vote": {
            "hash": "RgNYwznrTfJZXsPkoWFPzvx4iRPV2GBvjA1LFkyzv9L",
            "slots": [147078734],
            "timestamp": 1657486664,
        },
        "voteAccount": "5ZWgXcyqrrNpQHCme5SdC5hCeYb2o3fEJhF7Gok3bTVN",
        "voteAuthority": "dv1ZAGvdsz5hHLwWXsVnM94hWf1pjbKVau1QVkaMJ92",
    },
    "type": "vote",
}
reveal_type(long_example)
