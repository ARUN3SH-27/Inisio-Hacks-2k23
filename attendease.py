import tkinter as tk

# Function to calculate attendance percentage based on classes attended
def calculate_attendance_attended():
    total_classes = int(total_classes_entry.get())
    classes_attended = int(classes_attended_entry.get())
    minimum_attendance = int(minimum_attendance_entry.get())

    if total_classes > 0:
        attendance_percentage = (classes_attended / total_classes) * 100
        result_label.config(text=f"Attendance: {attendance_percentage:.2f}%", bg="#FFD1DC")  # Set background to pale pink

        if attendance_percentage >= minimum_attendance:
            status_label.config(text="Safe", bg="#FFD1DC")  # Set background to pale pink
        else:
            classes_needed = (minimum_attendance * total_classes - classes_attended * (100 - minimum_attendance)) / (100 - minimum_attendance)
            status_label.config(text=f"Classes Needed: {int(classes_needed)}", bg="#FFD1DC")  # Set background to pale pink
    else:
        result_label.config(text="Total classes cannot be zero.", bg="#FFD1DC")  # Set background to pale pink
        status_label.config("", bg="#FFD1DC")  # Set background to pale pink

# Function to calculate attendance percentage based on classes missed
def calculate_attendance_missed():
    total_classes = int(total_classes_entry.get())
    classes_missed = int(classes_missed_entry.get())
    minimum_attendance = int(minimum_attendance_entry.get())

    if total_classes > 0 and classes_missed >= 0:
        classes_attended = total_classes - classes_missed
        attendance_percentage = (classes_attended / total_classes) * 100
        result_label.config(text=f"Attendance: {attendance_percentage:.2f}%", bg="#FFD1DC")  # Set background to pale pink

        if attendance_percentage >= minimum_attendance:
            status_label.config(text="Safe", bg="#FFD1DC")  # Set background to pale pink
        else:
            classes_needed = (minimum_attendance * total_classes - classes_attended * (100 - minimum_attendance)) / (100 - minimum_attendance)
            status_label.config(text=f"Classes Needed: {int(classes_needed)}", bg="#FFD1DC")  # Set background to pale pink
    else:
        result_label.config(text="Total classes cannot be zero, and classes missed should be non-negative.", bg="#FFD1DC")  # Set background to pale pink
        status_label.config("", bg="#FFD1DC")  # Set background to pale pink

# Create the main window
window = tk.Tk()
window.title("AttendEase")
window.geometry("400x300")  # Set window dimensions

# Set the background color to pale pink
window.configure(bg="#FFD1DC")  # Hex color code for pale pink

# Label for the title
title_label = tk.Label(window, text="AttendEase", font=("Helvetica", 16), bg="#FFD1DC")
title_label.pack()

# Label and entry for total classes
total_classes_label = tk.Label(window, text="Total Classes:", bg="#FFD1DC")  # Set background to pale pink
total_classes_label.pack()
total_classes_entry = tk.Entry(window, bg="#FFFFE0")  # Set background to pale yellow
total_classes_entry.pack()

# Label and entry for classes attended
classes_attended_label = tk.Label(window, text="Classes Attended:", bg="#FFD1DC")  # Set background to pale pink
classes_attended_label.pack()
classes_attended_entry = tk.Entry(window, bg="#FFFFE0")  # Set background to pale yellow
classes_attended_entry.pack()

# Label and entry for classes missed
classes_missed_label = tk.Label(window, text="Classes Missed:", bg="#FFD1DC")  # Set background to pale pink
classes_missed_label.pack()
classes_missed_entry = tk.Entry(window, bg="#FFFFE0")  # Set background to pale yellow
classes_missed_entry.pack()

# Label for minimum attendance needed
minimum_attendance_label = tk.Label(window, text="Minimum Attendance Needed (%):", bg="#FFD1DC")  # Set background to pale pink
minimum_attendance_label.pack()
minimum_attendance_entry = tk.Entry(window, bg="#FFFFE0")  # Set background to pale yellow
minimum_attendance_entry.pack()

# Buttons to calculate attendance
calculate_attended_button = tk.Button(window, text="Calculate by Attended Classes", command=calculate_attendance_attended, bg="#FFD1DC")  # Set background to pale pink
calculate_attended_button.pack()

calculate_missed_button = tk.Button(window, text="Calculate by Missed Classes", command=calculate_attendance_missed, bg="#FFD1DC")  # Set background to pale pink
calculate_missed_button.pack()

# Labels to display the result and attendance status
result_label = tk.Label(window, text="", bg="#FFD1DC")  # Set background to pale pink
result_label.pack()
status_label = tk.Label(window, text="", bg="#FFD1DC")  # Set background to pale pink
status_label.pack()

# Start the Tkinter main loop
window.mainloop()