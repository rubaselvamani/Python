

records = [
    "101,Alice,US",
    "102,Bob,UK",
    "INVALID_RECORD",
    "104,John,US"
]

for i,record in enumerate(records,start =1):
    fields = record.split(",") #split keeping the recrds in list
    print(i,fields)

    if len(fields) !=3:
        print(f"Invalid record at line number {i}: {fields}")
