# Antivirus scaner for Flowkeeper

There are three things in this repo:

1. A Python script which uploads [Flowkeeper](https://flowkeeper.org) EXE files to [VirusTotal](https://www.virustotal.com/) using its [Python API](https://github.com/VirusTotal/vt-py)
2. Scan results ([all](https://flowkeeper-org.github.io/av-scan/vtscan-results-all.json) and [warnings only](https://flowkeeper-org.github.io/av-scan/vtscan-results-warnings.json)) in JSON format, which are then [hosted](https://flowkeeper-org.github.io/av-scan/) via GitHub Pages, for flowkeeper.org website to consume
3. A GitHub Actions workflow, which runs nightly, downloads the latest Flowkeeper release binaries, and triggers the scan
