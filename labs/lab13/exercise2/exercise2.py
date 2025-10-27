# TODO: Your code here
target = 91
found = False

for number in range(100):
    print(f'Checking number: {number}')
    if number == target:
        found = True
        print(f'Found {target}!')
        break  # Exit loop immediately
    print(f'Still inside loop, checking next...')  # This runs before break

print(f'Search complete. Found: {found}')  # Python jumps here after break
print(found_number)
