# Vercel Landing (Static)

This folder is a Vercel-ready static frontend for your Tables product.

## Deploy on Vercel

1. Push repo to GitHub.
2. In Vercel, click **Add New > Project** and import the repo.
3. Set **Root Directory** to `vercel-landing`.
4. Framework preset: **Other**.
5. Deploy.

## Important

Before deploying, edit `index.html` and replace:

- `https://YOUR-STREAMLIT-URL.streamlit.app`

with your actual live Streamlit URL.

## Why this approach

Vercel is ideal for frontend/static apps. Streamlit runs better on platforms with long-running Python services.
Use Vercel for landing/dashboard shell + Streamlit hosting for the data app.
