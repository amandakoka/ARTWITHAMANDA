# Testing

Testing is a crucial aspect of the development process for the "Art with Amanda" website. From the start of the project to its completion,  testing was conducted to ensure the functionality, usability, and reliability of the platform. This document outlines the various testing strategies used to deliver a seamless and robust user experience.

## Bugs
### Solved Bugs
|**Num** | **Bug** | **Fix** |
| ----------- | ----------- | ---------- |
| 1 | Image initially located in the static files directory was moved to the media directory for better organization, but the image wasn’t showing up in `index.html`. | Added the media context processor to `settings.py` to ensure `MEDIA_URL` is accessible in templates. Updated the HTML link in `index.html` to use the correct media URL. This change ensures proper display of the image and aligns with best practices for managing media files in Django projects. |
| 2 | `loaddata` command was failing because the JSON file contained incorrect image paths with an extra `media/` prefix. | Removed the `media/` prefix from the `image` field in `artworks.json` to ensure the paths match the `MEDIA_URL` and `MEDIA_ROOT` configuration. Deleted existing data from the database, reimported it and re-ran `python3 manage.py loaddata` to correctly populate the database with the updated paths. |
| 3 | Dropdown menu not showing all 3 options, The dropdown menu only displayed the selected category and did not show “All Categories” or other categories. Users could not switch between different categories, which limited navigation options in the shop. | Updated the artworks.html template to include a link for “All Categories” and iterate over all categories to display them in the dropdown menu. Ensured Bootstrap and jQuery libraries were properly included for dropdown functionality.|