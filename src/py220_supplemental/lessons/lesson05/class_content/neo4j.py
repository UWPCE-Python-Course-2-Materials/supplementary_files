"""
    neo4j example
"""

# code intentionally omitted - see git for complete module


with driver.session() as session:

    log.info('Adding a few Person nodes')
    for first, last in [('Bob', 'Jones'),
                        ('Nancy', 'Cooper'),
                        ('Alice', 'Cooper'),
                        ('Fred', 'Barnes'),
                        ('Mary', 'Evans'),
                        ('Marie', 'Curie'),
                        ]:
        cyph = "CREATE (n:Person {first_name:'%s', last_name: '%s'})" % (
            first, last)
        session.run(cyph)

    log.info("Get all of people in the DB:")
    cyph = """MATCH (p:Person)
              RETURN p.first_name as first_name, p.last_name as last_name
            """
    result = session.run(cyph)
    print("People in database:")
    for record in result:
        print(record['first_name'], record['last_name'])
