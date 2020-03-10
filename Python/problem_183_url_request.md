### 2020 March 09 - Daily Coding Problem #183

This problem was asked by Twitch.

Describe what happens when you type a URL into your browser.

*Answer*:

- **Check HSTS**: (Assuming the input was an url, if not then some verification steps will be performed in advance of this step) A modern browser will look up in its HSTS (HTTP Strict Transport Security) list. Basically, it means looking up in its stored table whether this url requested that a browser can only send request to it via HTTPS (a secured HTTP). Otherwise the browser will send the request via HTTP, unless, again, the server send back a request to order the browser to specifically send the request via HTTPS.

- **DNS lookup**: In the simplest form, this process will try to turn the url into an IP address, specifically the IP address of the server to which the url is referred. Usually it will be a table stored in the local machine. If it cannot retrieve this information locally, it will elevate the request until an IP address is received (upto a certain point, it cannot return a non-existent url's IP address).

- **Send request**: This part will happen more than once if the server specifically wants to be requested with HTTPS but received HTTP anyway. Also it will happen again if there are other components that need to be rendered aside from html (but who are we kidding, most websites nowaday have both CSS and javascript in them). Otherwise, a request will be sent to the server.

- **Receive HTTP request**: The server send back the requested components, first the HTML

- **Browser render**: The browser will then render the request onto the screen (plus request for more component if needed, then again, of course it will)
