# Tables

Tables is a starter web project for businesses to upload Excel files and quickly generate data visualizations.

## What this project does

- Accepts `.xlsx` / `.xls` uploads
- Supports selecting a sheet from a workbook
- Shows a data preview
- Builds charts (Bar, Line, Scatter, Histogram)
- Exports cleaned chart data as CSV

## Quick start (local)

```bash
cd tables
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Open your browser at `http://localhost:8501`

Tip: the app now starts with **demo data enabled** so you can instantly see charts even before uploading an Excel file.

---

## How to go live

You can deploy this app quickly using either **Streamlit Community Cloud** (easiest) or **Render/Railway/Fly.io** with Docker.

### Option A: Streamlit Community Cloud (fastest)

1. Push this repository to GitHub.
2. Go to <https://share.streamlit.io/> and sign in with GitHub.
3. Click **New app**.
4. Select:
   - Repository: your repo
   - Branch: main (or your deployment branch)
   - Main file path: `tables/app.py`
5. Click **Deploy**.

Notes:
- `tables/requirements.txt` is automatically used for dependencies.
- If you later add secrets (database/API keys), set them in Streamlit app settings.

### Option B: Docker deployment (Render, Railway, Fly.io, any VPS)

This project includes a ready `Dockerfile`.

Build and run locally first:

```bash
cd tables
docker build -t tables-app .
docker run -p 8501:8501 tables-app
```

Then deploy the same image to your platform.

#### Render (example)

1. Create a **Web Service** from your GitHub repo.
2. Choose **Docker** environment.
3. Set root directory to `tables`.
4. Expose port `8501`.
5. Deploy.


### Option C: Vercel (important limitation)

Vercel is optimized for **frontend apps** and **serverless functions**.
A Streamlit app needs a long-running Python web server, so it is **not a good direct fit** for Vercel hosting.

If you still want to use Vercel in your stack:

1. Deploy the Streamlit app to **Render/Railway/Fly.io/Streamlit Cloud**.
2. Use Vercel for a marketing site or dashboard shell (Next.js).
3. Link users from Vercel frontend to your Streamlit app URL.

If your goal is “single-platform deployment”, prefer **Render** or **Railway** for this Python/Streamlit project.

If you want Vercel anyway, this repo now includes a static frontend at `vercel-landing/` you can deploy directly on Vercel and point to your Streamlit backend URL.

---

## Production checklist (important)

Before sharing with real customers, do these first:

1. **Authentication**: restrict access per business account.
2. **Storage**: save uploaded files in object storage (S3/GCS) instead of local disk.
3. **Validation rules**: enforce expected columns and data types.
4. **Upload limits**: set file-size and row limits to avoid crashes.
5. **Async processing**: process large workbooks in background jobs.
6. **Observability**: add logging, error tracking, and metrics.
7. **Security**: encrypt data at rest and in transit; define retention policies.

---

## Suggested next features

1. **Authentication and organization workspaces**
   - Let each business keep private datasets and dashboards.
2. **Reusable dashboard templates**
   - Save chart settings and apply to future uploads.
3. **Data quality rules**
   - Validate columns, date formats, currencies, and missing values before charting.
4. **Scheduled ingestion**
   - Pull files from Google Drive, S3, or email automatically.
5. **Natural language insights**
   - Add AI summaries like “Top 3 regions by growth this month.”
6. **Role-based access**
   - Different access for owners, analysts, and viewers.

## Key problems to plan for

1. **Messy Excel files**
   - Real files include merged cells, multiple headers, and inconsistent schemas.
2. **Scalability**
   - Large files can be slow and memory-heavy; add size limits and background processing.
3. **Security and compliance**
   - Business data is sensitive. Use encryption, retention policies, and audit logs.
4. **Data correctness trust**
   - If charts are wrong due to parsing assumptions, users lose confidence quickly.
5. **Multi-tenant isolation**
   - Ensure one company cannot access another company’s files or dashboards.
6. **Versioning and reproducibility**
   - Uploaded data changes over time; keep versions so reports are explainable later.
