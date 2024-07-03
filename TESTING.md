# Testing

Testing is a crucial aspect of the development process for the "Art with Amanda" website. From the start of the project to its completion,  testing was conducted to ensure the functionality, usability, and reliability of the platform. This document outlines the various testing strategies used to deliver a seamless and robust user experience.

## Bugs
### Solved Bugs
|**Num** | **Bug** | **Fix** |
| ----------- | ----------- | ---------- |
| 1 | Image initially located in the static files directory was moved to the media directory for better organization, but the image wasn’t showing up in `index.html`. | Added the media context processor to `settings.py` to ensure `MEDIA_URL` is accessible in templates. Updated the HTML link in `index.html` to use the correct media URL. This change ensures proper display of the image and aligns with best practices for managing media files in Django projects. |
