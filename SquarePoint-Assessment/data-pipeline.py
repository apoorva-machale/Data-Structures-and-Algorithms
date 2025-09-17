import io
import os
from datetime import datetime

def parse_file(iostring):
    """
    Parse the custom payroll file format into a list of dicts.
    - Skips lines starting with '#'
    - Reads 'Columns:' metadata for headers
    - Builds list of dictionaries keyed by those headers
    """
    rows = []
    headers = []

    iostring.seek(0)
    for line in iostring:
        line = line.strip()
        if not line:
            continue
        if line.startswith("#"):
            # Pick up headers from Columns: metadata
            if line.lower().startswith("# columns:"):
                cols_str = line.split(":", 1)[1]
                headers = [h.strip() for h in cols_str.split(",")]
            continue

        # actual data line
        fields = [f.strip() for f in line.split(",")]
        if headers and len(fields) < len(headers):
            fields.extend([""] * (len(headers) - len(fields)))
        if headers:
            row = dict(zip(headers, fields))
        else:
            # fallback if no headers line
            row = {str(i): f for i, f in enumerate(fields)}
        rows.append(row)

    return rows


def earned_more_than_30K(data_struct):
    """
    Return the number of employees with salary > 30000.
    """
    count = 0
    for row in data_struct:
        salary_str = row.get("salary", "").replace(",", "").strip()
        try:
            salary = int(salary_str)
            if salary > 30000:
                count += 1
        except ValueError:
            continue  # skip missing/bad salary
    return str(count)   # return string if Hackerrank expects strings


def held_job_longest_in_day(data_struct):
    """
    Return the name of the employee who held their job the longest.
    Uses job_start_date and job_end_date (or today if missing).
    """
    longest_name = ""
    longest_days = -1
    today = datetime.today()

    for row in data_struct:
        start_str = row.get("job_start_date", "").strip()
        end_str = row.get("job_end_date", "").strip()

        try:
            start = datetime.strptime(start_str, "%Y-%m-%d") if start_str else None
        except ValueError:
            start = None
        try:
            end = datetime.strptime(end_str, "%Y-%m-%d") if end_str else today
        except ValueError:
            end = today

        if start is None:
            continue

        days = (end - start).days
        if days > longest_days:
            longest_days = days
            longest_name = row.get("employee_name", "")
    return longest_name


def second_highest_salary(data_struct):
    """
    Return the name of the employee with the second-highest salary.
    """
    salaries = []
    for row in data_struct:
        salary_str = row.get("salary", "").replace(",", "").strip()
        try:
            salary = int(salary_str)
            salaries.append((salary, row.get("employee_name", "")))
        except ValueError:
            continue

    if len(salaries) < 2:
        return ""

    salaries.sort(key=lambda x: x[0], reverse=True)
    highest = salaries[0][0]

    for salary, name in salaries[1:]:
        if salary < highest:
            return name
    return ""

def main():
    """Run locally in VS Code by reading from a file."""
    filename = "datapipeline.txt"  # change if needed
    with open(filename, "r") as infile:
        file_content = infile.read()

    f = io.StringIO(file_content)
    pf = parse_file(f)

    r1 = earned_more_than_30K(pf)
    r2 = held_job_longest_in_day(pf)
    r3 = second_highest_salary(pf)

    print(f"1. How many people have earned more than 30,000? {r1}")
    print(f"2. Who has held their job the longest? {r2}")
    print(f"3. Who has earned the second-highest salary ever? {r3}")


if __name__ == "__main__":
    main()
    
"""
Input
# FileType: employee-salary
# Columns: employee_id,employee_name,job_title,salary,job_start_date,job_end_date
# Types: int,str,str,int,datetime,datetime
41,Alan,Chef,40000,2018-10-29,
52,Brenda,Teacher,30000,,2018-01-13

Output
1. How many people have earned more than 30,000? 1
2. Who has held their job the longest? Alan
3. Who has earned the second-highest salary ever? Brenda

"""

