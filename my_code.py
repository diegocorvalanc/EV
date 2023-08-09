import json
import argparse
from datetime import datetime

def load_data(file_name):
    student_record = {}  # Dictionary to store student and attendance information
    with open(file_name, "r") as file:
        for n, line in enumerate(file):
            command = line.strip().split() 
            if command[0] == "Student":
                # If the line begins with the command "Student", it registers a new student in the dictionary
                student_name = command[1] 
                student_record[student_name] = {"attendances": []}  
            elif command[0] == "Presence":
                # If the line begins with the command "Pressence", an attendance is recorded for the current student
                student_name = command[1] 
                day = int(command[2]) # Day of attendance in the range of 1 - 7
                try:
                    start_time = parse_time(command[3])
                except ValueError:
                    print(f"Error on line {n+1}: Invalid Start Time")
                    continue
                try:
                    end_time = parse_time(command[4])
                except ValueError:
                    print(f"Error on line {n+1}: Invalid End Time")
                    continue
                student_record[student_name]["attendances"].append((day, start_time, end_time))

    return student_record


def parse_time(time_str):
    valid_time = datetime.strptime(time_str, "%H:%M")
    
    return valid_time


def process_data(student_record):
    # Function that calculates the total minutes and total "single days" of attendance for each student
    result = {}
    for student, student_data in student_record.items():
        attendances = student_data["attendances"]
        total_minutes = 0  # Variable that will store the total minutes of attendance
        unique_days = set()  # Dataset that will store the unique days of attendance
        for item in attendances:
            # All content related to student attendance in variable item
            (day,start_time,end_time,) = item  
            # Function that will calculate and return the total minutes of attendance
            minutes = time_to_minutes(start_time, end_time)
            if day < 1 or day > 7:
                # If "day" is outrangem, the attendance is ignored
                continue
            if minutes is None or minutes < 5:
                # If minutes is less than 5 minutes, the attendance is ignored
                continue
            total_minutes += minutes  
            unique_days.add(day)  # The day is added to the dataset to keep track of "single days"
        result[student] = {"total_minutes": total_minutes, "unique_days": unique_days}

    return result


def report(student_record):
    # Function that prints a report of attendance days and minutes for each student
    for student, student_data in sorted(student_record.items(), key=lambda x: x[1]["total_minutes"], reverse=True): # Sorting from highest to lowest
        total_days = len(student_data["unique_days"])
        total_minutes = student_data["total_minutes"]
        if total_minutes == 0:
            print(f"{student}: {total_minutes} minutes")
        elif total_days == 1:
            print(f"{student}: {total_minutes} minutes in {total_days} day")
        else:
            print(f"{student}: {total_minutes} minutes in {total_days} days")


def time_to_minutes(start_time, end_time):
    
    minutes = ((end_time.hour * 60) + end_time.minute) - ((start_time.hour * 60) + start_time.minute)
        
    return minutes


def store_results(result):
    # Function that stores the results in a JSON file
    for student_data in result.values():
        student_data["unique_days"] = list(student_data["unique_days"])
    with open("output.json","w") as file_output:
        json.dump(result, file_output)
        
        
def parse_arguments():
    # Function that parses the argument typed through the command line
    parser = argparse.ArgumentParser(description='Process input file and generate a report.')
    parser.add_argument('input_file', type=str, help='Path to the input file')
    
    return parser.parse_args()
    

def main():
    # Main Function
    args = parse_arguments()  # Variable that parses the argument typed in the command line
    student_record = load_data(args.input_file)  # Variable that stores in a dictionary the name of students and their attendances
    result = process_data(student_record)  # Variable that processes an dicctionary data returning the total minutes and unique days of attendance in another dicctionary
    report(result)  # Function thar prints a report of attendances day and minutes for each student
    store_results(result)  # Function that stores the results in a JSON file


if __name__ == "__main__":
    main()
