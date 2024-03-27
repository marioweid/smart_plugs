/** @type {import('next').NextConfig} */
const nextConfig = {
    output: 'standalone',
    rewrites() {
        return [
            {
                // Das Frontend (also die Applikation die im Browser läuft, darf nicht direkt an das Backend senden)
                // Stattdessen muss ein Proxy im WebServer eingerichtet werden, damit dieser die "Anfragen" vom Server entgegennimmt und selbst den requests senden.
                // Hier ist sichergestellt, dass das Frontend lediglich mit dem Backend kommuniziert, jeder </path> wird zu <backend>/path weitergeleitet
                // Nur Ergebnisse von <backend> dürfen entgegengenommen werden
                // Für mehr Infos kann man sich bischen mehr im Thema CORS einlesen
                // Wenn man in einer Komponente direkt einen request senden möchte, dann würde das über fetch("/api/meine_nice_url") gehen (nicht in den pages in /app/*), da ist SSR
                source:"/api/:path*",
                destination:`http://${process.env.NEXT_PUBLIC_BACKEND_HOST}:${process.env.NEXT_PUBLIC_BACKEND_PORT}/:path*`, // Proxy to Backend
            }
        ]
    }
}

module.exports = nextConfig