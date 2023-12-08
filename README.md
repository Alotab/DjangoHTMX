# Django HTMX User Search Project
Welcome to the Django HTMX User Search Project! This is a simple, yet powerful Django application that leverages the power of HTMX to enable live search functionality for users in the database. The beauty of this project lies in its simplicity - it achieves its goal without writing a single line of JavaScript!

## Overview
The project uses HTMX, a modern tool that allows you to access AJAX, CSS Transitions, WebSockets and Server Sent Events directly in HTML, without needing to write any JavaScript. This makes our code cleaner, easier to understand, and more maintainable.

In this project, we have a search feature that allows you to start typing in a search box, and it will immediately start showing the search results from the user database, updating as you type. All of this is done without needing to refresh the page or write complex JavaScript code.


## Code Snippet
Here’s a glimpse of the HTML code that powers the frontend of this application:

```
<h3>
    <span class="htmx-indicator">
      ...
   </span>
</h3>

<form>
    {% csrf_token %}
    <input class="form-control" type="search"
           name="search" placeholder="Begin Typing To Search Users..."
           hx-get="/search/results/"
           hx-trigger="keyup changed, search"
           hx-target="#search-results"
           hx-indicator=".htmx-indicator">
</form>

<div id="search-results">
    {% include "sim/search_results.html" %}
</div>

```


Stay tuned for more updates and feel free to contribute to this project! Happy coding! 🚀