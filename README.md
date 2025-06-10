# Antivirus scaner for Flowkeeper

There are three things in this repo:

1. A Python script which uploads Flowkeeper EXE files to VirusTotal using its API
2. Scan results in JSON format, which are then hosted via GitHub Pages, for flowkeeper.org website to consume
3. A GitHub Actions workflow, which runs nightly, downloads the latest Flowkeeper release binaries, and triggers the scan
