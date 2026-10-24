
seconds = int(input("Seconds: "))

hours = seconds // 3600
remaining_seconds = seconds % 3600

minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"{hours}h {minutes}min {seconds}s")
