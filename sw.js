// This is the Vasantha IT Lab Service Worker
const CACHE_NAME = 'vasantha-lab-v1';

self.addEventListener('install', (event) => {
  console.log('Vasantha Lab Service Worker: Installed');
});

self.addEventListener('activate', (event) => {
  console.log('Vasantha Lab Service Worker: Activated');
});

// This is the part that Play Store requires for "Offline" support
self.addEventListener('fetch', (event) => {
  event.respondWith(
    fetch(event.request).catch(() => {
      return new Response("You are offline, but Vasantha Lab is still here!");
    })
  );
});