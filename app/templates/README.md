Template inheritance

as our application grows we will be needing to implement more pages, and this navigation bar will have to be copied to all of them. Then you will have to keep all these identical copies of the navigation bar in sync, and that could become a lot of work if you have a lot of pages and templates.

Instead, we can use Jinja2's template inheritance feature, which allows us to move the parts of the page layout that are common to all templates and put them in a base template from which all other templates are derived.

example below

<html>
  <head>
    {% if title %}
    <title>{{ title }} - microblog</title>
    {% else %}
    <title>Welcome to microblog</title>
    {% endif %}
  </head>
  <body>
    <div>Microblog: <a href="/index">Home</a></div>
    <hr>
    {% block content %}{% endblock %}
  </body>
</html>

then you will inherit such as below for your next page

{% extends "base.html" %}
{% block content %}
    <h1>Hi, {{ user.nickname }}!</h1>
    {% for post in posts %}
    <div><p>{{ post.author.nickname }} says: <b>{{ post.body }}</b></p></div>
    {% endfor %}
{% endblock %}
