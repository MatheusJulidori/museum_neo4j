from pprintpp import pprint as pp
from db.database import Graph
from art import Sculpture,Painting

class Museum(object):
    def __init__(self):
        self.db = Graph(uri='bolt://44.195.31.216:7687',user='neo4j',password='ponds-beans-water')

    def create_museum(self, name, city, foundationYear):
        return self.db.execute_query('CREATE (n:Museum {name:$name, city:$city, foundationYear:$foundationYear}) return n',
                                     {'name': name, 'city': city,'foundationYear':foundationYear })

    def create_art(self, art):
        if isinstance(art,Sculpture):
            self.db.execute_query('CREATE (n:Sculpture {name:$name, year:$year, last_inspection:$last_inspection,material:$material, artist:$artist}) return n',{'name': art.name, 'year': art.year,'last_inspection':art.last_inspection,'material':art.material,'artist':art.artist })

        else:
            self.db.execute_query('CREATE (n:Painting {name:$name, year:$year, last_inspection:$last_inspection,technic:$technic, artist:$artist}) return n',{'name': art.name, 'year': art.year,'last_inspection':art.last_inspection,'technic':art.technic,'artist':art.artist })
        

    def read_painting_by_name(self, name):
        return self.db.execute_query('MATCH (n:Painting {name:$name}) RETURN n',
                                     {'name': name})
    
    def read_sculpture_by_name(self, name):
        return self.db.execute_query('MATCH (n:Sculpture {name:$name}) RETURN n',
                                     {'name': name})    

    def read_all_nodes(self):
        return self.db.execute_query('MATCH (n) RETURN n')

    def update_painting_last_inspection(self, name, new_inspection):
        return self.db.execute_query('MATCH (n:Painting {name:$name}) SET n.last_inspection = $new_inspection RETURN n',
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

    def create_relation(self,art_type,art_name,museum_name):
        if art_type == '1':
            self.db.execute_query('MATCH (m:Museum {name:$museum_name}), (s:Sculpture {name:$name}) CREATE (m)-[:CONTAINS]->(s)',{'museum_name': museum_name, 'name': art_name})
        else:
            self.db.execute_query('MATCH (m:Museum {name:$museum_name}), (p:Painting {name:$name}) CREATE (m)-[:CONTAINS]->(p)',{'museum_name': museum_name, 'name': art_name})


def divider():
    print('\n' + '-' * 80 + '\n')

museum = Museum()

while 1:    
    option = input('1. Create Museum\n2. Create Sculpture\n3. Create Painting\n4. Create relation\n5. Read Sculpture\n6. Read Painting\n7. Read all nodes\n8. Update Sculpture\n9. Update Painting\n10. Delete Sculpture\n11. Delete Painting\n12. Delete all nodes\n')

    if option == '1':
        name = input('  Name: ')
        city = input('  City: ')
        foundationYear = input('  Foundation Year: ')
        aux = museum.create_museum(name,city,foundationYear)

    elif option == '2':
        name = input('  Name: ')
        year = input('  Year: ')
        last_inspection = input('  Last Inspection: ')
        material = input('  Material:  ')
        artist = input('  Artist:  ')
        art = Sculpture(name,year,last_inspection,artist,material)
        aux = museum.create_art(art)

    elif option == '3':
        name = input('  Name: ')
        year = input('  Year: ')
        last_inspection = input('  Last Inspection: ')
        technic = input('  Technic:  ')
        artist = input('  Artist:  ')
        art = Painting(name,year,last_inspection,artist,technic)
        aux = museum.create_art(art)

    elif option == '4':
        art_type = input('  Art type(1 - Sculpture, 2-Painting):  ')
        art_name = input('  Art name:  ')
        museum_name = input('  Museum name:  ')
        aux = museum.create_relation(art_type,art_name,museum_name)

    elif option == '5':
        name = input('  Name: ')
        aux = museum.read_sculpture_by_name(name)
        print(aux)
        divider()

    elif option == '6':
        name = input('  Name: ')
        aux = museum.read_painting_by_name(name)
        print(aux)
        divider()

    elif option == '7':
        aux = museum.read_all_nodes()
        print(aux)
        divider()

    elif option == '8':
        name = input('  Name: ')
        new_inspection = input('  New Inspection:  ')
        aux = museum.update_sculpture_last_inspection(name,new_inspection)
        print(aux)
        divider()

    elif option == '9':
        name = input('  Name: ')
        new_inspection = input('  New Inspection:  ')
        aux = museum.update_painting_last_inspection(name,new_inspection)
        print(aux)
        divider()

    elif option == '10':
        name = input('  Name: ')
        aux = museum.delete_sculpture(name)

    elif option == '11':
        name = input('  Name: ')
        aux = museum.delete_painting(name)

    elif option == '12':
        aux = museum.delete_all_nodes()

    else:
        break

museum.db.close()