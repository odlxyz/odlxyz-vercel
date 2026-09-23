from pathlib import Path
import re
import sys

src = Path(sys.argv[1] if len(sys.argv) > 1 else "blogger-theme.xml")
out = Path(sys.argv[2] if len(sys.argv) > 2 else "index.html")

xml = src.read_text(encoding="utf-8")

# Récupérer le CSS du thème Blogger
start = xml.find("<b:skin><![CDATA[")
end = xml.find("</b:skin>", start)

if start == -1 or end == -1:
    raise SystemExit("Bloc <b:skin> introuvable.")

css = xml[start + len("<b:skin><![CDATA["):end]
css = css.replace("]]>", "").strip()

# Récupérer aussi le bloc <style> placé après b:skin
extra_style = re.search(
    r"</b:skin>\s*<style>(.*?)</style>",
    xml,
    re.S
)

if extra_style:
    css += "\n" + extra_style.group(1)

# Nettoyage de fragments CSS problématiques
css = css.replace(
    "to{transform:translateX(-50%)}}",
    ""
)

css = css.replace(
    "to{transform:translateX(0)}}",
    ""
)

# Le fichier Vercel qui contient toute la logique ODLXYZ
shell = Path("vercel-shell.html")

if not shell.exists():
    raise SystemExit("vercel-shell.html est manquant.")

html = shell.read_text(encoding="utf-8")

# Remplacer automatiquement le CSS par celui du XML Blogger
html = re.sub(
    r'<style id="blogger-theme-css">.*?</style>',
    '<style id="blogger-theme-css">\n'
    + css +
    '\n</style>',
    html,
    count=1,
    flags=re.S
)

out.write_text(html, encoding="utf-8")

print("✅ index.html généré automatiquement")
