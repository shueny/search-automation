from scripts.google_search import google_search
from scripts.career_page import find_career_page, search_for_job

company_list = ["Company A", "Company B", "Company C"]
target_job = "Frontend Engineer"

for company in company_list:
    site_url = google_search(company)
    if site_url:
        career_page = find_career_page(site_url)
        if career_page:
            result = search_for_job(career_page, target_job)
            print(f"Result for {company}: {result}")
        else:
            print(f"No career page found for {company}")
    else:
        print(f"No relevant site found for {company}")
