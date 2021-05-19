######
Extras
######

Compare database types
== == == == == == == == == == ==

+--------------------+--------------------+--------------------+--------------------+
| Database | Strengths | Weaknesses | Good uses |
+--------------------+--------------------+--------------------+--------------------+
| Redis: | Rapid access where | Querying | Look up data |
| | data size can be | | (reference data). |
| Data structure | predetermined(all | All data needs to | |
                                 | server, message | data held in | fit in RAM | Caching. |
                                 | queuing, caching | memory). | | |
| | | Security very | Very fast access |
| | Realtime | basic | to data - real |
| | applications - | | time apps |
| | “instant” access | | |
| | to data by its | | |
| | key. | | |
| | | | |
| | Easily store sets | | |
| | and lists. | | |
| | | | |
| | High availability | | |
+--------------------+--------------------+--------------------+--------------------+
| Neo4j: | | | Applications that |
| | | | emphasize |
| Graph database | Powerful querying | Scaling can be a | maintaining and |
| | | problem in certain | tracking complex |
| | Very fast | situations(very | relationships |
                           | | | high end). | between data, such |
| | Flexible data | | as master data |
| | structures, | Doesn’t offer an | management, and |
| | handles | advantage if data | analyzing business |
| | complexity. | structure and | events. |
| | | relationships are | |
| | Fully ACID | simple. | Investigative |
| | compliant | | applications |
| | (protects data | | (stock trades). |
     | | quality and | | |
     | | integrity) | | |
| | | | |
| | | | |
+--------------------+--------------------+--------------------+--------------------+


Redis
== == =

Redis is a great database to help improve performance of an application.
It can act as a cache, but while this makes things very fast, it can require
significant memory to hold all the data. Application startup time can be slowed
down too, due to the time to initially populate, or seed the cache.

For more details see:

* https: // redislabs.com / lp / python - redis/
* https: // opensource.com / article / 18 / 4 / how - build - hello - redis - with-python


Neo4J
== == =

In computing, a graph database is a database that uses graph concepts
and theory from math to represent and store data.

This is in contrast to RDBMSs, where the data are stored in individual
tables, with the relationships between the tables maintained via primary
and foreign keys, and the actual relationships determined on the fly by
searching multiple tables during “join” queries. RDBMSs are well
optimized for these kinds of queries, but Graph Databases can be much
more efficient for data retrieval when the records have complex
relationships.

For more detail see:

https: // en.wikipedia.org / wiki / Graph_database
https: // medium.com / labcodes / graph - databases - talking - about - your - data - relationships - with-python - b438c689dc89
https: // neo4j.com / developer / python/


Persistence and Serialization
== == == == == == == == == == == == == == =

Beyond using databases, there are various simple ways to store data in
our Python programs. We refer to these as persistence and serialization,
which are closely related. Serialization means taking a potentially
complex data structure and converting it into a single string of
bytes. Persistence is storing data simply in a way that it will persist
beyond the run - time of your program.

Serialization:
`h < https: // en.wikipedia.org / wiki / Serializa_on % 20 > `__\ `ttps: // en.wikipedia.org / wiki / Serializa\_on < https: // en.wikipedia.org / wiki / Serializa_on % 20 > `__

Persistence: \ https: // en.wikipedia.org / wiki / Persistence_(computer_science)

They are closely related, because most forms of persistent storage –
simple text files, databases, etc, require that it be turned into a
simple string of bytes first. After all, everything done with computers
is ultimately a serial string of bytes. And serialization is also very
useful for transmitting information between systems, such as
over a network.

Examples
--------

We are going to illustrate persistence using Pickle, Shelve, CSV files
and JSON.

Pickle is a simple way to store and retrieve the contents of a Python
object. Pickle serializes the data before writing it to disk, and
deserializes it when reading from disk. Here is a good article that
summarized Pickle:

https: // pythontips.com / 2013 / 08 / 02 / what - is-pickle - in-python/

Shelve stores objects too, but the objects must be associated with a
key. This key is used to retrieve the shelved object. See:

https: // pythontips.com / 2013 / 08 / 02 / what - is-pickle - in-python/

CSV, or comma separated files, are used for data interchange between a
very wide range of software products, including most notably
spreadsheets. There are many forms of CSV files, but all share the common
property of using the comma to delimit field values, and end of line to
separate records. See:

https: // en.wikipedia.org / wiki / Comma - separated_values

Finally, JSON files, which stands for Javascript Object Notation, are
used in many modern web applications. They are easier to read and write
(both for humans and computers) than the interchange format they often
replace, which is XML. See:

https: // en.wikipedia.org / wiki / JSON

Here is an example of a partial program that uses each of these:

.. code-block: : python

    """
    pickle etc
    """

    # code intentionally omitted - see git for complete module

    def run_example(furniture_items):
        """
        various persistence and serialization scenarios

        """

        def run_pickle():
            """
            Write and read with pickle
            """
            log.info("\n\n====")
            log.info('Demonstrate persistence with pickle')
            log.info('Write a pickle file with the furniture data')

            pickle.dump(furniture_items, open('data/data.pkl', 'wb'))

            log.info('Now read it back from the pickle file')
            read_data = pickle.load(open('data/data.pkl', 'rb'))
            log.info('Show that the write and read were successful')
            assert read_data == furniture_items
            log.info("and print the data")
            pprint.pprint(read_data)

        def run_shelve():
            """
            write and read with shelve

            """
            log.info("\n\n====")
            log.info("Demonstrate working with shelve")
            shelf_file = shelve.open('data/shelve.dat')
            log.info("store data at key")
            shelf_file['key'] = furniture_items

            log.info("Now retrieve a COPY of data at key")
            read_items = shelf_file['key']

            log.info("Check it worked")
            assert read_items == furniture_items

            log.info("And now print the copy")
            pprint.pprint(read_items)

            log.info("delete data stored at key to cleanup and close")
            del shelf_file['key']
            shelf_file.close()

        def run_csv():
            """
            write and read a csv
            """
            log.info("\n\n====")
            peopledata = [
                ('John', 'second guitar', 117.45),
                ('Paul', 'bass', 22.01),
                ('George', 'lead guitar', 45.99),
                ('Ringo', 'drume', 77.0),
                ('Roger', 'vocals', 12.5),
                ('Keith', 'drums', 6.25),
                ('Pete', 'guitar', 0.1),
                ('John', 'bass', 89.71)
            ]
            log.info("Write csv file")
            with open('data/rockstars.csv', 'w') as people:
                peoplewriter = csv.writer(people)
                peoplewriter.writerow(peopledata)

            log.info("Read csv file back")
            with open('data/rockstars.csv', 'r') as people:
                people_reader = csv.reader(
                    people, delimiter=',', quotechar='"')
                for row in people_reader:
                    pprint.pprint(row)

        def run_json():
            log.info("\n\n====")
            log.info("Look at working with json data")
            furniture = [{'product': 'Red couch', 'description': 'Leather low back'},
                         {'product': 'Blue couch', 'description': 'Cloth high back'},
                         {'product': 'Coffee table', 'description': 'Plastic'},
                         {'product': 'Red couch', 'description': 'Leather high back'}]

            log.info("Return json string from an object")
            furniture_string = json.dumps(furniture)

            log.info("Print the json")
            pprint.pprint(furniture_string)

            log.info("Returns an object from a json string representation")
            furniture_object = json.loads(furniture_string)
            log.info("print the string")
            pprint.pprint(furniture_object)

        run_pickle()
        run_shelve()
        run_csv()
        run_json()

        return

.. raw: : html

    < / div >



