class CareerPage:
    def __init__(self):
        self.job_posts = []
        self.applications = []

    class Admin:
        def __init__(self, career_page):
            self.career_page = career_page

        def add_job_post(self, title, description, requirements):
            job_post = {
                "title": title,
                "description": description,
                "requirements": requirements,
            }
            self.career_page.job_posts.append(job_post)

        def get_application_details(self):
            return self.career_page.applications

    class User:
        def __init__(self, career_page):
            self.career_page = career_page

        def view_job_posts(self):
            return self.career_page.job_posts

        def apply_for_job(self, job_post_index, name, email, resume):
            if 0 <= job_post_index < len(self.career_page.job_posts):
                application = {
                    "job_post": self.career_page.job_posts[job_post_index],
                    "name": name,
                    "email": email,
                    "resume": resume,
                }
                self.career_page.applications.append(application)
                return "Application submitted successfully."
            else:
                return "Invalid job post index. Please choose a valid job post."
career_page = CareerPage()

admin = CareerPage.Admin(career_page)
admin.add_job_post("Software Engineer", "Join our team as a software engineer.", "Bachelor's degree in CS")
admin.add_job_post("Data Analyst", "We are looking for a data analyst to analyze data.", "SQL skills required")

user1 = CareerPage.User(career_page)
user2 = CareerPage.User(career_page)

print("Available Job Posts:")
job_posts = user1.view_job_posts()
for idx, job_post in enumerate(job_posts):
    print(f"{idx + 1}. {job_post['title']}")

user1.apply_for_job(0, "Dixit", "Dixit@example.com", "Resume File")
user2.apply_for_job(1, "Danish", "Danish@example.com", "Resume File")

admin_view = CareerPage.Admin(career_page)
applications = admin_view.get_application_details()
print("\nApplications:")
for idx, application in enumerate(applications):
    print(f"Application {idx + 1}:")
    print(f"Job Post: {application['job_post']['title']}")
    print(f"Applicant Name: {application['name']}")
    print(f"Applicant Email: {application['email']}\n")
