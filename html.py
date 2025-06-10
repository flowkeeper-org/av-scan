import datetime
import os

if __name__ == '__main__':
    print('<h1>VirusTotal scan results for <a href="https://flowkeeper.org">Flowkeeper</a></h1>')
    print('<ul>')
    for f in os.listdir('vt-scan-results'):
        if f.endswith('.json'):
            print(f'<li><a href="vt-scan-results/{f}">{f}</a></li>')
    print('</ul>')
    print(f'<p>Last update: {datetime.datetime.now(tz=datetime.timezone.utc)}</p>')
