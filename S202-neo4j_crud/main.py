from pprintpp import pprint as pp
from db.database import Graph
from art import Sculpture,Paiting

class Museum(object):
    def __init__(self):
        self.db = Graph(uri='bolt://44.195.31.216:7687',user='neo4j',password='ponds-beans-water')

    def create_museum(self, name, city, foundationYear):
        return self.db.execute_query('CREATE (n:Museum {name:$name, city:$city, foundationYear:$foundationYear}) return n',
                                     {'name': name, 'city': city,'foundationYear':foundationYear })

    def create_art(self, art ,museum_name):
        if isinstance(art,Sculpture):
            query = self.db.execute_query('CREATE (n:Sculpture {name:$name, year:$year, last_inspection:$last_inspection,material:$material, artist:$artist}) return n',
            {'name': art['name'], 'year': art['year'],'last_inspection':art['last_inspection'],'material':art['material'],'artist':art['artist'] })
            self.db.execute_query('MATCH (m:Museum {name:$name}), (s:Sculpture {nameS:$nameS}) CREATE (m)-[:CONTAINS]->(s)',
            {'name': museum_name, 'nameS': art['name']})

        else:
            query = self.db.execute_query('CREATE (n:Painting {name:$name, year:$year, last_inspection:$last_inspection,technic:$technic, artist:$artist}) return n',
            {'name': art['name'], 'year': art['year'],'last_inspection':art['last_inspection'],'technic':art['technic'],'artist':art['artist'] })
            self.db.execute_query('MATCH (m:Museum {name:$name}), (p:Paiting {nameP:$nameP}) CREATE (m)-[:CONTAINS]->(p)',
            {'name': museum_name, 'nameP': art['name']})
        

    def read_painting_by_name(self, name):
        return self.db.execute_query('MATCH (n:Painting {name:$name}) RETURN n',
                                     {'name': name})
    
    def read_sculpture_by_name(self, name):
        return self.db.execute_query('MATCH (n:Sculpture {name:$name}) RETURN n',
                                     {'name': name})    

    def read_all_nodes(self):
        return self.db.execute_query('MATCH (n) RETURN n')

    def update_painting_last_inspection(self, name, new_inspection):
        return self.db.execute_query('MATCH (n:Paiting {name:$name}) SET n.last_inspection = $new_inspection RETURN n',
                                     {'name': name, 'new_inspection': new_inspection})

    def update_sculpture_last_inspection(self, name, new_inspection):
        return self.db.execute_query('MATCH (n:Sculpture {name:$name}) SET n.last_inspection = $new_inspection RETURN n',
                                     {'name': name, 'new_inspection': new_inspection})                                     

    def delete_painting(self, name):
        return self.db.execute_query('MATCH (n:Painting {name:$name}) DETACH DELETE n',
                                     {'name': name})

    def delete_sculpture(self, name):
        return self.db.execute_query('MATCH (n:Sculpture {name:$name}) DETACH DELETE n',
                                     {'name': name})

    def delete_all_nodes(self):
        return self.db.execute_query('MATCH (n) DETACH DELETE n')

def divider():
    print('\n' + '-' * 80 + '\n')

museum = Museum()

while 1:    
    option = input('1. Create Museum\n2. Create Sculpture\n3. Create Painting\n4. Read Sculpture\n5. Read Painting\n6. Read all nodes\n7. Update Sculpture\n8. Update Painting\n9. Delete Sculpture\n10. Delete Painting\n11. Delete all nodes\n')

    if option == '1':
        name = input('  Name: ')
        age = input('   Age: ')
        person = {
            'name': name,
            'age': age
        }
        aux = dao.create(person)
        divider()

    elif option == '2':
        aux = dao.read_all_nodes()
        pp(aux)
        divider()

    elif option == '3':
        name = input('  Name: ')
        age = input('   Age: ')
        person = {
            'name': name,
            'age': age
        }
        
        aux = dao.update_age(person)
        divider()

    elif option == '4':
        name = input('  Name: ')
        person = {
            'name': name
        }
        
        aux = dao.delete(person)
        divider()

    else:
        break

dao.db.close()