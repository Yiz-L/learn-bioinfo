samples = []
samples.append({"id":"S001", "type":"血清", "volume":1.5, "date":"2024-06-01"})
samples.append({"id":"S002", "type":"血浆", "volume":2.0, "date":"2024-06-01"})
samples.append({"id":"S003", "type":"血清", "volume":0.8, "date":"2024-06-01"})
for sample in samples:
    print(sample["id"] + " | " 
          + sample["type"] + " | " 
          + str(sample["volume"]) + "mL | " 
          + sample["date"])
total_volume = 0
for sample in samples:
    total_volume = total_volume + sample["volume"]
print("总体积：" + str(total_volume) + " mL")
