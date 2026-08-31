def resume_required(func):
    def wrapper(name, resume):
        if resume.lower() == "yes":
            return func(name, resume)
        else:
            print("Application cannot be submitted.")
            print("Please upload your resume first.")

    return wrapper


@resume_required
def apply_job(name, resume):
    print(f"Application submitted successfully for {name}!")


name = input("Enter your name: ")
resume = input("Have you uploaded your resume? (yes/no): ")

apply_job(name, resume)