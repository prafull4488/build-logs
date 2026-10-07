#!/usr/bin/env python3
"""Single source for build-logs: generates README.md files and projects.json."""
import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))

PROJECTS = [
 {
  "slug": "garage-os",
  "name": "Garage OS",
  "tagline": "An operating system for a motorcycle service centre",
  "kind": "build",
  "role": "Designed and built (AI-assisted development)",
  "status": "Live, building module by module",
  "problem": "Getting a motorcycle serviced in India usually means no appointment, no clear price and half a day lost at the garage. Inside the garage, work moves through reception, the manager, mechanics, washing and quality checks, and paper and memory lose track of it. Customers lose trust when extra work appears on the bill without being approved first.",
  "planned": [
   "Map the full service lifecycle first: booking, check-in, inspection, estimate, customer approval, service, wash, quality check, payment, delivery, follow-up.",
   "Start with one in-house garage, but structure data so more garages can be added later.",
   "Give managers and mechanics separate experiences: a full manager app, and a mobile-first app that shows a mechanic only their own jobs.",
   "Build one module at a time, each with an explicit list of what not to build yet."
  ],
  "architecture": "flowchart LR\n  M[Manager app] --> FE[React + TypeScript SPA on Netlify]\n  K[Mechanic app, mobile-first] --> FE\n  FE --> AUTH[Supabase Auth: manager / mechanic roles]\n  FE --> DB[(Postgres with row-level security)]\n  FE --> RT[Realtime: live workshop board]\n  FE --> EF[Edge Function: privileged account creation]",
  "architecture_note": "No custom backend server. The apps talk to Supabase directly with the public key only; data access is enforced in the database.",
  "tech": ["React", "TypeScript", "Vite", "Tailwind CSS", "React Router", "Supabase (Postgres, Auth, RLS, Realtime, Edge Functions)", "Netlify"],
  "ai": [
   "Every module was scoped as a separate task with Claude: inspect the current schema and code first, report findings, then build the smallest usable increment.",
   "Claude wrote most of the code and migrations; I set the product rules, the scope of each task and the house rules, and reviewed and deployed each step.",
   "A running docs pack (overview, business context, architecture, schema, flows, decisions, roadmap) keeps each new AI session up to speed."
  ],
  "decisions": [
   ["Security in the database, not the front end", "Row-level security isolates each garage; mechanics can only reach their own job rows. The service key never ships to the browser; the one privileged action runs in an Edge Function."],
   ["Additive-only migrations", "Every schema change adds and is safe to re-run, so nothing already live breaks."],
   ["Two experiences, one platform", "Mechanics never see revenue, reports or settings, only their jobs and a way to request approval for extra work."],
   ["Reuse before new tables", "Approval requests extend the existing issues table instead of a parallel structure."],
   ["A small, fixed service catalogue", "Thirteen services that match how the garage works, instead of a configurable catalogue nobody would maintain."]
  ],
  "learned": [
   "Scope discipline is what makes AI-assisted building work: each task says what not to build, so the code stays small and reviewable.",
   "Write down judgement calls as you make them; the decisions log saved re-discovering why two similar tables both exist.",
   "Delivering changes as archives over a Git checkout can leave deleted files behind; always check git status after applying a drop."
  ],
  "demo": [{"label": "Live app (sign-in required)", "url": "https://bookamech.netlify.app"}],
  "repo": {"visibility": "private", "note": "Code is private; activity is summarised below."},
  "milestones": [
   ["09-08-2026", "First version deployed on Netlify"],
   ["30-08-2026", "Editable digital job cart"],
   ["31-08-2026", "Mechanic dashboard"]
  ],
  "activity_source": "bookamech",
  "screenshots": []
 },
 {
  "slug": "studio-planner",
  "name": "Azumi Studio Planner",
  "tagline": "A studio operating system for an interior design practice",
  "kind": "build",
  "role": "Designed and built (AI-assisted development)",
  "status": "Live, in daily use",
  "problem": "An interior design studio was running projects across chats, spreadsheets and notes. Client onboarding was different every time, budgets were tracked separately from scope, and clients had no simple way to see progress.",
  "planned": [
   "One secure web app that runs a project from first enquiry to handover.",
   "Standardise onboarding: discovery brief, room-by-room scope, clauses, budget and a first-meeting checklist.",
   "Keep it a single file with no build step, so it is easy to change and deploy.",
   "Give clients a read-only view of exactly what the studio chooses to share."
  ],
  "architecture": "flowchart LR\n  U[Studio staff] --> APP[Single-file HTML/JS app on Netlify]\n  C[Client] --> CV[Read-only client view]\n  APP --> LS[(Browser storage, offline first)]\n  APP -. sync .-> SB[(Supabase Postgres with RLS)]\n  APP --> AUTH[Supabase Auth: admin / editor / viewer / client]\n  APP --> EF[Edge Function: client invites]\n  S[Client survey page] --> NF[Netlify Forms, emailed to the studio]",
  "architecture_note": "Offline first, synced to Supabase. Keys are injected from host environment variables at build time; the public key has no data access on its own.",
  "tech": ["HTML, CSS and JavaScript (single file, no framework)", "Supabase (Postgres, Auth, RLS, Edge Functions)", "Netlify (hosting, Forms)", "Playwright (release checks)"],
  "ai": [
   "Claude handled planning, code and tests across the redesign, delivered in four phases.",
   "Every release was checked headless with Playwright at desktop and 375 px before deploying.",
   "A docs pack (overview, architecture, data model, flows, issues, changelog, design system) carries context between AI sessions."
  ],
  "decisions": [
   ["Single file, no build step", "Fast to change and deploy; the whole app is one reviewable file."],
   ["Roles enforced with row-level security", "Admin, editor, viewer and client roles; the public key alone cannot read any data."],
   ["Admin key never in the browser", "Creating client accounts and invite links runs in an Edge Function."],
   ["One room list per project", "Scope and checklist share the same rooms, so renaming or removing a room updates both."]
  ],
  "learned": [
   "Lock down data access before adding features; adding logins and RLS early changed the shape of every later screen.",
   "Phased redesigns keep a live tool usable while it changes.",
   "Single-file apps are fast to ship, but user input needs escaping everywhere, not only on new screens."
  ],
  "demo": [{"label": "Live app (sign-in required)", "url": "https://soft-lokum-c2858d.netlify.app/"}],
  "repo": {"visibility": "private", "note": "Code is private; activity is summarised below."},
  "milestones": [
   ["10-06-2026", "First version with Supabase sync"],
   ["04-10-2026", "Logins, roles and row-level security"],
   ["04-10-2026", "Client view and invites"],
   ["04-10-2026", "Redesign phases 1 to 4"],
   ["05-10-2026", "Client summary charts, budget tab and survey email"]
  ],
  "activity_source": "studio-planner",
  "screenshots": [
   {"file": "screenshots/studio-planner-dashboard.png", "caption": "Dashboard (sample data)"},
   {"file": "screenshots/studio-planner-projects.png", "caption": "Projects (sample data)"}
  ]
 },
 {
  "slug": "azumi-website",
  "name": "Azumi Designs website",
  "tagline": "A public website with a built-in CMS for an interior design studio",
  "kind": "build",
  "role": "Designed and built (AI-assisted development)",
  "status": "Live",
  "problem": "The studio's old site was hard to update and did little to turn visitors into enquiries. The studio needed to publish projects and articles without a developer, keep search rankings from the old URLs, and see where enquiries came from.",
  "planned": [
   "A section-based site the studio can edit itself through a private admin console.",
   "Server-side SEO, so titles, canonicals and redirects work without a heavy server.",
   "Lead capture across form, WhatsApp, phone and email, with the source of every enquiry."
  ],
  "architecture": "flowchart LR\n  V[Visitor] --> E[Edge Function: SEO, redirects, 404]\n  E --> S[React SPA on Netlify]\n  S --> API[Netlify Function API]\n  A[Admin console] --> API\n  API --> B[(Netlify Blobs: content, images, revisions)]\n  S --> F[Netlify Forms]",
  "architecture_note": "Content is one JSON document with the last 30 revisions, so every save is atomic and any change can be undone.",
  "tech": ["React", "Vite", "Tailwind CSS", "Netlify Functions", "Netlify Edge Functions", "Netlify Blobs", "Netlify Forms"],
  "ai": [
   "Built with AI-assisted development: planning, code and documentation, including an operations runbook and a decisions log."
  ],
  "decisions": [
   ["Netlify Blobs instead of a database", "The site is small; Blobs needs no extra service and survives deploys."],
   ["One content document with revisions", "Atomic saves and easy undo."],
   ["Edge Function for SEO", "Real titles, canonical URLs, 301s and 404 status without server-side rendering."],
   ["Optimistic concurrency", "Two editors cannot overwrite each other's changes."]
  ],
  "learned": [
   "Plan redirects from the old site before launch; search traffic depends on it.",
   "A small site still benefits from revisions and conflict checks once non-developers edit it."
  ],
  "demo": [{"label": "azumidesigns.co.in", "url": "https://azumidesigns.co.in"}],
  "repo": {"visibility": "private", "note": "Code is private; activity is summarised below."},
  "milestones": [
   ["30-08-2026", "First website"],
   ["03-10-2026", "Redesign with admin console and CMS backend"],
   ["03-10-2026", "Project pages, redirects from the old site, lead tracking"]
  ],
  "activity_source": "azumi-website",
  "screenshots": []
 },
 {
  "slug": "autodocbg",
  "name": "AutoDocBG",
  "tagline": "Vehicle inspection booking platform for Bulgaria",
  "kind": "collaboration",
  "role": "Product collaboration",
  "status": "Pre-launch",
  "problem": "AutoDocBG is a friends' venture. I helped shape it from a problem I'd experienced first-hand while living in Bulgaria into a launch-ready product — defining what it should do, how users should move through it, how the platform should be structured, and how it should be taken to launch.",
  "agency_note": "The website and apps were developed by an external agency.",
  "journey": ["Problem", "Concept", "Features", "User flows", "Platform structure", "Website & app", "App Store approval", "Pre-launch"],
  "table": [
   ["Status", "iOS approved on the App Store · Android in Google Play review · Pre-launch"],
   ["Ownership", "Friends' venture"],
   ["My role", "Product shaping: features, user flows, platform structure, launch planning"],
   ["Development", "External agency"]
  ],
  "screenshots": []
 },
 {
  "slug": "portfolio",
  "name": "This portfolio",
  "tagline": "A personal site built from an interview, not a template",
  "kind": "build",
  "role": "Designed and built (AI-assisted development)",
  "status": "Live",
  "problem": "A CV-style page listed what I had done but not how I think. I wanted a site that shows the engineering first and the person behind it second, without reading like a job-hunting profile.",
  "planned": [
   "Start with an interview, not a layout: what should a visitor remember, and what should they not assume.",
   "Separate what I engineered from what I helped shape, and say so on every project.",
   "Keep project detail in this public repo, so the site and the logs never drift apart."
  ],
  "architecture": "flowchart LR\n  P[Private working repo] -->|curated by hand| BL[Public build-logs repo]\n  BL --> J[projects.json]\n  J --> SITE[Static site on Vercel]\n  SITE --> V[Visitor]",
  "architecture_note": "Static HTML with no framework. Project pages read projects.json from this repo, with a built-in copy as a fallback.",
  "tech": ["HTML, CSS, JavaScript", "WebGL", "Vercel", "GitHub"],
  "ai": [
   "Claude ran the narrative interview, drafted the structure and copy for review, and built the pages.",
   "Every claim on the site was checked against the project docs; anything unverified was flagged for me to confirm."
  ],
  "decisions": [
   ["Interview before design", "The site's story came from answers, not from portfolio conventions."],
   ["Role tags on every project", "Engineered work and product collaborations are labelled differently, without ranking them."],
   ["Public logs, private code", "Private repos stay private; only curated summaries and commit counts are published."]
  ],
  "learned": [
   "Deciding what stays private is as important as deciding what to show."
  ],
  "demo": [{"label": "prafull-patil.vercel.app", "url": "https://prafull-patil.vercel.app"}],
  "repo": {"visibility": "public", "url": "https://github.com/prafull4488/build-logs", "note": "Project logs are public in this repo."},
  "milestones": [
   ["04-10-2026", "Deployed on Vercel from Git"],
   ["05-10-2026", "Narrative interview and redesign"]
  ],
  "activity_source": "portfolio",
  "screenshots": []
 },
 {
  "slug": "ai-ops-lab",
  "name": "AI operations lab",
  "tagline": "Local-first model routing and agents for infrastructure work",
  "kind": "build",
  "role": "Designed and built",
  "status": "Ongoing",
  "problem": "I wanted to use LLM agents for monitoring, RCA and automation without sending everything to paid APIs by default, and to understand model serving and routing hands-on.",
  "planned": [
   "Route every model call through one local gateway, with local models first and paid APIs only as a fallback.",
   "Build agents and workflows for infrastructure monitoring and automation on top of it."
  ],
  "architecture": "flowchart LR\n  A[Agents and scripts] --> R[Local router: OmniRoute]\n  R --> L[Local models: Ollama]\n  R -. fallback .-> C[Paid APIs]",
  "architecture_note": "OpenAI-compatible gateway on the local machine.",
  "tech": ["OmniRoute", "Ollama", "Claude", "Cursor", "MCP"],
  "ai": ["This project is the AI work itself: routing, local inference and agents."],
  "decisions": [["Local first", "Cost and privacy: local models handle what they can, paid APIs only when needed."]],
  "learned": [],
  "demo": [],
  "repo": {"visibility": "none", "note": "No public repo yet."},
  "milestones": [],
  "activity_source": None,
  "screenshots": []
 }
]

ACTIVITY = {
 "bookamech": {"2026-08-09": 4, "2026-08-10": 3, "2026-08-15": 2, "2026-08-30": 4, "2026-08-31": 1},
 "studio-planner": {"2026-06-10": 4, "2026-06-13": 5, "2026-06-20": 1, "2026-06-21": 2, "2026-10-04": 12},
 "azumi-website": {"2026-08-30": 4, "2026-08-31": 4, "2026-09-10": 5, "2026-10-03": 3},
 "portfolio": {"2026-10-04": 4}
}

def md(p):
    L = [f"# {p['name']}", "", f"**{p['tagline']}**", "",
         f"Role: {p['role']} · Status: {p['status']}", ""]
    if p["kind"] == "collaboration":
        L += [p["problem"], "", p["agency_note"], "", "**" + " → ".join(p["journey"]) + "**", "",
              "| | |", "|---|---|"] + [f"| **{a}** | {b} |" for a, b in p["table"]] + [""]
        return "\n".join(L)
    act = ACTIVITY.get(p.get("activity_source") or "", {})
    L += ["## The problem", "", p["problem"], "",
          "## What I planned", ""] + [f"- {x}" for x in p["planned"]] + ["",
          "## Architecture", "", "```mermaid", p["architecture"], "```", "", p["architecture_note"], "",
          "## Technologies", "", ", ".join(p["tech"]), "",
          "## How AI was used", ""] + [f"- {x}" for x in p["ai"]] + ["",
          "## Key decisions", "", "| Decision | Why |", "|---|---|"] + [f"| {a} | {b} |" for a, b in p["decisions"]] + [""]
    L += ["## What I learned", ""] + ([f"- {x}" for x in p["learned"]] or ["Still in progress."]) + [""]
    L += ["## Demo", ""] + ([f"- [{d['label']}]({d['url']})" for d in p["demo"]] or ["No public demo yet."]) + [""]
    r = p["repo"]
    L += ["## GitHub repo", "", (f"[{r['url']}]({r['url']})" if r.get("url") else r["note"]), ""]
    L += ["## Activity", ""]
    if act:
        L += [f"{sum(act.values())} commits across {len(act)} active days, {min(act)} to {max(act)} (counts only; commit messages stay private).", ""]
    if p["milestones"]:
        L += ["| Date | Milestone |", "|---|---|"] + [f"| {d} | {m} |" for d, m in p["milestones"]] + [""]
    if not act and not p["milestones"]:
        L += ["Not tracked yet.", ""]
    if p["screenshots"]:
        L += ["## Screenshots", ""] + [f"![{s['caption']}]({s['file']})" for s in p["screenshots"]] + [""]
    L += ["## Status", "", p["status"], ""]
    return "\n".join(L)

def main(out):
    os.makedirs(out, exist_ok=True)
    for p in PROJECTS:
        d = os.path.join(out, "projects", p["slug"]); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "README.md"), "w").write(md(p))
    data = {"updated": "05-10-2026", "projects": PROJECTS, "activity": ACTIVITY}
    json.dump(data, open(os.path.join(out, "projects.json"), "w"), indent=1, ensure_ascii=False)
    rows = "\n".join(f"| [{p['name']}](projects/{p['slug']}/) | {p['tagline']} | {p['role']} | {p['status']} |" for p in PROJECTS)
    open(os.path.join(out, "README.md"), "w").write(f"""# Build logs

Curated logs of what I build outside my day job, by Prafull Patil, platform and DevOps architect.
Portfolio: [prafull-patil.vercel.app](https://prafull-patil.vercel.app)

Each log covers the problem, what I planned, the architecture, technologies, how AI was used, key decisions, what I learned, demo links, repo, activity and status.

| Project | What it is | My role | Status |
|---|---|---|---|
{rows}

## How to read the roles
- **Designed and built (AI-assisted development):** I defined the product, made the technical decisions and shipped it, with AI writing much of the code under my direction.
- **Product collaboration:** I shaped the product; others own it and built it.

## What is not here
Source code for private projects, client names and data, budgets, credentials, and anything from my employer. Activity for private repos is shown as commit counts and milestones only.

`projects.json` holds the same content in machine-readable form; the portfolio site reads it.
""")

if __name__ == "__main__":
    import sys
    main(sys.argv[1] if len(sys.argv) > 1 else ROOT)
