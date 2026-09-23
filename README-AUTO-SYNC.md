# ODLXYZ — synchronisation Blogger → Vercel

Ce dossier automatise la conversion du thème Blogger vers `index.html`.

## Important
Blogger ne pousse pas automatiquement son XML vers GitHub. Pour déclencher la mise à jour,
il faut remplacer `blogger-theme.xml` dans GitHub par le XML exporté depuis Blogger.
Ensuite GitHub Actions génère `index.html` et Vercel redéploie automatiquement.

Le fichier `vercel-shell.html` garde la logique Vercel (feed Blogger, navigation, hiérarchie,
À propos, Contact, PDF, etc.). `blogger-theme.xml` est la source du style Blogger.
