# GitHub setup · Electronics II amplifier

## Recommended repository metadata

**Repository name:** `Electronics-II-Multistage-Amplifier`

**Description (paste into GitHub → About):**

> Design and LTspice simulation of a two-phase multistage analog amplifier featuring a BJT differential input, current-mirror biasing, Class-AB push-pull output stage, and global negative feedback.

**Topics (paste into GitHub → About → ⚙️ → Topics, one by one):**

`ltspice` · `analog-electronics` · `circuit-simulation` · `amplifier-design` · `multistage-amplifier` · `audio-amplifier` · `bjt` · `push-pull-amplifier` · `negative-feedback` · `sharif-university-of-technology`

On GitHub these are **repository topics**, not Git release tags. Git release tags (such as `v1.0.0`) are optional and should be created only when you want to mark a specific version.

## 1. Create an empty GitHub repository

1. Sign in to GitHub as **AmirAli-jb**.
2. Click **+ → New repository**.
3. Use the repository name above and select **Public** or **Private**.
4. **Do not** initialize it with a README, `.gitignore`, or license. All those files except a license are already in this folder.
5. Click **Create repository**.

## 2. Extract the ZIP on your computer

Extract `Electronics-II-Multistage-Amplifier.zip`. Open **Terminal**, **Git Bash**, or **PowerShell** inside the extracted `Electronics-II-Multistage-Amplifier` folder. Run:

```bash
git --version
git init
git add .
git commit -m "Initial commit: Electronics II amplifier phases I and II"
git branch -M main
git remote add origin https://github.com/AmirAli-jb/Electronics-II-Multistage-Amplifier.git
git push -u origin main
```

If Git reports your identity is not configured, run these first and retry the commit:

```bash
git config --global user.name "AmirAli Jahanbakhshi"
git config --global user.email "YOUR_GITHUB_EMAIL"
```

Replace `YOUR_GITHUB_EMAIL` with the address you actually use for Git commits (or your GitHub-provided noreply email). **Never put a GitHub password or access token into the README or repository.**

If the GitHub repository uses a different name, change the URL in `git remote add origin` accordingly.

GitHub authentication normally opens a login browser through Git Credential Manager. Complete the authentication when prompted.

## 3. Set the GitHub About description and topics

On your repository page, click the small **gear ⚙️** by the **About** section. Paste the description above; add the topics listed above. Save your changes.

## 4. Verify the upload

After a successful push, GitHub should display `README.md` and these folders:

- `phase-1/` and `phase-2/` — original LTspice schematics and reports
- `project-specifications/` — the two assignment PDFs
- `assets/` — schematic previews used in the README
- `scripts/` — reproducible component-cost estimate

The `.gitignore` prevents LTspice-generated `.raw`, `.log` and `.net` files from getting committed automatically; it does **not** ignore the essential `.asc`, `.pdf`, or `.wav` files.

## 5. Updating after future edits

```bash
git status
git add .
git commit -m "Update amplifier documentation"
git push
```

## Before making the repository public

The source PDFs include the student's name and student number. Review them for any information you don't want published. The files have not been redacted or edited.

The recorded performance metrics in `README.md` come from the submitted reports. The exact simulation files were preserved rather than rewritten to reproduce every report test automatically.
