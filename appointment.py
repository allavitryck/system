from datetime import datetime, timedelta

class Appointment:
    def __init__(self, date, time, description):
        self.date = date
        self.time = time
        self.description = description

    def reschedule(self, new_date, new_time):
        self.date = new_date
        self.time = new_time
        print(f"Appointment rescheduled to {new_date} at {new_time}.")

    def __str__(self):
        return f"Date: {self.date}\nTime: {self.time}\nDescription: {self.description}"

class AppointmentScheduler:
    def __init__(self):
        self.appointments = []

    def schedule_appointment(self, appointment):
        self.appointments.append(appointment)
        print(f"Appointment scheduled for {appointment.date} at {appointment.time}.")

    def view_upcoming_appointments(self):
        today = datetime.now()
        print("Upcoming Appointments:")
        for appointment in self.appointments:
            appointment_date = datetime.strptime(appointment.date, "%Y-%m-%d")
            if appointment_date >= today:
                print(appointment)

    def reschedule_appointment(self, index, new_date, new_time):
        if 0 <= index < len(self.appointments):
            appointment = self.appointments[index]
            appointment.reschedule(new_date, new_time)
        else:
            print("Invalid appointment index.")

    def cancel_appointment(self, index):
        if 0 <= index < len(self.appointments):
            canceled_appointment = self.appointments.pop(index)
            print(f"Canceled appointment: {canceled_appointment.date} at {canceled_appointment.time}")
        else:
            print("Invalid appointment index.")

def main():
    appointment_scheduler = AppointmentScheduler()

    while True:
        print("\nAppointment Scheduling Menu:")
        print("1. Schedule Appointment")
        print("2. View Upcoming Appointments")
        print("3. Reschedule Appointment")
        print("4. Cancel Appointment")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter appointment date (YYYY-MM-DD): ")
            time = input("Enter appointment time: ")
            description = input("Enter appointment description: ")
            appointment = Appointment(date, time, description)
            appointment_scheduler.schedule_appointment(appointment)
        elif choice == "2":
            appointment_scheduler.view_upcoming_appointments()
        elif choice == "3":
            index = int(input("Enter the index of the appointment to reschedule: "))
            new_date = input("Enter new appointment date (YYYY-MM-DD): ")
            new_time = input("Enter new appointment time: ")
            appointment_scheduler.reschedule_appointment(index, new_date, new_time)
        elif choice == "4":
            index = int(input("Enter the index of the appointment to cancel: "))
            appointment_scheduler.cancel_appointment(index)
        elif choice == "5":
            print("Exiting the Appointment Scheduling System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
