# ARTWITHAMANDA Deployment Migration

# Goal
Restore my Django e-commerce website on a new development machine and migrate it from Heroku to a modern deployment platform.

### Original Deployment

| Component | Service |
|----------|----------|
| Hosting | Heroku |
| Database | ElephantSQL |
| Media Storage | AWS S3 |
| Payments | Stripe |

### New Deployment

| Component | Service |
|----------|----------|
| Hosting | Render |
| Database | Supabase PostgreSQL |
| Media Storage | AWS S3 |
| Payments | Stripe |

### Restoring the Project Locally

The original django project was restored locally first. My project was developed on my old mac book using older Python and Django versions, and I needed to set it up on a new development machine.

Steps completed:

- Cloned the GitHub repository.
- Created and activated a Python virtual environment.
- Installed project dependencies.
- Restored the local environment configuration (`env.py`).

## Dependency Issues

Installing the project dependencies at the beginning failed because the new machine was using Python 3.13, which was incompatible with several older project packages.

### Solution

- Installed Python 3.11.
- Recreated the virtual environment.
- Reinstalled all dependencies successfully.

A second issue occurred because Pillow was not installed, preventing Django from loading `ImageField` models.

This was resolved by installing Pillow and updating the project dependencies.

### Missing Environment Configuration

After installing dependencies, Django failed to start because the `SECRET_KEY` environment variable was not configured on the new machine.

The original environment configuration files wree not in the github repository for securty, so it was copied frpm the old machine.

## Applying Database Migrations

After the project configuration was valid, Django's existing migrations were applied to recreate the database schema.

No database existed initially. Running the migrations recreated all required database tables based on the application's models.

The Django administration interface was then verified to ensure the application was functioning correctly.

## Restoring Initial Data

After applying the migrations, the database was empty. The existing fixture files were used to restore the initial artwork and category data.

```bash
python manage.py loaddata categories
python manage.py loaddata artworks
```

## Reconfiguring AWS S3

The application stores uploaded artwork images using AWS S3. After restoring the project, the existing S3 bucket needed to be reconnected to the new development environment.

Steps completed:

- Recovered access to the original AWS account.
- Generated a new IAM access key and secret access key.
- Updated the local environment configuration with the AWS credentials.
- Verified that media files were successfully served from the existing S3 bucket.

This ensured that all uploaded artwork images remained available without needing to re-upload any files.

## Migrating to Supabase PostgreSQL

The original project used ElephantSQL, which is no longer available.

Steps completed:

- Created a new Supabase PostgreSQL database.
- Updated Django to use the new `DATABASE_URL`.
- Applied database migrations.
- Verified the application connected successfully.

## Deploying to Render

The application was migrated from Heroku to Render.

Steps completed:

- Connected the GitHub repository.
- Configured the Render Web Service.
- Added production environment variables, including the `DATABASE_URL`, AWS credentials, Stripe API keys and Django `SECRET_KEY`.
- Successfully deployed the application.

## Deployment Issues

Render initially attempted to deploy the project using Python 3.14.

Since Django 3.2 depends on Python's deprecated `cgi` module, deployment failed.

This was resolved by configuring the deployment to use Python 3.11, matching the project's development environment.

## Outcome

The application was successfully migrated from Heroku and ElephantSQL to a modern deployment stack using Render, Supabase PostgreSQL, AWS S3 and Stripe.

The project is now fully functional and automatically redeploys whenever changes are pushed to GitHub.