import random 

def generate_otp():
    otp=""
    for _ in range(4):
        otp=otp+str(random.randint(0,9))
    return otp

def send_otp(phone_number,otp):
    print("OTP sent to {}:{}".format(phone_number,otp))

def verify_otp(input_otp,expected_otp):
    return input_otp==expected_otp

if __name__ == "__main__":
    phone_number="9573276136"
    otp=generate_otp()
    send_otp(phone_number,otp)
    user_input=input("Enter the OTP you received:")
    if verify_otp(user_input,otp):
        print("OTP verification successful!")
    else:
        print("OTP verification failed.")


    
