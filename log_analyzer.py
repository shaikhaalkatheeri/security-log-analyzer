file = open("sample-logs.txt", "r")

logs = file.readlines()

file.close()

print("Total log entries:", len(logs))
