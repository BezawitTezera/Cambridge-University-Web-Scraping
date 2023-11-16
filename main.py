import time
import os
from bs4 import BeautifulSoup
import requests


def clean_directory_name(name, max_length=100):
    # Remove characters that are not allowed in directory names
    invalid_chars = r'\/:*?"<>|'
    cleaned_name = ''.join(c for c in name if c not in invalid_chars)

    # Replace spaces, underscores, and newlines with dashes
    cleaned_name = cleaned_name.replace(" ", "-")
    cleaned_name = cleaned_name.replace("_", "-")
    cleaned_name = cleaned_name.replace("\n", "-")

    # Remove any remaining whitespace and leading/trailing dashes
    cleaned_name = cleaned_name.strip('-')

    # Limit the directory name length
    cleaned_name = cleaned_name[:max_length]

    return cleaned_name


def save_all_to_single_dlc(course_infos, file_path):
    # Combine all course information into a single DLC file
    with open(file_path, 'w') as f:
        f.write(f"DLC Format\n")
        for course_info in course_infos:
            f.write(course_info + "\n")


def find_courses():
    url = 'https://www.cl.cam.ac.uk/teaching/2122/'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        # Find the section containing the course list
        course_section = soup.find('div', class_='campl-column9 campl-main-content')

        # Find all the <li> elements within the course section
        course_items = course_section.find_all('li')

        current_part = None  # Initialize a variable to keep track of the current part
        course_infos_for_current_part = []  # Initialize a list to store course information for each part

        for index, course_item in enumerate(course_items):
            course_text = course_item.get_text().strip()

            # Check if the course item indicates a new part
            if course_text.startswith("Part "):
                # Extract the part name and clean it up
                current_part = course_text.strip()
                current_part = clean_directory_name(current_part)
                current_part_directory = os.path.join("CambridgeCourses", "Part", current_part)
                os.makedirs(current_part_directory, exist_ok=True)

                # Save the combined course information to a single DLC file for the current part
                single_dlc_file_path = os.path.join(current_part_directory, f'Part-{index}.dlc')
                save_all_to_single_dlc(course_infos_for_current_part, single_dlc_file_path)

                # Reset the list for the new part
                course_infos_for_current_part = []
            else:
                # If not a part, save the course information to the current part's directory in CCF format
                ccf_file_path = os.path.join(current_part_directory, f'Course-{index}.ccf')

                # Save in CCF format
                with open(ccf_file_path, 'w') as f:
                    f.write(course_text + "\n")

                # Append to the list of course information for the current part
                course_infos_for_current_part.append(course_text)

        # After the loop, save the last combined course information for the last part
        single_dlc_file_path = os.path.join(current_part_directory, f'Part-{len(course_items)}.dlc')
        save_all_to_single_dlc(course_infos_for_current_part, single_dlc_file_path)

        print("Files Saved")

    else:
        print("Failed to retrieve data from the website. Status code:", response.status_code)


if __name__ == '__main__':
    while True:
        find_courses()
        time_wait = 10
        print(f'Waiting {time_wait} minutes ...')
        time.sleep(time_wait * 60)
