min = int(input("Enter the time in  minutes: "))

hours = min // 60
remaining_min = min % 60

print("Original minute: " , min , "minutes")
print("Converted time: " , hours, "hour" , remaining_min , "minutes")