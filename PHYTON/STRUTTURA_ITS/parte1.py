class Room:
    def __init__(self,id:str,floor:int,seats:int):
        self.id:str = id
        self.floor:int = floor
        self.seats:int = seats
    def get_id(self) -> str:
        return  self.id
    def get_floor(self) -> int: 
        return self.floor
    def get_seats(self) -> int:
        return self.seats
    def get_area(self) -> float :
        area:float = self.seats * 2
        return area
    
class Building:
    def __init__(self,name:str,address:str,floors:tuple):
        self.name=name
        self.address=address
        self.floors=floors
        self.rooms=[]
    def get_floors(self):
        return self.floors
    def get_rooms(self):
        return self.rooms
    def add_room(self,room):
        if room.get_floor() >= self.floors [0] and room.get_floor() <= self.floors [1]:
            if room not in self.rooms:
                self.rooms.append(room)
    def area(self):
        building_area = 0
        for room in self.rooms:
            building_area += room.get_area()
        return building_area
    