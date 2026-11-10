"""Publish the owner-supplied Qatalyst HTML without the site's layout or CSS."""
import os
import re

ROUTES = (
    'blogs/qatalyst-algorithm-discovery-for-science',
    'projects/algorithm-discovery-for-science',
)


def publish(root, output):
    source = (root / 'algo-sim-index.html').read_text()
    for route in ROUTES:
        destination = output / route / 'index.html'
        destination.parent.mkdir(parents=True, exist_ok=True)
        # Preserve the standalone document. Only make site-root asset references
        # relative so previews and the existing local-link checker work too.
        def asset(match):
            relative = os.path.relpath(output / match[2].lstrip('/'), destination.parent)
            return match[1] + relative.replace(os.sep, '/') + match[3]
        html = re.sub(r'((?:href|src|srcset)=")(/(?:assets|artifacts)/[^"<>]+)(")', asset, source)
        destination.write_text(html)
