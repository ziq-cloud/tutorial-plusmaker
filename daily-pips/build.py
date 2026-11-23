"""Build index.html (artifact) and standalone.html from src.html + images + gifenc."""
import base64, pathlib
here = pathlib.Path(__file__).parent
src = (here / 'src.html').read_text()
gif = (here.parent / 'performance-card' / 'index.html').read_text()
start = gif.index('/* gifenc 1.0.3'); end = gif.index('</script>', start)
uri = lambda f: 'data:image/jpeg;base64,' + base64.b64encode((here / f).read_bytes()).decode()
out = src.replace('/*GIFENC*/', gif[start:end]).replace('/*PLATE*/', uri('plate.jpg')).replace('/*ICON*/', uri('icon.jpg'))
(here / 'index.html').write_text(out)
(here / 'standalone.html').write_text('<!doctype html>\n<html lang="ms"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"></head><body style="margin:0">\n' + out + '\n</body></html>\n')
