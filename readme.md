                     
<h1 align="center" style="font-weight: bold;">Meals Django Backend 💻</h1>

<p align="center">
<a href="#tech">Technologies</a>
<a href="#started">Getting Started</a>
</p>


<p align="center">The Meals project is a app to help you organize your meal planning, ingredient inventory and shopping list.</p>
 
<h2 id="technologies">💻 Technologies</h2>

- Django
- MySQL Database
- React Frontend
 
<h2 id="started">🚀 Getting started</h2>

Here you describe how to run your project locally
 
<h3>Prerequisites</h3>

Here you list all prerequisites necessary for running your project. For example:

- [Python](https://www.python.org/downloads/)
- [XAMPP](https://www.apachefriends.org/download.html)
- [MySQL](https://dev.mysql.com/downloads/)
 
<h3>Cloning</h3>

How to clone your project

```bash
git clone https://github.com/bel-caylor/Meals_Django
```
 
<h3>Config .env variables</h2>


<h3>Starting</h3>

How to start your project

```bash
cd Meals-Django-React
python -m venv myvenv
myvenv\Scripts\activate
pip install django
pip install mysqlclient
```
Run XAMPP.  Start Apache and MySQL.
Create database `meals`.  Add database information to `meals/.env` file

Start backend
```bash
python manage.py runserver
```
 
<h2 id="routes">📍 API Endpoints</h2>

Here you can list the main routes of your API, and what are their expected request bodies.
​
| route               | description                                          
|----------------------|-----------------------------------------------------
| <kbd>GET /authenticate</kbd>     | retrieves user info see [response details](#get-auth-detail)
| <kbd>POST /authenticate</kbd>     | authenticate user into the api see [request details](#post-auth-detail)


