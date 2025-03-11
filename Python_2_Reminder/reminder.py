import time
import json
import datetime
import os
import pygame


REMINDER_FILE = "calendar.json"

def load_reminders():
  if os.path.exists(REMINDER_FILE):
    with open(REMINDER_FILE, "r") as file:
      return json.load(file)
  return{}

def save_reminders(reminders):
  with open(REMINDER_FILE, "w") as file:
    json.dump(reminders, file, indent=4)

def set_reminder():
  reminders = load_reminders()
  today = datetime.date.today()

  print("\n-- Set Medicine Reminder --")
  medicine_name = input("Enter medicine name: ")
  time_to_take = input("Enter reminder time (HH:MM 24-hour format): ")

  for i in range(30):
    day = today + datetime.timedelta(days = i)
    reminders[str(day)] = {
      "medicine": medicine_name,
      "time": time_to_take,
      "status": "Pending"
    }

  save_reminders(reminders)
  print("✅ Medicine reminder set for 30 days!")

def play_alarm():
  print("\n⏰ Time for your medicine! Take your dose!")
  pygame.mixer.init()
  pygame.mixer.music.load("alarm.mp3")
  pygame.mixer.music.play()

  while pygame.mixer.music.get_busy():
    continue

def check_reminder():
  reminders = load_reminders()
  today = str(datetime.date.today())

  if today in reminders and reminders[today]["status"] == "Pending":
    reminder_time = reminders[today]["time"]
    current_time = datetime.datetime.now().strftime("%H:%M")

    if current_time >= reminder_time:
      play_alarm()
      snooze_or_mark_taken(reminders, today)
    else:
      print("🎉 No prnding reminders for today!")

def snooze_or_mark_taken(reminders, today):
  while True:
    action = input("Enter (1) to Mark as Taken, (2) to Snooze: ")
    if action == "1":
      reminders[today]["status"] = "Taken"
      save_reminders(reminders)
      print("✅ Medicine marked as taken. No more reminders today!")
      break
    elif action == "2":
      print("🔔 Snoozed for 5 minutes...")
      time.sleep(300)
      play_alarm()
    else:
      print("Invalid choice, try again.")

def show_calendar():
  reminders = load_reminders()
  today = str(datetime.date.today())

  print("\n-- Reminder Calendar --")
  for date, data in reminders.items():
    status = data["status"]
    day_left = (datetime.datetime.strptime(date, "%Y-%m-%d").date() - datetime.date.today()).days
    print(f"{date} - {data['medicine']} at {data['time']} | status: {status} | Days Left: {day_left}")
  
  print("\n🎯 Days remaining: ", sum(1 for d in reminders if reminders[d]["status"] == "Pending"))


def main():
  while True:
    print("\n Medicine Reminder System")
    print("1️⃣ Set Reminder")
    print("2️⃣ Check Today's Reminder")
    print("3️⃣ Show Calendar")
    print("4️⃣ Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
      set_reminder()
    elif choice == "2":
      check_reminder()
    elif choice == "3":
      show_calendar()
    elif choice == "4":
      print("👋 Exiting...")
      break
    else:
      print("❌ Invalid choice, try again!")

if __name__ == "__main__":
  main()
