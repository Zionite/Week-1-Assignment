print("👋 Hello! Let's get to know you a little better.")

name = input("What’s your name? 😊: ")
age = input("How old are you? 🎂: ")
location = input("Where do you live? 🌍: ")

try:
    age = int(age)
except ValueError:
    print("Hmm... That doesn't look like a number. Setting age to 'unknown'.")
    age = "unknown" 

print("\n--- 🌟 Your Personalized Greeting 🌟 ---")
print(f"Hello, {name.title()}! 👋")
print(f"It's wonderful to know that you're {age} years old and call {location.title()} your home. 🏠")
print("Thank you for sharing a bit about yourself with me! 😊")
print("-----------------------------------------")

print("\nThank you for running this program! Have a fantastic day! 🌞")
