attempt = 0

while attempt < 3 :
    password = input("Enter password : ")
    attempt += 1

#TODO: Your code here
    if password == "python123" :
        login_successful = "Access granted!"
        attempts_used = attempt
        break
    else :
        print(f"Wrong password. {3 - attempt} attempts remaining.")
        attempts_used = attempt
        
print(login_successful)
print(attempts_used)