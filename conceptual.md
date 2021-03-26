### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?

#### It is an open source relational database that uses SQL methods

- What is the difference between SQL and PostgreSQL?

#### they have small differences in their syntax but they are similar in how they make requests. Postgres has extra functionalities that SQL does not 

- In `psql`, how do you connect to a database?

#### \c dbname

- What is the difference between `HAVING` and `WHERE`?

#### where is used to filter  prior to grouping and having is used to filter after grouping

- What is the difference between an `INNER` and `OUTER` join?

#### inner join will focus on the commonalities of the tables and there must be some matching data in between the comparing tables. An outer join will  return all the extra rows that did not have matching data and can be classified as a left outer join, right outer join, or full join

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
###left join will return all information from table 1 and shared information from table 2. right join will return all information from table 2 and shared information from table 1

- What is an ORM? What do they do?
###ORM is object relational mapping. they allow you to query and manipulate data from databases

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
#### ajax calls are asynchronous  and does not usually result in  a page transition like http requests may

- What is CSRF? What is the purpose of the CSRF token?

####CRSF stands for cross-site request forgery. it is a way to prevent people from sending requests to our web browser that may trick the browser. It looks at all data sent to find a hidden key and if the key is not found then it rejects the data that was sent to the browser. It helps protect attacks through forms

- What is the purpose of `form.hidden_tag()`?

#### To generate a hidden field with a token to protect the form from attacks
