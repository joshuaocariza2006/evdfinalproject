# Lumpiara Website — Event-Driven Programming Project

A responsive website for Lumpiara, a student-friendly lumpia business concept. Built with HTML, CSS, and PyScript. The Python code handles product selection, quantity controls, cart totals, item removal, cart clearing, and order review.

## Files
- `index.html` — landing page, product menu, embedded promo video, and order form
- `styles.css` — responsive design and branding
- `main.py` — PyScript event-driven cart and order review logic
- `assets/` — original Lumpiara logo, food images, and 36-second promo video

## Run locally
PyScript loads Python in the browser and needs an internet connection for its CDN. For best results, run a local web server from this folder:

```bash
python -m http.server 8000
```
Then open `http://localhost:8000`. Do not open the HTML as a `file://` URL.

## GitHub setup
1. Create a **public** repository named `lumpiara-website` on GitHub.
2. Upload these files or run `git init`, `git add .`, and `git commit -m "Build Lumpiara business website"`.
3. Add all group members under **Settings → Collaborators**.
4. Each member should make their own meaningful changes and commits (for example, menu/content, styling, PyScript testing, video, or documentation). Do not share one account or make fake commits.
5. Push updates regularly.

## Before presenting
- Replace placeholder contact information with approved group details.
- Confirm final product prices and flavors with the group. The menu uses sample prices inspired by the business proposal.
- Test PyScript with an internet connection and check the browser console if it does not load.
- The order form is a demo only: it does not save orders to a server, send messages, or process payment.
- The promotional video is 36 seconds and currently silent; your group can add narration or licensed music if required.
