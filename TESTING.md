# Testing

Testing is a crucial aspect of the development process for the "Art with Amanda" website. From the start of the project to its completion,  testing was conducted to ensure the functionality, usability, and reliability of the platform. This document outlines the various testing strategies used to deliver a seamless and robust user experience.

## Bugs
### Solved Bugs
|**Num** | **Bug** | **Fix** |
| ----------- | ----------- | ---------- |
| 1 | Image initially located in the static files directory was moved to the media directory for better organization, but the image wasn’t showing up in `index.html`. | Added the media context processor to `settings.py` to ensure `MEDIA_URL` is accessible in templates. Updated the HTML link in `index.html` to use the correct media URL. This change ensures proper display of the image and aligns with best practices for managing media files in Django projects. |
| 2 | `loaddata` command was failing because the JSON file contained incorrect image paths with an extra `media/` prefix. | Removed the `media/` prefix from the `image` field in `artworks.json` to ensure the paths match the `MEDIA_URL` and `MEDIA_ROOT` configuration. Deleted existing data from the database, reimported it and re-ran `python3 manage.py loaddata` to correctly populate the database with the updated paths. |
| 3 | Dropdown menu not showing all 3 options, The dropdown menu only displayed the selected category and did not show “All Categories” or other categories. Users could not switch between different categories, which limited navigation options in the shop. | Updated the artworks.html template to include a link for “All Categories” and iterate over all categories to display them in the dropdown menu. Ensured Bootstrap and jQuery libraries were properly included for dropdown functionality.|
| 4 | Dropdown menu showed all selected categories instead of only the current category when changing filters. | Updated artworks.html template to show only the selected category and added “All Categories” option to clear the current filter. Applied CSS to highlight the active dropdown item with a light grey background. |
| 5 | “Back to Home” Button Moves Up on Smaller Screens so it's not aligned with the categories button | Resolved by updating the Bootstrap classes used for the “Back to Home” button and the categories button. Adjusted the CSS classes to ensure consistent alignment across different screen sizes. |
| 6 | Incorrect location for bag.html template. Forgot to create a bag folder in the templates directory and initially placed bag.html in the wrong directory. |Created a bag folder within the templates directory and moved bag.html into it to ensure the bag page loads the correct template. |
| 7 | Quantity buttons for incrementing and decrementing were not functioning due to the missing {% block postloadjs %} in base.html, which prevented the inclusion of the JavaScript file responsible for these actions. | Added the {% block postloadjs %}{% endblock %} section to base.html to ensure that the quantity_script.js JavaScript file is included in the template. This fix resolved the issue with the quantity buttons not functioning by ensuring that the JavaScript code for handling button clicks was properly loaded.|
| 8 | The remove button on artworks in the bag doesn't work when clicked, which prevents a user from removing an unwanted item from their bag.|   |

### Deployment Bug

**Bug Encountered During Deployment:**

During deployment, the application failed to build correctly when pushing to Heroku due to version incompatibility issues. The deployment process resulted in build failures because certain package versions were not compatible with each other or with the Heroku environment.

**Troubleshooting Steps:**

1. **Issue Identification:**
   - The build failed with errors related to version incompatibilities between packages.

2. **Initial Troubleshooting:**
   - Attempted to resolve the issue by debugging and changing package versions but did not achieve a successful build.

3. **Seeking Support:**
   - Contacted the Code Institute tutor for support, which provided guidance on resolving the issue.

4. **Solution:**
   - **Adjusted Package Versions:**
     - Set `setuptools` to version `58.0.4`.
     - Updated `Django Allauth` to version `0.50.0`.
   - **Created `runtime.txt`:**
     - Added a `runtime.txt` file to specify the Python version as `python-3.10.14`.
   - **Added `env.py`:**
     - Created an `env.py` file to securely store the secret key.

5. **Final Deployment:**
   - With the correct package versions and configurations in place, redeployed the application successfully.

**Resolution:** After making the necessary adjustments to package versions and configurations, the build process completed successfully, and the application was deployed without issues.

### Additional Updates

**Runtime File:**

- **`runtime.txt`:** Created a `runtime.txt` file in the root directory to specify the Python version to be used in the Heroku environment. This file includes:
  ```plaintext
  python-3.10.14
