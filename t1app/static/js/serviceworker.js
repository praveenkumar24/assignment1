var staticCacheName = 't1app-v1';

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(staticCacheName).then(function(cache) {
      return cache.addAll([
       '/base_layout',
       '/static/images/icon-160x160.png',
       '/static/images/icon.jpg'
      ]);
    })
  );
});

/*
self.addEventListener('fetch', function(event) {
  var requestUrl = new URL(event.request.url);
    if (requestUrl.origin === location.origin) {
      if ((requestUrl.pathname === '/')) {
        event.respondWith(caches.match('/'));
        return;
      }
    }
    event.respondWith(
      caches.match(event.request).then(function(response) {
        return response || fetch(event.request);
      })
    );
});
*/

self.addEventListener('fetch', function(event) {
  var requestUrl = new URL(event.request.url);

    event.respondWith(
      caches.match(event.request).then(function(response) {
        return response || fetch(event.request);
      })
    );
});


/*
self.addEventListener('fetch', event => {
  event.respondWith(
    caches.open(CACHE_NAME).then(cache => {
     return cache.match(event.request.url).then(response => {
      return response || fetch(event.request.url)
      .then(response => {
        const responseClone = response.clone();
        cache.put(event.request.url, responseClone);
        })
      })
    }
 );)
});
*/
