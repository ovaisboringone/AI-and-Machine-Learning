log1_events = ["A101", "B202", "C303", "A101", "D404"]
log2_events = {"C303", "E505", "F606", "B202"}

log1_events = set(log1_events)

print("Unique events:", log1_events)
print("Common events:", log1_events.intersection(log2_events))
print("All events:", log1_events.union(log2_events))