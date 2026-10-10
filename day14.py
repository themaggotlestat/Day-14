careers = [
    {"career": "Software Engineer", "salary": 30, "remote": True},
    {"career": "Cybersecurity", "salary": 25, "remote": True},
    {"career": "Web Developer", "salary": 20, "remote": True},
    {"career": "IT Support", "salary": 18, "remote": False}
]

def find_high_paying_jobs(job_list, minimum_salary):
    matching_jobs = []

    for job in job_list:
        if job["salary"] >= minimum_salary:
            matching_jobs.append(job)

    return matching_jobs

minimum_salary = int(input("What is your minimum salary? "))

results = find_high_paying_jobs(careers, minimum_salary)

print(results)

def find_remote_jobs(job_list):
    matching_jobs = []

    for job in job_list:
        if job["remote"]:
            matching_jobs.append(job)

    return matching_jobs

remote_results = find_remote_jobs(careers)

print(f'This is a list of remote careers:\n{remote_results}')