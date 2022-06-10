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
        city = input('   City: ')
        foudationYear = input('   Foundation Year: ')
        aux = museum.create_museum(name,city,foundationYear)

    elif option == '2':
        name = input('  Name: ')
        year = input('  Year: ')
        last_inspection = input('  Last Inspection: ')
        material = input('  Material:  ')
        artist = input('  Artist  ')
        museum_name = input('  Museum Name  ')
        art = Sculpture(name,year,last_inspection,artist,material)
        aux = museum.create_art(art,museum_name)

    elif option == '3':
        name = input('  Name: ')
        year = input('  Year: ')
        last_inspection = input('  Last Inspection: ')
        technic = input('  Technic:  ')
        artist = input('  Artist  ')
        museum_name = input('  Museum Name  ')
        art = Painting(name,year,last_inspection,artist,technic)
        aux = museum.create_art(art,museum_name)

    elif option == '4':
        name = input('  Name: ')
        aux = museum.read_sculpture_by_name(name)
        print(aux)
        divider()

    elif option == '5':
        name = input('  Name: ')
        aux = museum.read_painting_by_name(name)
        print(aux)
        divider()

    elif option == '6':
        aux = museum.read_all_nodes()
        print(aux)
        divider()

    elif option == '7':
        name = input('  Name: ')
        new_inspection = input('  New Inspection:  ')
        aux = museum.update_sculpture_last_inspection(name,new_inspection)
        print(aux)
        divider()

    elif option == '8':
        name = input('  Name: ')
        new_inspection = input('  New Inspection:  ')
        aux = museum.update_painting_last_inspection(name,new_inspection)
        print(aux)
        divider()

    elif option == '9':
        name = input('  Name: ')
        aux = museum.delete_sculpture(name)

    elif option == '10':
        name = input('  Name: ')
        aux = museum.delete_painting(name)

    elif option == '11':
        aux = museum.delete_all_nodes()

    else:
        break

dao.db.close()