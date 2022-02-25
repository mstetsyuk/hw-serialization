SCHEMA = {
  "name": "MyClass",
  "type": "record",
  "namespace": "com.acme.avro",
  "fields": [
    {
      "name": "words",
      "type": "string"
    },
    {
      "name": "list",
      "type": {
        "type": "array",
        "items": "int"
      }
    },
    {
      "name": "dict",
      "type": {
        "name": "dict",
        "type": "record",
        "fields": [
          {
            "name": "0",
            "type": "string"
          },
          {
            "name": "1",
            "type": "string"
          },
          {
            "name": "2",
            "type": "string"
          },
          {
            "name": "3",
            "type": "string"
          },
          {
            "name": "4",
            "type": "string"
          },
          {
            "name": "5",
            "type": "string"
          },
          {
            "name": "6",
            "type": "string"
          },
          {
            "name": "7",
            "type": "string"
          },
          {
            "name": "8",
            "type": "string"
          },
          {
            "name": "9",
            "type": "string"
          },
          {
            "name": "10",
            "type": "string"
          },
          {
            "name": "11",
            "type": "string"
          },
          {
            "name": "12",
            "type": "string"
          },
          {
            "name": "13",
            "type": "string"
          },
          {
            "name": "14",
            "type": "string"
          },
          {
            "name": "15",
            "type": "string"
          },
          {
            "name": "16",
            "type": "string"
          },
          {
            "name": "17",
            "type": "string"
          },
          {
            "name": "18",
            "type": "string"
          },
          {
            "name": "19",
            "type": "string"
          },
          {
            "name": "20",
            "type": "string"
          },
          {
            "name": "21",
            "type": "string"
          },
          {
            "name": "22",
            "type": "string"
          },
          {
            "name": "23",
            "type": "string"
          },
          {
            "name": "24",
            "type": "string"
          },
          {
            "name": "25",
            "type": "string"
          },
          {
            "name": "26",
            "type": "string"
          },
          {
            "name": "27",
            "type": "string"
          },
          {
            "name": "28",
            "type": "string"
          },
          {
            "name": "29",
            "type": "string"
          },
          {
            "name": "30",
            "type": "string"
          },
          {
            "name": "31",
            "type": "string"
          },
          {
            "name": "32",
            "type": "string"
          },
          {
            "name": "33",
            "type": "string"
          },
          {
            "name": "34",
            "type": "string"
          },
          {
            "name": "35",
            "type": "string"
          },
          {
            "name": "36",
            "type": "string"
          },
          {
            "name": "37",
            "type": "string"
          },
          {
            "name": "38",
            "type": "string"
          },
          {
            "name": "39",
            "type": "string"
          },
          {
            "name": "40",
            "type": "string"
          },
          {
            "name": "41",
            "type": "string"
          },
          {
            "name": "42",
            "type": "string"
          },
          {
            "name": "43",
            "type": "string"
          },
          {
            "name": "44",
            "type": "string"
          },
          {
            "name": "45",
            "type": "string"
          },
          {
            "name": "46",
            "type": "string"
          },
          {
            "name": "47",
            "type": "string"
          },
          {
            "name": "48",
            "type": "string"
          },
          {
            "name": "49",
            "type": "string"
          },
          {
            "name": "50",
            "type": "string"
          },
          {
            "name": "51",
            "type": "string"
          },
          {
            "name": "52",
            "type": "string"
          },
          {
            "name": "53",
            "type": "string"
          },
          {
            "name": "54",
            "type": "string"
          },
          {
            "name": "55",
            "type": "string"
          },
          {
            "name": "56",
            "type": "string"
          },
          {
            "name": "57",
            "type": "string"
          },
          {
            "name": "58",
            "type": "string"
          },
          {
            "name": "59",
            "type": "string"
          },
          {
            "name": "60",
            "type": "string"
          },
          {
            "name": "61",
            "type": "string"
          },
          {
            "name": "62",
            "type": "string"
          },
          {
            "name": "63",
            "type": "string"
          },
          {
            "name": "64",
            "type": "string"
          },
          {
            "name": "65",
            "type": "string"
          },
          {
            "name": "66",
            "type": "string"
          },
          {
            "name": "67",
            "type": "string"
          },
          {
            "name": "68",
            "type": "string"
          },
          {
            "name": "69",
            "type": "string"
          },
          {
            "name": "70",
            "type": "string"
          },
          {
            "name": "71",
            "type": "string"
          },
          {
            "name": "72",
            "type": "string"
          },
          {
            "name": "73",
            "type": "string"
          },
          {
            "name": "74",
            "type": "string"
          },
          {
            "name": "75",
            "type": "string"
          },
          {
            "name": "76",
            "type": "string"
          },
          {
            "name": "77",
            "type": "string"
          },
          {
            "name": "78",
            "type": "string"
          },
          {
            "name": "79",
            "type": "string"
          },
          {
            "name": "80",
            "type": "string"
          },
          {
            "name": "81",
            "type": "string"
          },
          {
            "name": "82",
            "type": "string"
          },
          {
            "name": "83",
            "type": "string"
          },
          {
            "name": "84",
            "type": "string"
          },
          {
            "name": "85",
            "type": "string"
          },
          {
            "name": "86",
            "type": "string"
          },
          {
            "name": "87",
            "type": "string"
          },
          {
            "name": "88",
            "type": "string"
          },
          {
            "name": "89",
            "type": "string"
          },
          {
            "name": "90",
            "type": "string"
          },
          {
            "name": "91",
            "type": "string"
          },
          {
            "name": "92",
            "type": "string"
          },
          {
            "name": "93",
            "type": "string"
          },
          {
            "name": "94",
            "type": "string"
          },
          {
            "name": "95",
            "type": "string"
          },
          {
            "name": "96",
            "type": "string"
          },
          {
            "name": "97",
            "type": "string"
          },
          {
            "name": "98",
            "type": "string"
          },
          {
            "name": "99",
            "type": "string"
          }
        ]
      }
    },
    {
      "name": "int",
      "type": "int"
    },
    {
      "name": "float",
      "type": "float"
    }
  ]
}