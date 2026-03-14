const CACHE = 'chichi-v1';

// Core files to cache for offline / fast load
const CORE = [
  './',
  './index.html',
  './manifest.json',
  './assets/index-CEMZM_Ao.js',
  './assets/index-rege5v42.css',
  './launchicon.jpg',
  './launchicon_transparent.png',
  './c1.png', './g1.png', './g2.png',
  './l1.png', './m1.png', './r1.png',
  './sfx_c1.mp3', './sfx_g1.mp3', './sfx_g2.mp3',
  './sfx_l1.mp3', './sfx_m1.mp3', './sfx_r1.mp3',
  './sfx_x2.mp3', './sfx_x3.mp3', './sfx_x4.mp3'
];

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE).then(c => c.addAll(CORE)).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  e.respondWith(
    caches.match(e.request).then(r => r || fetch(e.request).then(res => {
      // Cache images and audio on first fetch
      if (e.request.url.match(/\.(png|jpg|mp3|webp)$/)) {
        const clone = res.clone();
        caches.open(CACHE).then(c => c.put(e.request, clone));
      }
      return res;
    }))
  );
});
